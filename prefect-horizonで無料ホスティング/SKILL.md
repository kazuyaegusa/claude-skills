# Prefect Horizonで無料ホスティング

> FastMCPサーバーをPrefect Horizonプラットフォームに無料でデプロイし、リモートから利用可能にする

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: other

## なぜ使うのか

ローカル実行では外部からアクセスできないため、本番環境やチーム共有のためにホスティングが必要になる

## いつ使うのか

MCPサーバーを外部公開したい時、チームで共有したい時

## やり方

1. FastMCPサーバーを実装
2. Prefect Horizonにサインアップ
3. デプロイ手順（公式ドキュメント参照）に従ってサーバーをアップロード
4. 提供されたURLでクライアントから接続

### 入力

- FastMCPサーバーコード
- Prefect Horizonアカウント

### 出力

- 公開URL
- リモートアクセス可能なMCPサーバー

## 使うツール・ライブラリ

- Prefect Horizon
- fastmcp

## 前提知識

- Python 3.xの基礎知識
- 型ヒント（Type Hints）の理解
- デコレータの基本概念
- Model Context Protocol（MCP）の概要
- LLMツール統合の基本的な動機

## 根拠

> When you're ready to deploy, Prefect Horizon offers free hosting for FastMCP users.
