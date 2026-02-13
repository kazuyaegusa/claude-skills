"""
Discord コンテキスト検索・抽出スクリプト

使用方法:
    python3 extract_context.py <keyword> [--exports-dir <path>] [--output-dir <path>] [--context-size <N>]

処理内容:
    - exports ディレクトリ内の全 messages.csv を検索
    - キーワードを含むメッセージとその前後の文脈を抽出
    - 返信チェーンも追跡
    - conversation.csv と metadata.json を出力

引数:
    keyword         検索キーワード（大文字小文字区別なし）
    --exports-dir   エクスポートディレクトリのパス（デフォルト: カレントディレクトリ下を自動検索）
    --output-dir    出力先ディレクトリ（デフォルト: exports/keyword_search/<keyword>/）
    --context-size  前後に取得するメッセージ数（デフォルト: 15）
"""

import argparse
import csv
import json
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple


def find_exports_dir(start_path: Path) -> Optional[Path]:
    """exports ディレクトリを自動検索"""
    candidates = [
        start_path / "exports",
        start_path / "02_claude" / "exports",
        start_path / "data" / "exports",
    ]
    for c in candidates:
        if c.exists() and any(c.rglob("messages.csv")):
            return c
    # フォールバック: 再帰検索（深さ3まで）
    for depth in range(1, 4):
        pattern = "/".join(["*"] * depth) + "/exports"
        for p in start_path.glob(pattern):
            if p.is_dir() and any(p.rglob("messages.csv")):
                return p
    return None


def find_message_csvs(exports_dir: Path) -> List[Path]:
    """messages.csv を全て検索（keyword_search・タイムスタンプ付き重複フォルダは除外）"""
    csvs = []
    stable_names: Set[str] = set()

    # まず安定ディレクトリ（タイムスタンプなし）を収集
    for p in exports_dir.rglob("messages.csv"):
        parent_name = p.parent.name
        if "keyword_search" in str(p):
            continue
        # タイムスタンプ付きでなければ安定ディレクトリ
        import re
        if not re.search(r"_\d{8}_\d{6}$", parent_name):
            stable_names.add(parent_name)
            csvs.append(p)

    # タイムスタンプ付きは、対応する安定ディレクトリがなければ採用
    for p in exports_dir.rglob("messages.csv"):
        parent_name = p.parent.name
        if "keyword_search" in str(p):
            continue
        import re
        match = re.search(r"_\d{8}_\d{6}$", parent_name)
        if match:
            base_name = parent_name[:match.start()]
            if base_name not in stable_names:
                csvs.append(p)

    return sorted(csvs)


def load_messages(csv_path: Path) -> List[Dict[str, str]]:
    """CSV から全メッセージを読み込む"""
    messages = []
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            messages.append(dict(row))
    return messages


def search_keyword(messages: List[Dict[str, str]], keyword: str) -> List[Dict[str, str]]:
    """キーワードを含むメッセージを検索（内容・送信者名・表示名を対象）"""
    keyword_lower = keyword.lower()
    matches = []
    for msg in messages:
        content = msg.get("内容", "").lower()
        sender = msg.get("送信者表示名", msg.get("送信者", "")).lower()
        sender_name = msg.get("送信者名", "").lower()
        channel = msg.get("チャンネル名", msg.get("チャンネル", "")).lower()
        if (keyword_lower in content
                or keyword_lower in sender
                or keyword_lower in sender_name
                or keyword_lower in channel):
            matches.append(msg)
    return matches


def extract_context(
    messages: List[Dict[str, str]],
    matches: List[Dict[str, str]],
    context_size: int = 15
) -> List[Dict[str, str]]:
    """マッチしたメッセージの前後の文脈を抽出（返信チェーンも追跡）"""
    # チャンネル別にメッセージをインデックス化
    ch_key = "チャンネルID" if "チャンネルID" in (messages[0] if messages else {}) else "チャンネル"
    channel_messages: Dict[str, List[Tuple[int, Dict]]] = defaultdict(list)
    for i, msg in enumerate(messages):
        ch_id = msg.get(ch_key, "")
        channel_messages[ch_id].append((i, msg))

    include_indices: Set[int] = set()
    reply_ids_to_find: Set[str] = set()

    msg_id_key = "メッセージID"
    reply_key = "返信先ID" if "返信先ID" in (messages[0] if messages else {}) else "返信先"

    for match in matches:
        match_id = match.get(msg_id_key, "")
        ch_id = match.get(ch_key, "")
        ch_msgs = channel_messages.get(ch_id, [])

        for pos, (global_idx, msg) in enumerate(ch_msgs):
            if msg.get(msg_id_key) == match_id:
                start = max(0, pos - context_size)
                end = min(len(ch_msgs), pos + context_size + 1)
                for j in range(start, end):
                    include_indices.add(ch_msgs[j][0])

                reply_id = match.get(reply_key, "")
                if reply_id:
                    reply_ids_to_find.add(str(reply_id))
                break

    # 返信元メッセージも含める
    for i, msg in enumerate(messages):
        if msg.get(msg_id_key, "") in reply_ids_to_find:
            include_indices.add(i)
            ch_id = msg.get(ch_key, "")
            ch_msgs = channel_messages.get(ch_id, [])
            for pos, (global_idx, m) in enumerate(ch_msgs):
                if global_idx == i:
                    start = max(0, pos - 5)
                    end = min(len(ch_msgs), pos + 5 + 1)
                    for j in range(start, end):
                        include_indices.add(ch_msgs[j][0])
                    break

    return [messages[i] for i in sorted(include_indices)]


def main():
    parser = argparse.ArgumentParser(description="Discord コンテキスト検索・抽出")
    parser.add_argument("keyword", help="検索キーワード")
    parser.add_argument("--exports-dir", help="エクスポートディレクトリのパス")
    parser.add_argument("--output-dir", help="出力先ディレクトリ")
    parser.add_argument("--context-size", type=int, default=15, help="前後の文脈メッセージ数")
    args = parser.parse_args()

    keyword = args.keyword

    # exports ディレクトリを特定
    if args.exports_dir:
        exports_dir = Path(args.exports_dir)
    else:
        exports_dir = find_exports_dir(Path.cwd())

    if not exports_dir or not exports_dir.exists():
        print("ERROR: exports ディレクトリが見つかりません", file=sys.stderr)
        print("  --exports-dir でパスを指定するか、exports/ を含むディレクトリで実行してください", file=sys.stderr)
        sys.exit(1)

    # 出力先ディレクトリ
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = exports_dir / "keyword_search" / keyword

    output_dir.mkdir(parents=True, exist_ok=True)

    # CSV ファイル検索
    csv_files = find_message_csvs(exports_dir)
    if not csv_files:
        print("ERROR: messages.csv が見つかりません: {}".format(exports_dir), file=sys.stderr)
        sys.exit(1)

    print("検索キーワード: {}".format(keyword))
    print("exports ディレクトリ: {}".format(exports_dir))
    print("対象CSV: {}ファイル".format(len(csv_files)))

    all_context: List[Dict[str, str]] = []
    all_matches_count = 0
    sources = []
    people: Set[str] = set()
    channels: Set[str] = set()
    dates: List[str] = []

    for csv_path in csv_files:
        server_name = csv_path.parent.name
        print("\n--- {} ---".format(server_name))

        messages = load_messages(csv_path)
        print("  メッセージ数: {}".format(len(messages)))

        matches = search_keyword(messages, keyword)
        print("  マッチ: {}件".format(len(matches)))

        if matches:
            context = extract_context(messages, matches, args.context_size)
            print("  文脈含む抽出: {}件".format(len(context)))
            all_context.extend(context)
            all_matches_count += len(matches)

            sources.append({
                "server": server_name,
                "match_count": len(matches),
                "context_count": len(context),
                "total_messages": len(messages),
            })

            for msg in context:
                p = msg.get("送信者表示名", msg.get("送信者", ""))
                if p:
                    people.add(p)
                ch = msg.get("チャンネル名", msg.get("チャンネル", ""))
                if ch:
                    channels.add(ch)
                dt = msg.get("送信日時", "")
                if dt:
                    dates.append(dt)

    if not all_context:
        print("\nキーワード「{}」に該当するメッセージは見つかりませんでした。".format(keyword))
        # 空でも metadata は出力
        metadata = {
            "keyword": keyword,
            "search_date": datetime.now().isoformat(),
            "total_matches": 0,
            "total_context_messages": 0,
            "sources": [],
            "channels": [],
            "people": [],
            "date_range": {"from": "", "to": ""},
            "output_dir": str(output_dir),
        }
        with open(output_dir / "metadata.json", "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        sys.exit(0)

    # CSV ヘッダーを実データから取得
    headers = list(all_context[0].keys())

    # conversation.csv 出力
    csv_output = output_dir / "conversation.csv"
    with open(csv_output, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(all_context)

    # 日付範囲
    dates.sort()
    date_range = {"from": dates[0] if dates else "", "to": dates[-1] if dates else ""}

    # metadata.json 出力
    metadata = {
        "keyword": keyword,
        "search_date": datetime.now().isoformat(),
        "total_matches": all_matches_count,
        "total_context_messages": len(all_context),
        "sources": sources,
        "channels": sorted(channels),
        "people": sorted(people),
        "date_range": date_range,
        "output_dir": str(output_dir),
    }

    meta_output = output_dir / "metadata.json"
    with open(meta_output, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    print("\n=== 結果 ===")
    print("マッチ数: {}件".format(all_matches_count))
    print("文脈含む抽出: {}件".format(len(all_context)))
    print("サーバー: {}".format(", ".join(s["server"] for s in sources)))
    print("チャンネル: {}".format(", ".join(sorted(channels))))
    print("関連人物: {}".format(", ".join(sorted(people))))
    print("期間: {} 〜 {}".format(date_range["from"][:10], date_range["to"][:10]))
    print("出力先: {}".format(output_dir))


if __name__ == "__main__":
    main()
