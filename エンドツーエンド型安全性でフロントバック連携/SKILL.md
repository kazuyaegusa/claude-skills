# エンドツーエンド型安全性でフロント・バック連携

> バックエンド関数の型定義をフロントエンドで自動推論させることで、サードパーティライブラリなしに完全な型安全性を実現する

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: dev-tool

## なぜ使うのか

通常、React + Node.js構成ではフロント・バック間の型共有にtRPC/GraphQL Codegenなどの追加ツールが必要だが、Waspはフレームワークレベルで型推論を行うため、設定不要・学習コスト不要で型安全性が得られる

## いつ使うのか

新しいAPI操作を追加する時、既存APIのレスポンス型を変更する時（フロント側の型エラーで影響範囲が即座に判明）

## やり方

1. バックエンドで`query`または`action`を定義（例: `src/queries.ts`に`export const getReports: GetReports = async (args, context) => { ... }`）
2. Waspがこの関数の型を自動抽出し、フロントエンド用の型定義を生成
3. フロントエンドで`import { getReports } from '@wasp/queries'`してuseQueryフックで呼び出すと、引数・戻り値の型が自動で推論される
4. TypeScriptコンパイラがフロント・バック間の型不整合を即座に検出

### 入力

- バックエンド関数の型定義（TypeScript）

### 出力

- フロントエンドで自動推論される型安全なクエリ・アクションフック
- 型不整合による実行時エラーの防止

## 使うツール・ライブラリ

- Wasp framework（型推論エンジン）
- TypeScript

## コード例

```
// Backend: src/queries.ts
export const getReports: GetReports = async (args, context) => {
  return context.entities.Report.findMany({ where: { userId: context.user.id } });
};

// Frontend: 自動生成された型でuseQueryが型安全に
import { useQuery } from '@wasp/queries';
import getReports from '@wasp/queries/getReports';

const { data } = useQuery(getReports); // data の型が自動推論される
```

## 前提知識

- Node.js/npmの基礎知識
- React + TypeScriptの基本（コンポーネント・フック）
- REST API/データベース操作の概念（Prismaの経験があると理想的）
- Stripe/決済API統合の基本知識（決済機能を使う場合）
- Dockerまたはクラウドデプロイの基礎（本番運用時）
