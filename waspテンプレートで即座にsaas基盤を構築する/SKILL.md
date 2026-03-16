# Waspテンプレートで即座にSaaS基盤を構築する

> Wasp CLIの`wasp new -t saas`コマンドで、認証・決済・メール・ジョブ・UI・AI統合が事前設定されたプロジェクトを生成する

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: claude-code-workflow

## なぜ使うのか

SaaSに必須の機能を個別にインストール・設定する手間を省き、初日からビジネスロジックの実装に集中するため

## いつ使うのか

新規SaaSプロジェクトの初期セットアップ時、または既存プロジェクトでWaspへの移行を検討する時

## やり方

1. Wasp CLIをインストール: `npm i -g @wasp.sh/wasp-cli`
2. テンプレートから新規プロジェクト作成: `wasp new -t saas`
3. 生成されたディレクトリに移動し、環境変数（Stripe/SendGrid等）を設定
4. `wasp start`で開発サーバーを起動
5. 必要に応じてAGENTS.mdを参照しながらAIツールで機能追加

### 入力

- Node.js環境
- Stripe/Lemon Squeezy等の決済サービスAPIキー（オプション）
- SendGrid/MailGun等のメールサービス認証情報（オプション）

### 出力

- フル機能SaaSプロジェクトのディレクトリ
- 設定済みの認証フロー（Email/Google/GitHub等）
- 決済統合の基本実装
- ShadCN UIベースのコンポーネント
- AI開発ツール用のAGENTS.md/スキル

## 使うツール・ライブラリ

- Wasp CLI
- React
- Node.js
- Prisma
- ShadCN UI
- Stripe/Lemon Squeezy
- SendGrid/MailGun/SMTP
- Playwright

## コード例

```
npm i -g @wasp.sh/wasp-cli
wasp new -t saas
cd <project-name>
wasp start
```

## 前提知識

- Node.js/npmの基本的な使い方
- React/TypeScriptの基礎知識
- Prismaの基本的なスキーマ定義（データモデル構築時）
- Stripe/Lemon Squeezy等の決済サービスの基本概念（決済統合時）

## 根拠

> 「First, to install the latest version of Wasp on macOS, Linux, or Windows with WSL, run the following command: `npm i -g @wasp.sh/wasp-cli`. Then, create a new SaaS app with the following command: `wasp new -t saas`」
