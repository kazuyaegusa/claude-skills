# AI開発ツール向けのAGENTS.md/スキルを活用する

> プロジェクトに同梱されたAGENTS.md、Cursorルール、llms-full.txtをAIコーディングツール（Claude Code/Cursor等）に読み込ませ、コンテキストを与える

- 出典: https://github.com/wasp-lang/open-saas
- 投稿者: wasp-lang
- カテゴリ: claude-code-workflow

## なぜ使うのか

AIツールはプロジェクト固有の構成・命名規則・ベストプラクティスを知らないため、適切なコンテキストを与えないと不適切なコードを生成する。Open SaaSはWasp特有の設定パターンをドキュメント化済み

## いつ使うのか

AIコーディングツールを使ってOpen SaaSプロジェクトを拡張する全ての場面

## やり方

1. プロジェクトルートのAGENTS.mdをAIツールに参照させる
2. Cursorの場合は.cursorrules、Claude Codeの場合はCLAUDE.mdに内容を統合
3. AIにコード生成を依頼する際、「AGENTS.mdのガイドラインに従って」と指示
4. 生成されたコードがWaspの規約に沿っているか確認

### 入力

- AGENTS.md/Cursorルール/llms-full.txt
- AIコーディングツール（Claude Code/Cursor等）

### 出力

- Wasp規約に沿ったAI生成コード

## 使うツール・ライブラリ

- Claude Code
- Cursor
- その他LLMベースのコーディングツール

## 前提知識

- Node.js/npmの基本的な使い方
- React/TypeScriptの基礎知識
- Prismaの基本的なスキーマ定義（データモデル構築時）
- Stripe/Lemon Squeezy等の決済サービスの基本概念（決済統合時）
