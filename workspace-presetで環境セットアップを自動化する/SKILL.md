# Workspace Presetで環境セットアップを自動化する

> .superset/config.jsonにsetup/teardownスクリプトを定義し、worktree作成時に自動実行する

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

worktreeは空のディレクトリなので、.env, node_modules等の環境を毎回手動セットアップするのは非効率。スクリプト化により即座に開発可能な状態にする

## いつ使うのか

複数worktreeで同じ環境セットアップが必要、またはdependencyインストール・DBマイグレーション等の定型作業がある場合

## やり方

1. リポジトリルートに `.superset/config.json` を作成
2. `setup` に実行したいコマンド配列を記述（例: `cp ../.env .env`, `bun install`）
3. `teardown` にworktree削除前のクリーンアップコマンドを記述
4. Supersetが新規workspace作成時に自動でsetupスクリプトを実行
5. workspace削除時にteardownを実行

### 入力

- 親リポジトリに.superset/config.json
- setup/teardownスクリプトファイル（実行権限必須）

### 出力

- worktree作成直後に即開発可能な環境
- SUPERSET_WORKSPACE_NAME, SUPERSET_ROOT_PATH等の環境変数

## 使うツール・ライブラリ

- bash/zsh等のシェル
- Superset

## コード例

```
// .superset/config.json
{
  "setup": ["./.superset/setup.sh"],
  "teardown": ["./.superset/teardown.sh"]
}

// .superset/setup.sh
#!/bin/bash
cp ../.env .env
bun install
echo "Workspace $SUPERSET_WORKSPACE_NAME ready!"
```

## 前提知識

- Git 2.20+の基本操作（worktree概念の理解）
- CLI AgentのインストールとAPI認証設定
- macOS環境（Windows/Linux未検証）
- Bun v1.0+のインストール（ソースビルド時）
- GitHub CLI（gh）のインストール

## 根拠

> 「Scripts have access to environment variables: SUPERSET_WORKSPACE_NAME, SUPERSET_ROOT_PATH」（config.json仕様）
