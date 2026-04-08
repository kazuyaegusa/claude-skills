# workspace preset自動セットアップ

> .superset/config.json でworktree作成時の環境構築スクリプトを定義し、依存関係インストールや環境変数コピーを自動化する

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

各worktreeで毎回手動セットアップすると時間がかかり、設定漏れが発生するため

## いつ使うのか

複数worktreeで同じ環境構築手順を繰り返す場合、チームで標準化したい場合

## やり方

1. `.superset/config.json` に setup/teardown スクリプトを記述
2. setup.sh で .env コピー、bun install、初期化処理を実行
3. worktree作成時に自動で setup が走る
4. worktree削除時に teardown で後片付け
5. スクリプト内で SUPERSET_WORKSPACE_NAME 等の環境変数が利用可能

### 入力

- .superset/config.json 設定ファイル
- setup/teardown用シェルスクリプト
- メインリポジトリの .env や依存関係定義

### 出力

- 自動構築された実行可能なworktree環境
- 統一された開発環境

## 使うツール・ライブラリ

- bash/sh
- bun / npm / yarn等のパッケージマネージャ

## コード例

```
{
  "setup": ["./.superset/setup.sh"],
  "teardown": ["./.superset/teardown.sh"]
}

# setup.sh
cp ../.env .env
bun install
echo "Workspace ready!"
```

## 前提知識

- git worktreeの基本概念（メインリポジトリと独立した作業ツリー）
- CLIベースのAIコーディングエージェントの使用経験
- macOS環境（現時点でWindows/Linuxは未検証）
- Bun v1.0+、git 2.20+、gh CLI、Caddyのインストール

## 根拠

> 「setup.sh内で環境変数 SUPERSET_WORKSPACE_NAME, SUPERSET_ROOT_PATH が利用可能」
