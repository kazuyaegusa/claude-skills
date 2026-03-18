# AI開発ツール向けAGENTS.mdとスキルを同梱

> Claude Code/Cursor等のAIエージェントが参照する AGENTS.md（コードベース全体の構造・ルール）と、各機能のスキル定義を、テンプレート標準で提供する

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: claude-code-workflow

## なぜ使うのか

AIエージェントにボイラープレートの設計意図・制約を事前学習させることで、開発者がプロンプトを書くだけで適切なカスタマイズコードを生成できるようにするため

## いつ使うのか

AIエージェントでボイラープレートをカスタマイズする際、フレームワークの作法を守りながらコード生成させたい時

## やり方

1. Open SaaS テンプレートに含まれる AGENTS.md をプロジェクトルートに配置（既に含まれている）
2. Claude Code や Cursor の設定で AGENTS.md を読み込むよう指定
3. スキル（例: 認証フロー追加、Stripe商品登録）をプロンプトで指示すると、AIがAGENTS.mdの制約に従ってコードを生成
4. 必要に応じて AGENTS.md にプロジェクト固有のルール（API命名規則、状態管理方針等）を追記

### 入力

- Open SaaS テンプレートに含まれる AGENTS.md
- AI開発ツール（Claude Code/Cursor/Codex等）の設定

### 出力

- AIエージェントがWaspの宣言的設定、Prismaスキーマ、React構造を理解した状態でのコード生成
- フレームワークの制約（例: main.waspでルート定義必須）を守った提案

## 使うツール・ライブラリ

- AGENTS.md（プロジェクト構造定義）
- Claude Code / Cursor / Codex（AI開発ツール）

## コード例

```
# AGENTS.md 抜粋
## 認証フロー追加時の制約
- main.waspの`auth`ブロックでプロバイダーを宣言
- src/server/auth.ts に認証後フックを実装
- Prisma schemaにUserモデルを追加し`wasp db migrate-dev`実行
```

## 前提知識

- Node.js 18+ の基礎知識
- React と TypeScript の基本文法
- SaaSアプリの構成要素（認証・決済・メール送信）への理解
- Prisma ORM の基本（Schema定義、マイグレーション）
- CLIツールの基本操作（npm、git）

## 根拠

> 「wasp new -t saas - This will create a clean copy of the Open SaaS template into a new directory」

> 「Full-stack Authentication - Email verified + social Auth in a few lines of code」

> 「AI-ready with tailored AGENTS.md, skills, and Claude Code plugin」

> 「100% free modern JS SaaS boilerplate (React, NodeJS, Prisma). Full-featured: Auth (email, google, github, slack, MS), Email sending, Background jobs, Landing page, Payments (Stripe, Polar.sh), Shadcn UI, S3 file upload」
