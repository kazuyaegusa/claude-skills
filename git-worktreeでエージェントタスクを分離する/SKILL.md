# git worktreeでエージェントタスクを分離する

> 各エージェントタスクに専用のgit worktree（独立した作業ディレクトリ+ブランチ）を割り当て、タスク間の干渉を物理的に防ぐ。

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: claude-code-workflow

## なぜ使うのか

複数エージェントが同じディレクトリで動くと、ファイル変更の競合・git状態の混乱・予期しないマージが発生する。worktreeで完全分離すれば、各エージェントが独立して安全に動作できる。

## いつ使うのか

2つ以上のタスクを同時に進めたいとき、エージェント実行中に別タスクへ切り替えたいとき

## やり方

1. Supersetで新規ワークスペースを作成（⌘N または Quick create ⌘⇧N）
2. 内部でgit worktree add <path> <branch> が自動実行され、専用ディレクトリ+ブランチが生成される
3. 各ワークスペースで異なるエージェント（Claude Code, Cursor Agent等）を起動
4. エージェント完了後、Built-in Diff Viewerで変更を確認し、必要に応じてメインブランチへマージ

### 入力

- git管理されたリポジトリ
- 実行したいタスクの明確な指示

### 出力

- 各タスク専用のディレクトリ（worktree）
- 独立したgitブランチ
- 干渉なく並列実行されたエージェントの成果物

## 使うツール・ライブラリ

- git 2.20+
- Superset

## 前提知識

- git 2.20以上の基礎知識（worktree概念の理解が望ましい）
- macOS環境（現時点でWindows/Linuxは未検証）
- Bun v1.0+, GitHub CLI (gh), Caddy（開発時のみ）
- CLIベースのコーディングエージェント（Claude Code, Cursor Agent等）のいずれか

## 根拠

> 「Isolate each task in its own git worktree so agents don't interfere with each other」
