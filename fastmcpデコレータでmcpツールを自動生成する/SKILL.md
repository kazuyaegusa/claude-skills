# FastMCPデコレータでMCPツールを自動生成する

> Pythonの通常関数に@mcp.toolデコレータを付けるだけで、MCPプロトコル準拠のツールとして公開できる

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: other

## なぜ使うのか

型ヒント・docstringから自動でJSONスキーマを生成し、バリデーション・ドキュメント生成を省略できるため、実装コストが劇的に減る

## いつ使うのか

PythonでMCPサーバーを実装する全てのケース（特に既存関数の再利用時）

## やり方

1. FastMCPインスタンスを作成（mcp = FastMCP("名前")）
2. ツール化したい関数に@mcp.toolデコレータを追加
3. 関数の型ヒント（a: int等）とdocstringを記述
4. mcp.run()でサーバー起動

### 入力

- Python 3.x環境
- 型ヒント付き関数定義
- docstring（ツールの説明用）

### 出力

- MCPプロトコル準拠のツールサーバー
- 自動生成されたJSONスキーマ
- Claude Desktop等から呼び出し可能なツール

## 使うツール・ライブラリ

- fastmcp（uv pip install fastmcp推奨）

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

- Python 3.x の基本文法（関数定義、デコレータ）
- 型ヒント（type hints）の理解
- MCP（Model Context Protocol）の概念（LLMとツールを接続するプロトコル）
- FastAPIやFlaskのようなPythonフレームワークの使用経験があると理解が早い
