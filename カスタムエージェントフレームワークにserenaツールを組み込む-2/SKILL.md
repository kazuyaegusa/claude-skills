# カスタムエージェントフレームワークにSerenaツールを組み込む

> Serenaのツール実装を独自のエージェントフレームワーク（LangChain、AutoGPT等）に統合し、フレームワーク固有のツール呼び出しで利用する

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: agent-orchestration

## なぜ使うのか

Serenaのツールはフレームワーク非依存に設計されているため、既存のエージェントフレームワークに容易に組み込める。これにより既存ワークフローを維持しながらSerenaの機能を追加できる

## いつ使うのか

既存のエージェントフレームワークを使っており、MCPではなくフレームワーク統合でSerenaを使いたい時

## やり方

1. Serenaのソースコードから`serena.agent.Tool`サブクラスを確認
2. 各ツールの`apply`メソッドをフレームワークのツール定義形式でラップ
3. フレームワークのツールリストにSerenaツールを追加
4. エージェントがフレームワーク経由でSerenaツールを呼び出す

### 入力

- Serenaソースコード（serena.agent.Tool）
- エージェントフレームワーク（LangChain、AutoGPT等）

### 出力

- フレームワーク統合されたSerenaツール

## 使うツール・ライブラリ

- Serenaコードベース
- LangChain/AutoGPT等のエージェントフレームワーク

## コード例

```
# 概念的なカスタム統合例（Serenaドキュメント参照）
# from serena.agent import Tool
# class CustomTool(Tool):
#     def apply(self, symbol_name: str) -> dict:
#         # シンボル検索ロジック
#         return {'symbols': [...]}
```

## 前提知識

- Model Context Protocol（MCP）の基本概念
- Language Server Protocol（LSP）の基礎知識
- LLMエージェントの動作原理（ツール呼び出し・Function Calling）
- Python環境構築（uv等のパッケージマネージャー）
- コードベースにおけるシンボル（関数・クラス・変数等）の概念
- （JetBrainsプラグイン利用時）JetBrains IDEの基本操作
