# Waspテンプレートからプロジェクト初期化

> Wasp CLIの公式SaaSテンプレートを使い、認証・決済・ジョブ・UI・デプロイ設定を含むプロジェクトを生成する

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: automation-pipeline

## なぜ使うのか

SaaS開発で必要な機能（メール認証、OAuth、Stripe決済、cronジョブ、S3アップロード等）を個別に統合すると数週間かかる。テンプレートで一括導入し、差別化機能に注力するため

## いつ使うのか

SaaSのMVPを構築する初期フェーズで、認証・決済・メール送信などの定型機能を迅速に実装したいとき

## やり方

1. `npm i -g @wasp.sh/wasp-cli` でWasp CLIをインストール
2. `wasp new -t saas` を実行してテンプレートをクローン
3. 生成されたディレクトリ内で `wasp start` を実行して開発サーバー起動
4. `.env` ファイルにStripe API key、SendGrid key等を設定
5. `src/` 配下のコードをカスタマイズ

### 入力

- Node.js環境（macOS/Linux/WSL）
- Stripe/Lemon Squeezyアカウント（決済が必要な場合）
- SendGrid/MailGun/SMTPの認証情報（メール送信が必要な場合）

### 出力

- 認証・決済・ジョブを含むフルスタックSaaSプロジェクト
- ローカル開発サーバー（React + NodeJS + Prisma）
- Astroベースのドキュメント・ブログサイト

## 使うツール・ライブラリ

- Wasp CLI
- React
- NodeJS
- Prisma
- Astro（Starlight）

## コード例

```
npm i -g @wasp.sh/wasp-cli
wasp new -t saas
cd <project-name>
wasp start
```

## 前提知識

- Node.js/npm基礎知識
- React・TypeScriptの基本構文
- Prisma ORMの概念（スキーマ定義・マイグレーション）
- REST API / HTTPクライアントの理解
- Stripe/決済APIの基本的な動作原理（サブスク課金を使う場合）

## 根拠

> 「Wasp new -t saas」でクリーンなSaaSテンプレートが生成される

> 「npm i -g @wasp.sh/wasp-cli」「wasp new -t saas」の実行手順が明記
