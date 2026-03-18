# Langfuse自動トレーシング実装

> LLMアプリケーションの全実行フローを自動でトレースし、各LLM呼び出し・retrieval・embedding・agent actionを記録する

- 出典: https://github.com/langfuse/langfuse
- 投稿者: langfuse
- カテゴリ: agent-orchestration

## なぜ使うのか

デバッグ・パフォーマンス分析・コスト管理のために、誰がいつどのプロンプトでLLMを呼び、どんな結果が返ったかを追跡可能にする必要があるため

## いつ使うのか

LLMアプリを本番環境にデプロイする前、または既にデプロイ済みでデバッグ・監視基盤が必要になった時

## やり方

1. Langfuse SDKをインストール (`pip install langfuse openai`)
2. 環境変数にLangfuse認証情報をセット (LANGFUSE_SECRET_KEY, LANGFUSE_PUBLIC_KEY, LANGFUSE_BASE_URL)
3. コード内で `from langfuse.openai import openai` のようにdrop-in replacementでOpenAI SDKをラップ
4. 関数に `@observe()` デコレーターを付与することで自動的にトレーシング開始
5. Langfuse UIで trace/span/タイムスタンプ/入出力を確認

### 入力

- LangfuseプロジェクトのAPI認証情報（Cloudまたはself-hostedインスタンス）
- LLM呼び出しを含むPython/JS/TSアプリケーションコード

### 出力

- Langfuse UIで閲覧可能なトレース（各LLM呼び出しの入出力・レイテンシ・コスト・モデルパラメータ）
- ユーザーセッション単位のログ・複雑なマルチステップ実行の可視化

## 使うツール・ライブラリ

- langfuse (Python SDK)
- langfuse-openai (OpenAI統合)
- langfuse-langchain (LangChain統合)
- langfuse-llama-index (LlamaIndex統合)

## コード例

```
from langfuse import observe
from langfuse.openai import openai

@observe()
def story():
    return openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "What is Langfuse?"}],
    ).choices[0].message.content

@observe()
def main():
    return story()

main()
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
