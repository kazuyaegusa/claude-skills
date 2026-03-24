# サブエージェント構造の標準化

> 全エージェント定義ファイルを `name, description, tools, model` のYAML frontmatterと、役割説明、チェックリスト、通信プロトコル、開発ワークフローの本文で構成する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

統一フォーマットにより、(1)Claude Codeが機械的にメタデータを読み取れる、(2)人間が読んで即座に役割を理解できる、(3)新規エージェント作成時にテンプレートとして再利用できる、という3つの利点を得るため

## いつ使うのか

新規サブエージェントを作成する時、または既存エージェントを標準フォーマットに移行したい時

## やり方

1. ファイル冒頭にYAML frontmatter(`---`で囲む)を配置し、以下を記述:
   - `name:` エージェント識別名(ケバブケース)
   - `description:` いつ起動すべきかの説明文
   - `tools:` 許可するツールのカンマ区切りリスト
   - `model:` opus/sonnet/haiku/inherit
2. frontmatter直後に「You are a [役割と専門領域]...」で始まるシステムプロンプトを記述
3. エージェント固有のチェックリスト、パターン、ガイドラインを箇条書きまたはMarkdown形式で列挙
4. 必要に応じて「## Communication Protocol」でエージェント間通信仕様を定義
5. 「## Development Workflow」で構造化された実装フェーズを記述

### 入力

- エージェントの役割、責務、専門知識
- 必要なツールとモデル

### 出力

- 標準化されたMarkdownファイル(例: `python-pro.md`)
- Claude Codeが解釈可能なfrontmatterメタデータ

## 使うツール・ライブラリ

- YAML
- Markdown

## コード例

```
---
name: python-pro
description: Python ecosystem master
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
---

You are a Python expert specializing in...

## Communication Protocol
Inter-agent communication specifications...

## Development Workflow
1. Requirements analysis
2. Design phase
3. Implementation
4. Testing
```

## 前提知識

- Claude Code CLIの基本操作(/agents コマンド、サブエージェント概念)
- Markdownの読み書き(frontmatterとYAML構文)
- Bashコマンド(curl, chmod)の基礎知識
- プロジェクトとグローバルの設定ファイル配置の違い(~/.config vs .config的な概念)
- 開発ライフサイクル(開発→テスト→デプロイ→運用)の理解

## 根拠

> 「This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.」

> 「Tool Assignment Philosophy: Each subagent's tools field specifies Claude Code built-in tools, optimized for their role」

> 「127+ subagents covering a wide range of development use cases」

> 「10 Categories: Core Development, Language Specialists, Infrastructure, Quality & Security, Data & AI, Developer Experience, Specialized Domains, Business & Product, Meta & Orchestration, Research & Analysis」
