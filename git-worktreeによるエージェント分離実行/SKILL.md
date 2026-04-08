# git worktreeによるエージェント分離実行

> 1つのリポジトリから複数のworktreeを作成し、各エージェントを独立した作業ディレクトリで実行する

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: claude-code-workflow

## なぜ使うのか

複数エージェントが同じファイルを同時編集すると競合が発生するため、物理的に作業ディレクトリを分離する必要がある

## いつ使うのか

2つ以上のタスクを並列実行したい時、エージェントの待ち時間中に別作業をしたい時

## やり方

1. メインリポジトリから `git worktree add` で新しいworktreeを作成
2. 各worktreeに専用のブランチを割り当て
3. SupersetのUIから各worktreeでエージェント（Claude Code, Codex等）を起動
4. エージェントが完了したらdiff viewerで変更を確認
5. 承認後にメインブランチへマージ

### 入力

- git 2.20+がインストールされた環境
- 並列実行したい複数のタスク定義
- CLIベースのコーディングエージェント

### 出力

- 各タスク専用のworktreeとブランチ
- 並列実行されたエージェントの変更差分
- マージ可能なPRまたはコミット

## 使うツール・ライブラリ

- git worktree
- Superset (オーケストレーター)
- Claude Code / Codex / Cursor Agent等

## コード例

```
git worktree add ../worktree-feature-a -b feature-a
git worktree add ../worktree-bugfix-b -b bugfix-b
```

## 前提知識

- git worktreeの基本概念（メインリポジトリと独立した作業ツリー）
- CLIベースのAIコーディングエージェントの使用経験
- macOS環境（現時点でWindows/Linuxは未検証）
- Bun v1.0+、git 2.20+、gh CLI、Caddyのインストール

## 根拠

> 「Isolate each task in its own git worktree so agents don't interfere with each other」
