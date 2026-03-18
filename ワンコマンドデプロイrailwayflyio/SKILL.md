# ワンコマンドデプロイ（Railway/Fly.io）

> Wasp CLIの `wasp deploy` コマンドで、DB・サーバー・クライアントを一括で本番環境にデプロイする

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: infrastructure

## なぜ使うのか

手動でDB接続設定・環境変数・ビルド・ホスティング設定を行うと数時間かかる作業を、CLI一発で完了させるため

## いつ使うのか

ローカル開発完了後、MVPを即座に本番公開したい時、またはステージング環境を素早く構築したい時

## やり方

1. Railway または Fly.io のアカウントを作成し、CLIログイン（`railway login` / `flyctl auth login`）
2. プロジェクトルートで `wasp deploy fly launch` または `wasp deploy railway` を実行
3. Wasp が自動で Dockerfile 生成、PostgreSQL プロビジョニング、環境変数設定、ビルド、デプロイを実行
4. デプロイ後、CLIが出力するURLで本番アプリにアクセス可能

### 入力

- Wasp プロジェクト
- Railway または Fly.io アカウント
- 環境変数（Stripe API キー等）

### 出力

- 本番稼働するSaaSアプリ（HTTPS対応）
- プロビジョニングされたPostgreSQLデータベース
- 自動生成されたDockerfile

## 使うツール・ライブラリ

- Wasp CLI
- Railway CLI / Fly.io CLI
- Docker（内部でWaspが生成）

## コード例

```
# Railway へのデプロイ
wasp deploy railway

# Fly.io へのデプロイ
flyctl auth login
wasp deploy fly launch

# 環境変数を .env.server に記載しておくと自動で反映される
```

## 前提知識

- Node.js 18+ の基礎知識
- React と TypeScript の基本文法
- SaaSアプリの構成要素（認証・決済・メール送信）への理解
- Prisma ORM の基本（Schema定義、マイグレーション）
- CLIツールの基本操作（npm、git）

## 根拠

> 「wasp new -t saas - This will create a clean copy of the Open SaaS template into a new directory」

> 「Full-stack Authentication - Email verified + social Auth in a few lines of code」

> 「One-command Deploy - Easily deploy your DB, Server, & Client with one commaned to Railway or Fly.io via the CLI」

> 「100% free modern JS SaaS boilerplate (React, NodeJS, Prisma). Full-featured: Auth (email, google, github, slack, MS), Email sending, Background jobs, Landing page, Payments (Stripe, Polar.sh), Shadcn UI, S3 file upload」
