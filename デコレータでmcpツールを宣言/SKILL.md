# デコレータでMCPツールを宣言

> Python関数に`@mcp.tool`デコレータを付けるだけでMCPツールとして公開する

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: other

## なぜ使うのか

型ヒントとdocstringから自動的にJSONスキーマ・バリデーション・ドキュメントを生成するため、手動でプロトコル仕様を書く必要がなく、コードの重複とメンテナンスコストを削減できる

## いつ使うのか

既存のPython関数をLLMから呼び出せるようにしたい時、または新規にMCPツールを実装する時

## やり方

1. `FastMCP("サーバー名")`でインスタンス生成
2. 通常のPython関数を定義（型ヒント必須、docstringで説明記述）
3. `@mcp.tool`デコレータを関数に付与
4. `mcp.run()`でサーバー起動
5. MCPクライアント（Claude Desktop等）から関数名で呼び出し可能に

### 入力

- 型ヒント付きPython関数
- docstring（ツールの説明）
- FastMCPインスタンス

### 出力

- MCP準拠のツールエンドポイント
- 自動生成されたJSONスキーマ
- 自動バリデーション機能

## 使うツール・ライブラリ

- fastmcp
- uv（推奨パッケージマネージャ）

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

- Python 3.x基礎知識
- 型ヒント（Type Hints）の理解
- デコレータの基本概念
- Model Context Protocol (MCP)の概要理解
- 非同期プログラミング（async/await）の基礎（応用時）
