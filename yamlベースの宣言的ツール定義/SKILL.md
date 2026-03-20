# YAMLベースの宣言的ツール定義

> データベースツールをYAML形式で定義し、複数フレームワーク・言語で再利用可能な形式で管理する

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: agent-orchestration

## なぜ使うのか

ツール定義をアプリケーションコードから分離することで、ツールの更新・バージョン管理・共有が容易になり、複数のエージェントやフレームワーク間で一貫性を保てる

## いつ使うのか

複数のAIフレームワークや言語でデータベースツールを共有したい時、ツール定義を中央管理したい時

## やり方

1. `tools.yaml`に`sources`セクションでデータベース接続情報を定義
2. `tools`セクションで各ツールのtype（postgres-sql等）、source、description、parameters、statementを記述
3. `toolsets`セクションでツールをグループ化
4. Toolboxサーバーを`toolbox --tools-file tools.yaml`で起動
5. クライアントSDKから`client.load_toolset('toolset_name')`でツールを読み込み

### 入力

- データベース接続情報（host, port, database, user, password）
- SQLクエリまたはツールロジック
- パラメータ定義（name, type, description）

### 出力

- フレームワーク非依存のツール定義
- MCPプロトコル経由でアクセス可能なツールエンドポイント

## 使うツール・ライブラリ

- MCP Toolbox server
- tools.yaml

## コード例

```
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
```

## 前提知識

- Model Context Protocol (MCP)の基本概念
- AIエージェントフレームワーク（LangChain、LlamaIndex、Genkit等）の基礎知識
- データベース接続の基本（PostgreSQL、MySQL、Spanner、BigQuery等）
- YAML形式の読み書き
- Docker/コンテナ技術の基礎（本番デプロイ時）
- OpenTelemetryによる可観測性の概念（本番運用時）
