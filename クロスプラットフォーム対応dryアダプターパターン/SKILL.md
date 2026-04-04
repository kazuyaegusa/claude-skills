# クロスプラットフォーム対応（DRYアダプターパターン）

> Claude Code/Cursor/Codex/OpenCodeの異なるフックイベントシステムを、共通のscripts/hooks/*.jsで処理し、各ハーネス用のアダプター層（.cursor/hooks/adapter.js等）で差分を吸収する

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

各ハーネスでフックスクリプトを重複実装するとメンテナンスコストが爆発。共通ロジックを一元化し、ハーネス固有の差分のみをアダプターで変換すればDRYを維持できる

## いつ使うのか

複数のAIハーネスを併用している、ハーネス間でワークフローを統一したい、メンテナンスコストを最小化したい場合

## やり方

1. scripts/hooks/*.js に共通ロジック（session-start.js, session-end.js等）を実装 2. Claude Code は hooks/hooks.json から直接呼び出し 3. Cursor は .cursor/hooks/adapter.js がCursorのstdin JSONをClaude Code形式に変換し、scripts/hooks/*.js を再利用 4. Codexは AGENTS.md + config.toml、OpenCode は plugin hooks でそれぞれ統合 5. 新機能は scripts/hooks/ に追加すれば全ハーネスで利用可能

### 入力

- ハーネス固有のフックイベント仕様（Claude Code: 8種類、Cursor: 15種類、OpenCode: 11種類）
- 共通フックロジック（scripts/hooks/*.js）

### 出力

- 全ハーネスで統一されたフック動作
- ハーネス固有コードの最小化（アダプター層のみ）
- 新機能の一元管理・自動展開

## 使うツール・ライブラリ

- scripts/hooks/*.js（共通ロジック）
- .cursor/hooks/adapter.js（Cursor用変換）
- hooks/hooks.json（Claude Code）
- .opencode/plugins/（OpenCode）

## コード例

```
// 共通フック（scripts/hooks/session-start.js）
// Claude Code、Cursor、Codex、OpenCode全てで再利用

// Cursorアダプター（.cursor/hooks/adapter.js）
const cursorEvent = JSON.parse(stdinData);
const claudeFormat = transformCursorToClaude(cursorEvent);
execSync(`node scripts/hooks/session-start.js`, { input: JSON.stringify(claudeFormat) });

// 新機能追加時
// → scripts/hooks/new-feature.js に実装
// → hooks/hooks.json と .cursor/hooks/ に登録するだけで全ハーネス対応
```

## 前提知識

- Claude Code CLI v2.1.0以上の基本操作知識
- 使用する言語スタック（TypeScript/Python/Go等）の基礎知識
- git、npm/pnpm/yarn/bunの基本操作
- JSON/YAML/TOML形式の理解
- CI/CDパイプラインの基礎（AgentShield統合時）
- セキュリティベストプラクティスの基本（OWASP Top 10等）

## 根拠

> 「Production-ready agents, skills, hooks, rules, MCP configurations, and legacy command shims evolved over 10+ months of intensive daily use building real products.」

> 「CLAUDE_AUTOCOMPACT_PCT_OVERRIDE: 50 (default 95) → Compacts earlier — better quality in long sessions」

> 「AgentShield integration — /security-scan skill runs AgentShield directly from Claude Code; 1282 tests, 102 rules」

> 「Cursor: 15 hook events, DRY adapter pattern lets Cursor reuse Claude Code's hook scripts without duplication」

> 「Codex: First-class support for both macOS app and CLI, with reference config, Codex-specific AGENTS.md supplement, and shared skills」
