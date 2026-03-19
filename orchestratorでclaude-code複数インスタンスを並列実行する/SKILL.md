# OrchestratorでClaude Code複数インスタンスを並列実行する

> Orchestratorsカテゴリのリソース（例: sudocode、Claude Squad、Happy Coder）をインストールし、複数のClaude Codeインスタンスを異なるタスク・ワークツリーで並列実行・管理する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

大規模プロジェクトでは、Feature A開発、Bug B修正、PR Cレビューを並行実行したい。Orchestratorは複数Claude Codeインスタンスをタスク管理し、Docker/tmux/Worktreeで隔離された環境を提供する

## いつ使うのか

複数の独立したタスクをClaude Codeで並列実行したい、チームで複数のClaude Codeインスタンスを協調させたい時

## やり方

1. awesome-claude-codeの「Orchestrators」セクションからツールを選択（例: sudocode）
2. ツールをインストール: `npm install -g sudocode` 等
3. プロジェクトルートで `sudocode init` 等を実行し、タスク定義ファイルを作成
4. タスクごとにClaude Codeインスタンスを起動: `sudocode start task-a task-b`
5. 各インスタンスが独立したディレクトリ or Dockerコンテナで動作し、完了後にPRを作成

### 入力

- タスク定義（仕様ファイル、Issue URL等）
- プロジェクトのgitリポジトリ

### 出力

- タスクごとのgitブランチ or PR
- 並列実行されたClaude Codeインスタンスの実行ログ

## 使うツール・ライブラリ

- sudocode
- Claude Squad
- Happy Coder
- Auto-Claude
- TSK

## 前提知識

- Claude Codeの基本的な使い方（インストール、起動、プロンプト入力）
- Claude Codeの設定ファイル構造（.claude/ディレクトリ、hooks.json、commands/、skills/）
- GitHubの基本操作（リポジトリのクローン、READMEの読解）
- JSON、Markdown、Bashの基礎知識
