# AIコーディング支援環境を標準装備

> Open SaaSテンプレートに同梱されたAGENTS.md、Cursorルール、llms-full.txtを使い、Claude Code/Cursor/Codex等のAIツールが即座にプロジェクト構造・コーディング規約を理解できる環境を提供する

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: claude-code-workflow

## なぜ使うのか

AIツールは初期状態ではプロジェクト固有のルール（認証フロー、DB schema、API構造等）を理解できず、生成コードが不正確になる。事前定義されたAGENTS.md等により、AIが正確なコード補完・生成を行える

## いつ使うのか

新機能開発時にAIに「認証済みユーザーのみアクセスできるAPIを作って」と依頼する時、既存コードのリファクタリングをAIに任せる時

## やり方

1. Open SaaSテンプレートを`wasp new -t saas`で生成すると、プロジェクトルートにAGENTS.md・.cursorrules・llms-full.txtが自動配置される
2. Claude Code使用時: AGENTS.mdが自動読み込まれ、Waspのエンティティ・操作・ルーティング規約が認識される
3. Cursor使用時: .cursorrulesが適用され、コード補完時にWasp固有の構文（例: `@src/`インポートパス）が提案される
4. その他AI: llms-full.txtをコンテキストに含めることで、プロジェクト全体構造をLLMに学習させる

### 入力

- Open SaaSテンプレート（AGENTS.md等が同梱）
- Claude Code/Cursor等のAIコーディングツール

### 出力

- AIがWaspの型定義・認証フロー・DB操作を正確に理解したコード生成
- プロジェクト規約に沿った一貫性のあるコード補完

## 使うツール・ライブラリ

- AGENTS.md（プロジェクトコンテキスト定義）
- .cursorrules（Cursor IDE設定）
- llms-full.txt（LLM向けコンテキスト全文）
- Claude Code/Cursor/Codex

## コード例

```
# プロジェクト生成時に自動配置されるファイル
wasp new -t saas my-saas
# -> my-saas/AGENTS.md
# -> my-saas/.cursorrules
# -> my-saas/llms-full.txt

# Claude Codeでの使用例（自動）
# AGENTS.mdが読み込まれ、以下のようなプロンプトが有効化:
# "Create a new protected API route for /api/reports that requires authentication"
# -> Waspの`query`定義 + `@src/`インポートで正確なコード生成
```

## 前提知識

- Node.js/npmの基礎知識
- React + TypeScriptの基本（コンポーネント・フック）
- REST API/データベース操作の概念（Prismaの経験があると理想的）
- Stripe/決済API統合の基本知識（決済機能を使う場合）
- Dockerまたはクラウドデプロイの基礎（本番運用時）

## 根拠

> 「A 100% free modern JS SaaS boilerplate (React, NodeJS, Prisma). Full-featured: Auth (email, google, github, slack, MS), Email sending, Background jobs, Landing page, Payments (Stripe, Polar.sh), Shadcn UI, S3 file upload. AI-ready with tailored AGENTS.md, skills, and Claude Code plugin.」

> 「npm i -g @wasp.sh/wasp-cli」「wasp new -t saas」でテンプレート生成可能
