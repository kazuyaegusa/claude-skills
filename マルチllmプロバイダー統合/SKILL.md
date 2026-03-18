# マルチLLMプロバイダー統合

> OpenAI、Anthropic、Ollama（ローカル）、AWS Bedrock、Azure等のLLMを統一インターフェースで切り替え・監視する

- 出典: https://github.com/langfuse/langfuse
- 投稿者: langfuse
- カテゴリ: infrastructure

## なぜ使うのか

プロバイダーをロックインせず、コスト・レイテンシ・品質で最適なモデルを選択できるようにし、全てのトレースを単一基盤で比較可能にするため

## いつ使うのか

複数LLMプロバイダーを試したい時、コスト削減のためモデルを切り替えたい時、ローカルLLMと商用APIを混在させたい時

## やり方

1. LiteLLM統合を利用すると100以上のLLMをdrop-in replacementで呼び出し可能
2. Langfuse SDKでLiteLLM呼び出しを自動トレース
3. または、Vercel AI SDK、Haystack、MastraなどフレームワークのLangfuse統合を活用
4. トレース上でモデル名・コスト・レイテンシを比較し、最適プロバイダーを選定

### 入力

- 各LLMプロバイダーのAPI key（または自己ホストエンドポイント）
- LiteLLM/Vercel AI SDK等の統合ライブラリ

### 出力

- プロバイダー横断のトレースログ
- モデル別コスト・レイテンシ・品質の比較データ

## 使うツール・ライブラリ

- LiteLLM
- Vercel AI SDK
- Haystack
- Mastra
- Langfuse統合SDK

## コード例

```
# LiteLLM + Langfuseの統合例（ドキュメント参照）
# import litellm
# from langfuse.litellm import LangfuseLogger
# litellm.success_callback = [LangfuseLogger()]
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
