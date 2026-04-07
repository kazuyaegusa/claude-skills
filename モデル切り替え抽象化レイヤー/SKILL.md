# モデル切り替え抽象化レイヤー

> `hermes model`で200+のLLMプロバイダを自由に切り替え、コード変更なしで動作

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

OpenAI以外のモデル（Kimi/MiniMax/OpenRouter等）を試したい、コスト最適化したい、特定タスクで最適なモデルを選びたい場合に必要。

## いつ使うのか

複数のLLMプロバイダを試したい場合、ベンダーロックインを避けたい場合、タスクごとに最適なモデルを使い分けたい場合

## やり方

1. `hermes model`で対話的にプロバイダ・モデル選択 2. 設定ファイルに保存 3. 以降の会話は選択したモデルで実行 4. いつでも`hermes model [provider:model]`で切り替え可能

### 入力

- LLMプロバイダのAPIキー

### 出力

- プロバイダ・モデル設定
- 切り替え可能な推論バックエンド

## 使うツール・ライブラリ

- OpenRouter（200+モデル）
- Kimi/Moonshot
- MiniMax
- z.ai/GLM
- Nous Portal
- OpenAI

## コード例

```
hermes model
hermes model openrouter:anthropic/claude-3.5-sonnet
```

## 前提知識

- 基本的なコマンドライン操作
- LLM APIキー（OpenRouter/OpenAI/Anthropic等のいずれか）
- gitがインストールされた環境
- Linux/macOS/WSL2のいずれか

## 根拠

> It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions.

> Use any model you want — Nous Portal, OpenRouter (200+ models), z.ai/GLM, Kimi/Moonshot, MiniMax, OpenAI, or your own endpoint. Switch with `hermes model` — no code changes, no lock-in.
