# カテゴリ別リソース検索でClaude Code拡張を発見する

> awesome-claude-codeリポジトリの目次から、Agent Skills、Hooks、Slash Commands、Status Lines、Tooling、CLAUDE.mdファイル等のカテゴリを辿り、目的に合ったリソースを見つける

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeは拡張性が高いが、コミュニティリソースが散在しており発見が困難。カテゴリ分類により、「TDD強制」「セキュリティスキャン」「Git自動化」等のニーズから直接対応するリソースへアクセスできる

## いつ使うのか

Claude Codeで特定の機能（例: TDD、プロンプトインジェクション検知、使用量ダッシュボード）を実現したいが、どのリソースが存在するか分からない時

## やり方

1. https://github.com/hesreallyhim/awesome-claude-code を開く
2. 目次（Contents）から目的のカテゴリ（例: Hooks、Slash Commands - Version Control & Git）をクリック
3. 各リソースの説明を読み、GitHubリンクから詳細を確認
4. README内の検索機能（Ctrl+F / Cmd+F）でキーワード検索も可能
5. 気になるリソースをクローン or ダウンロードして試用

### 入力

- 実現したい機能・ワークフローの明確な要件

### 出力

- 要件に合致する既存リソースのリスト
- 各リソースのGitHubリポジトリURL、作者、機能説明

## 使うツール・ライブラリ

- awesome-claude-code リポジトリ

## 前提知識

- Claude Codeの基本的な使い方（インストール、起動、プロンプト入力）
- Claude Codeの設定ファイル構造（.claude/ディレクトリ、hooks.json、commands/、skills/）
- GitHubの基本操作（リポジトリのクローン、READMEの読解）
- JSON、Markdown、Bashの基礎知識

## 根拠

> ## Agent Skills 🤖 - Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

> ## Hooks 🪝 - Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.

> ## Slash-Commands 🔪 - Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task.

> ## Tooling 🧰 - Tooling denotes applications that are built on top of Claude Code and consist of more components than slash-commands and CLAUDE.md files.
