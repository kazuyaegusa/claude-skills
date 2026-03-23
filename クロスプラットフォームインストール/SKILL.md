# クロスプラットフォームインストール

> 単一のインストーラーで、Claude Code/Cursor/Codex/OpenCode に対応した設定を自動配置

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

各ツールは異なる設定フォーマット（JSON/YAML/TOML）を使う。手動コピーはミスが多く、メンテナンスが困難

## いつ使うのか

新しいマシンのセットアップ、チームメンバーへの標準設定配布、複数ツールを併用している

## やり方

1. git clone https://github.com/affaan-m/everything-claude-code.git
2. ./install.sh --target cursor typescript（または python/golang/swift/php）
3. スクリプトが自動判定：Claude Code なら ~/.claude/、Cursor なら ~/.cursor/、Codex なら ~/.codex/ に配置
4. 言語固有のルール（rules/typescript/, rules/python/ など）を選択的にインストール
5. パッケージマネージャー（npm/pnpm/yarn/bun）を自動検出して hooks を調整

### 入力

- リポジトリの clone
- install.sh --target <cursor|codex|antigravity> <typescript|python|golang|swift|php>

### 出力

- ~/.claude/ または ~/.cursor/ または ~/.codex/ への設定ファイル配置
- agents/*.md, commands/*.md, skills/*/SKILL.md, rules/*/*.md のコピー
- hooks.json と scripts/hooks/*.js の配置

## 使うツール・ライブラリ

- Bash script (install.sh)
- PowerShell script (install.ps1)
- Node.js (scripts/sync-ecc-to-codex.sh for Codex)

## コード例

```
# macOS/Linux
./install.sh --target cursor typescript python

# Windows PowerShell
.\install.ps1 --target cursor typescript python
```

## 前提知識

- Claude Code CLI v2.1.0 以降のインストール
- Node.js 18 以降（hooks/scripts の実行に必要）
- Git の基本操作（clone, commit, PR）
- npm/pnpm/yarn/bun のいずれか
- JSON/YAML/TOML の基本文法
- 使用する言語のツールチェーン（TypeScript なら tsc, Python なら pytest など）

## 根拠

> 「Won the Anthropic x Forum Ventures hackathon in Sep 2025 with @DRodriguezFX — built zenith.chat entirely using Claude Code.」

> 「Not just configs. A complete system: skills, instincts, memory optimization, continuous learning, security scanning, and research-first development. Production-ready agents, hooks, commands, rules, and MCP configurations evolved over 10+ months of intensive daily use building real products.」

> 「AgentShield integration — /security-scan skill runs AgentShield directly from Claude Code; 1282 tests, 102 rules」

> 「Hooks fire on tool events. Example - warn about console.log: {matcher: 'tool == "Edit" && tool_input.file_path matches "\\.(ts|tsx|js|jsx)$"', hooks: [{type: 'command', command: 'grep -n 'console\.log' "$file_path" && echo '[Hook] Remove console.log' >&2'}]}」

> 「Cross-platform support — Windows, macOS, and Linux, alongside tight integration across major IDEs (Cursor, OpenCode, Antigravity) and CLI harnesses. All hooks and scripts have been rewritten in Node.js for maximum compatibility.」
