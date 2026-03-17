# End-to-End型安全性でフロント・バック連携

> バックエンドのクエリ/アクション関数にTypeScript型を付けると、フロントエンドで自動的に型推論されたAPIが利用できる

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: dev-tool

## なぜ使うのか

従来はtRPC/GraphQLを別途導入し、スキーマ定義とコード生成のセットアップが必要。Waspはファイルベースの規約で型を自動伝播させ、ビルド時に検証する

## いつ使うのか

API型のズレによるランタイムエラーを防ぎたい、かつ追加ライブラリなしで型安全性を確保したいとき

## やり方

1. `src/server/queries.ts` に `export const getUser: GetUser<...> = async (args, context) => { ... }` を実装
2. `main.wasp` で `query getUser { fn: import { getUser } from "@server/queries" }` を宣言
3. フロント側で `import { useQuery } from '@wasp/queries'` → `useQuery(getUser, args)` と呼ぶだけで型推論が効く
4. リンクも `<Link to="/user/:id">` で型安全にパラメータを渡せる

### 入力

- Waspの `query`/`action` 宣言
- TypeScript型定義

### 出力

- フロントで自動推論されるAPI型
- 型安全な `useQuery`/`useAction` フック

## 使うツール・ライブラリ

- Wasp
- TypeScript

## コード例

```
// server/queries.ts
export const getUser: GetUser<Pick<User, 'id' | 'name'>, { id: string }> = async ({ id }, context) => {
  return context.entities.User.findUnique({ where: { id } });
};

// client
const { data } = useQuery(getUser, { id: '123' }); // data は型推論される
```

## 前提知識

- Node.js/npm基礎知識
- React・TypeScriptの基本構文
- Prisma ORMの概念（スキーマ定義・マイグレーション）
- REST API / HTTPクライアントの理解
- Stripe/決済APIの基本的な動作原理（サブスク課金を使う場合）
