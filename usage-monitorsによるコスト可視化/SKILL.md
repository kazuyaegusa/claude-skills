# Usage Monitorsによるコスト可視化

> Claude Codeのトークン消費・API呼び出し・コストをリアルタイムまたは事後に可視化し、予算超過・非効率利用を検出する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

AI coding agentは便利だが、無制限に使うとコストが膨大になる。可視化により、どのタスク・セッションが高コストかを把握し、最適化・予算管理ができる

## いつ使うのか

Claude Codeを本格利用し始めた段階。特にチーム利用・長時間セッション・複数プロジェクト並行時

## やり方

1. 用途に応じたMonitorを選定（例：Web UI重視→「ccflare」「better-ccflare」、CLI重視→「CC Usage」、リアルタイム→「Claude Code Usage Monitor」）
2. Monitorをインストール（多くはローカルログ解析型、一部はクラウド同期型）
3. Claude Codeのログパスを設定（通常は`~/.cache/claude-code/`等）
4. ダッシュボードで消費状況を確認（トークン数・コスト・burn rate・セッション別内訳等）
5. 高コストタスクを特定し、プロンプト改善・スキル導入等で最適化

### 入力

- Claude Codeのログファイル（JSONL形式）
- サブスクリプションプラン情報（無制限/従量課金等）

### 出力

- トークン消費量・コストのダッシュボード
- burn rate（消費速度）
- セッション別・プロジェクト別内訳
- 予算超過アラート

## 使うツール・ライブラリ

- ccflare（Web UI、詳細メトリクス）
- better-ccflare（ccflareのフォーク、Docker対応）
- CC Usage（CLI、コスト分析）
- Claude Code Usage Monitor（TUI、リアルタイム監視）
- Claudex（セッション履歴ブラウザ、全文検索）

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

> 「Trail of Bits Security Skills - A very professional collection of over a dozen security-focused skills for code auditing and vulnerability detection.」
