# トークン制限前に会話履歴を自動圧縮する

> 会話が長くなりトークン上限に近づくと、古い履歴を自動要約して文脈を保ちながらトークン数を削減する

- 出典: https://x.com/m72511taizo/status/2013246955351072909
- 投稿者: Shinji Kimura
- カテゴリ: other

## なぜ使うのか

長時間稼働やマルチターン対話でトークン制限エラーを回避し、重要な文脈は保持するため

## いつ使うのか

長時間の対話セッション、大量のコード生成タスク、トークン制限が厳しいモデル使用時

### 具体的な適用場面

- 複数LLMプロバイダーを同時に評価し、タスク別に最適なモデルを選択したい
- 開発・レビュー・QAなど役割分担したエージェントチームで複雑なタスクを処理したい
- 過去の会話から関連知識を自動検索して文脈に注入したい
- 長時間稼働でトークン制限に達する前に会話履歴を自動圧縮したい

## やり方

1. MOCOが内部でトークン数を監視 2. 設定した閾値（例: 80%）に達すると古い会話ブロックを要約APIで圧縮 3. 圧縮後のサマリーを履歴に保持し、生データは削除 4. 圧縮設定は `config.yaml` で `memory.compression.enabled: true` と `threshold_ratio: 0.8` で調整可能

### 入力

- 累積会話履歴
- トークン制限設定値

### 出力

- 圧縮された会話履歴（要約形式）
- トークン制限内での継続的な対話

## 使うツール・ライブラリ

- moco-ai

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
