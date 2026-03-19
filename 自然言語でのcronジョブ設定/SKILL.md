# 自然言語でのcronジョブ設定

> チャットから自然言語でスケジュールタスクを登録し、定時実行させる。

- 出典: https://github.com/chenhg5/cc-connect
- 投稿者: chenhg5
- カテゴリ: agent-orchestration

## なぜ使うのか

cron構文は覚えにくく、エンジニアでも設定ミスが多い。自然言語で「毎朝6時にGitHub trendingをまとめて」と指示できれば、非エンジニアでも自動化タスクを設定できる。

## いつ使うのか

定期的な情報収集・レポート生成・監視タスクを自動化したい時。

## やり方

1. チャットで `/cron add 0 6 * * * Summarize GitHub trending` を実行
2. cc-connectがcron式と自然言語タスクを解釈し、内部スケジューラに登録
3. 指定時刻になると、AIエージェントに自動的にプロンプトが送信され、結果がチャットに返信される

### 入力

- cron式（0 6 * * * = 毎日6:00）
- 実行させたいタスクの自然言語記述

### 出力

- 指定時刻にAIエージェントがタスクを実行し、チャットに結果を送信

## 使うツール・ライブラリ

- cc-connect内蔵スケジューラ

## コード例

```
/cron add 0 6 * * * Summarize GitHub trending
/cron add 0 */2 * * * Check server logs for errors
```

## 前提知識

- ローカルマシンにNode.js or Go環境（cc-connectインストールに必要）
- Claude Code, Cursor, Gemini CLI等のAIエージェントがインストール済みであること
- メッセンジャープラットフォーム（Telegram/Slack/Discord等）のBot Token取得方法の基礎知識
- TOML形式の設定ファイル編集スキル
- WebSocket/Long Polling等の接続方式の概念理解（必須ではないが理解があると設定が楽）

## 根拠

> 「/cron add 0 6 * * * Summarize GitHub trending」（自然言語cron設定例）
