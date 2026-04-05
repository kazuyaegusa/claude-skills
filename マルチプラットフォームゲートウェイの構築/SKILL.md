# マルチプラットフォームゲートウェイの構築

> 単一のゲートウェイプロセスでTelegram/Discord/Slack/WhatsApp/Signal/Email/CLIから同一エージェントと会話できるようにする

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

ユーザーはプラットフォームを横断して活動するため、エージェントも同様に存在すべき。音声メモの文字起こしやクロスプラットフォーム会話継続も可能にする

## いつ使うのか

複数のメッセージングアプリからエージェントにアクセスしたい、音声入力を使いたい、会話を途切れさせたくない場合

## やり方

1. `hermes gateway setup` で各プラットフォームのBot認証を設定
2. `hermes gateway start` でゲートウェイプロセスを起動
3. 各プラットフォームのBotにメッセージを送ると同一エージェントインスタンスが応答
4. 音声メモはWhisper等で自動文字起こし
5. 会話履歴はプラットフォーム横断で共有
6. `/sethome` でホームプラットフォームを設定

### 入力

- 各プラットフォームのBot認証トークン
- ユーザーID（許可リスト）

### 出力

- 全プラットフォームで統一されたエージェント体験
- 文字起こしされた音声メモ
- クロスプラットフォーム会話履歴

## 使うツール・ライブラリ

- Telegram Bot API
- Discord API
- Slack API
- WhatsApp API
- Signal API
- Whisper（音声文字起こし）

## コード例

```
hermes gateway setup
hermes gateway start
```

## 前提知識

- Linux/macOS/WSL2環境（WindowsネイティブはWSL2必須）
- git（インストールスクリプトの唯一の前提条件）
- LLMプロバイダーのAPIキー（Anthropic, OpenRouter, OpenAI等）
- （オプション）メッセージングプラットフォームのBot認証トークン
- （オプション）SSH/Daytona/Modal等のバックエンド認証情報

## 根拠

> "Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity."

> "Use any model you want — Nous Portal, OpenRouter (200+ models), z.ai/GLM, Kimi/Moonshot, MiniMax, OpenAI, or your own endpoint. Switch with `hermes model` — no code changes, no lock-in."
