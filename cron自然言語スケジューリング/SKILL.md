# cron自然言語スケジューリング

> 自然言語でタスクをスケジュール登録し、cron的に定期実行→結果を任意プラットフォームに配信

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

cronの文法は難解で、結果通知の配信設定も別途必要。自然言語で「毎日9時にレポート」→Telegramに送信まで一括設定できれば非エンジニアでも使える

## いつ使うのか

日次レポート、夜間バックアップ、週次監査等、定期的に無人実行したいタスクがある場合

## やり方

1. 自然言語でスケジュール指示（例: 'Daily at 9am, summarize my emails and send to Telegram'）
2. LLMがcron式 + タスクスクリプトに変換
3. 内部cronデーモンが定期実行
4. 実行結果を指定プラットフォーム（Telegram/Discord等）に配信

### 入力

- 自然言語スケジュール指示
- 配信先プラットフォーム

### 出力

- cron登録済みタスク
- 定期実行結果の配信

## 使うツール・ライブラリ

- cronライブラリ（Python schedule or APScheduler推測）
- ゲートウェイ配信機能

## コード例

```
# 内部cron登録例（conceptual）
schedule.every().day.at('09:00').do(lambda: agent.run_task('summarize_emails', deliver_to='telegram'))
```

## 前提知識

- Linux/macOS/WSL2環境（Windowsネイティブ非対応）
- gitインストール済み
- AIエージェント・LLM基礎知識（tool calling, context window等）
- ターミナル操作の基本（bash, curl等）
- 各メッセージングプラットフォームのBot API取得方法（Telegram/Discord等）
- （サーバーレス利用時）Daytona/ModalアカウントとAPI認証
- （LLM利用）OpenRouter/OpenAI等のAPIキー

## 根拠

> 「Six terminal backends — local, Docker, SSH, Daytona, Singularity, and Modal. Daytona and Modal offer serverless persistence — your agent's environment hibernates when idle and wakes on demand」

> 「Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity」
