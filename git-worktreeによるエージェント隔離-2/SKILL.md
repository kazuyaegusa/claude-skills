# git worktreeによるエージェント隔離

> 各AIエージェントのタスクを別々のgit worktree（独立した作業ディレクトリ＋ブランチ）で実行し、相互干渉を防ぐ

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

同じリポジトリで複数のエージェントが同時にファイルを変更すると競合が発生する。worktreeを使えば各タスクが独立したディレクトリとブランチを持つため、並列実行時にマージ競合やファイルロックを回避できる。

## いつ使うのか

2つ以上の独立したタスクを同時進行させたい時、特にAIエージェントの応答待ち時間が発生する場合

## やり方

1. Supersetで新しいworkspaceを作成すると、自動的にgit worktreeが生成される
2. 各workspaceは独自のブランチと作業ディレクトリを持つ
3. エージェントはそのworktree内でコード変更を行う
4. 作業完了後、built-in diff viewerで変更をレビュー
5. 問題なければメインブランチへマージ、不要ならworktreeを削除

### 入力

- git管理されたリポジトリ
- 並列実行したい複数のタスク（機能追加、バグ修正等）

### 出力

- 独立したブランチごとの変更差分
- マージ可能な状態のプルリクエスト候補

## 使うツール・ライブラリ

- git worktree
- Superset（ターミナルアプリ）

## 前提知識

- gitの基本操作（branch、merge、worktreeの概念）
- CLIベースのAIエージェント（Claude Code、Codex等）の基本的な使い方
- macOS環境（現時点でmacOSのみサポート）
- Bun v1.0+、Git 2.20+、GitHub CLI、Caddyのインストール

## 根拠

> Isolate each task in its own git worktree so agents don't interfere with each other
