# Hooksによるライフサイクル制御

> Claude Codeの特定タイミング（ファイル書き込み前、Bash実行前等）で自動的にスクリプトを実行し、検証・変換・通知を行う

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

危険なコマンドをブロックしたり、コード品質チェックを自動化したり、作業完了を通知したりすることで、安全性と生産性を向上できる。

## いつ使うのか

TDD違反をブロックしたい時、危険なコマンドを防ぎたい時、タスク完了を通知したい時、コードフォーマットを自動適用したい時

## やり方

1. .claude/hooks/{hook-name}.json を作成
2. トリガータイミング（pre-write、post-bash等）とスクリプトパスを指定
3. スクリプトで検証・変換・通知ロジックを実装
4. hookが失敗するとClaude Codeの操作がブロックされる

### 入力

- トリガーイベント
- 検証・変換ロジック

### 出力

- hook設定ファイル
- 自動実行されるスクリプト

## 使うツール・ライブラリ

- TDD Guard
- Dippy
- TypeScript Quality Hooks
- Claudio

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
