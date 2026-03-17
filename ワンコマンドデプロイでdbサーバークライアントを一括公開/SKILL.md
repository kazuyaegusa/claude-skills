# ワンコマンドデプロイでDB・サーバー・クライアントを一括公開

> Wasp CLIの `wasp deploy` コマンドでRailway/Fly.ioへDB・バックエンド・フロントエンドを自動デプロイする

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: infrastructure

## なぜ使うのか

従来はVercel/Heroku/AWS等へ個別デプロイし、環境変数・DB接続・ビルド設定をそれぞれ管理する必要がある。Waspは設定を解析して依存関係を自動解決し、一括デプロイする

## いつ使うのか

MVPを即座に本番環境へ公開し、手動デプロイの手間を削減したいとき

## やり方

1. Railway/Fly.ioのアカウントを取得しCLIでログイン
2. `wasp deploy fly launch` （Fly.io）または `railway login && wasp deploy railway` （Railway）を実行
3. Waspが自動的にPostgreSQL DBをプロビジョニング
4. サーバー（NodeJS）とクライアント（静的サイト）をビルドしてデプロイ
5. 環境変数（Stripe key等）は `wasp deploy fly secrets` で追加

### 入力

- Railway/Fly.ioアカウント
- 環境変数（API key等）

### 出力

- 本番稼働中のDB・サーバー・クライアント
- HTTPSエンドポイント

## 使うツール・ライブラリ

- Wasp CLI
- Fly.io / Railway
- PostgreSQL

## コード例

```
wasp deploy fly launch
wasp deploy fly secrets set STRIPE_KEY=sk_live_...
```

## 前提知識

- Node.js/npm基礎知識
- React・TypeScriptの基本構文
- Prisma ORMの概念（スキーマ定義・マイグレーション）
- REST API / HTTPクライアントの理解
- Stripe/決済APIの基本的な動作原理（サブスク課金を使う場合）

## 根拠

> 「Wasp new -t saas」でクリーンなSaaSテンプレートが生成される

> 「One-command Deploy - Easily deploy your DB, Server, & Client with one command」

> 「npm i -g @wasp.sh/wasp-cli」「wasp new -t saas」の実行手順が明記
