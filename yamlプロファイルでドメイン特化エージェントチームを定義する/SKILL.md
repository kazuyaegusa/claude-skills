# YAMLプロファイルでドメイン特化エージェントチームを定義する

> 開発・セキュリティ・税務など特定領域に特化した複数エージェントとツールをYAMLで宣言的に定義する

- 出典: https://x.com/m72511taizo/status/2013246955351072909
- 投稿者: Shinji Kimura
- カテゴリ: agent-orchestration

## なぜ使うのか

ドメイン知識・役割・利用ツールをコードから分離し、非エンジニアでも編集可能にするため

## いつ使うのか

複数の専門役割が必要なタスク、チーム構成を頻繁に変更したい、ドメインごとに異なるツールセットが必要

### 具体的な適用場面

- 複数LLMプロバイダーを同時に評価し、タスク別に最適なモデルを選択したい
- 開発・レビュー・QAなど役割分担したエージェントチームで複雑なタスクを処理したい
- 過去の会話から関連知識を自動検索して文脈に注入したい
- 長時間稼働でトークン制限に達する前に会話履歴を自動圧縮したい

## やり方

1. `profiles/development.yaml` を作成 2. `agents:` セクションに `- name: developer
  role: コード実装
  tools: [file_editor, git]` のように定義 3. `tools:` セクションで各ツールの実装クラスを指定 4. `moco run --profile development '新機能実装'` で起動するとYAMLで定義したエージェントチームが協調動作

### 入力

- YAMLプロファイルファイル（エージェント・ツール定義）
- 実行タスクの指示文

### 出力

- マルチエージェント協調による実行結果
- 各エージェントの会話ログ

## 使うツール・ライブラリ

- moco-ai
- YAML

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
