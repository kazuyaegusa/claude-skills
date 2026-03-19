# Waspテンプレートから新規SaaSプロジェクトを生成

> Wasp CLIを使ってOpen SaaSテンプレートをクローンし、認証・決済・UI・デプロイ設定が全て揃ったプロジェクトを即座に作成する

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: infrastructure

## なぜ使うのか

SaaS開発で毎回必要になる定型機能（ユーザー登録、ログイン、課金、管理画面等）を手作業で組み込むと数週間〜数ヶ月かかるため、実証済みテンプレートで初期セットアップを数分に短縮する

## いつ使うのか

新規SaaSプロジェクトを開始する最初のステップとして、または既存システムをモダンスタックに移行する際のスケルトンとして使う

## やり方

1. `npm i -g @wasp.sh/wasp-cli` でWasp CLIをグローバルインストール
2. `wasp new -t saas` でOpen SaaSテンプレートからプロジェクト生成
3. 生成されたディレクトリに移動し、.envファイルにStripe/SendGrid/AWS等のAPIキーを設定
4. `wasp db migrate-dev` でPrismaマイグレーション実行
5. `wasp start` で開発サーバー起動

### 入力

- Node.js環境（macOS/Linux/WSL）
- Stripe/SendGrid/AWS等のアカウント（オプション、後から設定可）

### 出力

- React + Node.js + Prisma構成のフルスタックプロジェクト
- 認証フロー（email検証・Google・GitHub・Slack・MS）
- 決済統合（Stripe or Lemon Squeezy）
- ShadCN UIベースの管理画面
- S3ファイルアップロード機能
- バックグラウンドジョブ設定

## 使うツール・ライブラリ

- Wasp CLI
- React
- Node.js
- Prisma
- ShadCN UI
- Stripe/Lemon Squeezy
- Playwright

## コード例

```
# Install Wasp CLI
npm i -g @wasp.sh/wasp-cli

# Create new SaaS project
wasp new -t saas

# Start development
cd <project-name>
wasp start
```

## 前提知識

- Node.js/npmの基礎知識
- React + TypeScriptの基本（コンポーネント・フック）
- REST API/データベース操作の概念（Prismaの経験があると理想的）
- Stripe/決済API統合の基本知識（決済機能を使う場合）
- Dockerまたはクラウドデプロイの基礎（本番運用時）

## 根拠

> 「npm i -g @wasp.sh/wasp-cli」「wasp new -t saas」でテンプレート生成可能
