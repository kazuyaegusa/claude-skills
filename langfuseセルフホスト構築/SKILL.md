# Langfuseセルフホスト構築

> Langfuseをローカル/VM/Kubernetesで自前インフラ上に5分～30分でデプロイし、外部SaaS依存なしで運用する

- 出典: https://github.com/langfuse/langfuse
- 投稿者: langfuse
- カテゴリ: infrastructure

## なぜ使うのか

データ主権・コンプライアンス・コスト最適化のため、LLMの入出力ログを自社インフラに閉じて保存・分析したいため

## いつ使うのか

Langfuse Cloudの無料枠を超える規模になった時、または最初からセキュリティ要件で外部SaaS利用が許可されない時

## やり方

1. リポジトリをclone (`git clone https://github.com/langfuse/langfuse.git`)
2. ローカルならDocker Composeで起動 (`docker compose up`)
3. 本番環境ならKubernetesにHelm chartデプロイ、またはAWS/Azure/GCP TerraformテンプレートでIaCデプロイ
4. 環境変数で認証・DB接続（ClickHouse推奨）を設定
5. Langfuse Web UIにアクセスしてプロジェクト作成・API key発行

### 入力

- Docker/Kubernetes環境
- ClickHouse（推奨）またはPostgreSQL互換DB
- Terraformコード（AWS/Azure/GCP環境の場合）

### 出力

- 稼働中のLangfuse Webサーバー（UI + API）
- 自社インフラ内のトレース・評価データDB

## 使うツール・ライブラリ

- Docker/Docker Compose
- Kubernetes + Helm
- Terraform (AWS/Azure/GCP)
- ClickHouse (推奨データベース)

## コード例

```
# ローカル起動
git clone https://github.com/langfuse/langfuse.git
cd langfuse
docker compose up
```

## 前提知識

- LLMアプリケーション開発の基礎知識（OpenAI API、LangChain/LlamaIndex等のフレームワーク）
- Docker/Kubernetes等のコンテナ環境の基本操作（セルフホスト時）
- Python/TypeScript/JavaScriptのいずれかでのコーディング経験
- トレーシング・オブザーバビリティの基本概念（span、trace、loggingの違い）
- プロンプトエンジニアリング・評価手法（LLM-as-a-judge等）の理解

## 根拠

> "Langfuse is an open source LLM engineering platform. It helps teams collaboratively develop, monitor, evaluate, and debug AI applications. Langfuse can be self-hosted in minutes and is battle-tested."

> "LLM Application Observability: Instrument your app and start ingesting traces to Langfuse, thereby tracking LLM calls and other relevant logic in your app such as retrieval, embedding, or agent actions."

> "Evaluations are key to the LLM application development workflow, and Langfuse adapts to your needs. It supports LLM-as-a-judge, user feedback collection, manual labeling, and custom evaluation pipelines via APIs/SDKs."

> "Self-Host Langfuse: Run Langfuse on your own infrastructure: Local (docker compose): Run Langfuse on your own machine in 5 minutes using Docker Compose. VM, Kubernetes (Helm), Terraform Templates: AWS, Azure, GCP"

> "Top open-source Python projects that use Langfuse, ranked by stars: langflow-ai/langflow (116251 stars), open-webui/open-webui (109642 stars), abi/screenshot-to-code (70877 stars), lobehub/lobe-chat (65454 stars), infiniflow/ragflow (64118 stars), etc."
