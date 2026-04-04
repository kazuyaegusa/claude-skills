# stdlib-only Pythonツールで依存地獄を回避

> 332個のCLIツール全てをPython標準ライブラリのみで実装し、pip install不要・即実行可能にする

- 出典: https://github.com/alirezarezvani/claude-skills
- 投稿者: alirezarezvani
- カテゴリ: claude-code-workflow

## なぜ使うのか

pipパッケージ依存があると、バージョン競合・インストール失敗・セキュリティリスク（supply chain attack）が発生する。stdlibのみならPython 3.xがあれば動作保証でき、10年後も動く

## いつ使うのか

長期保守が必要なツール、複数環境（CI/CD、ユーザーマシン、コンテナ）で確実に動作させたいツールを書くとき

## やり方

1. 必要な機能（例: JSON処理→json, HTTP→urllib, CLI引数→argparse）をstdlibから選定
2. 外部ライブラリ（requests, pandas等）を使わずにロジックを実装
3. スクリプト冒頭にShebang（#!/usr/bin/env python3）を追加
4. chmod +x scripts/*.py で実行権限付与
5. python3 scripts/tool_name.py --help で動作確認

### 入力

- 実装したい機能（例: RICE優先度計算、ブランド音声分析、技術的負債スコアリング）
- Python 3.x（3.8以上推奨）

### 出力

- 単一ファイルの実行可能Pythonスクリプト
- --help でUsageを表示するCLI

## 使うツール・ライブラリ

- Python標準ライブラリ（json, argparse, csv, pathlib, re, urllib等）

## コード例

```
#!/usr/bin/env python3
import argparse
import json
import sys

def calculate_rice(reach, impact, confidence, effort):
    """RICE score = (Reach × Impact × Confidence) / Effort"""
    return (reach * impact * confidence) / effort

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='RICE prioritization')
    parser.add_argument('--reach', type=int, required=True)
    parser.add_argument('--impact', type=float, required=True)
    parser.add_argument('--confidence', type=float, required=True)
    parser.add_argument('--effort', type=float, required=True)
    parser.add_argument('--json', action='store_true', help='JSON output')
    
    args = parser.parse_args()
    score = calculate_rice(args.reach, args.impact, args.confidence, args.effort)
    
    if args.json:
        print(json.dumps({'rice_score': score}))
    else:
        print(f'RICE Score: {score:.2f}')
    sys.exit(0)
```

## 前提知識

- Claude Code / Cursor / Aider 等いずれかのAIコーディングツールの基本的な使い方
- Git / GitHub の基本操作（clone, pull）
- Python 3.x の実行環境（スクリプトツール利用時）
- Bashシェルの基本知識（インストールスクリプト実行時）
- （任意）マーケティング・PM・コンプライアンス等の各ドメイン知識（該当スキル使用時）

## 根拠

> Python tools — 332 CLI scripts (all stdlib-only, zero pip installs)
