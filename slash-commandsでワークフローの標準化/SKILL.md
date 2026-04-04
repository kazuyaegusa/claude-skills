# Slash Commandsでワークフローの標準化

> 頻繁に使うプロンプトを /command-name 形式でショートカット化し、チーム全体で同じ手順を共有する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Git操作、PR作成、ドキュメント生成など定型作業の品質を保ち、チームメンバー間で一貫性を確保できる。

## いつ使うのか

Git操作を標準化したい時、PR/ドキュメント生成の品質を統一したい時、チームで同じワークフローを使いたい時

## やり方

1. .claude/commands/{command-name}.md を作成
2. Claude Codeに与える詳細なプロンプトをマークダウンで記述
3. /command-name で呼び出し
4. 引数を受け取る設計も可能（例: /fix-issue 123）

### 入力

- 定型タスクの要件

### 出力

- commandファイル
- 再利用可能なプロンプト

## 使うツール・ライブラリ

- .claude/commands/ディレクトリ
- 既存コマンドリポジトリ

## 前提知識

- Claude Codeの基本的な使い方（CLI操作、セッション管理）
- Gitの基礎知識（ブランチ、コミット、PR等）
- シェルスクリプトまたはPython/TypeScriptの基礎（Hook・Skill作成に必要）
- プロジェクトのビルド・テストコマンドの理解

## 根拠

> Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

> Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.

> Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task

> CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards

> Alternative Clients are alternative UIs and front-ends for interacting with Claude Code, either on mobile or on the desktop.
