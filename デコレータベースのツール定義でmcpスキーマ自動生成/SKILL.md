# デコレータベースのツール定義でMCPスキーマ自動生成

> Python関数に`@mcp.tool`デコレータを付けるだけで、MCP準拠のツールスキーマ・バリデーション・ドキュメントが自動生成される

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: other

## なぜ使うのか

MCPでは各ツールのJSON Schemaを手動定義する必要があるが、これは保守コストが高くミスも起きやすい。関数シグネチャから自動導出することで、型安全性を保ちながら実装速度を上げる

## いつ使うのか

Pythonで書かれた既存ロジックをMCPツールとして公開したいとき。型ヒントとdocstringだけでスキーマが自動生成されるため、追加の定義ファイルが不要

## やり方

1. `from fastmcp import FastMCP`でインポート
2. `mcp = FastMCP("サーバー名")`でインスタンス作成
3. 通常のPython関数を定義（型ヒント付き）
4. 関数に`@mcp.tool`デコレータを付与
5. docstringを書く（これがツール説明になる）
6. `mcp.run()`でサーバー起動

### 入力

- 型ヒント付きPython関数
- 関数のdocstring（ツール説明用）

### 出力

- MCP準拠のツールスキーマ（JSON Schema）
- 実行可能なMCPサーバー

## 使うツール・ライブラリ

- fastmcp (PyPI: uv pip install fastmcp)

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

- Pythonの基本文法（関数定義、デコレータ、型ヒント）
- MCPの基本概念（ツール・リソース・プロンプトの役割）
- 非同期プログラミングの基礎（Clientsを使う場合）

## 根拠

> 「FastMCP 1.0 was incorporated into the official MCP Python SDK in 2024.」（公式SDK統合実績）

> 「downloaded a million times a day, and some version of FastMCP powers 70% of MCP servers across all languages」（採用実績）

> 「We recommend installing FastMCP with uv: uv pip install fastmcp」（推奨インストール方法）

> 「When you're ready to deploy, Prefect Horizon offers free hosting for FastMCP users.」（無料ホスティング提供）
