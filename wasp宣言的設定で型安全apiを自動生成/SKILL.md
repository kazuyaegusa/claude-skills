# Wasp宣言的設定で型安全APIを自動生成

> main.wasp ファイルにクエリ・アクション（CRUD操作）を宣言すると、バックエンド関数の型がフロントエンドに自動推論され、型安全なAPIクライアントが生成される

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: dev-tool

## なぜ使うのか

tRPCやGraphQLのようなコード生成ツールなしに、設定ファイルだけでエンドツーエンドの型安全性を実現し、ボイラープレート記述を削減するため

## いつ使うのか

フロントエンドとバックエンド間のAPI通信を型安全にしたい全てのケース（CRUD、認証後のデータ取得、決済処理など）

## やり方

1. main.wasp で `query` または `action` ブロックを定義し、バックエンド関数（TypeScript）のパスを指定
2. バックエンド関数で引数と戻り値の型を定義
3. フロントエンド（React）で `import { useQuery } from 'wasp/client/operations'` を使うと、引数・戻り値が自動で型推論される
4. Wasp コンパイラが裏でクライアント用の型定義とAPIフェッチ関数を生成

### 入力

- main.wasp の query/action 定義
- src/server/ 配下のバックエンドTypeScript関数

### 出力

- 型安全なuseQueryフック（React Query互換）
- 自動生成されたクライアントコード（.wasp/out/sdk/wasp/client/operations）

## 使うツール・ライブラリ

- Wasp フレームワーク
- Prisma（ORMとして内部利用）
- React Query（フロントエンドのデータフェッチ基盤）

## コード例

```
// main.wasp
query getTasks {
  fn: import { getTasks } from "@server/tasks",
  entities: [Task]
}

// src/server/tasks.ts
export const getTasks = async (args, context) => {
  return context.entities.Task.findMany();
};

// src/client/TaskPage.tsx
import { useQuery } from 'wasp/client/operations';
const { data: tasks } = useQuery(getTasks); // 型が自動推論される
```

## 前提知識

- Node.js 18+ の基礎知識
- React と TypeScript の基本文法
- SaaSアプリの構成要素（認証・決済・メール送信）への理解
- Prisma ORM の基本（Schema定義、マイグレーション）
- CLIツールの基本操作（npm、git）

## 根拠

> 「wasp new -t saas - This will create a clean copy of the Open SaaS template into a new directory」
