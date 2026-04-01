# プラグインベースのマルチツール構成管理

> Claude Code/Cursor/OpenCode/Codexで共通動作するエージェント・スキル・コマンド・フック・ルールをプラグイン形式で一元管理する

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

各ツール固有の設定を個別管理するとメンテナンスコストが爆発し、知見が分散する。共通フォーマット（AGENTS.md/SKILL.md/YAML frontmatter）で記述し、ツール固有部分だけをアダプタで吸収することで移植性と再利用性を最大化する

## いつ使うのか

複数のAIコーディングツールを併用している、またはツール移行を検討しているとき

## やり方

1. リポジトリをクローン 2. `./install.sh --profile full` で全コンポーネントを `~/.claude/` 配下にインストール 3. 各ツール用のアダプタ（`.cursor/hooks/adapter.js` や `.opencode/opencode.json`）がツール固有イベントを共通フォーマットに変換 4. `scripts/hooks/*.js` の共通スクリプトが実処理を担当 5. ツール切り替え時も設定を再利用

### 入力

- GitHubリポジトリ（affaan-m/everything-claude-code）
- 対象ツール（Claude Code/Cursor/OpenCode/Codexのいずれか）
- インストール対象言語（TypeScript/Python/Go/Swift/PHP等）

### 出力

- ~/.claude/agents/*.md（36エージェント）
- ~/.claude/skills/*（142スキル）
- ~/.claude/commands/*.md（68コマンド）
- ~/.claude/rules/{common,typescript,python,golang,swift,php}/*（34ルール）
- hooks/hooks.json（フック定義）
- mcp-configs/mcp-servers.json（MCPサーバ設定）

## 使うツール・ライブラリ

- Claude Code CLI v2.1.0+
- Cursor IDE
- OpenCode
- Codex macOS app/CLI
- Node.js（フックスクリプト実行用）

## コード例

```
# インストール（macOS/Linux）
./install.sh --profile full
# または言語別
./install.sh typescript python golang

# Cursor向け
./install.sh --target cursor typescript

# Codex向け自動セットアップ
npm install && bash scripts/sync-ecc-to-codex.sh
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

> 「Works across Claude Code, Codex, Cowork, and other AI agent harnesses.」

> 「AgentShield integration — /security-scan skill runs AgentShield directly from Claude Code; 1282 tests, 102 rules」

> 「model=sonnet, MAX_THINKING_TOKENS=10000, CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50 で ~60% cost reduction」
