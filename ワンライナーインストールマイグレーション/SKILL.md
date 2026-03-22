# ワンライナーインストール+マイグレーション

> curl | bash で全依存（Python/Node.js/hermes CLI）を自動インストールし、OpenClawからの設定・メモリ・スキル移行も自動

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェント導入のハードルは初期設定。既存ツール（OpenClaw）からの移行パスがないと乗り換えコストが高い。ワンライナー+自動マイグレーションで移行障壁を最小化

## いつ使うのか

新規導入時、またはOpenClawから移行したい場合

## やり方

1. curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash 実行
2. インストーラーがPython/Node.js/依存を自動セットアップ
3. hermes setup 初回起動時に ~/.openclaw 検出→自動マイグレーション提案
4. SOUL.md/MEMORY.md/USER.md/スキル/APIキーを一括インポート
5. hermes claw migrate --dry-run で事前確認可能

### 入力

- 既存OpenClaw設定ディレクトリ（任意）

### 出力

- インストール済みhermes環境
- 移行済み設定・メモリ・スキル

## 使うツール・ライブラリ

- Bashインストールスクリプト
- Python/Node.jsインストーラー

## コード例

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
hermes
# OpenClawマイグレーション
hermes claw migrate --dry-run
hermes claw migrate --overwrite
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

> 「curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash」

> 「hermes claw migrate — Interactive migration (full preset) from OpenClaw」
