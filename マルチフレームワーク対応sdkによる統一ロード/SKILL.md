# マルチフレームワーク対応SDKによる統一ロード

> Python/JS/Go各言語で、LangChain/LlamaIndex/Genkit/ADK等のフレームワーク別SDKを用いて、同一ツールをフレームワーク固有形式に変換する

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: agent-orchestration

## なぜ使うのか

各フレームワークはツールのインターフェース（schema定義・実行関数の形式）が異なるため、toolbox側で吸収することで開発者が変換コードを書かずに済む

## いつ使うのか

複数フレームワークでプロトタイプを比較検証する時、フレームワーク移行時にツール定義を再利用したい時

## やり方

1. フレームワークに応じたSDKをインストール（例：pip install toolbox-langchain）
2. 各SDK提供のToolboxClientでツールをロード
3. SDK内部でフレームワーク固有のtool形式に自動変換
4. そのままフレームワークのagent/chainに渡す

### 入力

- MCP Toolboxサーバーエンドポイント
- 各フレームワークのSDK

### 出力

- フレームワーク固有のtoolオブジェクト（LangChain Tool/Genkit Tool等）

## 使うツール・ライブラリ

- toolbox-langchain
- toolbox-llamaindex
- @toolbox-sdk/core（JS）
- mcp-toolbox-sdk-go

## コード例

```
# Python LangChain
from toolbox_langchain import ToolboxClient
async with ToolboxClient("http://127.0.0.1:5000") as client:
    tools = client.load_toolset()  # LangChain Tool形式

# JS Genkit
import { ToolboxClient } from '@toolbox-sdk/core';
const client = new ToolboxClient('http://127.0.0.1:5000');
const toolboxTools = await client.loadToolset('toolsetName');
const tools = toolboxTools.map(t => ai.defineTool({
  name: t.getName(),
  description: t.getDescription(),
  schema: t.getParamSchema()
}, t));
```

## 前提知識

- MCPプロトコルの基本概念（Model Context Protocol）
- LLMエージェントフレームワークの基礎（LangChain/LlamaIndex/Genkit等のいずれか）
- データベース接続の基本（PostgreSQL/MySQL等の接続文字列）
- YAMLの基本文法
- ツール呼び出しの仕組み（Function Calling）
