# Prompt Management統合

> プロンプトをコードから分離してLangfuse UIで一元管理し、バージョン管理・A/Bテスト・リアルタイム更新を可能にする

- 出典: https://github.com/langfuse/langfuse
- 投稿者: langfuse
- カテゴリ: prompt-engineering

## なぜ使うのか

プロンプトをコードにハードコードすると、変更の度にデプロイが必要になり、バージョン履歴も残らない。中央管理すればノンエンジニアでも改善サイクルを回せるため

## いつ使うのか

プロンプトを頻繁に改善したい時、複数チームで共同編集したい時、A/Bテストで効果測定したい時

## やり方

1. Langfuse UIでプロンプトテンプレートを作成・バージョン登録
2. アプリケーションコードから `langfuse.get_prompt(name, version)` APIでプロンプトをフェッチ
3. サーバー・クライアント側で強力にキャッシュされるため、レイテンシ影響は最小限
4. UIで新バージョン公開→アプリは次回フェッチ時に自動的に最新版を取得
5. トレース上でどのプロンプトバージョンが使われたかを記録・分析

### 入力

- Langfuseプロジェクト
- プロンプトテンプレート（変数プレースホルダー含む）

### 出力

- バージョン管理されたプロンプト
- トレースとプロンプトバージョンの紐付け
- プロンプト変更時のデプロイ不要のホット更新

## 使うツール・ライブラリ

- langfuse SDK (get_prompt API)
- Langfuse Web UI

## コード例

```
# 例（Pythonコード内）
from langfuse import Langfuse
client = Langfuse()
prompt = client.get_prompt("my-prompt", version=2)
messages = prompt.compile(user_input="example")
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

> "Prompt Management helps you centrally manage, version control, and collaboratively iterate on your prompts. Thanks to strong caching on server and client side, you can iterate on prompts without adding latency to your application."

> "Evaluations are key to the LLM application development workflow, and Langfuse adapts to your needs. It supports LLM-as-a-judge, user feedback collection, manual labeling, and custom evaluation pipelines via APIs/SDKs."

> "Self-Host Langfuse: Run Langfuse on your own infrastructure: Local (docker compose): Run Langfuse on your own machine in 5 minutes using Docker Compose. VM, Kubernetes (Helm), Terraform Templates: AWS, Azure, GCP"
