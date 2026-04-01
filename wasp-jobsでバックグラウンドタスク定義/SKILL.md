# Wasp Jobsでバックグラウンドタスク定義

> main.waspで関数を宣言するだけでcronジョブやキューワーカーを実装

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: automation-pipeline

## なぜ使うのか

Bull/Bee-Queue等のライブラリでは手動でRedis接続・ワーカープロセス・リトライロジックを書く必要があるが、Waspは設定だけで全て処理するため

## いつ使うのか

定期的なメール送信、データ集計、APIポーリング等のバックグラウンド処理が必要な時

## やり方

1. main.waspで `job myJob { ... }` ブロック定義
2. `executor`（PgBoss等）、`schedule`（cron式）を指定
3. サーバーコードで実行関数を実装
4. `wasp start` で自動的にジョブワーカーが起動

### 入力

- main.wasp設定
- 実行する関数実装

### 出力

- スケジュール実行されるジョブ
- 非同期キュー処理

## 使うツール・ライブラリ

- Wasp Jobs
- PgBoss（デフォルトexecutor）

## 前提知識

- Node.js基礎知識（npm/yarn操作）
- React基礎（コンポーネント、Hooks）
- TypeScript基礎（型アノテーション）
- Prisma ORM基本概念（スキーマ定義、マイグレーション）
- SaaS基本概念（認証、決済フロー、サブスクリプション）

## 根拠

> コマンド例: `npm i -g @wasp.sh/wasp-cli` → `wasp new -t saas`
