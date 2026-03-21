# ワークスペースプリセットによる環境自動セットアップ

> .superset/config.jsonでsetup/teardownスクリプトを定義し、workspace作成時に環境構築を自動化する

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

worktreeを新規作成するたびに手動で.envコピーやbun installを実行するのは非効率。プリセットスクリプトで自動化すれば、エージェント起動までの準備時間を削減できる。

## いつ使うのか

複数のworktreeを頻繁に作成する場合、特に環境構築手順が複数ステップある場合

## やり方

1. リポジトリルートに.superset/config.jsonを作成
2. setupフィールドに実行するスクリプトのパスを配列で指定（例: ["./.superset/setup.sh"]）
3. setup.shで環境変数コピー、依存インストール等を記述
4. teardownフィールドにクリーンアップスクリプトを指定（任意）
5. Supersetで新規workspaceを作成すると自動的にsetupスクリプトが実行される

### 入力

- .superset/config.json（設定ファイル）
- setup/teardownシェルスクリプト

### 出力

- 即座に使える状態のworktree環境（.envコピー済み、依存インストール済み）

## 使うツール・ライブラリ

- Superset
- シェルスクリプト（bash等）

## コード例

```
# .superset/setup.sh
#!/bin/bash
cp ../.env .env
bun install
echo "Workspace ready!"
```

## 前提知識

- gitの基本操作（branch、merge、worktreeの概念）
- CLIベースのAIエージェント（Claude Code、Codex等）の基本的な使い方
- macOS環境（現時点でmacOSのみサポート）
- Bun v1.0+、Git 2.20+、GitHub CLI、Caddyのインストール
