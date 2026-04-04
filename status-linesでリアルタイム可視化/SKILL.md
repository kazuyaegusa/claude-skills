# Status Linesでリアルタイム可視化

> Claude Codeのステータスバーをカスタマイズし、トークン使用量・コスト・Gitブランチ・進捗状況等を表示する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

トークン消費やコストをリアルタイムで把握し、予算超過を防ぎながら効率的に作業できる。

## いつ使うのか

トークン使用量を管理したい時、複数プロジェクト間で作業している時、コスト意識を持ちながら開発したい時

## やり方

1. claude-powerline、CCometixLine等のツールをインストール
2. 設定ファイルで表示項目・テーマをカスタマイズ
3. Claude Code起動時に自動的にステータスラインが表示される

### 入力

- 表示したいメトリクス（トークン、コスト、Git情報等）

### 出力

- カスタマイズされたステータスライン

## 使うツール・ライブラリ

- claude-powerline
- CCometixLine
- ccstatusline

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
