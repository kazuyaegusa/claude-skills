# tools.yamlによるデータベースツールの宣言的定義

> データベース接続情報（sources）、実行するSQL/操作（tools）、ツールのグループ化（toolsets）をYAMLで定義し、MCPサーバーとして起動する

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: agent-orchestration

## なぜ使うのか

ツール定義をコードから分離することで、複数のフレームワーク・エージェント間で同一ツールを再利用でき、更新時にアプリケーション本体の再デプロイが不要になる

## いつ使うのか

複数のLLMフレームワークで同じデータベース操作を行う必要がある時、または複数のエージェント間でツール定義を共有したい時

## やり方

1. tools.yamlにsources（データベース接続情報）を定義
2. toolsセクションでツール名・説明・パラメータ・実行するSQLを記述
3. toolsetsで用途別にツールをグループ化
4. `toolbox --tools-file tools.yaml`でMCPサーバーを起動
5. 各フレームワークのSDK（toolbox-langchain, toolbox-llamaindex等）で`client.load_toolset()`を呼び出してツールをロード

### 入力

- データベース接続情報（ホスト、ポート、認証情報）
- ツールとして公開したいSQL文・パラメータ定義
- ツールの説明文（LLMがツールを選択する際の判断材料）

### 出力

- 起動中のMCPサーバー（デフォルトポート5000）
- 各フレームワークで利用可能なツールオブジェクト

## 使うツール・ライブラリ

- MCP Toolbox Server（バイナリ/コンテナ/NPM）
- toolbox-langchain/toolbox-llamaindex/toolbox-core（Python SDK）
- @toolbox-sdk/core, @toolbox-sdk/adk（JS/TS SDK）
- mcp-toolbox-sdk-go（Go SDK）

## コード例

```
# tools.yaml
kind: sources
name: my-pg-source
type: postgres
host: 127.0.0.1
port: 5432
database: toolbox_db
user: toolbox_user
password: my-password
---
kind: tools
name: search-hotels-by-name
type: postgres-sql
source: my-pg-source
description: Search for hotels based on name.
parameters:
  - name: name
    type: string
    description: The name of the hotel.
statement: SELECT * FROM hotels WHERE name ILIKE '%' || $1 || '%';
---
toolsets:
  hotel_tools:
    - search-hotels-by-name

# Python（LangChain例）
from toolbox_langchain import ToolboxClient

async with ToolboxClient("http://127.0.0.1:5000") as client:
    tools = client.load_toolset("hotel_tools")
```

## 前提知識

- MCP（Model Context Protocol）の基本概念
- LLMエージェントフレームワーク（LangChain/LlamaIndex/Genkit等）の基礎知識
- SQL、データベース接続（ホスト/ポート/認証）の基本
- YAML設定ファイルの読み書き
- Docker/コンテナの基本操作（コンテナ版を使う場合）
- 各言語のパッケージマネージャー（pip, npm, go get）の使用経験
