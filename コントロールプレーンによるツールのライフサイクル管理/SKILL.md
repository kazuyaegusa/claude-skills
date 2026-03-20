# コントロールプレーンによるツールのライフサイクル管理

> Toolboxサーバーを中央コントロールプレーンとして、複数のアプリケーション・エージェントが同一のツールを参照し、ツール更新を一元管理する

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: agent-orchestration

## なぜ使うのか

ツールが各アプリケーションに分散せず中央管理されるため、バージョン管理・権限制御・監査ログが容易になり、エンタープライズ要件を満たせる

## いつ使うのか

複数のマイクロサービスやエージェントが同じツールを使う場合、ツールのバージョン管理と監査が必要な場合、ツールの段階的ロールアウトをしたい場合

## やり方

1. Toolboxサーバーを本番環境にデプロイ（Cloud Run、Kubernetes、VM等）
2. 複数のアプリケーション・エージェントが同一のToolboxエンドポイントを参照
3. ツール更新時は`tools.yaml`を編集してサーバーをリロード（または再起動）
4. 全クライアントが次回呼び出し時に自動的に新バージョンを使用
5. OpenTelemetryでツール使用状況をモニタリング

### 入力

- tools.yamlの更新
- OpenTelemetryエクスポーター設定（オプション）

### 出力

- 一元化されたツール管理
- メトリクス・トレーシングデータ

## 使うツール・ライブラリ

- MCP Toolbox server
- OpenTelemetry
- Docker/Kubernetes/Cloud Run

## コード例

```
# Dockerで本番デプロイ
export VERSION=0.29.0
docker run -p 5000:5000 \
  -v $(pwd)/tools.yaml:/app/tools.yaml \
  us-central1-docker.pkg.dev/database-toolbox/toolbox/toolbox:$VERSION \
  --tools-file /app/tools.yaml
```

## 前提知識

- Model Context Protocol (MCP)の基本概念
- AIエージェントフレームワーク（LangChain、LlamaIndex、Genkit等）の基礎知識
- データベース接続の基本（PostgreSQL、MySQL、Spanner、BigQuery等）
- YAML形式の読み書き
- Docker/コンテナ技術の基礎（本番デプロイ時）
- OpenTelemetryによる可観測性の概念（本番運用時）
