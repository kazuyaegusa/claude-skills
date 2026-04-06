# クロスプラットフォーム対応（Cursor/OpenCode/Codex）

> Claude Code向けに書かれたエージェント・スキル・フックをCursor IDE、OpenCode、Codex macOS app/CLIに移植し、同一の設定基盤を複数ツールで共有

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

各ツールで独自にベストプラクティスを再発明する無駄を排除。AGENTS.mdを共通ファイルとし、ツール固有の変換スクリプトで自動適用

## いつ使うのか

複数のAIコーディングツールを併用しており、統一された設定・ワークフローを維持したい場合

## やり方

1. Cursor: ./install.sh --target cursor typescript でYAML frontmatter形式のrulesと.cursor/hooks/adapter.js（DRYアダプタパターン）を配置。CursorのbeforeShellExecution等15種イベントをClaude Code形式に変換し、既存scripts/hooks/*.jsを再利用
2. OpenCode: .opencode/opencode.json にplugin/instructions/agent/commandを定義。ecc-universal npmパッケージをインストールし、11種プラグインイベントとカスタムツール6種を有効化
3. Codex: bash scripts/sync-ecc-to-codex.sh で.codex/config.toml（TOML形式MCP設定）と.agents/skills/（SKILL.md + agents/openai.yaml）を~/.codexにマージ。add-only戦略で既存設定を保護
4. 全ツールで共通のAGENTS.mdをルートに配置し、各ツールが読み込む

### 入力

- Claude Code向けECC設定一式
- 各ツールのインストーラスクリプト

### 出力

- Cursor: .cursor/hooks/*.js、.cursor/rules/*.md（YAML frontmatter）
- OpenCode: .opencode/opencode.json、plugin hooks
- Codex: ~/.codex/config.toml、.agents/skills/*.md

## 使うツール・ライブラリ

- install.sh（Cursor対応）
- scripts/sync-ecc-to-codex.sh（Codex対応）
- ecc-universal（OpenCode npmプラグイン）

## コード例

```
# Cursor向けインストール
./install.sh --target cursor typescript python

# Codex向け同期（add-only、既存設定保護）
bash scripts/sync-ecc-to-codex.sh --dry-run
bash scripts/sync-ecc-to-codex.sh --update-mcp

# OpenCode向けプラグインインストール
npm install ecc-universal
# opencode.json に "plugin": ["ecc-universal"] を追加
```

## 前提知識

- Claude Code CLI v2.1.0以降、またはCursor/OpenCode/Codexのいずれか
- npm/pnpm/yarn/bunのいずれかのパッケージマネージャー
- Gitの基本操作（クローン、コミット）
- JSON/YAML形式の理解
- 対象言語のテストフレームワーク（pytest/jest/go test等）の基礎知識
- （オプション）claude -p サブスクリプション認証（継続学習に必要）

## 根拠

> 「Won the Anthropic x Forum Ventures hackathon in Sep 2025 with @DRodriguezFX — built zenith.chat entirely using Claude Code.」

> 「CLAUDE_AUTOCOMPACT_PCT_OVERRIDE: 50 — Compacts earlier — better quality in long sessions」

> 「AgentShield integration — /security-scan skill runs AgentShield directly from Claude Code; 1282 tests, 102 rules」

> 「Cursor has more hook events than Claude Code (20 vs 8). The .cursor/hooks/adapter.js module transforms Cursor's stdin JSON to Claude Code's format」

> 「Codex macOS app + CLI support — Direct AGENTS.md-based Codex support, installer targeting, and Codex docs」
