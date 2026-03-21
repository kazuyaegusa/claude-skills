# MCP Toolboxサーバーを起動してツールを提供する

> tools.yamlでツール定義を記述し、toolboxバイナリまたはnpxでMCPサーバーを起動する

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: agent-orchestration

## なぜ使うのか

ツール定義を一元管理し、複数のAIエージェント・フレームワークから再利用可能にするため。また、アプリケーション側に接続管理やセキュリティロジックを書かずに済む

## いつ使うのか

AIエージェントにデータベースアクセス機能を追加したい時、複数フレームワークでツールを共有したい時

## やり方

1. tools.yamlにsources（データベース接続情報）とtools（SQL文・パラメータ定義）を記述
2. バイナリの場合: `./toolbox --tools-file tools.yaml` でサーバー起動
3. npxの場合: `npx @toolbox-sdk/server --tools-file tools.yaml` で起動
4. デフォルトでポート5000で起動し、動的リロードが有効（--disable-reloadで無効化可能）

### 入力

- tools.yaml（sources, tools, toolsets定義）
- データベース接続情報（host, port, database, user, password）

### 出力

- ポート5000（デフォルト）で稼働するMCPサーバー
- HTTP経由で利用可能なツールエンドポイント

## 使うツール・ライブラリ

- toolboxバイナリ（Linux/macOS/Windows用）
- @toolbox-sdk/server（npm）
- Docker（オプション）

## コード例

```
# tools.yaml例
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

# サーバー起動
./toolbox --tools-file tools.yaml
```

## 前提知識

- MCPプロトコルの基本概念（サーバー・クライアント・ツール）
- 使用するデータベース（PostgreSQL/MySQL/BigQuery等）の接続情報
- AIフレームワーク（LangChain/LlamaIndex/Genkit等）の基本的な使い方
- YAML形式の理解
- 非同期処理（async/await）の理解（Python/JS SDKを使う場合）

## 根拠

> 「By connecting your IDE to your databases with MCP Toolbox, you can delegate complex and time-consuming database tasks」

> 現在beta版、v1.0までは破壊的変更の可能性あり（「MCP Toolbox for Databases is currently in beta, and may see breaking changes until the first stable release (v1.0).」）
