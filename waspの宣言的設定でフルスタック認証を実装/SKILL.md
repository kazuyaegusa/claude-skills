# Waspの宣言的設定でフルスタック認証を実装

> Waspの設定ファイル（wasp.config）に認証方式（email/Google/GitHub/Slack等）を記述するだけで、バックエンド・フロントエンドの認証フローを自動生成する

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: dev-tool

## なぜ使うのか

従来はPassport.js/NextAuth等でルート・ミドルウェア・DB連携を手動実装し、フロント側のトークン管理も別途必要。Waspは設定を解釈してコード生成し、型安全なクライアントAPIも自動提供する

## いつ使うのか

複数のOAuthプロバイダとメール認証を組み合わせたい、かつ型安全なAPIを自動生成したいとき

## やり方

1. `main.wasp` ファイルの `auth` ブロックに `methods: { email: {...}, google: {...} }` を記述
2. `userEntity` と `User` モデルをPrisma schemaで定義
3. `wasp db migrate-dev` でDBマイグレーション実行
4. フロントで `import { useAuth } from '@wasp/auth'` を使い、認証状態を取得
5. サーバーサイドで `context.user` から認証ユーザー情報を参照

### 入力

- OAuth client ID/secret（Google/GitHub/Slack等）
- SendGrid/MailGun APIキー（メール認証用）
- Prisma対応DB（PostgreSQL推奨）

### 出力

- 認証済みユーザーのセッション管理
- 型安全な `useAuth()` フック
- `context.user` でのサーバーサイド認証

## 使うツール・ライブラリ

- Wasp
- Prisma
- Passport.js（内部で利用）

## コード例

```
// main.wasp
auth {
  userEntity: User,
  methods: {
    email: { ... },
    google: { ... }
  },
  onAuthFailedRedirectTo: "/login"
}
```

## 前提知識

- Node.js/npm基礎知識
- React・TypeScriptの基本構文
- Prisma ORMの概念（スキーマ定義・マイグレーション）
- REST API / HTTPクライアントの理解
- Stripe/決済APIの基本的な動作原理（サブスク課金を使う場合）
