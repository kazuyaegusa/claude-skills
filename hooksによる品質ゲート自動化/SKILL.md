# Hooksによる品質ゲート自動化

> Claude Codeのライフサイクルイベント（ファイル書き込み前後、Bashコマンド実行前等）にスクリプトを挿入し、TDD違反・セキュリティリスク・危険コマンドを自動検出・ブロックする

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

AIエージェントは指示に従うが、常に最善の判断をするわけではない（テストスキップ、危険コマンド実行、シークレット混入等）。Hooksで機械的にチェックすることで、人間レビュー前の品質を担保できる

## いつ使うのか

品質基準が明確で、機械的チェックで担保できる場合。特にTDD・セキュリティ・危険操作防止が重要なプロジェクト

## やり方

1. 目的に応じたHookを選定（例：TDD強制→「TDD Guard」、危険コマンド防止→「Dippy」、プロンプトインジェクション検出→「parry」）
2. Hookをインストール（多くはスクリプト配置+設定ファイル記述）
3. `.claude/hooks/` に設定を記述（JSON形式でイベント・実行スクリプト・条件を指定）
4. 動作確認（意図的にTDD違反・危険コマンドを試し、ブロックされることを確認）
5. チーム全体に展開（リポジトリに`.claude/hooks/`をcommit）

### 入力

- 品質基準（TDD必須、特定コマンド禁止、シークレットスキャン等）
- Hook実行タイミング（ファイル書き込み前、Bash実行前等）

### 出力

- 自動品質チェック機構
- 違反時のエラーメッセージ・ブロック
- チーム全体での品質基準統一

## 使うツール・ライブラリ

- TDD Guard（TDD違反検出）
- Dippy（危険Bashコマンド自動承認/プロンプト）
- parry（プロンプトインジェクション・シークレットスキャン）
- TypeScript Quality Hooks（TS/ESLint/Prettier自動実行）

## コード例

```
// .claude/hooks/example.json (概念)
{
  "on_file_write": {
    "script": "./hooks/tdd-guard.sh",
    "block_on_failure": true
  },
  "on_bash_command": {
    "script": "./hooks/dippy-approve.sh",
    "block_on_failure": false
  }
}
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
