# スラッシュコマンドによるカスタムプロンプトのテンプレート化

> 頻繁に使う複雑なプロンプトを `/commit`、`/tdd`、`/create-pr` などのスラッシュコマンドとして登録し、再利用可能にする

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

同じ指示を何度も入力する手間を省き、プロンプトの品質を標準化できるため。チーム全体で共通のワークフローを強制することも可能

## いつ使うのか

Git コミットメッセージを自動生成したい時、GitHub Issue を自動解決したい時、TDD ワークフローを強制したい時、PR 作成を自動化したい時

## やり方

1. `.claude/commands/` ディレクトリに Markdown ファイルを作成
2. ファイル名をコマンド名にする（例：`commit.md` → `/commit`）
3. Markdown 内にプロンプトテンプレートを記述
4. パラメータが必要な場合は `{issue_number}` などのプレースホルダーを使用
5. Claude Code セッション中に `/commit` などで呼び出す

### 入力

- コマンド定義ファイル（Markdown）
- プロンプトテンプレート
- パラメータ（オプション）

### 出力

- Claude に渡される展開済みプロンプト
- 自動実行されるタスク（コミット、PR 作成など）

## 使うツール・ライブラリ

- /commit（conventional commit 形式）
- /tdd（TDD ワークフロー）
- /create-pr（PR 自動作成）
- /analyze-issue（Issue 分析）

## コード例

```
---
name: commit
description: Generate conventional commit message
---

Analyze the staged changes and create a conventional commit message with appropriate emoji.
Format: `type(scope): message`
```

## 前提知識

- Claude Code の基本的な使い方（インストール、セッション開始、プロンプト入力）
- Git の基礎知識（コミット、ブランチ、PR 作成）
- Markdown の基本文法
- シェルスクリプト（Bash）の基礎知識（フック・スラッシュコマンドのカスタマイズに必要）
- JSON の基本構造（フック設定ファイルの編集に必要）

## 根拠

> "A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow."

> "Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities."

> "Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle."

> "Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task"

> "CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards"
