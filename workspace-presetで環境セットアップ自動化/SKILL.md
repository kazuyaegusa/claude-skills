# Workspace Presetで環境セットアップ自動化

> .superset/config.json にセットアップ・ティアダウンスクリプトを定義し、worktree作成時に自動で環境変数コピー、依存関係インストール等を実行する

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

worktreeを新規作成するたびに手動で .env をコピーしたり `npm install` を実行するのは非効率。スクリプトで自動化すれば、エージェントが即座に作業を開始できる。

## いつ使うのか

新しいworktreeで毎回同じ初期化処理が必要な時、チームで標準化されたセットアップを共有したい時

## やり方

1. プロジェクトルートに `.superset/config.json` を作成
2. `setup` フィールドに実行したいシェルスクリプトのパスを配列で指定（例: `["./.superset/setup.sh"]`）
3. `setup.sh` 内で環境変数コピー、依存関係インストール、DBマイグレーション等を記述
4. `teardown` フィールドに後処理スクリプトを指定（例: 一時ファイル削除）
5. Supersetでワークスペース作成時、自動的に `setup` スクリプトが実行される
6. 環境変数 `SUPERSET_WORKSPACE_NAME`, `SUPERSET_ROOT_PATH` が利用可能

### 入力

- .superset/config.json
- セットアップスクリプト（.sh等）

### 出力

- worktree作成と同時に完了した環境準備
- エージェントがすぐ作業開始できる状態

## 使うツール・ライブラリ

- シェルスクリプト
- Superset config.json

## コード例

```
{
  "setup": ["./.superset/setup.sh"],
  "teardown": ["./.superset/teardown.sh"]
}

#!/bin/bash
# .superset/setup.sh
cp ../.env .env
bun install
echo "Workspace ready!"
```

## 前提知識

- git 2.20以上がインストールされていること（worktree機能）
- macOS環境（Windows/Linuxは未検証）
- Bun v1.0+ランタイム（ビルド・実行用）
- GitHub CLI（gh）とCaddy（開発サーバー用）のインストール
- CLIベースのAIエージェント（Claude Code, Codex, Gemini CLI等）が動作する環境
- git worktreeの基本概念（複数の作業ディレクトリを同一リポジトリで管理）の理解

## 根拠

> ".superset/config.json" で "setup": ["./.superset/setup.sh"] を定義することでワークスペース作成時に自動実行

> "⌘1-9: Switch to workspace 1-9"（キーボードショートカット仕様）
