# IDE Integrationsでエディタ内でClaude Codeを操作

> VS Code、Neovim、Emacs等のエディタ内でClaude Codeとインタラクティブに対話

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

ターミナルとエディタを行き来する手間を削減し、コード編集とAI支援をシームレスに統合するため

## いつ使うのか

エディタ中心のワークフローでClaude Codeを使いたいとき、リアルタイムでコード提案を受けたいとき

## やり方

1. 対象エディタ用の拡張機能/プラグインをインストール（例：claude-code.nvim、claude-code-ide.el、Claudix for VSCode）
2. 設定ファイルでClaude Code CLIパス等を指定
3. エディタ内でコマンド実行（例：`:ClaudeCode`）
4. インライン補完、チャットインターフェース、diff表示等で対話

### 入力

- エディタ種別（VS Code/Neovim/Emacs）
- Claude Code CLI

### 出力

- エディタ統合されたAI支援
- インラインコード提案
- 差分表示

## 使うツール・ライブラリ

- claude-code.nvim
- claude-code-ide.el
- Claudix（VSCode拡張）

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
