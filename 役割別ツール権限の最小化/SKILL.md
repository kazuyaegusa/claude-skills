# 役割別ツール権限の最小化

> Subagentごとに必要最小限のClaude Code Built-inツールのみを許可する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

レビュアーが誤ってコードを変更したり、アナリストがデプロイコマンドを実行するリスクを防ぐため

## いつ使うのか

Subagentの誤操作を防ぎ、意図しない変更やコマンド実行を制限したい場合

## やり方

1. 読み取り専用タスク（reviewer, auditor）→ tools: Read, Grep, Glob
2. 調査タスク（analyst, researcher）→ tools: Read, Grep, Glob, WebFetch, WebSearch
3. コード書き込みタスク（developer, engineer）→ tools: Read, Write, Edit, Bash, Glob, Grep
4. ドキュメント作成タスク（writer, documenter）→ tools: Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
5. 必要に応じてMCP serverや外部ツールを追加可能

### 入力

- Subagentの役割（レビュアー/開発者/調査者等）

### 出力

- 役割に応じて制限されたツールセット

## 使うツール・ライブラリ

- Claude Code Built-in tools (Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch)

## コード例

```
---
name: code-reviewer
tools: Read, Grep, Glob  # 読み取り専用
---

---
name: backend-developer
tools: Read, Write, Edit, Bash, Glob, Grep  # 書き込み可能
---
```

## 前提知識

- Claude Codeの基本的な使用経験
- Subagentの概念（独立したコンテキストウィンドウ、専門性、ツール権限）の理解
- GitHubからのリポジトリクローンまたはcurlでのファイル取得方法
- ~/.claude/agents/と.claude/agents/の違い（グローバル vs プロジェクト固有）

## 根拠

> This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.

> Read-only agents (reviewers, auditors): Read, Grep, Glob - analyze without modifying

> Code writers (developers, engineers): Read, Write, Edit, Bash, Glob, Grep - create and execute

> claude plugin marketplace add VoltAgent/awesome-claude-code-subagents
