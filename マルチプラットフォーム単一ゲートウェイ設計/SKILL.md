# マルチプラットフォーム単一ゲートウェイ設計

> CLI/Telegram/Discord/Slack/WhatsApp/Signalを単一プロセスで統合し、どのプラットフォームからでも同じエージェントと会話できる

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

ユーザーは複数のメッセージングアプリを使い分けるため、プラットフォームごとにエージェントを立てると文脈が分断される。1つのゲートウェイで全て統合すれば、どこからでも同じ文脈を引き継げる。

## いつ使うのか

Telegram等のメッセージアプリから常駐エージェントを操作したい場合、複数のチャネルで同一エージェントを使いたい場合

## やり方

1. `hermes gateway setup`でプラットフォームを設定 2. `hermes gateway start`で単一ゲートウェイプロセス起動 3. 各プラットフォームからメッセージを受信 4. 音声メモは自動文字起こし 5. 会話履歴はプラットフォーム横断で共有

### 入力

- Telegram/Discord/Slack等のBot Token
- 音声メモ（自動文字起こし）

### 出力

- 統一された会話履歴
- プラットフォーム横断の応答

## 使うツール・ライブラリ

- hermes gateway

## コード例

```
hermes gateway setup
hermes gateway start
```

## 前提知識

- 基本的なコマンドライン操作
- LLM APIキー（OpenRouter/OpenAI/Anthropic等のいずれか）
- gitがインストールされた環境
- Linux/macOS/WSL2のいずれか

## 根拠

> Use any model you want — Nous Portal, OpenRouter (200+ models), z.ai/GLM, Kimi/Moonshot, MiniMax, OpenAI, or your own endpoint. Switch with `hermes model` — no code changes, no lock-in.

> Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity.
