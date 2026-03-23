# CLAUDE.md によるプロジェクト固有ルールの注入

> プロジェクトルートに `CLAUDE.md` ファイルを配置し、コーディング規約・アーキテクチャ・禁止事項などを Claude に自動読み込ませる

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude がプロジェクトのコンテキスト（使用言語、フレームワーク、設計方針など）を理解せずにコードを生成すると、既存コードベースと整合性が取れなくなるため

## いつ使うのか

新規プロジェクト立ち上げ時、チーム開発で規約を統一したい時、特定のフレームワーク（Next.js、Laravel など）に特化した指示が必要な時

## やり方

1. プロジェクトルートに `CLAUDE.md` を作成
2. プロジェクトの技術スタック、ディレクトリ構造、コーディング規約を記述
3. 禁止事項（特定ライブラリの使用禁止など）を明記
4. ビルド・テストコマンドを列挙
5. Claude Code セッション開始時に自動読み込まれる

### 入力

- CLAUDE.md ファイル（Markdown 形式）
- プロジェクトの技術スタック情報
- コーディング規約

### 出力

- Claude のコンテキストに注入されたプロジェクト知識
- 規約に準拠したコード生成

## 使うツール・ライブラリ

- Metabase CLAUDE.md（Clojure TDD）
- Giselle CLAUDE.md（TypeScript + pnpm）
- HASH CLAUDE.md（Rust ドキュメント規約）

## コード例

```
# Project: MyApp

## Tech Stack
- TypeScript 5.x
- Next.js 14 (App Router)
- pnpm

## Rules
- NEVER use `any` type
- Always write tests before implementation (TDD)

## Commands
- Build: `pnpm build`
- Test: `pnpm test`
```

## 前提知識

- Claude Code の基本的な使い方（インストール、セッション開始、プロンプト入力）
- Git の基礎知識（コミット、ブランチ、PR 作成）
- Markdown の基本文法
- シェルスクリプト（Bash）の基礎知識（フック・スラッシュコマンドのカスタマイズに必要）
- JSON の基本構造（フック設定ファイルの編集に必要）

## 根拠

> "A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow."

> "Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities."

> "Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle."

> "Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task"

> "CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards"
