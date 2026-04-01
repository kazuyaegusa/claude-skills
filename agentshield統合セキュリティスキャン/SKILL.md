# AgentShield統合セキュリティスキャン

> CLAUDE.md/settings.json/hooks/MCP設定を1282テスト・102ルールで静的解析し、秘密情報・権限過剰・インジェクションリスクを検出する

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

AIエージェント設定はセキュリティレビューが手薄になりがち。AgentShieldは14パターンの秘密情報検出・フックインジェクション解析・MCPサーバリスク評価を自動実行し、--opusフラグでred-team/blue-team/auditorの3エージェント評価も可能

## いつ使うのか

AIエージェント設定を本番環境にデプロイする前、秘密情報の誤混入を防ぎたい、MCP権限を最小化したいとき

## やり方

1. npx ecc-agentshield scan で現在の設定をスキャン 2. --fix で自動修正可能な問題を修正 3. --opus --stream で3エージェント（攻撃者・防御者・監査者）による敵対的推論実行 4. 出力（A-Fグレード）をCI/CDに統合（exit code 2でクリティカル検出時ビルド失敗）

### 入力

- ~/.claude/設定ファイル一式
- npxコマンド

### 出力

- A-Fセキュリティグレード
- 検出された脆弱性リスト（JSON/Markdown/HTML）
- 修正可能な問題の自動パッチ（--fix時）

## 使うツール・ライブラリ

- ecc-agentshield（npm）
- Claude Opus 4.6（--opusモード）

## コード例

```
# クイックスキャン
npx ecc-agentshield scan

# 自動修正
npx ecc-agentshield scan --fix

# 3エージェント深層解析（red-team/blue-team/auditor）
npx ecc-agentshield scan --opus --stream

# CI統合（exit code 2でクリティカル検出時失敗）
npx ecc-agentshield scan --format json > audit.json

# Claude Code内から実行
/security-scan
```

## 前提知識

- Claude Code CLI v2.1.0以上のインストール
- Node.js環境（フックスクリプト実行用）
- Git（リポジトリクローン用）
- 対象言語の開発環境（TypeScript/Python/Go等）
- Claude Codeのサブスクリプション（トークン消費制限緩和のため推奨）
- AIエージェント・プロンプトエンジニアリングの基礎知識

## 根拠

> 「Won the Anthropic x Forum Ventures hackathon in Sep 2025 with @DRodriguezFX — built zenith.chat entirely using Claude Code.」

> 「Not just configs. A complete system: skills, instincts, memory optimization, continuous learning, security scanning, and research-first development.」

> 「Works across Claude Code, Codex, Cowork, and other AI agent harnesses.」

> 「AgentShield integration — /security-scan skill runs AgentShield directly from Claude Code; 1282 tests, 102 rules」
