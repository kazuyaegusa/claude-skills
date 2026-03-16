# Waspの宣言的設定で認証を数行で実装する

> Waspの設定ファイルに認証プロバイダーを宣言するだけで、フルスタック認証（Email確認・ソーシャルログイン）を自動生成する

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: ui-ux

## なぜ使うのか

PassportJS等の手動統合は設定が煩雑でエラーが起きやすい。Waspは設定を型安全に管理し、フロントエンド・バックエンド両方のコードを自動生成するため

## いつ使うのか

ユーザー登録・ログイン機能が必要な全てのSaaSアプリ開発時

## やり方

1. Wasp設定ファイル（main.wasp）で認証方式を宣言（例: `auth: { userEntity: User, methods: { email: {...}, google: {...} } }`）
2. 環境変数にOAuthクライアントID/シークレットを設定
3. Waspが自動生成する認証ルート・コンポーネントをフロントエンドで利用
4. `wasp db migrate-dev`でPrismaスキーマを同期

### 入力

- 認証プロバイダーのOAuth認証情報（Google/GitHub等）
- メール確認用のSMTP設定

### 出力

- 認証API（/auth/email, /auth/google等）
- フロントエンド用のLoginForm/SignupFormコンポーネント
- 認証済みユーザー情報を返すuseAuthフック

## 使うツール・ライブラリ

- Wasp
- Prisma

## 前提知識

- Node.js/npmの基本的な使い方
- React/TypeScriptの基礎知識
- Prismaの基本的なスキーマ定義（データモデル構築時）
- Stripe/Lemon Squeezy等の決済サービスの基本概念（決済統合時）

## 根拠

> 「First, to install the latest version of Wasp on macOS, Linux, or Windows with WSL, run the following command: `npm i -g @wasp.sh/wasp-cli`. Then, create a new SaaS app with the following command: `wasp new -t saas`」
