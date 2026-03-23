# Prefect Horizon無料ホスティングで本番デプロイ

> 開発したFastMCPサーバーをPrefect Horizonにデプロイし、無料で本番環境として公開する

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: automation-pipeline

## なぜ使うのか

MCPサーバーをローカル開発からクラウド公開に移行する際、インフラ構築・認証・スケーリングが課題となる。Prefect HorizonはFastMCPユーザー向けに無料ホスティングを提供し、これらを自動化する

## いつ使うのか

プロトタイプを他者と共有したい、または本番環境で継続運用したいとき。インフラ管理を避けたい個人開発者やスタートアップに最適

## やり方

1. FastMCPサーバーを実装
2. Prefect Horizonアカウント作成（https://www.prefect.io/horizon）
3. FastMCPプロジェクトをPrefect Horizonにデプロイ（詳細は公式ドキュメント参照）
4. 生成されたURLで外部から接続可能に

### 入力

- FastMCPで実装したサーバーコード
- Prefect Horizonアカウント

### 出力

- 公開MCPサーバーURL
- 管理ダッシュボード

## 使うツール・ライブラリ

- Prefect Horizon (https://www.prefect.io/horizon)
- fastmcp

## 前提知識

- Pythonの基本文法（関数定義、デコレータ、型ヒント）
- MCPの基本概念（ツール・リソース・プロンプトの役割）
- 非同期プログラミングの基礎（Clientsを使う場合）

## 根拠

> 「When you're ready to deploy, Prefect Horizon offers free hosting for FastMCP users.」（無料ホスティング提供）
