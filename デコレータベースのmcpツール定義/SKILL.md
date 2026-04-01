# デコレータベースのMCPツール定義

> Python関数に`@mcp.tool`デコレータを付けることで、MCPツールとして自動的にスキーマ生成・公開される

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: other

## なぜ使うのか

手動でのスキーマ定義、バリデーション、ドキュメント生成を排除し、関数の型ヒントとdocstringから自動生成することで実装コストとメンテナンスコストを削減する

## いつ使うのか

LLMから呼び出し可能なツールを最小限のコードで実装したい時、型ヒントとdocstringから自動的にスキーマを生成したい時

## やり方

1. `from fastmcp import FastMCP`でインポート
2. `mcp = FastMCP("サーバー名")`でインスタンス化
3. 通常のPython関数を定義（型ヒントとdocstringを付ける）
4. 関数に`@mcp.tool`デコレータを適用
5. `if __name__ == "__main__": mcp.run()`でサーバー起動

### 入力

- 型ヒント付きのPython関数
- 関数のdocstring（ツールの説明として使用）

### 出力

- MCPプロトコル準拠のツールスキーマ
- バリデーション機能付きの実行可能なMCPツール

## 使うツール・ライブラリ

- fastmcp（uv pip install fastmcp）

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

- Pythonの基本的な関数定義・型ヒント・デコレータの知識
- Model Context Protocol（MCP）の概念理解（LLMがツールを呼び出すプロトコル）
- LLMツール統合の基本的な理解

## 根拠

> 「FastMCP 1.0 was incorporated into the official MCP Python SDK in 2024. Today, the actively maintained standalone project is downloaded a million times a day, and some version of FastMCP powers 70% of MCP servers across all languages.」

> 「with FastMCP, best practices are built in.」

> 「When you're ready to deploy, Prefect Horizon offers free hosting for FastMCP users.」
