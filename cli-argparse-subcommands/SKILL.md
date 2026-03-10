---
title: CLI Argparse Subcommands Pattern
description: argparseでサブコマンドベースのCLIツールを構築するパターン
tags: [cli, argparse, python]
---

# CLI Argparse Subcommands Pattern

argparseを使用してサブコマンドベースのCLIツールを構築する汎用パターン。

## 使い方

```python
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Your CLI Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # サブコマンド追加例
    create_parser = subparsers.add_parser("create", help="Create something")
    create_parser.add_argument("name", help="Name of the item")
    create_parser.add_argument("--type", default="default", help="Type of item")
    
    list_parser = subparsers.add_parser("list", help="List items")
    list_parser.add_argument("--filter", help="Filter criteria")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # コマンド処理
    if args.command == "create":
        print(f"Creating {args.name} of type {args.type}")
    elif args.command == "list":
        print(f"Listing items with filter: {args.filter}")
```

## 実行例

```bash
# ヘルプ表示
python cli.py --help

# サブコマンド実行
python cli.py create "myitem" --type "special"
python cli.py list --filter "active"
```

## 特徴

- サブコマンドごとに独自の引数を定義可能
- 自動的にヘルプメッセージ生成
- 引数のバリデーション機能付き
- 型変換サポート（int, float など）