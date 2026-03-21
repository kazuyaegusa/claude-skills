# SDKでツールをAIフレームワークに読み込む

> Toolbox SDKを使い、起動したToolboxサーバーからツール定義を取得し、LangChain/LlamaIndex/Genkit等のフレームワークで利用可能な形式に変換する

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: agent-orchestration

## なぜ使うのか

各フレームワークのツール形式に手動で変換する手間を省き、統一されたインターフェースでツールを利用できるようにするため

## いつ使うのか

PythonやJavaScript/TypeScriptでAIエージェントを実装している時、複数のエージェントで同じツールセットを共有したい時

## やり方

1. 言語・フレームワーク別SDKをインストール（例: `pip install toolbox-langchain`）
2. ToolboxClientをインスタンス化し、サーバーURL（例: http://127.0.0.1:5000）を指定
3. `client.load_toolset('toolset_name')` でツール一覧を取得
4. 取得したツールをそのままエージェントに渡す

### 入力

- 稼働中のToolboxサーバーのURL
- toolset名（tools.yamlで定義）

### 出力

- フレームワーク用のツールオブジェクト（LangChain Tool / LlamaIndex Tool等）

## 使うツール・ライブラリ

- toolbox-langchain（Python）
- toolbox-llamaindex（Python）
- toolbox-core（Python/JS）
- @toolbox-sdk/core（JS/TS）
- @toolbox-sdk/adk（JS/TS）
- mcp-toolbox-sdk-go（Go）

## コード例

```
# Python LangChain例
from toolbox_langchain import ToolboxClient

async with ToolboxClient("http://127.0.0.1:5000") as client:
    tools = client.load_toolset()  # これをエージェントに渡す

# JavaScript Core例
import { ToolboxClient } from '@toolbox-sdk/core';
const client = new ToolboxClient('http://127.0.0.1:5000');
const tools = await client.loadToolset('toolsetName');
```

## 前提知識

- MCPプロトコルの基本概念（サーバー・クライアント・ツール）
- 使用するデータベース（PostgreSQL/MySQL/BigQuery等）の接続情報
- AIフレームワーク（LangChain/LlamaIndex/Genkit等）の基本的な使い方
- YAML形式の理解
- 非同期処理（async/await）の理解（Python/JS SDKを使う場合）

## 根拠

> 「Toolbox sits between your application's orchestration framework and your database, providing a control plane」

> 「By connecting your IDE to your databases with MCP Toolbox, you can delegate complex and time-consuming database tasks」

> 現在beta版、v1.0までは破壊的変更の可能性あり（「MCP Toolbox for Databases is currently in beta, and may see breaking changes until the first stable release (v1.0).」）
