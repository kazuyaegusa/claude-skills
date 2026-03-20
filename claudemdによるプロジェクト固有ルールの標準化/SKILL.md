# CLAUDE.mdによるプロジェクト固有ルールの標準化

> プロジェクトルート（または`.claude/`）に`CLAUDE.md`を配置し、コーディング規約・ビルドコマンド・アーキテクチャ・禁止事項等をClaude Codeに事前学習させる

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

プロジェクトごとに技術スタック・規約・ワークフローは異なる。CLAUDE.mdで明示することで、毎回説明する手間を省き、一貫性を保てる

## いつ使うのか

新規プロジェクト立ち上げ時、またはClaude Code導入時。特に複数人がClaude Codeを使う場合、一貫性担保のため必須

## やり方

1. プロジェクトの特性を整理（言語・フレームワーク・ビルドツール・テスト戦略・コーディング規約）
2. 参考となるCLAUDE.mdを探す（例：TypeScript→「Giselle」、Kotlin Multiplatform→「DroidconKotlin」、Python→「EDSL」）
3. テンプレートをカスタマイズ（不要なセクション削除、プロジェクト固有情報追加）
4. リポジトリルートに`CLAUDE.md`を配置
5. Claude Codeが自動的に読み込み、指示に従うことを確認

### 入力

- プロジェクトの技術スタック・規約・ワークフロー
- 参考CLAUDE.mdテンプレート

### 出力

- プロジェクト固有の`CLAUDE.md`
- Claude Codeの一貫した動作
- チーム全体での規約統一

## 使うツール・ライブラリ

- CLAUDE.md examples（Giselle, Metabase, HASH, Inkline等）
- GitHub（各プロジェクトのCLAUDE.mdを参照）

## コード例

```
# CLAUDE.md example (TypeScript/React)
## Tech Stack
- TypeScript 5.x, React 18, Vite
- pnpm for package management
- Vitest for testing

## Coding Standards
- Use Composition API, not Options API
- All new code must have tests
- Run `pnpm format` before commit

## Build Commands
- `pnpm dev` - start dev server
- `pnpm test` - run tests
- `pnpm build` - production build
```

## 前提知識

- Claude Codeの基本的な使い方（CLI起動、プロンプト入力、ファイル操作承認等）
- gitの基礎知識（branch, commit, PR等）
- 開発ワークフローの基礎（TDD, CI/CD, コードレビュー等の概念）
- JSON/Markdown形式の読み書き（Hooks設定、CLAUDE.md記述に必要）

## 根拠

> 「A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow.」

> 「Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.」

> 「Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.」

> 「ccflare - Claude Code usage dashboard with a web-UI that would put Tableau to shame. Thoroughly comprehensive metrics, frictionless setup, detailed logging, really really nice UI.」

> 「Claude Squad - manages multiple Claude Code, Codex (and other local agents including Aider) in separate workspaces, allowing you to work on multiple tasks simultaneously.」
