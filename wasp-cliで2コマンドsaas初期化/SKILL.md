# Wasp CLIで2コマンドSaaS初期化

> Waspフレームワークの公式CLIを使い、フル機能SaaSテンプレートを即座にクローンして起動する

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動でReact・Node・Prisma・認証・決済を組み合わせると数週間かかる初期セットアップを、2コマンド・数分で完了させるため

## いつ使うのか

新規SaaSプロジェクトの開始時、または既存プロジェクトの参考実装として構造を学びたい時

## やり方

1. `npm i -g @wasp.sh/wasp-cli` でWasp CLIをグローバルインストール
2. `wasp new -t saas` でOpen SaaSテンプレートをクローン
3. 生成されたディレクトリに移動し `wasp start` で開発サーバー起動（デフォルトでDB・サーバー・クライアント全て立ち上がる）

### 入力

- Node.js 18+ がインストール済みの環境
- macOS/Linux/WSL環境（Windowsネイティブは非推奨）

### 出力

- 認証（Email/Google/GitHub/Slack/MS）、Stripe決済、メール送信、S3アップロード、管理画面、ランディングページを含む動作するSaaSアプリ
- main.wasp 設定ファイル（宣言的にルート・認証・ジョブ・デプロイを定義）
- AGENTS.md と Claude Code スキル（AI開発ツール用のコンテキスト）

## 使うツール・ライブラリ

- Wasp CLI (@wasp.sh/wasp-cli)
- Open SaaS テンプレート

## コード例

```
npm i -g @wasp.sh/wasp-cli
wasp new -t saas
cd <project-name>
wasp start
```

## 前提知識

- Node.js 18+ の基礎知識
- React と TypeScript の基本文法
- SaaSアプリの構成要素（認証・決済・メール送信）への理解
- Prisma ORM の基本（Schema定義、マイグレーション）
- CLIツールの基本操作（npm、git）

## 根拠

> 「wasp new -t saas - This will create a clean copy of the Open SaaS template into a new directory」
