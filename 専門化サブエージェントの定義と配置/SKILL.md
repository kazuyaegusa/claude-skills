# 専門化サブエージェントの定義と配置

> 特定タスク（例: TypeScript開発、AWS構築、セキュリティ監査）に特化したサブエージェント定義（YAML frontmatter形式）を作成し、プロジェクトまたはグローバルディレクトリに配置する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

汎用AIより専門プロンプトとツール制限を持つエージェントの方が、タスク精度が高く、不要なツールアクセスを防ぎセキュリティを確保できるため

## いつ使うのか

特定の言語・フレームワーク・インフラに関するタスクを反復的に実行する場合、またはチーム全体で統一されたAI支援パターンを導入したい場合

## やり方

1. リポジトリから該当カテゴリ（例: `categories/02-language-specialists/typescript-pro.md`）のエージェント定義をダウンロード
2. `~/.claude/agents/`（グローバル）または `.claude/agents/`（プロジェクト固有）にコピー
3. 必要に応じてYAMLヘッダーの `tools` フィールドでツール権限を調整
4. `description` フィールドを編集してエージェント起動トリガーをカスタマイズ
5. Claude Code起動後、該当タスクで自動的にサブエージェントが呼び出される

### 入力

- サブエージェント定義ファイル（.md形式、YAML frontmatter付き）
- 配置先ディレクトリ（`~/.claude/agents/` または `.claude/agents/`）

### 出力

- Claude Codeで自動認識される専門サブエージェント
- タスク実行時に独立したコンテキストで動作するエージェントセッション

## 使うツール・ライブラリ

- Claude Code CLI
- Git（リポジトリクローン用）
- curl（スタンドアロンインストーラー利用時）

## コード例

```
---
name: typescript-pro
description: TypeScript開発タスクで起動
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
---

You are a TypeScript specialist...

## Development Workflow
1. 型定義を先に作成
2. tsconfig.jsonの厳密性を確認
3. eslint/prettierでフォーマット
```

## 前提知識

- Claude Codeの基本操作（CLI起動、エージェント呼び出し）
- サブエージェントの概念理解（独立コンテキスト、ツール権限、モデル選択）
- YAML frontmatter形式の基本構造
- Git操作（クローン、ファイルコピー）またはcurlコマンドの使用
- 対象領域（言語・インフラ・QA等）の基礎知識（各エージェントを活用する場合）

## 根拠

> 「This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.」

> 「Smart Model Routing: Each subagent includes a `model` field that automatically routes it to the right Claude model — balancing quality and cost」

> 「Tool Assignment Philosophy: Each subagent's `tools` field specifies Claude Code built-in tools, optimized for their role」

> 「Project Subagents: `.claude/agents/` Current project only, Higher precedence」

> 「Global Subagents: `~/.claude/agents/` All projects, Lower precedence」
