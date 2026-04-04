# Subagent定義の標準テンプレート化

> 全Subagentをname, description, tools, model, role, checklist, communication protocolの統一フォーマットで記述する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

Subagentの動作が予測可能になり、チーム間での再利用性が向上するため

## いつ使うのか

新規Subagentを作成する場合、または既存Subagentをチーム標準に合わせる場合

## やり方

1. frontmatter（YAML）でname, description, tools, modelを定義
2. 本文で役割説明（You are a [role]...）
3. チェックリスト・パターン・ガイドラインを箇条書き
4. Communication Protocol（他Subagentとの連携方法）
5. Development Workflow（実装フェーズ）を記載

### 入力

- Subagentの役割と専門領域

### 出力

- 標準フォーマットに従ったSubagent定義ファイル（.md）

## 使うツール・ライブラリ

- Markdown
- YAML frontmatter

## コード例

```
---
name: subagent-name
description: When this agent should be invoked
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
---

You are a [role description and expertise areas]...

[Agent-specific checklists, patterns, and guidelines]...

## Communication Protocol
Inter-agent communication specifications...

## Development Workflow
Structured implementation phases...
```

## 前提知識

- Claude Codeの基本的な使用経験
- Subagentの概念（独立したコンテキストウィンドウ、専門性、ツール権限）の理解
- GitHubからのリポジトリクローンまたはcurlでのファイル取得方法
- ~/.claude/agents/と.claude/agents/の違い（グローバル vs プロジェクト固有）

## 根拠

> This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.
