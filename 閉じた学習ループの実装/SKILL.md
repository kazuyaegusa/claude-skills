# 閉じた学習ループの実装

> エージェントが経験から自律的にスキルを生成・改善し、記憶を整理・検索し、ユーザーモデルを深化させる仕組みを構築する

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

単なる会話履歴保持では知識が散逸し、同じ失敗を繰り返す。学習ループを閉じることで、セッション跨ぎで能力が向上し、ユーザー固有の文脈を理解できる

## いつ使うのか

エージェントに単発タスクではなく、継続的に学習・進化してほしい場合

## やり方

1. 複雑タスク完了後に自動的にスキルを生成（autonomous skill creation）
2. スキル使用中にLLMが改善点を検出し自己改善（skills self-improve during use）
3. 定期的に記憶整理を促すナッジを発行（periodic nudges for agent-curated memory）
4. FTS5全文検索でLLMサマリーを使って過去会話を検索（FTS5 session search with LLM summarization）
5. Honcho dialecticでユーザーモデルを対話的に構築・更新
6. agentskills.io標準に準拠してスキルを保存

### 入力

- 複雑なタスク実行履歴
- ユーザーとの対話履歴
- スキル改善のフィードバック

### 出力

- 自動生成されたスキル（agentskills.io準拠）
- 改善されたスキル
- 整理された記憶
- ユーザーモデル

## 使うツール・ライブラリ

- FTS5（SQLiteの全文検索拡張）
- Honcho（dialectic user modeling）
- agentskills.io（スキル標準）

## 前提知識

- Linux/macOS/WSL2環境（WindowsネイティブはWSL2必須）
- git（インストールスクリプトの唯一の前提条件）
- LLMプロバイダーのAPIキー（Anthropic, OpenRouter, OpenAI等）
- （オプション）メッセージングプラットフォームのBot認証トークン
- （オプション）SSH/Daytona/Modal等のバックエンド認証情報

## 根拠

> "It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions."

> "Six terminal backends — local, Docker, SSH, Daytona, Singularity, and Modal. Daytona and Modal offer serverless persistence — your agent's environment hibernates when idle and wakes on demand, costing nearly nothing between sessions."

> "Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall. Honcho dialectic user modeling."

> "Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity."

> "Use any model you want — Nous Portal, OpenRouter (200+ models), z.ai/GLM, Kimi/Moonshot, MiniMax, OpenAI, or your own endpoint. Switch with `hermes model` — no code changes, no lock-in."
