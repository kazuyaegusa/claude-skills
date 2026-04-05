# cron的な定期自動化の組み込み

> 自然言語でスケジュール可能なcron機能を内蔵し、任意のプラットフォームに配信できるようにする

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェントは対話だけでなく、無人で定期実行すべきタスク（レポート生成、バックアップ、監査）も担うべき。自然言語でスケジュール指定できれば、プログラミング不要で自動化できる

## いつ使うのか

日次レポート、夜間バックアップ、週次監査など、無人定期実行が必要な場合

## やり方

1. cron schedulerをエージェントに統合
2. 自然言語でスケジュール指定（例: 「毎日9時にレポート作成してSlackに送る」）
3. 指定時刻にタスクを実行
4. 結果を指定プラットフォーム（Telegram/Discord/Slack等）に配信
5. `hermes cron` コマンドでスケジュール管理

### 入力

- タスク内容（自然言語）
- スケジュール（cron式または自然言語）
- 配信先プラットフォーム

### 出力

- 定期実行されたタスク結果
- 指定プラットフォームへの配信

## 使うツール・ライブラリ

- cronライブラリ（詳細不明）

## 前提知識

- Linux/macOS/WSL2環境（WindowsネイティブはWSL2必須）
- git（インストールスクリプトの唯一の前提条件）
- LLMプロバイダーのAPIキー（Anthropic, OpenRouter, OpenAI等）
- （オプション）メッセージングプラットフォームのBot認証トークン
- （オプション）SSH/Daytona/Modal等のバックエンド認証情報

## 根拠

> "Use any model you want — Nous Portal, OpenRouter (200+ models), z.ai/GLM, Kimi/Moonshot, MiniMax, OpenAI, or your own endpoint. Switch with `hermes model` — no code changes, no lock-in."

> "Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly audits — all in natural language, running unattended."
