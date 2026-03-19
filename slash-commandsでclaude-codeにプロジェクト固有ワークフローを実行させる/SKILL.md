# Slash CommandsでClaude Codeにプロジェクト固有ワークフローを実行させる

> Slash Commandsカテゴリのリソース（例: /commit、/create-pr、/tdd-implement）を `.claude/commands/` にインストールし、`/commit` 等のコマンドで複雑なワークフローを1ステップで実行する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

毎回「conventional commitメッセージを書いてgit commitして...」と指示するのは非効率。Slash Commandsは頻出ワークフローをテンプレート化し、1コマンドで実行できる

## いつ使うのか

Git操作、PR作成、テスト実行、ドキュメント生成等の定型ワークフローをClaude Codeに繰り返し実行させたい時

## やり方

1. awesome-claude-codeの「Slash Commands 🔪」セクションから目的のコマンドを選択（例: /commit）
2. コマンドファイル（Markdownファイル）をダウンロード
3. `.claude/commands/` ディレクトリに配置（例: `.claude/commands/commit.md`）
4. Claude Codeで `/commit` を実行
5. Claude Codeがコマンドファイルの指示に従い、git status確認→conventional commitメッセージ生成→commit実行を自動化

### 入力

- ワークフローの定義（Markdownファイル）
- プロジェクト固有の規約（commit規約、PRテンプレート等）

### 出力

- Claude Codeで利用可能なスラッシュコマンド
- コマンド実行時の自動化されたワークフロー

## 使うツール・ライブラリ

- /commit
- /create-pr
- /tdd-implement
- /analyze-issue

## コード例

```
# .claude/commands/commit.md 例
---
name: commit
description: conventional commitでコミットを作成
---

1. `git status` で変更を確認
2. conventional commit形式でメッセージを生成
3. `git commit -m "<message>"` を実行
```

## 前提知識

- Claude Codeの基本的な使い方（インストール、起動、プロンプト入力）
- Claude Codeの設定ファイル構造（.claude/ディレクトリ、hooks.json、commands/、skills/）
- GitHubの基本操作（リポジトリのクローン、READMEの読解）
- JSON、Markdown、Bashの基礎知識

## 根拠

> # Awesome Claude Code - A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow.

> ## Agent Skills 🤖 - Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

> ## Hooks 🪝 - Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.

> ## Slash-Commands 🔪 - Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task.

> ## Tooling 🧰 - Tooling denotes applications that are built on top of Claude Code and consist of more components than slash-commands and CLAUDE.md files.
