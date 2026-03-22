# 統一メッセージングゲートウェイ

> Telegram/Discord/Slack/WhatsApp/Signal/CLI/Emailを単一ゲートウェイプロセスで処理し、音声メモ文字起こし・会話継続性を提供

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

プラットフォームごとにボットを別々に立てると管理が煩雑。1プロセスで全プラットフォームを統合すれば、同一エージェント状態を全チャネルで共有でき、音声入力も一元処理できる

## いつ使うのか

モバイル/デスクトップ/チーム用チャット等、複数環境から同一エージェントにアクセスしたい場合

## やり方

1. hermes gateway setup で各プラットフォームのトークン設定
2. hermes gateway start で統一ゲートウェイ起動
3. 各プラットフォームからのメッセージを内部キューで受信
4. 音声メモは自動文字起こし→テキストとして処理
5. セッションIDで会話継続性を保証（プラットフォーム跨ぎ可）

### 入力

- 各プラットフォームのAPIトークン
- 音声メモファイル（任意）

### 出力

- 全プラットフォームで共通の会話履歴
- 文字起こし済みテキスト

## 使うツール・ライブラリ

- Telegram Bot API
- Discord.py
- Slack SDK
- Twilio（WhatsApp/Signal）
- 音声文字起こしライブラリ（未明記、おそらくWhisper等）

## コード例

```
# ゲートウェイ起動（conceptual）
hermes gateway start
# 内部的にはasyncio event loop
async def handle_message(platform, message):
    session = get_or_create_session(platform, user_id)
    if message.is_voice:
        text = transcribe(message.audio)
    else:
        text = message.text
    await agent.process(session, text)
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

> 「Use any model you want — Nous Portal, OpenRouter (200+ models), z.ai/GLM, Kimi/Moonshot, MiniMax, OpenAI, or your own endpoint. Switch with hermes model — no code changes, no lock-in」

> 「Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity」

> 「curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash」

> 「hermes claw migrate — Interactive migration (full preset) from OpenClaw」
