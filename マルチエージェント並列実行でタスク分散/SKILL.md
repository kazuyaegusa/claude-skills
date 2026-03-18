# マルチエージェント並列実行でタスク分散

> 複数の Claude Code インスタンスを並列に起動し、それぞれ独立したタスクを実行させることで、開発速度を向上させる仕組み。オーケストレーターツールが各エージェントを管理し、結果を統合する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

単一の Claude Code インスタンスでは、長時間かかるタスク（テスト実行、セキュリティ監査、ドキュメント生成など）を直列実行するため時間がかかる。並列実行することで、複数のサブタスクを同時に処理し、全体の完了時間を短縮できる

## いつ使うのか

複数の独立した機能を同時開発したい場合、CI/CD パイプラインで並列テスト実行したい場合、大規模リファクタリングを分散処理したい場合

## やり方

1. オーケストレーターツールをインストール（例: Claude Squad, Auto-Claude, TSK, sudocode）
2. タスクリストを定義（JSON, YAML, またはコマンドライン引数）
3. オーケストレーターが各タスクに対して Docker コンテナまたは tmux セッションで Claude Code を起動
4. 各エージェントは独立した git worktree または専用ディレクトリで作業
5. 完了後、オーケストレーターが結果を集約・レポート生成

### 入力

- タスク定義（JSON/YAML）
- オーケストレーター設定
- Docker または tmux 環境

### 出力

- 各タスクの実行結果
- 統合レポート
- Git ブランチ（タスクごと）

## 使うツール・ライブラリ

- Claude Squad
- Auto-Claude
- TSK
- sudocode
- claude-tmux

## コード例

```
# claude-squad コマンド例
claudesquad run --tasks tasks.json --workers 4
```

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
