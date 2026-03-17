# Waspのジョブ定義でcronとキューを実装

> 設定ファイルにジョブ（cron/キュー）を宣言し、TypeScript関数を実装するだけでバックグラウンド処理を実行する

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: automation-pipeline

## なぜ使うのか

BullMQ/Agenda等のライブラリは設定が煩雑で、Redis/MongoDBの追加管理が必要。Waspはジョブランナーを内蔵し、設定ファイルで管理できるため運用コストを削減

## いつ使うのか

定期的なレポート生成、メール送信、データ集計などをバックグラウンドで実行したいとき

## やり方

1. `main.wasp` に `job dailyReport { executor: PgBoss, schedule: { cron: "0 9 * * *" } }` を記述
2. `src/server/jobs.ts` に `export const dailyReport: DailyReportJob = async () => { ... }` を実装
3. `wasp start` で自動的にジョブランナーが起動し、指定時刻に実行
4. キュー型ジョブの場合は `schedule` を省略し、クライアント/サーバーから `await dailyReport.submit({...})` で呼び出し

### 入力

- PgBoss対応のPostgreSQL DB
- ジョブ実行関数の実装

### 出力

- cronスケジュールでの自動実行
- キュー経由の非同期タスク処理

## 使うツール・ライブラリ

- Wasp
- PgBoss

## コード例

```
// main.wasp
job dailyReport {
  executor: PgBoss,
  schedule: { cron: "0 9 * * *" },
  entities: [User]
}

// src/server/jobs.ts
export const dailyReport: DailyReportJob = async () => {
  // 集計処理
}
```

## 前提知識

- Node.js/npm基礎知識
- React・TypeScriptの基本構文
- Prisma ORMの概念（スキーマ定義・マイグレーション）
- REST API / HTTPクライアントの理解
- Stripe/決済APIの基本的な動作原理（サブスク課金を使う場合）
