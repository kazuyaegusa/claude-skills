# End-to-End型安全性の自動推論

> サーバー側の関数に型を付けると、クライアント側で自動的に型が推論され、tRPC等の追加設定不要で型安全なRPCが可能

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: dev-tool

## なぜ使うのか

手動でGraphQL/tRPCスキーマを書くとコードと型定義が二重管理になるが、Waspはサーバー関数の型からクライアント型を自動生成するため

## いつ使うのか

フルスタックTypeScriptプロジェクトで型安全性を保ちながらAPI呼び出しをしたい時

## やり方

1. サーバー側で `export const getUser: GetUser = async (args, context) => { ... }` と型付き関数を定義
2. クライアントで `import { getUser } from 'wasp/client/operations'` をインポート
3. 呼び出し時に引数・返り値が自動で型チェックされる

### 入力

- サーバー側の型付き関数定義

### 出力

- クライアント側で型推論されたAPI関数

## 使うツール・ライブラリ

- Wasp framework
- TypeScript

## 前提知識

- Node.js基礎知識（npm/yarn操作）
- React基礎（コンポーネント、Hooks）
- TypeScript基礎（型アノテーション）
- Prisma ORM基本概念（スキーマ定義、マイグレーション）
- SaaS基本概念（認証、決済フロー、サブスクリプション）
