# 環境変数でLLMプロバイダーを切り替える

> Gemini/OpenAI/OpenRouter/Z.aiを単一の環境変数で切り替え可能にする

- 出典: https://x.com/m72511taizo/status/2013246955351072909
- 投稿者: Shinji Kimura
- カテゴリ: other

## なぜ使うのか

コード変更なしでプロバイダー移行・A/Bテスト・フォールバックを実現するため

## いつ使うのか

プロバイダー依存を排除したい時、API障害時のフォールバック、コスト最適化のためのプロバイダー選択

### 具体的な適用場面

- 複数LLMプロバイダーを同時に評価し、タスク別に最適なモデルを選択したい
- 開発・レビュー・QAなど役割分担したエージェントチームで複雑なタスクを処理したい
- 過去の会話から関連知識を自動検索して文脈に注入したい
- 長時間稼働でトークン制限に達する前に会話履歴を自動圧縮したい

## やり方

1. `pip install moco-ai` でインストール 2. `.env` に `MOCO_PROVIDER=gemini` と `GEMINI_API_KEY=xxx` を設定（または `MOCO_PROVIDER=openai` + `OPENAI_API_KEY`）3. `moco run 'タスク'` で実行すると環境変数に応じたプロバイダーが使われる 4. CLIで `moco run --provider openai 'タスク'` と明示指定も可能

### 入力

- 環境変数 MOCO_PROVIDER (gemini/openai/openrouter/zai)
- 各プロバイダーのAPIキー環境変数

### 出力

- プロバイダー透過的なLLM応答

## 使うツール・ライブラリ

- moco-ai
- Gemini API
- OpenAI API
- OpenRouter API
- Z.ai API

## 前提知識

- Python 3.9以上の環境
- pip によるパッケージインストール知識
- 環境変数の設定方法（.envまたはシェル）
- YAML基本文法の理解
- LLM APIキーの取得方法（Gemini/OpenAI等）

## 根拠

> 新しいマルチエージェントフレームワーク「MOCO」を公開しました。GeminiやOpenAIとか複数のLLMを簡単にオーケストレーションできるやつです

> 開発、セキュリティ、税務とか、特定のドメインに特化したエージェントチームをサクッと作れます

> GitHub README: **🔄 Multi-provider Support**: Switch between Gemini, OpenAI, OpenRouter, and Z.ai via environment variables or CLI options

> GitHub README: **📦 Profile-based Configuration**: Define agents and tools for specific domains (development, security, tax, etc.) using YAML

> GitHub README: **🧠 Semantic Memory**: Automatically recall past knowledge and incidents using FAISS-based similarity search
