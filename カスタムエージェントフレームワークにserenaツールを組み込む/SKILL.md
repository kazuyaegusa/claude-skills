# カスタムエージェントフレームワークにSerenaツールを組み込む

> Serenaのツール実装（`serena.agent.Tool`サブクラス）を独自エージェントフレームワークに移植し、フレームワーク固有のツール呼び出しインターフェースで利用する

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: agent-orchestration

## なぜ使うのか

SerenaのツールロジックはMCPに依存せず、`apply`メソッドとして実装されているため、任意のエージェントフレームワーク（LangChain/AutoGPT/独自実装等）で再利用可能

## いつ使うのか

既存のエージェントフレームワーク（LangChain等）を使っており、Serenaのコード操作ツールだけを追加したい場合

## やり方

1. `serena.agent.Tool`を継承して新ツールを実装（`apply`メソッドに処理を記述）
2. フレームワークのツール登録API（例: LangChainの`@tool`デコレータ）でラップ
3. エージェント実行時に`SerenaAgent`が新ツールを自動認識
4. ドキュメント（https://oraios.github.io/serena/03-special-guides/custom_agent.html）参照

### 入力

- カスタムエージェントフレームワーク
- Serenaソースコード（`serena.agent.Tool`クラス）

### 出力

- フレームワーク統合されたSerenaツール
- 既存エージェントでのシンボルレベルコード操作

## 使うツール・ライブラリ

- Serena（ツール実装部分）
- 任意のエージェントフレームワーク

## コード例

```
from serena.agent import Tool

class MyCustomTool(Tool):
    def apply(self, symbol_name: str) -> str:
        # シンボル検索ロジック
        return result

# フレームワーク統合例（LangChain）
from langchain.tools import tool

@tool
def find_symbol_tool(symbol_name: str) -> str:
    """Find symbol in codebase"""
    return MyCustomTool().apply(symbol_name)
```

## 前提知識

- Model Context Protocol (MCP) の基本概念
- Language Server Protocol (LSP) の役割（IDE補完・参照解析の仕組み）
- LLMのツール呼び出し（Function Calling）の仕組み
- Python環境とuvパッケージマネージャーの使い方
- コーディングエージェント（Claude Code/Cursor等）の基本的な使用経験
