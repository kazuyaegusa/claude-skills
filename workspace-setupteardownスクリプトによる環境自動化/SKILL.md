# workspace setup/teardownスクリプトによる環境自動化

> workspaceごとに.envコピー、依存インストール、DB初期化等を自動実行する

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

worktreeは新規ディレクトリなので、毎回手動で環境セットアップすると時間がかかる。setup/teardownスクリプトで自動化すれば、エージェント起動前に環境が整い、削除時にクリーンアップも完了する

## いつ使うのか

worktreeごとに.envや依存パッケージが必要な場合。DB接続、APIキー等のシークレットをworktree間で共有したい時

## やり方

1. プロジェクトルートに.superset/config.jsonを作成
2. setup/teardownキーに実行スクリプトパスを配列で記述
3. .superset/setup.shにcp ../.env .env、bun install等を記述
4. 実行権限付与（chmod +x .superset/setup.sh）
5. workspace作成時に自動実行される

### 入力

- .superset/config.json（setup/teardown配列）
- .superset/setup.sh等のスクリプトファイル
- 環境変数：SUPERSET_WORKSPACE_NAME, SUPERSET_ROOT_PATH

### 出力

- workspace作成時に自動セットアップされた環境
- workspace削除時に自動クリーンアップ

## 使うツール・ライブラリ

- シェルスクリプト（bash等）
- .superset/config.json

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
echo "Workspace ready!"
```

## 前提知識

- git worktreeの基本概念（1つのリポジトリから複数の作業ディレクトリを作成できる）
- CLIエージェント（Claude Code、Codex等）の基本的な使い方
- git操作の基礎（branch、merge、diff）
- macOS環境（現時点ではWindows/Linux未対応）
- Bun、Git 2.20+、GitHub CLIのインストール

## 根拠

> 「Open any workspace where you need it with one-click handoff to your editor or terminal」

> 「Scripts have access to environment variables: SUPERSET_WORKSPACE_NAME, SUPERSET_ROOT_PATH」
