# Git worktreeでAgentタスクを隔離実行する

> 各AI Agentを独立したgit worktree（別ディレクトリ）で起動し、同一リポジトリ内で複数タスクを並行実行する

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: claude-code-workflow

## なぜ使うのか

通常のgit branchだけでは作業ディレクトリが共有されるため、複数Agentが同時にファイル編集すると衝突する。worktreeなら物理的にディレクトリが分離されるため干渉しない

## いつ使うのか

複数の独立タスクを同時進行させたい、かつ各タスクが同じリポジトリ内の異なる箇所を触る場合

## やり方

1. `git worktree add <path> <branch>` で新規worktreeを作成
2. Supersetが各worktreeでCLI Agent（claude code, codex等）を起動
3. 各Agentは独立したディレクトリ内で変更を実施
4. 完了後、Superset内蔵diffビューアで各worktreeの変更をレビュー
5. 必要に応じてgit merge/rebase/cherry-pickで統合
6. worktree削除（`git worktree remove <path>`）またはteardownスクリプト実行

### 入力

- git 2.20+がインストール済みの環境
- CLI Agent（claude, codex, cursor等）がパスに存在
- 親リポジトリ（main）のクリーンな状態

### 出力

- 各worktree内の変更コミット
- Superset UI上での差分・ステータス表示
- 統合可能な複数ブランチ

## 使うツール・ライブラリ

- git worktree
- Superset（Electron製デスクトップアプリ）
- 任意のCLI Agent

## コード例

```
# Superset内部で実行される想定のコマンド例
git worktree add ../worktree-task1 feature/task1
cd ../worktree-task1
claude code "Implement feature X"

# 別ターミナル
git worktree add ../worktree-task2 feature/task2
cd ../worktree-task2
codex "Fix bug Y"
```

## 前提知識

- Git 2.20+の基本操作（worktree概念の理解）
- CLI AgentのインストールとAPI認証設定
- macOS環境（Windows/Linux未検証）
- Bun v1.0+のインストール（ソースビルド時）
- GitHub CLI（gh）のインストール

## 根拠

> 「Orchestrate swarms of Claude Code, Codex, and more in parallel.」（README冒頭）

> 「Isolate each task in its own git worktree so agents don't interfere with each other」（機能説明）
