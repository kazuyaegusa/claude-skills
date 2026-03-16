# git worktreeによるエージェント隔離

> 各タスクを独立したgit worktree（ブランチ＋作業ディレクトリ）に割り当て、複数エージェントが同一リポジトリで干渉せずに並列実行できるようにする

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: claude-code-workflow

## なぜ使うのか

通常の単一作業ディレクトリでは複数エージェントが同時にファイルを変更すると衝突し、コンテキストが混在する。worktreeで物理的に分離することで、各エージェントは独立した環境で安全に動作でき、変更のレビューも個別に行える。

## いつ使うのか

同一リポジトリで複数の開発タスクを並列で進めたい時

## やり方

1. Supersetで新規workspaceを作成（内部で`git worktree add`相当の処理）
2. 各workspaceに専用のブランチと作業ディレクトリが自動作成される
3. エージェント（Claude Code等）をそのディレクトリで起動
4. エージェントが変更を加えると、そのworktree内でのみ反映される
5. Superset UIで各workspaceの差分を一元管理・レビュー

### 入力

- git管理されたリポジトリ
- タスク定義（workspace名やブランチ名）

### 出力

- 独立したworktree（ブランチ＋ディレクトリ）
- 衝突のないエージェント実行環境

## 使うツール・ライブラリ

- git worktree
- Superset（Electron製UIラッパー）

## コード例

```
# Superset内部で実行される想定のgit操作
git worktree add ../workspace-feature-x feature-x
cd ../workspace-feature-x
# エージェント起動
claude-code ...
```

## 前提知識

- git 2.20以上（worktree機能）
- CLIベースのAIエージェント（Claude Code, Cursor Agent等）
- macOS環境（Windows/Linuxは未検証）
- 複数タスクを並列実行する意義の理解

## 根拠

> 「Isolate each task in its own git worktree so agents don't interfere with each other」（worktree分離の明示）

> 「.superset/config.json」「setup/teardown scripts」（preset自動化）

> 「Download Superset for macOS」（ビルド済み配布）

> 「Requirements: OS macOS, Runtime Bun v1.0+, Git 2.20+」（技術要件）
