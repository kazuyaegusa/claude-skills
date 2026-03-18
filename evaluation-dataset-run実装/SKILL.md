# Evaluation & Dataset Run実装

> テストセット（Dataset）を作成し、LLM-as-a-judge/ユーザーフィードバック/カスタム評価スクリプトで継続的に品質評価する

- 出典: https://github.com/langfuse/langfuse
- 投稿者: langfuse
- カテゴリ: prompt-engineering

## なぜ使うのか

LLMアプリの品質は定性的になりがちだが、ベンチマーク化しないとプロンプト変更の効果測定ができず、リグレッションも防げないため

## いつ使うのか

プロンプト改善前にリグレッションテストしたい時、本番デプロイ前に品質保証したい時、A/Bテストで勝者を決めたい時

## やり方

1. Langfuse UIまたはAPIでDatasetを作成し、入力例と期待出力をアイテム登録
2. Dataset Run APIを使い、各アイテムに対してLLM実行→結果を記録
3. LangfuseのEvaluation機能で、LLM-as-a-judgeによる自動評価、ユーザー手動レーティング、カスタムスコアリングを実施
4. Playground UIでトレース結果を見てすぐに改善テスト
5. 定期的にDataset Runを実行し、プロンプト変更前後でスコアを比較

### 入力

- 評価用テストセット（入力・期待出力）
- 評価基準（LLM-as-a-judge用プロンプト、またはカスタムスコアリング関数）

### 出力

- Dataset Run結果（各アイテムのスコア・合格率）
- トレースとスコアの紐付け
- 改善効果の定量レポート

## 使うツール・ライブラリ

- Langfuse Datasets API
- Langfuse Evaluation API
- Langfuse Playground (UI)

## コード例

```
# Dataset Runの概念（詳細はドキュメント参照）
# 1. Dataset作成
# 2. for item in dataset:
#      output = run_llm(item.input)
#      langfuse.score(run_id, score=evaluate(output, item.expected))
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

> "Datasets enable test sets and benchmarks for evaluating your LLM application. They support continuous improvement, pre-deployment testing, structured experiments, flexible evaluation, and seamless integration with frameworks like LangChain and LlamaIndex."

> "Self-Host Langfuse: Run Langfuse on your own infrastructure: Local (docker compose): Run Langfuse on your own machine in 5 minutes using Docker Compose. VM, Kubernetes (Helm), Terraform Templates: AWS, Azure, GCP"
