# YAMLベースのツール定義でMCPサーバー化

> データベース接続情報とSQL操作をtools.yamlに宣言的に定義し、toolboxコマンドでMCPサーバーとして起動する

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: agent-orchestration

## なぜ使うのか

ツール定義をコードから分離することで、エージェント本体を再デプロイせずにツールの追加・変更が可能になり、複数フレームワークでの再利用も容易になる

## いつ使うのか

複数のエージェントやフレームワークで同じDBツールを使い回したい時、ツールの更新頻度が高くエージェント再デプロイを避けたい時

## やり方

1. tools.yamlに`kind: source`でDB接続情報を定義
2. `kind: tool`でツール名・説明・パラメータ・SQL文を定義
3. `toolbox --config tools.yaml`でサーバー起動（デフォルトポート5000）
4. 各言語のSDK（Python/JS/Go）から`ToolboxClient(url).load_toolset()`でツールをロード
5. LLMフレームワークのtool形式に変換して利用

### 入力

- DB接続情報（host/port/database/user/password）
- ツールのパラメータスキーマ（名前・型・説明）
- 実行するSQL文（プレースホルダ$1, $2...でパラメータ参照）

### 出力

- 起動したMCPサーバー（HTTPエンドポイント）
- フレームワーク共通のツール定義（JSON Schema形式）
- ツール実行結果（クエリ結果のJSON）

## 使うツール・ライブラリ

- toolbox CLI（バイナリ/Docker/Homebrew/NPX）
- tools.yaml設定ファイル

## コード例

```
# tools.yaml
kind: source
name: my-pg-source
type: postgres
host: 127.0.0.1
port: 5432
database: toolbox_db
user: toolbox_user
password: my-password
---
kind: tool
name: search-hotels-by-name
type: postgres-sql
source: my-pg-source
description: Search for hotels based on name.
parameters:
  - name: name
    type: string
    description: The name of the hotel.
statement: SELECT * FROM hotels WHERE name ILIKE '%' || $1 || '%';

# 起動
toolbox --config tools.yaml

# Python利用側
from toolbox_core import ToolboxClient
async with ToolboxClient("http://127.0.0.1:5000") as client:
    tools = await client.load_toolset("toolset_name")
```

## 前提知識

- MCPプロトコルの基本概念（Model Context Protocol）
- LLMエージェントフレームワークの基礎（LangChain/LlamaIndex/Genkit等のいずれか）
- データベース接続の基本（PostgreSQL/MySQL等の接続文字列）
- YAMLの基本文法
- ツール呼び出しの仕組み（Function Calling）

## 根拠

> npx @toolbox-sdk/server --config tools.yaml - This runs the latest version of the toolbox server with your configuration file.
