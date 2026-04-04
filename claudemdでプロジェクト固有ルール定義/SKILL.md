# CLAUDE.mdでプロジェクト固有ルール定義

> プロジェクトルートに CLAUDE.md を配置し、コーディング規約・アーキテクチャ・ビルドコマンド・用語集等を定義する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeがプロジェクト固有の文脈・制約を理解し、一貫性のあるコード生成・提案ができるようになる。

## いつ使うのか

チーム開発で規約を統一したい時、特定フレームワークのベストプラクティスを強制したい時、プロジェクト用語を定義したい時

## やり方

1. プロジェクトルートに CLAUDE.md を作成
2. 言語・フレームワーク固有の規約、アーキテクチャ概要、重要なコマンド、用語定義等を記述
3. Claude Codeは自動的にこのファイルを読み込み、指示に従う

### 入力

- プロジェクト固有の規約・用語・制約

### 出力

- CLAUDE.mdファイル

## 使うツール・ライブラリ

- 既存CLAUDE.mdテンプレート（Metabase、HASH、Giselle等）

## 前提知識

- Claude Codeの基本的な使い方（CLI操作、セッション管理）
- Gitの基礎知識（ブランチ、コミット、PR等）
- シェルスクリプトまたはPython/TypeScriptの基礎（Hook・Skill作成に必要）
- プロジェクトのビルド・テストコマンドの理解

## 根拠

> Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

> Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.

> Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task

> CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards

> Alternative Clients are alternative UIs and front-ends for interacting with Claude Code, either on mobile or on the desktop.
