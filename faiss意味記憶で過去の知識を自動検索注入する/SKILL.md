# FAISS意味記憶で過去の知識を自動検索・注入する

> 会話履歴をベクトル化してFAISSに保存し、新しいタスク実行時に類似した過去の知識を自動で文脈に追加する

- 出典: https://x.com/m72511taizo/status/2013246955351072909
- 投稿者: Shinji Kimura
- カテゴリ: context-management

## なぜ使うのか

毎回同じ説明をさせず、過去の失敗・成功事例を活用して品質を向上させるため

## いつ使うのか

繰り返し似たタスクを実行する、過去のトラブルシューティング事例を参照したい、長期稼働で知識を蓄積したい

### 具体的な適用場面

- 複数LLMプロバイダーを同時に評価し、タスク別に最適なモデルを選択したい
- 開発・レビュー・QAなど役割分担したエージェントチームで複雑なタスクを処理したい
- 過去の会話から関連知識を自動検索して文脈に注入したい
- 長時間稼働でトークン制限に達する前に会話履歴を自動圧縮したい

## やり方

1. MOCOは自動で `.moco/memory/` にFAISSインデックスを作成 2. 会話終了時に重要な知見を自動抽出してベクトル化・保存 3. 新しいタスク開始時、タスク内容をクエリとして類似検索を実行 4. 上位K件の過去知識を「以前の学習内容」として文脈に注入 5. 設定は不要、自動で動作

### 入力

- 過去の会話履歴（自動保存）
- 新しいタスクのクエリ文

### 出力

- 類似度の高い過去知識の自動注入
- 文脈に基づいた精度の高い応答

## 使うツール・ライブラリ

- moco-ai
- FAISS
- sentence-transformers（推定）

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
