# Waspの宣言的設定で認証・ジョブ・デプロイを実装

> Waspの設定ファイル（.waspファイル）に認証プロバイダー、バックグラウンドジョブ、デプロイターゲットを宣言的に記述し、定型コードなしで機能を有効化する

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: automation-pipeline

## なぜ使うのか

Express/Passport/Bull等を手動で組み合わせると設定ミス・セキュリティリスクが高まり、型安全性も失われる。Waspの宣言的設定により、フレームワークがベストプラクティスを自動適用し、TypeScript型も自動生成される

## いつ使うのか

認証フローを追加する時、定期実行タスク（メール送信・レポート生成等）を設定する時、本番環境へデプロイする時

## やり方

1. main.waspファイルを開く
2. `auth`ブロックでemail/google/github等のプロバイダーを指定（例: `methods: { email: {}, google: {} }`）
3. `job`ブロックでcronスケジュールやキュー設定を記述（例: `job myJob { executor: PgBoss, perform: { fn: import { myJob } from '@src/jobs' } }`）
4. `app`ブロックの`deploy`セクションでRailway/Fly.ioターゲットを指定
5. `wasp build`で本番ビルド、`wasp deploy`でワンコマンドデプロイ実行

### 入力

- main.waspファイル
- 認証プロバイダーのクライアントID・シークレット
- デプロイ先（Railway/Fly.io）のアカウント

### 出力

- 認証フロー（サインアップ・ログイン・パスワードリセット）が自動生成される
- バックグラウンドジョブがPgBossキューで実行される
- DB・サーバー・クライアントが指定クラウドに自動デプロイされる

## 使うツール・ライブラリ

- Wasp framework
- PgBoss（ジョブキュー）
- Railway or Fly.io（デプロイ先）

## コード例

```
// main.wasp example
app MySaaS {
  auth: {
    userEntity: User,
    methods: { email: {}, google: {} }
  }
}

job sendWeeklyReport {
  executor: PgBoss,
  perform: { fn: import { sendReport } from '@src/jobs' },
  schedule: { cron: "0 9 * * 1" }
}
```

## 前提知識

- Node.js/npmの基礎知識
- React + TypeScriptの基本（コンポーネント・フック）
- REST API/データベース操作の概念（Prismaの経験があると理想的）
- Stripe/決済API統合の基本知識（決済機能を使う場合）
- Dockerまたはクラウドデプロイの基礎（本番運用時）
