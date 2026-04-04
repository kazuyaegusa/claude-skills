# AgentShield統合セキュリティスキャン

> CLAUDE.md/settings.json/MCP設定/フック/エージェント定義の5カテゴリを静的解析し、シークレット検出・権限監査・インジェクションリスク・MCP信頼性評価・エージェント設定レビューを実行

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

AIエージェントの設定ミスや権限過多は、シークレット漏洩・コマンドインジェクション・意図しない外部アクセスを引き起こす。静的解析+LLM敵対的評価で事前検出が必要

## いつ使うのか

新規プロジェクト初回セットアップ時、CI/CDパイプラインでのセキュリティゲート、定期的な設定監査、プルリクエスト前のチェック

## やり方

1. npx ecc-agentshield scan で現在のディレクトリをスキャン（インストール不要） 2. --fix フラグで安全な問題を自動修正 3. --opus フラグで3体のOpus 4.6エージェント（攻撃者/防御者/監査者）による敵対的評価を実行 4. 出力形式は Terminal（A-F評価）、JSON（CI用）、Markdown、HTML 5. クリティカル検出時は exit code 2 でビルドゲート可能 6. /security-scan コマンドでClaude Code内から直接実行も可能

### 入力

- CLAUDE.md, settings.json, MCP設定, hooks/, agents/, skills/
- （オプション）--opus フラグ使用時はAnthropic APIキー

### 出力

- A-F評価レポート（Terminal）
- JSON/Markdown/HTML形式レポート
- 検出された脆弱性リスト（14シークレットパターン、権限過多、インジェクション等）
- exit code 2（クリティカル検出時、CI連携用）

## 使うツール・ライブラリ

- ecc-agentshield（npm package）
- Claude Opus 4.6（--opusフラグ時）
- 1282テスト、102静的解析ルール

## コード例

```
# クイックスキャン（インストール不要）
npx ecc-agentshield scan

# 自動修正
npx ecc-agentshield scan --fix

# 深層敵対的評価（3体のOpus 4.6エージェント）
npx ecc-agentshield scan --opus --stream

# セキュアな設定を生成
npx ecc-agentshield init

# Claude Code内から実行
/security-scan

# CI統合例（GitHub Actions）
- run: npx ecc-agentshield scan --format json
  # exit code 2 on critical findings
```

## 前提知識

- Claude Code CLI v2.1.0以上の基本操作知識
- 使用する言語スタック（TypeScript/Python/Go等）の基礎知識
- git、npm/pnpm/yarn/bunの基本操作
- JSON/YAML/TOML形式の理解
- CI/CDパイプラインの基礎（AgentShield統合時）
- セキュリティベストプラクティスの基本（OWASP Top 10等）

## 根拠

> 「Not just configs. A complete system: skills, instincts, memory optimization, continuous learning, security scanning, and research-first development.」

> 「AgentShield integration — /security-scan skill runs AgentShield directly from Claude Code; 1282 tests, 102 rules」

> 「Cursor: 15 hook events, DRY adapter pattern lets Cursor reuse Claude Code's hook scripts without duplication」

> 「Codex: First-class support for both macOS app and CLI, with reference config, Codex-specific AGENTS.md supplement, and shared skills」

> 「OpenCode: 11 event types, 6 native custom tools」
