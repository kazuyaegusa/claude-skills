# デコレータベースのツール定義でスキーマ自動生成

> Pythonの関数に@mcp.toolデコレータを付けるだけでMCPツールとして公開し、型ヒントとdocstringから自動的にJSONスキーマ・バリデーション・ドキュメントを生成する

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: automation-pipeline

## なぜ使うのか

手動でのスキーマ記述・バリデーションコード・ドキュメント作成を省略し、実装ミス・メンテナンスコストを削減するため

## いつ使うのか

LLMに独自のPython関数を提供したい時、スキーマ定義を自動化したい時

## やり方

1. FastMCPインスタンスを作成（`mcp = FastMCP("サーバー名")`）
2. 関数に型ヒントとdocstringを記述
3. @mcp.toolデコレータを付与
4. mcp.run()でサーバー起動

### 入力

- 型ヒント付きPython関数
- 関数のdocstring（説明文）

### 出力

- MCPプロトコル準拠のツール
- JSONスキーマ
- バリデーションロジック

## 使うツール・ライブラリ

- fastmcp
- Python 3.x

## コード例

```
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

## 前提知識

- Python 3.xの基礎知識
- 型ヒント（Type Hints）の理解
- デコレータの基本概念
- Model Context Protocol（MCP）の概要
- LLMツール統合の基本的な動機
