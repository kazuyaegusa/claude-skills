# Workspace Presetsでエージェント環境を自動セットアップする

> .superset/config.json にsetup/teardownスクリプトを定義し、ワークスペース作成時の環境構築・削除時のクリーンアップを自動化する。

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェントを動かすには.envのコピー、依存関係のインストール、DBマイグレーション等が必要。手動でやると漏れ・ミスが発生し、エージェントが正しく動かない。自動化すれば確実で高速。

## いつ使うのか

エージェント実行前に毎回同じセットアップが必要なとき、チームで統一された環境構築手順を共有したいとき

## やり方

1. プロジェクトルートに .superset/config.json を作成
2. setup配列にワークスペース作成時のコマンド、teardown配列に削除時のコマンドを記述
3. 例: {"setup": ["./.superset/setup.sh"], "teardown": ["./.superset/teardown.sh"]}
4. setup.sh 内で cp ../.env .env && bun install のような初期化処理を実行
5. 環境変数 SUPERSET_WORKSPACE_NAME, SUPERSET_ROOT_PATH が自動注入されるため、スクリプト内で利用可能

### 入力

- セットアップ手順（シェルスクリプトまたはコマンド）
- .superset/config.json設定ファイル

### 出力

- 即座に使える完全な開発環境（依存関係・env・DB等）
- 削除時の自動クリーンアップ

## 使うツール・ライブラリ

- Superset
- bash/zsh等のシェル

## コード例

```
#!/bin/bash
# .superset/setup.sh

# Copy environment variables
cp ../.env .env

# Install dependencies
bun install

# Run any other setup tasks
echo "Workspace ready!"
```

## 前提知識

- git 2.20以上の基礎知識（worktree概念の理解が望ましい）
- macOS環境（現時点でWindows/Linuxは未検証）
- Bun v1.0+, GitHub CLI (gh), Caddy（開発時のみ）
- CLIベースのコーディングエージェント（Claude Code, Cursor Agent等）のいずれか

## 根拠

> setup/teardown スクリプト例: cp ../.env .env && bun install

> 環境変数: SUPERSET_WORKSPACE_NAME, SUPERSET_ROOT_PATH
