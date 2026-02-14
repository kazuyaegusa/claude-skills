#!/usr/bin/env python3
"""repo-tracker — GitHub リポジトリ変更監視スクリプト

任意の GitHub リポジトリの変更を定期フェッチし、
差分レポート（Markdown）生成 + Discord 通知を行う。
リモートへの書き込みは一切行わない（完全読み取り専用）。

使い方:
    repo_tracker.py add <URL> [--webhook <Discord URL>]
    repo_tracker.py check [名前]           # 省略時: 全リポジトリ
    repo_tracker.py list
    repo_tracker.py reports [名前]
    repo_tracker.py show [名前] [日付]
    repo_tracker.py setup-webhook <名前> <URL>
    repo_tracker.py test-notify <名前>
    repo_tracker.py install-schedule <名前> [--python <path>] [--hour <0-23>]
    repo_tracker.py remove <名前>
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import subprocess
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path.home() / ".repo-tracker"
PLIST_DIR = Path.home() / "Library" / "LaunchAgents"
USER_AGENT = "repo-tracker/1.0"


# ============================================================
# ユーティリティ
# ============================================================


def git(repo_dir: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_dir,
        capture_output=True,
        text=True,
    )


def repo_dir(name: str) -> Path:
    return BASE_DIR / name


def clone_dir(name: str) -> Path:
    return repo_dir(name) / "repo"


def reports_dir(name: str) -> Path:
    return repo_dir(name) / "reports"


def state_file(name: str) -> Path:
    return repo_dir(name) / ".state"


def config_file(name: str) -> Path:
    return repo_dir(name) / "config.json"


def log_file(name: str) -> Path:
    return repo_dir(name) / "tracker.log"


def load_config(name: str) -> dict:
    cf = config_file(name)
    if cf.exists():
        return json.loads(cf.read_text())
    return {}


def save_config(name: str, config: dict) -> None:
    config_file(name).write_text(
        json.dumps(config, indent=2, ensure_ascii=False) + "\n"
    )


def load_state(name: str) -> str | None:
    sf = state_file(name)
    if sf.exists():
        return sf.read_text().strip()
    return None


def save_state(name: str, commit_hash: str) -> None:
    state_file(name).write_text(commit_hash + "\n")


def get_all_repos() -> list[str]:
    if not BASE_DIR.exists():
        return []
    return sorted(
        d.name for d in BASE_DIR.iterdir()
        if d.is_dir() and (d / "config.json").exists()
    )


def extract_repo_name(url: str) -> str:
    """GitHub URL からリポジトリ名を抽出"""
    url = url.rstrip("/").removesuffix(".git")
    return url.split("/")[-1]


def get_default_branch(name: str) -> str:
    config = load_config(name)
    return config.get("default_branch", "main")


def remote_branch(name: str) -> str:
    return f"origin/{get_default_branch(name)}"


# ============================================================
# Git 情報取得（読み取り専用）
# ============================================================


def fetch(name: str) -> bool:
    result = git(clone_dir(name), "fetch", "origin")
    if result.returncode != 0:
        print(f"[error] {name}: git fetch 失敗: {result.stderr.strip()}")
        return False
    return True


def get_remote_head(name: str) -> str:
    return git(clone_dir(name), "rev-parse", remote_branch(name)).stdout.strip()


def get_commit_log(name: str, old: str, new: str) -> str:
    return git(clone_dir(name), "log", "--oneline", "--no-merges", f"{old}..{new}").stdout.strip()


def get_commits_with_body(name: str, old: str, new: str) -> list[dict[str, str]]:
    sep = "---COMMIT_SEP---"
    result = git(clone_dir(name), "log", f"--format={sep}%h%n%s%n%b", f"{old}..{new}")
    commits = []
    for block in result.stdout.split(sep):
        block = block.strip()
        if not block:
            continue
        lines = block.split("\n", 2)
        hash_ = lines[0].strip()
        subject = lines[1].strip() if len(lines) > 1 else ""
        body = lines[2].strip() if len(lines) > 2 else ""
        body = re.sub(r"Co-Authored-By:.*", "", body).strip()
        commits.append({"hash": hash_, "subject": subject, "body": body})
    return commits


def get_commit_log_detail(name: str, old: str, new: str) -> str:
    return git(clone_dir(name), "log", "--format=%h %ai %s", f"{old}..{new}").stdout.strip()


def get_changed_files(name: str, old: str, new: str) -> str:
    return git(clone_dir(name), "diff", "--name-only", f"{old}..{new}").stdout.strip()


def get_diff_stat(name: str, old: str, new: str) -> str:
    return git(clone_dir(name), "diff", "--stat", f"{old}..{new}").stdout.strip()


def get_diff(name: str, old: str, new: str) -> str:
    return git(clone_dir(name), "diff", f"{old}..{new}").stdout.strip()


def classify_files(name: str, old: str, new: str) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {"added": [], "modified": [], "deleted": []}
    for key, flag in [("added", "A"), ("modified", "M"), ("deleted", "D")]:
        out = git(clone_dir(name), "diff", f"--diff-filter={flag}", "--name-only", f"{old}..{new}")
        result[key] = [f for f in out.stdout.strip().splitlines() if f]
    return result


def get_numstat_total(name: str, old: str, new: str) -> tuple[int, int, int]:
    out = git(clone_dir(name), "diff", "--numstat", f"{old}..{new}").stdout.strip()
    added = deleted = file_count = 0
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) >= 3 and parts[0] != "-":
            added += int(parts[0])
            deleted += int(parts[1])
            file_count += 1
    return added, deleted, file_count


# ============================================================
# レポート生成
# ============================================================


def generate_report(name: str, old: str, new: str) -> Path:
    today = datetime.date.today().isoformat()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    config = load_config(name)
    repo_url = config.get("repo_url", "")

    log_oneline = get_commit_log(name, old, new)
    log_detail = get_commit_log_detail(name, old, new)
    changed = get_changed_files(name, old, new)
    stat = get_diff_stat(name, old, new)
    diff = get_diff(name, old, new)
    commit_count = len(log_oneline.splitlines()) if log_oneline else 0

    report = f"""# {name} 変更レポート

- **リポジトリ**: {repo_url}
- **確認日時**: {now}
- **前回確認コミット**: `{old[:8]}`
- **最新コミット**: `{new[:8]}`
- **新規コミット数**: {commit_count}

## コミット一覧

```
{log_detail or "(変更なし)"}
```

## 変更ファイル

```
{changed or "(変更なし)"}
```

## 変更統計

```
{stat or "(変更なし)"}
```

## 差分詳細

```diff
{diff or "(変更なし)"}
```
"""

    rd = reports_dir(name)
    rd.mkdir(parents=True, exist_ok=True)
    report_path = rd / f"{today}.md"
    if report_path.exists():
        timestamp = datetime.datetime.now().strftime("%H%M%S")
        report_path = rd / f"{today}_{timestamp}.md"
    report_path.write_text(report)
    return report_path


# ============================================================
# Discord 通知
# ============================================================


def _truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 4] + "\n..."


def _group_files_by_dir(files: list[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    labels = {
        "src": "ソースコード", "tests": "テスト", "docs": "ドキュメント",
        "skills": "スキル", ".github": "CI/CD", ".claude": "Claude設定",
        "lib": "ライブラリ", "cmd": "コマンド", "pkg": "パッケージ",
        "internal": "内部モジュール", "scripts": "スクリプト",
    }
    for f in files:
        top = f.split("/")[0] if "/" in f else "(root)"
        label = labels.get(top, top)
        groups[label].append(f.split("/")[-1])
    return dict(groups)


def _build_content_summary(commits: list[dict[str, str]]) -> str:
    lines = []
    for c in commits:
        subject = c["subject"]
        prefix_match = re.match(r"\[(\w+)\]\s*", subject)
        prefix = f"**[{prefix_match.group(1)}]** " if prefix_match else ""
        clean_subject = re.sub(r"^\[\w+\]\s*", "", subject)
        lines.append(f"{prefix}{clean_subject}")
        if c["body"]:
            for bl in c["body"].splitlines():
                bl = bl.strip().lstrip("- ")
                if bl and len(bl) > 5:
                    lines.append(f"  - {bl}")
    return "\n".join(lines)


def _build_file_section(classified: dict[str, list[str]]) -> str:
    parts = []
    icons = {"added": "+", "modified": "~", "deleted": "-"}
    labels_map = {"added": "新規", "modified": "変更", "deleted": "削除"}
    for key in ["added", "modified", "deleted"]:
        files = classified[key]
        if not files:
            continue
        grouped = _group_files_by_dir(files)
        group_strs = []
        for dir_label, fnames in grouped.items():
            if len(fnames) <= 3:
                group_strs.append(f"{dir_label}: {', '.join(fnames)}")
            else:
                group_strs.append(f"{dir_label}: {', '.join(fnames[:2])} 他{len(fnames)-2}件")
        parts.append(f"{icons[key]} {labels_map[key]} ({len(files)}): {' / '.join(group_strs)}")
    return "\n".join(parts)


def send_webhook(webhook_url: str, payload: dict) -> bool:
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json", "User-Agent": USER_AGENT},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status == 204
    except Exception as e:
        print(f"[error] Discord 通知失敗: {e}")
        return False


def notify_discord(
    name: str,
    webhook_url: str,
    old: str,
    new: str,
    commit_count: int,
    report_path: Path,
) -> bool:
    config = load_config(name)
    repo_url = config.get("repo_url", "")

    commits = get_commits_with_body(name, old, new)
    classified = classify_files(name, old, new)
    added_lines, deleted_lines, file_count = get_numstat_total(name, old, new)

    content_summary = _truncate(_build_content_summary(commits), 2000)
    file_section = _truncate(_build_file_section(classified), 900)
    scale = f"+{added_lines:,} / -{deleted_lines:,} 行 ({file_count} files)"

    embed = {
        "title": f"{name} 更新 ({commit_count} commits)",
        "url": repo_url,
        "color": 0x5865F2,
        "description": content_summary,
        "fields": [
            {"name": "ファイル変更", "value": f"```diff\n{file_section}\n```", "inline": False},
            {"name": "範囲", "value": f"`{old[:8]}` → `{new[:8]}`", "inline": True},
            {"name": "規模", "value": scale, "inline": True},
        ],
        "footer": {"text": f"レポート: {report_path.name}"},
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    return send_webhook(webhook_url, {"embeds": [embed]})


# ============================================================
# サブコマンド
# ============================================================


def cmd_add(args: argparse.Namespace) -> None:
    url: str = args.url.rstrip("/").removesuffix(".git")
    name = extract_repo_name(url)
    rd = repo_dir(name)

    if rd.exists() and config_file(name).exists():
        print(f"[info] {name} は既に追加済みです")
        return

    rd.mkdir(parents=True, exist_ok=True)
    reports_dir(name).mkdir(exist_ok=True)

    # clone
    cd = clone_dir(name)
    if not cd.exists():
        print(f"[add] git clone {url} ...")
        result = subprocess.run(
            ["git", "clone", url, str(cd)],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            print(f"[error] clone 失敗: {result.stderr.strip()}")
            sys.exit(1)
    print(f"[add] クローン完了: {cd}")

    # デフォルトブランチ検出
    branch_result = git(cd, "symbolic-ref", "refs/remotes/origin/HEAD")
    default_branch = "main"
    if branch_result.returncode == 0:
        default_branch = branch_result.stdout.strip().split("/")[-1]

    # 設定保存
    config = {
        "repo_url": url,
        "default_branch": default_branch,
        "discord_webhook_url": args.webhook or "",
    }
    save_config(name, config)

    # 初期状態を記録
    head = get_remote_head(name)
    save_state(name, head)

    print(f"[add] {name} を追加しました (branch: {default_branch}, HEAD: {head[:8]})")

    # Webhook テスト
    if args.webhook:
        ok = send_webhook(args.webhook, {"embeds": [{
            "title": f"repo-tracker: {name} 監視開始",
            "description": f"リポジトリ `{url}` の変更監視を開始しました。",
            "color": 0x57F287,
        }]})
        print(f"[add] Discord テスト通知: {'成功' if ok else '失敗'}")


def cmd_check(args: argparse.Namespace) -> None:
    names = [args.name] if args.name else get_all_repos()
    if not names:
        print("[info] 監視中のリポジトリはありません。add で追加してください")
        return

    for name in names:
        if not config_file(name).exists():
            print(f"[error] {name} は登録されていません")
            continue

        print(f"[check] {name}: git fetch ...")
        if not fetch(name):
            continue

        remote_head = get_remote_head(name)
        last_seen = load_state(name)

        if last_seen is None:
            save_state(name, remote_head)
            git(clone_dir(name), "merge", "--ff-only", remote_branch(name))
            print(f"[check] {name}: 初回記録 ({remote_head[:8]})")
            continue

        if last_seen == remote_head:
            print(f"[check] {name}: 変更なし")
            continue

        commit_count = len(get_commit_log(name, last_seen, remote_head).splitlines())
        print(f"[check] {name}: 変更検出 {last_seen[:8]} → {remote_head[:8]} ({commit_count} commits)")

        report_path = generate_report(name, last_seen, remote_head)
        print(f"[check] {name}: レポート → {report_path}")

        # Discord 通知
        config = load_config(name)
        webhook = config.get("discord_webhook_url", "")
        if webhook:
            print(f"[check] {name}: Discord 通知送信中...")
            ok = notify_discord(name, webhook, last_seen, remote_head, commit_count, report_path)
            if ok:
                print(f"[check] {name}: Discord 通知完了")
        else:
            print(f"[check] {name}: Discord 未設定")

        git(clone_dir(name), "merge", "--ff-only", remote_branch(name))
        save_state(name, remote_head)

    print("[check] 完了")


def cmd_list(_args: argparse.Namespace) -> None:
    repos = get_all_repos()
    if not repos:
        print("監視中のリポジトリはありません")
        return

    print(f"監視中のリポジトリ ({len(repos)} 件):\n")
    for name in repos:
        config = load_config(name)
        last = load_state(name)
        webhook = "設定済" if config.get("discord_webhook_url") else "未設定"
        plist = PLIST_DIR / f"com.repo-tracker.{name}.plist"
        schedule = "有効" if plist.exists() else "未設定"
        print(f"  {name}")
        print(f"    URL: {config.get('repo_url', '?')}")
        print(f"    最終確認: {last[:8] if last else '未確認'}")
        print(f"    Discord: {webhook} / 定期実行: {schedule}")
        print()


def cmd_reports(args: argparse.Namespace) -> None:
    name = args.name
    if not name:
        repos = get_all_repos()
        if len(repos) == 1:
            name = repos[0]
        else:
            print("リポジトリ名を指定してください")
            for r in repos:
                print(f"  {r}")
            return

    rd = reports_dir(name)
    if not rd.exists():
        print(f"{name} のレポートはありません")
        return

    reports = sorted(rd.glob("*.md"))
    if not reports:
        print(f"{name} のレポートはありません")
        return

    print(f"{name} のレポート ({len(reports)} 件):\n")
    for r in reports:
        lines = r.read_text().splitlines()
        count = ""
        for line in lines:
            if "新規コミット数" in line:
                count = line.split(": ", 1)[-1] if ": " in line else ""
                break
        print(f"  {r.name}  {count}")


def cmd_show(args: argparse.Namespace) -> None:
    name = args.name
    if not name:
        repos = get_all_repos()
        if len(repos) == 1:
            name = repos[0]
        else:
            print("リポジトリ名を指定してください")
            return

    rd = reports_dir(name)
    if not rd.exists():
        print(f"{name} のレポートはありません")
        return

    if args.date:
        matches = sorted(rd.glob(f"{args.date}*.md"))
        if not matches:
            print(f"{name} の '{args.date}' のレポートが見つかりません")
            return
        target = matches[-1]
    else:
        reports = sorted(rd.glob("*.md"))
        if not reports:
            print(f"{name} のレポートはありません")
            return
        target = reports[-1]

    print(target.read_text())


def cmd_setup_webhook(args: argparse.Namespace) -> None:
    name = args.name
    if not config_file(name).exists():
        print(f"[error] {name} は登録されていません")
        sys.exit(1)

    config = load_config(name)
    config["discord_webhook_url"] = args.webhook_url
    save_config(name, config)
    print(f"[setup] {name}: Webhook URL を保存しました")

    ok = send_webhook(args.webhook_url, {"embeds": [{
        "title": f"repo-tracker: {name} Webhook 設定完了",
        "description": "Discord 通知が正常に設定されました。",
        "color": 0x57F287,
    }]})
    print(f"[setup] テスト通知: {'成功' if ok else '失敗'}")


def cmd_test_notify(args: argparse.Namespace) -> None:
    name = args.name
    config = load_config(name)
    webhook = config.get("discord_webhook_url", "")
    if not webhook:
        print(f"[error] {name}: Discord 未設定。setup-webhook で設定してください")
        sys.exit(1)

    last = load_state(name)
    remote_head = get_remote_head(name)

    if last == remote_head or last is None:
        # 差分がない場合は直近3コミットで代用
        old = git(clone_dir(name), "rev-parse", f"{remote_branch(name)}~3").stdout.strip()
        new = remote_head
    else:
        old, new = last, remote_head

    commit_count = len(get_commit_log(name, old, new).splitlines())
    print(f"[test] {name}: {old[:8]} → {new[:8]} ({commit_count} commits)")
    ok = notify_discord(name, webhook, old, new, commit_count, Path("test_report.md"))
    print(f"[test] {'送信成功' if ok else '送信失敗'}")


def cmd_install_schedule(args: argparse.Namespace) -> None:
    name = args.name
    if not config_file(name).exists():
        print(f"[error] {name} は登録されていません")
        sys.exit(1)

    python_path = args.python or sys.executable
    script_path = Path(__file__).resolve()
    hour = args.hour

    plist_name = f"com.repo-tracker.{name}.plist"
    plist_path = PLIST_DIR / plist_name

    plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.repo-tracker.{name}</string>
    <key>ProgramArguments</key>
    <array>
        <string>{python_path}</string>
        <string>{script_path}</string>
        <string>check</string>
        <string>{name}</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>{hour}</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>{log_file(name)}</string>
    <key>StandardErrorPath</key>
    <string>{log_file(name)}</string>
    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
"""

    PLIST_DIR.mkdir(parents=True, exist_ok=True)
    plist_path.write_text(plist_content)
    print(f"[schedule] plist 作成: {plist_path}")
    print(f"[schedule] 毎日 {hour:02d}:00 に {name} をチェックします")
    print(f"[schedule] 有効化: launchctl load {plist_path}")


def cmd_remove(args: argparse.Namespace) -> None:
    name = args.name
    rd = repo_dir(name)
    if not rd.exists():
        print(f"[error] {name} は登録されていません")
        sys.exit(1)

    # launchd 解除
    plist_path = PLIST_DIR / f"com.repo-tracker.{name}.plist"
    if plist_path.exists():
        subprocess.run(["launchctl", "unload", str(plist_path)], capture_output=True)
        plist_path.unlink()
        print(f"[remove] 定期実行を解除しました")

    # ディレクトリ削除
    import shutil
    shutil.rmtree(rd)
    print(f"[remove] {name} を削除しました")


# ============================================================
# メイン
# ============================================================


def main() -> None:
    parser = argparse.ArgumentParser(
        description="GitHub リポジトリ変更監視ツール",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command")

    # add
    p_add = sub.add_parser("add", help="リポジトリを追加")
    p_add.add_argument("url", help="GitHub リポジトリ URL")
    p_add.add_argument("--webhook", help="Discord Webhook URL", default="")

    # check
    p_check = sub.add_parser("check", help="更新チェック")
    p_check.add_argument("name", nargs="?", help="リポジトリ名（省略時: 全て）")

    # list
    sub.add_parser("list", help="監視中リポジトリ一覧")

    # reports
    p_reports = sub.add_parser("reports", help="レポート一覧")
    p_reports.add_argument("name", nargs="?", help="リポジトリ名")

    # show
    p_show = sub.add_parser("show", help="レポート表示")
    p_show.add_argument("name", nargs="?", help="リポジトリ名")
    p_show.add_argument("date", nargs="?", help="日付 (YYYY-MM-DD)")

    # setup-webhook
    p_webhook = sub.add_parser("setup-webhook", help="Discord Webhook 設定")
    p_webhook.add_argument("name", help="リポジトリ名")
    p_webhook.add_argument("webhook_url", help="Discord Webhook URL")

    # test-notify
    p_test = sub.add_parser("test-notify", help="テスト通知送信")
    p_test.add_argument("name", help="リポジトリ名")

    # install-schedule
    p_schedule = sub.add_parser("install-schedule", help="定期実行セットアップ")
    p_schedule.add_argument("name", help="リポジトリ名")
    p_schedule.add_argument("--python", help="Python 実行パス", default="")
    p_schedule.add_argument("--hour", type=int, default=9, help="実行時刻 (0-23, デフォルト: 9)")

    # remove
    p_remove = sub.add_parser("remove", help="監視停止・削除")
    p_remove.add_argument("name", help="リポジトリ名")

    args = parser.parse_args()

    dispatch = {
        "add": cmd_add,
        "check": cmd_check,
        "list": cmd_list,
        "reports": cmd_reports,
        "show": cmd_show,
        "setup-webhook": cmd_setup_webhook,
        "test-notify": cmd_test_notify,
        "install-schedule": cmd_install_schedule,
        "remove": cmd_remove,
    }

    if args.command in dispatch:
        dispatch[args.command](args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
