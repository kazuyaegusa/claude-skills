# subagent標準テンプレート定義

> 全agentに共通のYAML frontmatter（name/description/tools/model）を強制し、役割・起動条件・ツール権限・モデル選択を明示する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

フォーマットがバラバラだとClaude Codeが正しく認識できず、チーム間で再利用もできない。標準化により、agentの動作が予測可能になり、tool権限でセキュリティリスクも制御できる

## いつ使うのか

新しいsubagentを作成するとき、または既存agentを標準化するとき

## やり方

1. frontmatterに必須フィールド（name, description, tools, model）を定義
2. descriptionには「いつ起動すべきか」を明記
3. toolsには最小権限の原則で必要なツールのみ列挙（例: Read-only agentはRead/Grep/Glob）
4. modelには適切なClaudeモデル（opus/sonnet/haiku）を指定
5. 本文には役割説明・チェックリスト・開発ワークフローを記載

### 入力

- agentの役割・専門領域
- 必要なツール権限
- タスクの複雑度（モデル選択の基準）

### 出力

- 標準フォーマットのagent定義ファイル（.md）

## コード例

```
---
name: python-pro
description: Python ecosystem master for web development, data processing, and automation
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
---

You are a Python specialist with deep expertise in...
```

## 前提知識

- Claude Codeの基本操作（subagent作成・呼び出し）
- YAML frontmatterの理解
- Claude APIのモデル種別（opus/sonnet/haiku）の特性
- ~/.claude/agents/ と .claude/agents/ の違い（global/project-specific）
- 最小権限の原則（Principle of Least Privilege）

## 根拠

> Standard template with YAML frontmatter: name, description, tools, model

> Tool Assignment Philosophy: Read-only (Read, Grep, Glob), Research (+ WebFetch, WebSearch), Code writers (+ Write, Edit, Bash), Documentation (all)
