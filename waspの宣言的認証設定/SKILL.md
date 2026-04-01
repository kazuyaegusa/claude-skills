# Waspの宣言的認証設定

> main.wasp設定ファイルに認証プロバイダーを列挙するだけで、複数SNS認証+メール認証を実装

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: ui-ux

## なぜ使うのか

Passport.js等の手動統合ではプロバイダーごとにコールバック・セッション管理・エラーハンドリングを書く必要があるが、Waspは宣言だけで全て自動生成するため

## いつ使うのか

SaaSアプリに認証機能を追加する時、複数のソーシャルログインを同時に有効化したい時

## やり方

1. `main.wasp` ファイルで `auth` ブロックを定義
2. `methods` に使いたいプロバイダー（email, google, github等）を列挙
3. 環境変数にOAuthクライアントID/Secretを設定
4. Waspが自動でルート・UI・DBスキーマを生成

### 入力

- main.wasp設定ファイル
- 各プロバイダーのOAuth認証情報（env変数）

### 出力

- ログイン/サインアップUI
- セッション管理機構
- Userテーブル自動生成

## 使うツール・ライブラリ

- Wasp framework

## 前提知識

- Node.js基礎知識（npm/yarn操作）
- React基礎（コンポーネント、Hooks）
- TypeScript基礎（型アノテーション）
- Prisma ORM基本概念（スキーマ定義、マイグレーション）
- SaaS基本概念（認証、決済フロー、サブスクリプション）
