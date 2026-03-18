# Workflows で複数ステージのプロセスを構造化する

> 開発プロセス全体（Research → Plan → Execute → Review など）を明示的なステージに分割し、各ステージで Claude Code の振る舞いを制御する枠組み。Subagents、Commands、CLAUDE.md、Skills を組み合わせて構築する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

AI エージェントに「とにかく全部やって」と指示すると、計画なしに実装を始めたり、テストを飛ばしたり、レビューをスキップしたりする。ワークフローで段階を区切ることで、人間のチェックポイントを挟みながら品質を保ちつつ自動化できる

## いつ使うのか

大規模な機能開発、複数人での協業、品質基準が厳格なプロジェクト、TDD やセキュリティ監査を組み込みたい場合

## やり方

1. プロジェクトに適したワークフローフレームワークを選択（例: RIPER Workflow, AB Method, ContextKit）
2. `.claude/` ディレクトリに Subagents、Commands、CLAUDE.md を配置
3. ワークフローのルールに従って Claude に指示（例: 「まず Research フェーズで仕様を分析して」）
4. 各ステージの完了時に人間が承認・フィードバック
5. 必要に応じて TodoWrite でタスク進捗を可視化

### 入力

- ワークフロー定義（Subagents, Commands, CLAUDE.md）
- プロジェクト仕様・要件
- 品質基準・テスト戦略

### 出力

- 段階的に完成するコード
- 各ステージのドキュメント
- テスト・レビューの記録

## 使うツール・ライブラリ

- RIPER Workflow
- AB Method
- ContextKit
- Claude CodePro
- Superpowers Skills

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
