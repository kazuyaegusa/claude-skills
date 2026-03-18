# Agent Skills でドメイン知識を注入する

> Claude Code に専門分野の知識・ワークフローを教え込み、特定タスクを自律実行させる仕組み。Skills は「モデル制御の設定ファイル群」として機能し、Claude が特定の知識や手順を必要とするタスクを実行できるようにする

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Code はデフォルトでは汎用的な知識しか持たないため、DevOps、セキュリティ監査、科学計算など専門性の高いタスクでは追加の文脈・手順・ツール知識が必要。Skills を導入することで、毎回プロンプトで指示する手間を省き、再現性の高い専門的作業を自動化できる

## いつ使うのか

特定ドメインの専門知識を繰り返し適用する場合、複雑な多段階ワークフローを自動化したい場合、チーム全体で標準化されたベストプラクティスを共有したい場合

## やり方

1. リポジトリから適切な Skills セットをクローン（例: `claude-scientific-skills`, `cc-devops-skills`, `Trail of Bits Security Skills`）
2. `~/.claude/skills/` ディレクトリに配置
3. Claude Code セッション開始時に Skills が自動ロードされ、特定のコマンドやワークフローが利用可能になる
4. 必要に応じてプロジェクト固有の Skills をカスタマイズ・追加

### 入力

- Skills リポジトリ（GitHub から入手）
- プロジェクト固有の要件・用語定義

### 出力

- 自動ロードされる専門知識
- 再利用可能なワークフロー
- 標準化された作業手順

## 使うツール・ライブラリ

- Claude Code Skills API
- GitHub（Skills リポジトリ配布）

## 前提知識

- Claude Code の基本的な使い方（インストール、セッション開始、ファイル操作）
- Git の基礎知識（ブランチ、コミット、PR）
- コマンドライン操作の基本（Bash, tmux など）
- 開発プロセスの基礎知識（TDD, CI/CD, コードレビュー）

## 根拠

> A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow.

> Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

> Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.

> Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task.

> CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards.
