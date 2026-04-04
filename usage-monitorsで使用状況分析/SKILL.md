# Usage Monitorsで使用状況分析

> Claude Codeのローカルログを解析し、トークン消費・コスト・セッション履歴をダッシュボード形式で可視化する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

過去の使用パターンを分析し、無駄なトークン消費を特定して最適化できる。予算管理や利用状況レポートにも活用できる。

## いつ使うのか

月次コストを把握したい時、トークン効率を改善したい時、チーム全体の使用状況を可視化したい時

## やり方

1. ccflare、CC Usage、Claudex等のツールをインストール
2. ローカルのClaude Codeログを読み込み
3. WebUIまたはCLIでダッシュボードを表示
4. トークン消費・コスト・セッション統計を確認

### 入力

- Claude Codeローカルログ

### 出力

- 使用状況ダッシュボード
- トークン/コスト分析レポート

## 使うツール・ライブラリ

- ccflare
- better-ccflare
- CC Usage
- Claudex

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
