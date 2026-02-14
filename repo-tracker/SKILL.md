---
name: repo-tracker
description: GitHub リポジトリの変更を定期監視し、差分レポート生成 + Discord 通知を行う汎用スキル。
user_invocable: true
---

# Repo Tracker — GitHub リポジトリ変更監視スキル

任意の GitHub リポジトリの更新を定期的にフェッチし、差分レポート（Markdown）を生成して Discord に通知する。リモートへの書き込みは一切行わない（完全読み取り専用）。

## 引数

```
/repo-tracker <GitHubリポジトリURL>
/repo-tracker <GitHubリポジトリURL> --webhook <Discord Webhook URL>
/repo-tracker list
/repo-tracker check [リポジトリ名]
```

- **GitHubリポジトリURL**（必須 ※初回追加時）: 監視対象の GitHub URL（`https://github.com/owner/repo` 形式）
- **--webhook**（省略可）: Discord Webhook URL。省略時は `AskUserQuestion` で確認する
- **list**: 監視中のリポジトリ一覧を表示
- **check**: 手動で更新チェックを実行

## 実行手順

### Phase 0: 引数解析

1. 引数を解析する:
   - GitHub URL が指定されている場合 → Phase 1 へ（新規追加フロー）
   - `list` → Phase 5 の一覧表示のみ実行
   - `check [名前]` → Phase 4 の手動チェックのみ実行
   - 引数なし → `AskUserQuestion` で GitHub URL を入力してもらう

2. GitHub URL からリポジトリ名（`owner/repo` → `repo`）を抽出する

### Phase 1: リポジトリセットアップ

1. 作業ディレクトリを確認・作成:
   ```
   ~/.repo-tracker/{repo-name}/
   ├── repo/           ← git clone 先
   ├── reports/         ← 差分レポート保存先
   ├── config.json      ← 設定（webhook URL 等）
   └── .state           ← 最後に確認したコミット hash
   ```

2. `Bash` で clone を実行:
   ```bash
   git clone <GitHub URL> ~/.repo-tracker/{repo-name}/repo
   ```
   - 既にクローン済みの場合はスキップ

3. デフォルトブランチ名を取得:
   ```bash
   git -C ~/.repo-tracker/{repo-name}/repo symbolic-ref refs/remotes/origin/HEAD | sed 's|refs/remotes/origin/||'
   ```

4. `config.json` を作成:
   ```json
   {
     "repo_url": "https://github.com/owner/repo",
     "default_branch": "main",
     "discord_webhook_url": ""
   }
   ```

### Phase 2: Discord Webhook 設定

1. 引数に `--webhook` があればその URL を使用
2. なければ `AskUserQuestion` で確認:
   - 「Discord Webhook URL を入力してください」
   - 選択肢: 「後で設定する」「今入力する（Other で URL を貼り付け）」

3. Webhook URL が提供された場合、`config.json` に保存

4. テスト送信を実行:
   ```bash
   python3 ~/.claude/skills/repo-tracker/repo_tracker.py test-notify {repo-name}
   ```

### Phase 3: 定期実行セットアップ

1. `Bash` で Python 実行パスを確認:
   ```bash
   which python3
   ```

2. LaunchAgent plist を生成・登録:
   ```bash
   python3 ~/.claude/skills/repo-tracker/repo_tracker.py install-schedule {repo-name} --python <pythonパス> [--hour 9]
   ```
   - デフォルト: 毎日 9:00 に実行
   - ユーザーが時間を指定した場合はそれに従う

3. launchctl で登録:
   ```bash
   launchctl load ~/Library/LaunchAgents/com.repo-tracker.{repo-name}.plist
   ```

### Phase 4: 動作確認

1. 手動で check を実行:
   ```bash
   python3 ~/.claude/skills/repo-tracker/repo_tracker.py check {repo-name}
   ```

2. 結果をユーザーに報告:
   - 「リポジトリ {repo-name} の監視を開始しました」
   - 「毎日 {HH:MM} に自動チェックします」
   - 「変更があれば Discord に通知されます」
   - 「手動チェック: `python3 ~/.claude/skills/repo-tracker/repo_tracker.py check {repo-name}`」

### Phase 5: 一覧・管理（list / check コマンド時）

- `list`: `~/.repo-tracker/` 配下のディレクトリを列挙し、各リポジトリの状態（最終チェック日時、Webhook 設定有無）を表示
- `check [名前]`: 指定リポジトリ or 全リポジトリをチェック

## スクリプト

メインスクリプト: `~/.claude/skills/repo-tracker/repo_tracker.py`

### サブコマンド一覧

| コマンド | 説明 |
|---------|------|
| `add <URL> [--webhook <URL>]` | リポジトリを追加 |
| `check [名前]` | 更新チェック（省略時: 全リポジトリ） |
| `list` | 監視中リポジトリ一覧 |
| `reports [名前]` | レポート一覧 |
| `show [名前] [日付]` | レポート表示 |
| `setup-webhook <名前> <URL>` | Discord Webhook 設定 |
| `test-notify <名前>` | テスト通知送信 |
| `install-schedule <名前>` | launchd 定期実行設定 |
| `remove <名前>` | 監視停止・データ削除 |

## 注意事項

- **完全読み取り専用**: リモートリポジトリへの push / issue 作成 / PR 作成は一切行わない
- **git fetch のみ**: clone 後は fetch + ff-only merge のみ実行
- **Webhook URL**: `.repo-tracker/` 内の `config.json` に保存。Git にコミットしない
- **macOS 専用**: 定期実行は launchd を使用（Linux の場合は cron に手動設定が必要）
- **複数リポジトリ対応**: 1つのスクリプトで複数リポジトリを監視可能
