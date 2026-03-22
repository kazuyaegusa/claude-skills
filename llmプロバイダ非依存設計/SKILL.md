# LLMプロバイダ非依存設計

> Nous Portal/OpenRouter/z.ai/Kimi/MiniMax/OpenAI等のプロバイダを hermes model で切り替え、コード変更なしで200+モデルを利用可能

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

特定ベンダーロックインを避け、コスト・品質・速度でモデルを柔軟に選びたい。OpenRouterだけで200+モデルあり、タスクごとに最適モデルを選べる

## いつ使うのか

コスト削減・最新モデル試用・プロバイダ障害時のフォールバックが必要な場合

## やり方

1. hermes model でプロバイダ:モデル名を選択
2. 内部で統一インターフェース（おそらくLiteLLM or 独自ラッパー）
3. 設定ファイルに認証情報保存
4. 会話中でも /model [provider:model] で即座に切り替え可能

### 入力

- プロバイダのAPIキー
- モデル名

### 出力

- 統一されたLLM呼び出しインターフェース

## 使うツール・ライブラリ

- OpenRouter API
- LiteLLM（推測）
- 各プロバイダSDK

## コード例

```
hermes model openrouter:anthropic/claude-3.5-sonnet
# または会話中に
/model openrouter:google/gemini-2.0-flash-exp
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

> 「The self-improving AI agent built by Nous Research. It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge」

> 「Use any model you want — Nous Portal, OpenRouter (200+ models), z.ai/GLM, Kimi/Moonshot, MiniMax, OpenAI, or your own endpoint. Switch with hermes model — no code changes, no lock-in」

> 「Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall. Honcho dialectic user modeling」

> 「curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash」

> 「hermes claw migrate — Interactive migration (full preset) from OpenClaw」
