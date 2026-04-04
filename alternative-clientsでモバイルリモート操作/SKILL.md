# Alternative Clientsでモバイル/リモート操作

> Claude CodeをモバイルアプリやWeb UIから操作・監視できるクライアントを使う

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

デスクトップから離れていてもClaude Codeの進捗を確認したり、承認が必要な操作を実行したりできる。

## いつ使うのか

外出中に進捗確認したい時、リモートで承認作業を行いたい時、チームメンバーとセッションを共有したい時

## やり方

1. Omnara、Happy Coder等のツールをインストール
2. セッション同期を設定（Web/モバイル間）
3. モバイルアプリまたはWebブラウザからClaude Codeを監視・操作

### 入力

- Claude Codeセッション

### 出力

- モバイル/Web UI
- リモート操作機能

## 使うツール・ライブラリ

- Omnara
- Happy Coder
- crystal

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
