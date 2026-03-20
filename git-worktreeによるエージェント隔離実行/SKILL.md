# Git worktreeによるエージェント隔離実行

> 各AIエージェントタスクに独立したgit worktree（ブランチ+作業ディレクトリ）を割り当て、並列実行時の干渉を完全に防ぐ

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

単一の作業ツリーで複数エージェントを動かすと、ファイル変更の競合、依存関係の不整合、意図しないgit状態の混在が発生する。worktreeで物理的に分離すれば各エージェントは独立したクリーンな環境で動作できる

## いつ使うのか

2つ以上のタスクを並行して進めたい時、または1つのエージェントが長時間実行される間に別タスクに着手したい時

## やり方

1. タスクごとに新規ワークスペースを作成（⌘N または ⌘⇧N）
2. Supersetが自動的にgit worktree add <path> <branch>を実行し、専用ディレクトリとブランチを生成
3. 各ワークスペースで異なるCLIエージェント（claude、codex等）を起動
4. .superset/setup.shに「cp ../.env .env && bun install」等の環境構築スクリプトを定義し、worktree作成時に自動実行
5. エージェント完了後、Built-in Diff Viewerで変更を確認し、不要なworktreeは削除（teardownスクリプトも自動実行）

### 入力

- Gitリポジトリ（Git 2.20+）
- .superset/config.jsonにsetup/teardownスクリプト定義
- 各エージェント用のCLIコマンド（claude、codex等）

### 出力

- 隔離されたブランチ＋作業ディレクトリのセット
- 各worktreeで独立して実行されるエージェントプロセス
- worktree単位でcommit可能な変更履歴

## 使うツール・ライブラリ

- git worktree
- Superset（macOS app）
- 任意のCLIコーディングエージェント

## コード例

```
# .superset/config.json
{
  "setup": ["./.superset/setup.sh"],
  "teardown": ["./.superset/teardown.sh"]
}

# .superset/setup.sh
#!/bin/bash
cp ../.env .env
bun install
echo "Workspace ready!"

# 環境変数も利用可能
# $SUPERSET_WORKSPACE_NAME, $SUPERSET_ROOT_PATH
```

## 前提知識

- Git 2.20以上（worktree機能）
- macOS環境（Windows/Linux未検証）
- Bun v1.0以上（ランタイム）
- GitHub CLI（gh）
- 使用したいCLIエージェント（Claude Code、Codex等）のインストールと認証設定
- git worktreeの基本概念（ブランチとディレクトリの分離）

## 根拠

> 「Isolate each task in its own git worktree so agents don't interfere with each other」（worktree隔離による干渉防止）

> setup.shサンプルコード：「cp ../.env .env && bun install」（環境構築自動化の実例）
