# Tool権限の最小化原則

> 各agentに必要最小限のClaude Code toolsのみを割り当て、不要な変更・実行を防ぐ

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

全agentに全ツールを与えると、レビュー専用agentがコードを書き換えたり、リサーチagentがビルドを実行したりする事故が起きる。Read-only/Research/Code writer/Documentationの4パターンで権限を分離すれば、意図しない副作用を防げる

## いつ使うのか

agentの責務を明確にし、誤操作を防ぎたいとき

## やり方

1. Read-only agents（reviewers/auditors）: Read, Grep, Globのみ
2. Research agents（analysts/researchers）: Read, Grep, Glob, WebFetch, WebSearch
3. Code writers（developers/engineers）: Read, Write, Edit, Bash, Glob, Grep
4. Documentation agents: Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
5. frontmatterの`tools`フィールドに列挙
6. 必要に応じてMCPサーバーや外部ツールを追加

### 入力

- agentの役割（読み取り専用／実装／調査等）

### 出力

- 最小権限のtools指定

## 使うツール・ライブラリ

- Claude Code tools (Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch)

## コード例

```
# レビュー専用（書き込み不可）
---
tools: Read, Grep, Glob
---

# 実装担当（全権限）
---
tools: Read, Write, Edit, Bash, Glob, Grep
---
```

## 前提知識

- Claude Codeの基本操作（subagent作成・呼び出し）
- YAML frontmatterの理解
- Claude APIのモデル種別（opus/sonnet/haiku）の特性
- ~/.claude/agents/ と .claude/agents/ の違い（global/project-specific）
- 最小権限の原則（Principle of Least Privilege）

## 根拠

> This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.

> 4 installation methods: Plugin (claude plugin install), Manual, Interactive installer (./install-agents.sh), Agent installer (via Claude Code)

> Tool Assignment Philosophy: Read-only (Read, Grep, Glob), Research (+ WebFetch, WebSearch), Code writers (+ Write, Edit, Bash), Documentation (all)
