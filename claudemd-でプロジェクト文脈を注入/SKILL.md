# CLAUDE.md でプロジェクト文脈を注入

> プロジェクトルートまたは `~/.claude/` に配置する Markdown ファイルで、プロジェクト固有のルール・コーディング規約・アーキテクチャ情報を Claude Code に伝える仕組み

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Code はプロジェクトの背景知識を持たないため、毎回説明しないと文脈に合わないコードを生成する。CLAUDE.md を用意することで、プロジェクトのルール（使用フレームワーク、命名規則、禁止事項など）を自動的に読み込ませ、一貫性のあるコード生成を実現できる

## いつ使うのか

新しいプロジェクトを Claude Code で開発する場合、既存プロジェクトに Claude Code を導入する場合、チーム全体で統一したルールを守らせたい場合

## やり方

1. プロジェクトルートに `CLAUDE.md` を作成
2. ファイル内に以下を記述:
   - プロジェクト概要・目的
   - 使用技術スタック・ツール
   - コーディング規約・命名規則
   - ビルド・テスト・デプロイコマンド
   - 禁止事項（例: 「絶対に本番データを触らない」）
3. Claude Code セッション開始時に自動ロードされる
4. 必要に応じてグローバル設定（`~/.claude/CLAUDE.md`）も併用

### 入力

- プロジェクト仕様
- コーディング規約
- 技術スタック情報

### 出力

- プロジェクト文脈を理解した Claude Code の応答
- 一貫性のあるコード生成

## 使うツール・ライブラリ

- CLAUDE.md 仕様（Claude Code 公式）

## コード例

```
# CLAUDE.md example

## Project Overview
This is a TypeScript monorepo using pnpm workspaces.

## Rules
- Always use `pnpm` instead of `npm`
- Follow ESLint + Prettier config
- Never skip tests

## Commands
- Build: `pnpm build`
- Test: `pnpm test`
- Lint: `pnpm lint`
```

## 前提知識

- Claude Code の基本的な使い方（インストール、セッション開始、ファイル操作）
- Git の基礎知識（ブランチ、コミット、PR）
- コマンドライン操作の基本（Bash, tmux など）
- 開発プロセスの基礎知識（TDD, CI/CD, コードレビュー）

## 根拠

> A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow.

> Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

> Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.

> Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task.

> CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards.
