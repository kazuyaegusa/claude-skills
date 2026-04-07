# カテゴリ別サブエージェント体系の構築

> 130種以上のサブエージェントを10カテゴリ（コア開発/言語専門家/インフラ/品質・セキュリティ/データAI/DX/特化ドメイン/ビジネス/メタ編成/リサーチ）に分類・定義する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

タスクの性質によって必要な専門知識・ツール権限・モデルが異なるため、カテゴリ化により適切なエージェントを即座に選択でき、無駄な汎用プロンプトを排除できる

## いつ使うのか

プロジェクトで複数の技術領域・ロールが混在し、汎用AIでは精度が落ちる場合

## やり方

1. タスク領域を10カテゴリに分類（categories/01-core-development/等）
2. 各カテゴリ内でエージェントを定義（例: typescript-pro.md, devops-engineer.md）
3. フロントマター（name/description/tools/model）で役割・権限・モデルを明示
4. Communication ProtocolとDevelopment Workflowセクションで動作パターンを標準化

### 入力

- タスク要件（言語、フレームワーク、役割）
- 必要なツール権限（読み取り専用 or 書き込み許可）
- コスト制約（opus/sonnet/haiku）

### 出力

- カテゴリ別に整理されたエージェント定義ファイル群
- プラグインパッケージ（voltagent-lang, voltagent-infra等）
- インストールスクリプト（install-agents.sh）

## 使うツール・ライブラリ

- Claude Code プラグインシステム
- Markdown frontmatter（YAML）
- Bash インストールスクリプト

## コード例

```
---
name: typescript-pro
description: TypeScript specialist
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
---

You are a TypeScript specialist...

## Communication Protocol
...

## Development Workflow
...
```

## 前提知識

- Claude Codeの基本操作とサブエージェント概念の理解
- 開発タスクのカテゴリ分類（言語/インフラ/品質等）に関する知識
- Claude APIのモデル違い（opus/sonnet/haiku）の理解
- Markdownとフロントマター（YAML）の基礎知識
- Claude Code組み込みツール（Read, Write, Edit, Bash等）の把握
