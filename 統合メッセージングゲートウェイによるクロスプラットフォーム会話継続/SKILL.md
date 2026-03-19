# 統合メッセージングゲートウェイによるクロスプラットフォーム会話継続

> 単一のゲートウェイプロセスでTelegram、Discord、Slack、WhatsApp、Signal、CLIから同一エージェントへアクセスし、音声メモ文字起こし・会話履歴共有を実現する

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

プラットフォームごとにボットを別々に立てると管理が煩雑で、会話履歴が分断される。統合ゲートウェイなら、どのプラットフォームから話しかけても同じエージェントが応答し、文脈が継続する

## いつ使うのか

複数のメッセージングプラットフォームから同一エージェントにアクセスしたいとき、音声入力を活用したいとき、どこからでも会話を継続したいとき

## やり方

1. `hermes gateway setup`で使いたいプラットフォーム（Telegram/Discord/Slack等）を設定
2. 各プラットフォームのAPIキー・Bot Token等を入力
3. `hermes gateway start`でゲートウェイプロセスを起動
4. TelegramやDiscordからボットにメッセージを送ると、同じエージェントが応答
5. 音声メモを送ると自動で文字起こしされて処理される
6. CLI（`hermes`）からも同じセッションにアクセス可能

### 入力

- 各プラットフォームのAPIキー・Bot Token
- 音声メモ（オプション）

### 出力

- クロスプラットフォーム統一エージェント
- 音声文字起こし
- 会話履歴共有

## 使うツール・ライブラリ

- Telegram Bot API
- Discord Bot
- Slack App
- WhatsApp
- Signal
- Hermes gateway

## コード例

```
hermes gateway setup
hermes gateway start
# Now talk to the agent from Telegram, Discord, CLI, etc.
```

## 前提知識

- Linux/macOS/WSL2環境（Windows nativeは非対応）
- git
- LLMプロバイダーAPIキー（OpenRouter/OpenAI/Anthropic/Kimi/MiniMax等のいずれか）
- Python 3.11+ (インストーラーが自動セットアップ)
- Node.js (インストーラーが自動セットアップ)
- Telegram/Discord等のBot Token（メッセージングゲートウェイ利用時）
- Daytona/Modalアカウント（サーバーレス利用時、オプション）

## 根拠

> 「Use any model you want — Nous Portal, OpenRouter (200+ models), z.ai/GLM, Kimi/Moonshot, MiniMax, OpenAI, or your own endpoint. Switch with `hermes model` — no code changes, no lock-in.」

> 「Works on Linux, macOS, and WSL2. The installer handles everything — Python, Node.js, dependencies, and the `hermes` command. No prerequisites except git.」

> 「Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity.」
