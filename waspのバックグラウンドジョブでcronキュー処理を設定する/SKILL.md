# Waspのバックグラウンドジョブでcron/キュー処理を設定する

> Waspの設定ファイルでジョブ関数を宣言し、cron式またはキューとして自動実行する仕組みを構築する

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: automation-pipeline

## なぜ使うのか

Node.jsでcronやワーカーキューを手動構築すると、別プロセス管理・エラーハンドリング・デプロイ設定が複雑化する。Waspは設定でジョブを定義するだけでインフラを抽象化する

## いつ使うのか

定期実行が必要なタスク（日次レポート、サブスク更新チェック等）やバックグラウンド処理（画像変換、メール送信等）を実装する時

## やり方

1. Waspファイルで`job myJob { ... }`を宣言し、実行関数とcron式またはキュー設定を記述
2. バックエンドで対応するTypeScript関数を実装
3. `wasp start`でジョブワーカーも自動起動
4. デプロイ時にWaspが自動的にワーカープロセスを設定

### 入力

- ジョブ関数の実装（TypeScript）
- cron式またはキュー設定

### 出力

- 自動実行されるバックグラウンドジョブ
- キューへのタスク追加API

## 使うツール・ライブラリ

- Wasp
- Node.js

## 前提知識

- Node.js/npmの基本的な使い方
- React/TypeScriptの基礎知識
- Prismaの基本的なスキーマ定義（データモデル構築時）
- Stripe/Lemon Squeezy等の決済サービスの基本概念（決済統合時）

## 根拠

> 「First, to install the latest version of Wasp on macOS, Linux, or Windows with WSL, run the following command: `npm i -g @wasp.sh/wasp-cli`. Then, create a new SaaS app with the following command: `wasp new -t saas`」
