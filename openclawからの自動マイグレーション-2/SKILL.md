# OpenClawからの自動マイグレーション

> 既存のOpenClawユーザーの設定・メモリ・スキル・APIキーをHermes Agentに自動移行する

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動マイグレーションは手間がかかり、設定ミスのリスクがある。自動検出＋移行により、ユーザーはシームレスに移行できる

## いつ使うのか

OpenClawから移行したい場合

## やり方

1. `hermes setup` で `~/.openclaw` を自動検出
2. `hermes claw migrate` で移行を実行
3. SOUL.md（ペルソナ）、MEMORY.md/USER.md、スキル、コマンド許可リスト、メッセージング設定、APIキー、TTSアセット、AGENTS.mdを移行
4. `--dry-run` でプレビュー、`--preset user-data` でシークレット除外、`--overwrite` で競合上書き
5. `openclaw-migration` スキルで対話的ガイド

### 入力

- ~/.openclaw ディレクトリ

### 出力

- 移行されたHermes Agent設定・データ

## コード例

```
hermes claw migrate
hermes claw migrate --dry-run
hermes claw migrate --preset user-data
```

## 前提知識

- Linux/macOS/WSL2環境（WindowsネイティブはWSL2必須）
- git（インストールスクリプトの唯一の前提条件）
- LLMプロバイダーのAPIキー（Anthropic, OpenRouter, OpenAI等）
- （オプション）メッセージングプラットフォームのBot認証トークン
- （オプション）SSH/Daytona/Modal等のバックエンド認証情報

## 根拠

> "Use any model you want — Nous Portal, OpenRouter (200+ models), z.ai/GLM, Kimi/Moonshot, MiniMax, OpenAI, or your own endpoint. Switch with `hermes model` — no code changes, no lock-in."

> "hermes claw migrate — Interactive migration (full preset)"
