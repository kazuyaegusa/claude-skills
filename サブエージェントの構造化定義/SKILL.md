# サブエージェントの構造化定義

> 各サブエージェントをYAML frontmatter + Markdown形式で定義し、name/description/tools/model/system promptを標準化する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

標準フォーマットに従うことで、エージェントの責務・権限・動作が明確になり、チーム間での共有・カスタマイズが容易になる。特にtools/model指定により実行権限とコスト最適化が可能

## いつ使うのか

新しいサブエージェントを作成する時、または既存エージェントをカスタマイズする時

## やり方

1. `---`で囲まれたYAML frontmatterにメタデータを記述（name, description, tools, model）
2. Markdown本文にエージェントの役割・チェックリスト・通信プロトコル・ワークフローを記述
3. `tools`フィールドで必要最小限のツール権限を指定（Read/Write/Edit/Bash/Glob/Grep等）
4. `model`フィールドでopus/sonnet/haikuを使い分け（深い推論/日常コーディング/クイックタスク）

### 入力

- エージェントの役割定義
- 必要なツール権限
- 使用するClaudeモデル

### 出力

- .mdファイル（エージェント定義）
- Claude Codeから呼び出し可能なエージェント

## 使うツール・ライブラリ

- Markdown
- YAML frontmatter

## コード例

```
---
name: python-pro
description: Python ecosystem specialist
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
---

You are a Python development expert specializing in...

## Development Workflow
1. Analyze requirements
2. Design implementation
3. Write tests first (TDD)
4. Implement functionality
5. Verify with tests
```

## 前提知識

- Claude Code CLIがインストールされている
- claude plugin機能の基本的な理解
- サブエージェントの概念（独立したコンテキストウィンドウ、ドメイン特化型プロンプト）
- Markdown/YAMLの基本文法

## 根拠

> Each subagent's `tools` field specifies Claude Code built-in tools, optimized for their role
