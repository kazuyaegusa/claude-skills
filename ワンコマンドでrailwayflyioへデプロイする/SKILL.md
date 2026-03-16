# ワンコマンドでRailway/Fly.ioへデプロイする

> Wasp CLIの`wasp deploy`コマンドで、DB・サーバー・クライアントを一括でホスティングサービスにデプロイする

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: infrastructure

## なぜ使うのか

手動デプロイではDB接続文字列、環境変数、ビルド設定を個別に設定する必要があるが、Waspは設定ファイルから自動的に全てをオーケストレーションする

## いつ使うのか

開発環境から本番環境への初回デプロイ時、または更新をデプロイする時

## やり方

1. RailwayまたはFly.ioのアカウントを作成
2. Wasp CLIにログイン: `wasp deploy`を実行し、プラットフォームを選択
3. CLIがDB、サーバー、クライアントを順次デプロイ
4. デプロイ完了後、提供されるURLでアプリにアクセス

### 入力

- Railway/Fly.ioアカウント
- 環境変数（本番用）

### 出力

- 本番環境のURL
- デプロイされたDB・サーバー・クライアント

## 使うツール・ライブラリ

- Wasp CLI
- Railway
- Fly.io

## コード例

```
wasp deploy
```

## 前提知識

- Node.js/npmの基本的な使い方
- React/TypeScriptの基礎知識
- Prismaの基本的なスキーマ定義（データモデル構築時）
- Stripe/Lemon Squeezy等の決済サービスの基本概念（決済統合時）

## 根拠

> 「First, to install the latest version of Wasp on macOS, Linux, or Windows with WSL, run the following command: `npm i -g @wasp.sh/wasp-cli`. Then, create a new SaaS app with the following command: `wasp new -t saas`」
