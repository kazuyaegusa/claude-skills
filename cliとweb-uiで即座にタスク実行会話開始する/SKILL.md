# CLIとWeb UIで即座にタスク実行・会話開始する

> ターミナルから `moco run` でタスク即実行、`moco chat` で対話開始、`moco ui` でブラウザUI起動が可能

- 出典: https://x.com/m72511taizo/status/2013246955351072909
- 投稿者: Shinji Kimura
- カテゴリ: dev-tool

## なぜ使うのか

開発者はCLI、非技術者はブラウザUIと、利用者に応じたインターフェースを提供するため

## いつ使うのか

CLIスクリプト統合、非エンジニア向けUI提供、バックグラウンドタスク監視が必要

### 具体的な適用場面

- 複数LLMプロバイダーを同時に評価し、タスク別に最適なモデルを選択したい
- 開発・レビュー・QAなど役割分担したエージェントチームで複雑なタスクを処理したい
- 過去の会話から関連知識を自動検索して文脈に注入したい
- 長時間稼働でトークン制限に達する前に会話履歴を自動圧縮したい

## やり方

1. `pip install moco-ai` 後、`moco run 'Pythonでクイックソート実装'` でワンショット実行 2. `moco chat` で対話モード起動、複数ターンの指示が可能 3. `moco ui` でローカルWebサーバー起動、ブラウザで http://localhost:8000 にアクセス 4. バックグラウンドタスクは `moco run --background` で実行し `moco status` で監視

### 入力

- タスク指示文（文字列）
- 対話形式の場合は複数ターンの入力

### 出力

- タスク実行結果（標準出力またはブラウザ表示）
- 実行ログ

## 使うツール・ライブラリ

- moco-ai
- Python 3.9+

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
