# OpenClaw自動マイグレーション

> OpenClawの設定・メモリ・スキル・APIキーを自動インポート

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

既存ユーザーが手動で移行する手間を排除し、即座にHermes Agentで既存資産を活用できるようにするため。

## いつ使うのか

OpenClawから移行する場合

## やり方

1. `hermes claw migrate`実行（または初回セットアップ時に自動検出） 2. `~/.openclaw`を検出 3. SOUL.md/MEMORY.md/スキル/APIキー/メッセージング設定を自動インポート 4. `--dry-run`で事前確認可能

### 入力

- ~/.openclawディレクトリ

### 出力

- インポートされた設定・スキル・メモリ

## 使うツール・ライブラリ

- hermes claw migrate

## コード例

```
hermes claw migrate
hermes claw migrate --dry-run
```

## 前提知識

- 基本的なコマンドライン操作
- LLM APIキー（OpenRouter/OpenAI/Anthropic等のいずれか）
- gitがインストールされた環境
- Linux/macOS/WSL2のいずれか

## 根拠

> Use any model you want — Nous Portal, OpenRouter (200+ models), z.ai/GLM, Kimi/Moonshot, MiniMax, OpenAI, or your own endpoint. Switch with `hermes model` — no code changes, no lock-in.
