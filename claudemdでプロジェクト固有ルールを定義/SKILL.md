# CLAUDE.mdでプロジェクト固有ルールを定義

> リポジトリのルート、またはグローバル設定に配置するMarkdownファイルで、Claude Codeにプロジェクト固有のコーディング規約・ワークフロー・コンテキストを指示

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

汎用的なClaude Codeにプロジェクト特有の知識（言語スタック、アーキテクチャ、命名規則、テスト方針等）を注入し、出力品質とプロジェクト適合性を向上させるため

## いつ使うのか

特定の言語（Kotlin Multiplatform、Clojure等）やフレームワーク（Next.js、Laravel TALL等）、開発手法（TDD、REPL駆動等）を使うプロジェクトで、Claude Codeに文脈を理解させたいとき

## やり方

1. プロジェクトルートに`CLAUDE.md`ファイルを作成
2. プロジェクト構成、技術スタック、コーディング規約、ワークフロー、禁止事項等を記述
3. Claude Code起動時に自動読み込み
4. 必要に応じて`.claude/rules/`で条件付きルールを追加

### 入力

- プロジェクト構成
- 技術スタック情報
- コーディング規約
- ワークフロー定義

### 出力

- プロジェクト適合性の高いコード
- 規約に準拠した実装

## 使うツール・ライブラリ

- Metabase CLAUDE.md（Clojure REPL駆動）
- Giselle CLAUDE.md（pnpm + Vitest）
- Laravel TALL Stack CLAUDE.md

## 前提知識

- Claude Codeの基本的な使い方（CLIでの起動、プロンプト入力、ファイル操作）
- Git、GitHub、PR、Issueなどの基本概念
- JSONファイルの編集（hooks.json等の設定）
- ターミナル操作、シェルスクリプトの基礎
- （リソースによって）Docker、Node.js、Python、Rust等の環境構築知識

## 根拠

> > A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow.

> Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

> Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.

> Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task

> CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards
