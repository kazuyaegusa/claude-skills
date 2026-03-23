# AgentShield セキュリティスキャン

> CLAUDE.md, settings.json, MCP configs, hooks, agents, skills を静的解析し、シークレット・権限・インジェクションリスクを検出

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

AI エージェントは強力だが、設定ミスでシークレット漏洩や権限昇格のリスクがある。自動スキャンで未然に防ぐ

## いつ使うのか

設定変更後、本番デプロイ前、CI/CD パイプライン、定期監査

## やり方

1. npx ecc-agentshield scan（インストール不要）
2. 14 のシークレットパターン（API キー、AWS キー、GitHub PAT など）を検出
3. --opus フラグで 3 つの Claude Opus 4.6 エージェント（攻撃者・防御者・監査者）による敵対的分析
4. --fix フラグで安全な修正を自動適用
5. 出力形式：ターミナル（A-F グレード）、JSON、Markdown、HTML
6. CI で exit code 2（クリティカル検出時）を使ってビルドゲート

### 入力

- CLAUDE.md, settings.json, mcp-configs/mcp-servers.json, hooks/hooks.json, agents/*.md, skills/*/SKILL.md

### 出力

- セキュリティグレード（A-F）
- 検出された脆弱性リスト（カテゴリ・重要度・修正案）
- CI 用 exit code（0=安全, 2=クリティカル）

## 使うツール・ライブラリ

- ecc-agentshield (npm package)
- Claude Opus 4.6（--opus フラグ時）

## コード例

```
npx ecc-agentshield scan --opus --stream --fix
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

> 「CLAUDE_AUTOCOMPACT_PCT_OVERRIDE: 50 → Compacts earlier — better quality in long sessions」

> 「AgentShield integration — /security-scan skill runs AgentShield directly from Claude Code; 1282 tests, 102 rules」

> 「Hooks fire on tool events. Example - warn about console.log: {matcher: 'tool == "Edit" && tool_input.file_path matches "\\.(ts|tsx|js|jsx)$"', hooks: [{type: 'command', command: 'grep -n 'console\.log' "$file_path" && echo '[Hook] Remove console.log' >&2'}]}」
