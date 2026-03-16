# Usage Monitorsでトークン消費を可視化・分析

> Claude Codeのトークン使用量、コスト、バーンレート、セッション履歴を詳細に追跡・可視化

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

予算管理、使用パターン分析、セッション最適化のために定量的データが必要なため

## いつ使うのか

トークン消費の予測、コスト管理、使用パターンの分析、チーム内での使用量比較を行いたいとき

## やり方

1. 監視ツール（例：ccflare、better-ccflare、Claudex）をインストール
2. ローカルのClaude Codeログファイルを解析
3. Webダッシュボード/TUIで使用量・コスト・バーンレート・セッション統計を表示
4. 必要に応じてエクスポート機能でデータ保存

### 入力

- Claude Codeログファイル（~/.claude/logs/）
- サブスクリプションプラン情報

### 出力

- 使用量ダッシュボード
- コスト予測
- セッション履歴
- エクスポートデータ（JSON/CSV等）

## 使うツール・ライブラリ

- ccflare / better-ccflare
- CC Usage
- Claudex
- viberank

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
