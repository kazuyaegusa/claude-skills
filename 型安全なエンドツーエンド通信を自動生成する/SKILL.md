# 型安全なエンドツーエンド通信を自動生成する

> バックエンドの関数型を定義すると、Waspがフロントエンドで型推論されたRPC関数を自動生成する

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: dev-tool

## なぜ使うのか

従来のREST/GraphQLではフロントエンドとバックエンドの型同期にtRPCやGraphQL Codegenが必要だが、Waspはビルド時に自動的に型を伝播させるため追加設定不要

## いつ使うのか

フロントエンド・バックエンド間の型安全性を保証したい全ての開発シーン

## やり方

1. バックエンドで`queries.ts`や`actions.ts`に型付き関数を定義
2. Waspファイルで`query`/`action`として宣言
3. フロントエンドで`import { useQuery } from 'wasp/client/operations'`し、型推論された関数を呼び出す
4. バックエンド側の型変更が即座にフロントエンドのTypeScriptエラーとして表示される

### 入力

- バックエンドの型付きクエリ/アクション関数

### 出力

- フロントエンドで型推論されたuseQuery/useMutationフック

## 使うツール・ライブラリ

- Wasp
- TypeScript

## 前提知識

- Node.js/npmの基本的な使い方
- React/TypeScriptの基礎知識
- Prismaの基本的なスキーマ定義（データモデル構築時）
- Stripe/Lemon Squeezy等の決済サービスの基本概念（決済統合時）
