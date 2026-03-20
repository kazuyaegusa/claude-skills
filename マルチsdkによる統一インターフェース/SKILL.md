# マルチSDKによる統一インターフェース

> Python、JavaScript/TypeScript、Go向けの公式SDKを使い、同一のツール定義を各フレームワーク（LangChain、LlamaIndex、Genkit、ADK等）で読み込む

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: agent-orchestration

## なぜ使うのか

各フレームワークごとに独自のツール実装をする必要がなくなり、ツールロジックの重複を排除し、保守コストを削減できる

## いつ使うのか

既存のLangChain/LlamaIndex/Genkit等のアプリケーションにデータベースツールを追加したい時、複数言語でツールを利用したい時

## やり方

1. 使用言語・フレームワークに対応するSDKをインストール（例: `pip install toolbox-langchain`）
2. ToolboxClientを初期化（例: `ToolboxClient('http://127.0.0.1:5000')`）
3. `client.load_toolset()`または`client.load_tool()`でツールを取得
4. フレームワーク固有の形式に自動変換されたツールをエージェントに渡す
5. エージェント実行時、ツール呼び出しはToolboxサーバー経由でデータベースに転送される

### 入力

- Toolboxサーバーのエンドポイント（URL）
- ツールセット名（オプション）

### 出力

- フレームワーク固有のツールオブジェクト（LangChainのTool、GenkitのFunctionDeclaration等）

## 使うツール・ライブラリ

- toolbox-core (Python/JS/Go)
- toolbox-langchain
- toolbox-llamaindex
- toolbox-adk
- toolbox-genkit

## コード例

```
from toolbox_langchain import ToolboxClient

async with ToolboxClient('http://127.0.0.1:5000') as client:
    tools = client.load_toolset('my_toolset')
    # これらのツールをLangChainエージェントに渡す
```

## 前提知識

- Model Context Protocol (MCP)の基本概念
- AIエージェントフレームワーク（LangChain、LlamaIndex、Genkit等）の基礎知識
- データベース接続の基本（PostgreSQL、MySQL、Spanner、BigQuery等）
- YAML形式の読み書き
- Docker/コンテナ技術の基礎（本番デプロイ時）
- OpenTelemetryによる可観測性の概念（本番運用時）
