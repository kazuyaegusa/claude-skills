# フレームワーク横断でのツール統一インターフェース

> Python（LangChain/LlamaIndex）、JS/TS（LangChain/Genkit/ADK）、Go（LangChain Go/Genkit/ADK/OpenAI/GenAI）で同一のMCPツールを利用する

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: agent-orchestration

## なぜ使うのか

各フレームワーク独自のツール形式に変換する処理を各SDKがカプセル化しているため、tools.yaml定義を1つ書けば、どのフレームワークでも同じツールが使える。フレームワーク移行時の再実装コストがゼロになる

## いつ使うのか

プロトタイピング時にフレームワークを頻繁に変更する時、または複数のプロジェクトで異なるフレームワークを使いながら同一のツール資産を共有したい時

## やり方

1. tools.yamlで一度ツール定義を作成
2. 使いたいフレームワークに対応するSDKをインストール（例: `pip install toolbox-langchain`）
3. 各SDKの`ToolboxClient`で`load_toolset()`を呼び出し
4. 返されたツールオブジェクトをそのままフレームワークのエージェントに渡す
5. 別のフレームワークに移行する際は、SDKのみ変更（tools.yamlは再利用）

### 入力

- tools.yaml（フレームワーク非依存）
- 使用するフレームワークに対応するToolbox SDK

### 出力

- 各フレームワークのツールオブジェクト（LangChain Tool、Genkit Tool等）

## 使うツール・ライブラリ

- Python: toolbox-langchain, toolbox-llamaindex, toolbox-core
- JS/TS: @toolbox-sdk/core, @toolbox-sdk/adk
- Go: mcp-toolbox-sdk-go（core, tbadk, tbgenkit）

## コード例

```
# Python - LangChain
from toolbox_langchain import ToolboxClient
async with ToolboxClient("http://127.0.0.1:5000") as client:
    tools = client.load_toolset("hotel_tools")

# Python - LlamaIndex
from toolbox_llamaindex import ToolboxClient
async with ToolboxClient("http://127.0.0.1:5000") as client:
    tools = client.load_toolset("hotel_tools")

# Go - Genkit
import "github.com/googleapis/mcp-toolbox-sdk-go/tbgenkit"
tool, _ := client.LoadTool("search-hotels-by-name", ctx)
genkitTool, _ := tbgenkit.ToGenkitTool(tool, g)

# JS/TS - Core SDK
import { ToolboxClient } from '@toolbox-sdk/core';
const client = new ToolboxClient('http://127.0.0.1:5000');
const tools = await client.loadToolset('hotel_tools');
```

## 前提知識

- MCP（Model Context Protocol）の基本概念
- LLMエージェントフレームワーク（LangChain/LlamaIndex/Genkit等）の基礎知識
- SQL、データベース接続（ホスト/ポート/認証）の基本
- YAML設定ファイルの読み書き
- Docker/コンテナの基本操作（コンテナ版を使う場合）
- 各言語のパッケージマネージャー（pip, npm, go get）の使用経験
