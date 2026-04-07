# ツール権限最小化設計

> 各エージェントの `tools` フィールドで必要最小限のClaude Code組み込みツールのみ許可し、不要な操作を防ぐ

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

読み取り専用エージェント（レビュアー、監査役）が誤ってコードを書き換えるリスクを排除し、安全性とタスク集中を保証する

## いつ使うのか

セキュリティ監査やコードレビューなど、読み取り専用保証が必要な時、権限分離でミスを防ぎたい時

## やり方

1. Read-only agents（reviewers, auditors）: `Read, Grep, Glob` のみ
2. Research agents: `Read, Grep, Glob, WebFetch, WebSearch`
3. Code writers: `Read, Write, Edit, Bash, Glob, Grep`
4. Documentation agents: `Read, Write, Edit, Glob, Grep, WebFetch, WebSearch`
5. 必要に応じてMCPサーバーや外部ツールを追加

### 入力

- エージェントの役割（読み取り/書き込み/実行）

### 出力

- ツール権限が明示されたエージェント定義

## 使うツール・ライブラリ

- Claude Code built-in tools (Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch)

## コード例

```
# Read-only example
tools: Read, Grep, Glob

# Code writer example
tools: Read, Write, Edit, Bash, Glob, Grep
```

## 前提知識

- Claude Codeの基本操作とサブエージェント概念の理解
- 開発タスクのカテゴリ分類（言語/インフラ/品質等）に関する知識
- Claude APIのモデル違い（opus/sonnet/haiku）の理解
- Markdownとフロントマター（YAML）の基礎知識
- Claude Code組み込みツール（Read, Write, Edit, Bash等）の把握

## 根拠

> 「This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.」

> 「Tool Assignment Philosophy: Read-only agents (reviewers, auditors): Read, Grep, Glob - analyze without modifying」

> 「130+ subagents across 10 categories: Core Development, Language Specialists, Infrastructure, Quality & Security, Data & AI, Developer Experience, Specialized Domains, Business & Product, Meta & Orchestration, Research & Analysis」
