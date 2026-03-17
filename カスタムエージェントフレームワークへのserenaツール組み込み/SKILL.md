# カスタムエージェントフレームワークへのSerenaツール組み込み

> Serenaのツール実装（serena.agent.Tool）をサブクラス化し、独自のエージェントフレームワークに統合する

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: agent-orchestration

## なぜ使うのか

SerenaのツールはMCPに依存せず実装されているため、任意のPythonベースエージェントフレームワーク（LangChain、AutoGen等）に組み込めるため

## いつ使うのか

既存の独自エージェントフレームワークにIDE風コードツールを追加したい時

## やり方

1. serena.agent.Toolをサブクラス化して新ツールを定義
2. applyメソッドを実装（シグネチャがツール要件に一致するよう設計）
3. SerenaAgentインスタンスに追加すると自動的に利用可能になる
4. エージェントフレームワークからSerenaAgentのツールを呼び出す（参考: https://github.com/oraios/serena/blob/main/docs/03-special-guides/custom_agent.md）

### 入力

- Pythonベースのエージェントフレームワーク
- Serenaライブラリ

### 出力

- カスタムエージェントで利用可能なSerenaツール

## 使うツール・ライブラリ

- Serena（Python SDK）
- 任意のエージェントフレームワーク

## コード例

```
from serena.agent import Tool

class MyTool(Tool):
    def apply(self, param):
        # 実装
        pass
```

## 前提知識

- MCPの概念と動作原理
- Language Server Protocol（LSP）の基礎知識
- LLMエージェントのツール呼び出しメカニズム
- Python環境管理（uv）の基本操作
- 対象言語のLanguage Serverインストール方法（LSPバックエンド使用時）
- JetBrains IDE操作の基礎（JetBrainsバックエンド使用時）
