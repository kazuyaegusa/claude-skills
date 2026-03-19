# ToolingでClaude Codeの可観測性・管理性を向上させる

> Toolingカテゴリのリソース（例: ccflare使用量ダッシュボード、claude-tmux、Claudex会話履歴ブラウザ）をインストールし、Claude Codeのトークン消費・セッション管理・会話履歴を可視化・操作する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeはターミナルベースで、使用量やセッション履歴の可視化が弱い。専用ツールを使うことで、コスト管理、セッション切り替え、過去の会話検索が容易になる

## いつ使うのか

Claude Codeのトークン消費を監視したい、複数セッションを管理したい、過去の会話を検索・復元したい時

## やり方

1. awesome-claude-codeの「Tooling 🧰」セクションから目的のツールを選択（例: ccflare）
2. ツールのリポジトリをクローン: `git clone https://github.com/snipeship/ccflare`
3. READMEに従いインストール（多くはDockerまたはローカルサーバー起動）
4. ツールのWeb UIまたはCLIを開く
5. Claude Codeのログファイルを解析し、ダッシュボード表示・検索・セッション復元等を実行

### 入力

- Claude Codeのログファイル（通常 `~/.cache/claude-code/` 配下）

### 出力

- 使用量ダッシュボード（トークン、コスト、バーンレート）
- セッション一覧・切り替えUI
- 会話履歴の全文検索結果

## 使うツール・ライブラリ

- ccflare
- better-ccflare
- Claudex
- claude-tmux
- recall

## 前提知識

- Claude Codeの基本的な使い方（インストール、起動、プロンプト入力）
- Claude Codeの設定ファイル構造（.claude/ディレクトリ、hooks.json、commands/、skills/）
- GitHubの基本操作（リポジトリのクローン、READMEの読解）
- JSON、Markdown、Bashの基礎知識

## 根拠

> # Awesome Claude Code - A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow.

> ## Agent Skills 🤖 - Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

> ## Hooks 🪝 - Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.

> ## Slash-Commands 🔪 - Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task.

> ## Tooling 🧰 - Tooling denotes applications that are built on top of Claude Code and consist of more components than slash-commands and CLAUDE.md files.
