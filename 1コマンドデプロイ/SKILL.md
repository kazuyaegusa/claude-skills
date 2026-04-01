# 1コマンドデプロイ

> Wasp CLIで `wasp deploy` 実行するだけでDB・サーバー・クライアントを一括デプロイ

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: infrastructure

## なぜ使うのか

手動デプロイではDB移行、環境変数設定、ビルド・デプロイ順序管理が必要だが、WaspはRailway/Fly.ioへの最適化されたデプロイフローを自動実行するため

## いつ使うのか

ローカル開発完了後、ステージング・本番環境へデプロイする時

## やり方

1. `wasp deploy fly` または `wasp deploy railway` を実行
2. CLIがインタラクティブに環境変数・リージョン・DB設定を質問
3. 自動でDockerビルド、DBマイグレーション、サービスデプロイを実行

### 入力

- Waspプロジェクト
- Fly.io/Railwayアカウント

### 出力

- 稼働中のWebアプリ（DB含む）

## 使うツール・ライブラリ

- Wasp CLI
- Fly.io / Railway

## コード例

```
wasp deploy fly
```

## 前提知識

- Node.js基礎知識（npm/yarn操作）
- React基礎（コンポーネント、Hooks）
- TypeScript基礎（型アノテーション）
- Prisma ORM基本概念（スキーマ定義、マイグレーション）
- SaaS基本概念（認証、決済フロー、サブスクリプション）

## 根拠

> 「One-command Deploy - Easily deploy your DB, Server, & Client with one commaned to Railway or Fly.io via the CLI」

> コマンド例: `npm i -g @wasp.sh/wasp-cli` → `wasp new -t saas`
