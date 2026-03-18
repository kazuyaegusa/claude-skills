# 使用量監視でコスト・トークン消費を可視化

> Claude Code のローカルログ（`.jsonl` ファイル）を解析し、トークン消費量・コスト・セッション履歴をダッシュボードで可視化するツール群

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Code は使い放題ではなく、サブスクリプションプランごとにトークン制限がある。使用量を把握しないと、気づかないうちに上限に達してサービスが止まったり、予想外のコストが発生したりする。監視ツールを使うことで、プロジェクトごとの消費傾向を把握し、最適化ポイントを見つけられる

## いつ使うのか

複数プロジェクトで Claude Code を使い分けている場合、チームでコスト管理が必要な場合、トークン上限に達する前に警告が欲しい場合、過去のセッションを振り返りたい場合

## やり方

1. 使用量監視ツールをインストール（例: ccflare, better-ccflare, CC Usage, Claudex）
2. ツールを起動すると、`~/.claude/` 配下のログファイルを自動解析
3. Web UI または TUI でトークン消費量・コスト・burn rate・セッション一覧を表示
4. リアルタイム監視モードでは、現在のセッションの消費状況を逐次更新
5. 必要に応じてエクスポート機能でレポート生成

### 入力

- Claude Code ログファイル（`~/.claude/` 配下）
- サブスクリプションプラン情報

### 出力

- トークン消費量ダッシュボード
- コスト推定レポート
- セッション履歴検索

## 使うツール・ライブラリ

- ccflare / better-ccflare
- CC Usage
- Claudex
- Claude Code Usage Monitor

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
