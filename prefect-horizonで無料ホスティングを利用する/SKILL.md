# Prefect Horizonで無料ホスティングを利用する

> FastMCPで作ったサーバーをPrefect Horizon（Prefect社の提供するホスティング）に無料デプロイする

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: other

## なぜ使うのか

ローカル開発から本番環境への移行が簡単になり、リモートMCPサーバーとして公開できる

## いつ使うのか

プロトタイプを本番化したい時、チームで共有可能なMCPサーバーを立てたい時

## やり方

1. FastMCPサーバーを実装
2. Prefect Horizonアカウント作成
3. 公式ドキュメントのデプロイガイドに従ってアップロード

### 入力

- 完成したFastMCPサーバーコード
- Prefect Horizonアカウント

### 出力

- インターネット経由でアクセス可能なMCPサーバー

## 使うツール・ライブラリ

- Prefect Horizon（無料プラン）

## 前提知識

- Python 3.x の基本文法（関数定義、デコレータ）
- 型ヒント（type hints）の理解
- MCP（Model Context Protocol）の概念（LLMとツールを接続するプロトコル）
- FastAPIやFlaskのようなPythonフレームワークの使用経験があると理解が早い

## 根拠

> 「Prefect Horizon offers free hosting for FastMCP users」（無料ホスティング）
