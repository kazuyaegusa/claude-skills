# Agentic WorkflowsによるGitHub Actions統合

> Markdown形式で記述されたAI駆動のGitHub Actionsワークフローを導入し、PR自動レビュー、ドキュメント生成、リリースノート作成などを自動化する

- 出典: https://github.com/github/awesome-copilot
- 投稿者: github
- カテゴリ: agent-orchestration

## なぜ使うのか

自然言語でワークフローを定義でき、AI判断を組み込んだ複雑な自動化を簡潔に実装できる

## いつ使うのか

CI/CDパイプラインにAI判断を組み込みたい時、自動レビュー・ドキュメント生成を導入したい時

## やり方

1. https://awesome-copilot.github.com/workflows でWorkflowを検索
2. Markdown形式のワークフロー定義を `.github/workflows/` に配置
3. GitHub ActionsがトリガーされるとAIがMarkdown指示を解釈して実行
4. 必要に応じてワークフロー定義をカスタマイズ

### 入力

- Markdown形式のワークフロー定義
- GitHub Actionsトリガー設定

### 出力

- AI駆動の自動化ワークフロー
- 自動生成されたレビューコメント、ドキュメント、リリースノート

## 使うツール・ライブラリ

- GitHub Actions
- GitHub Copilot
- Awesome Copilot Workflows collection

## 前提知識

- GitHub Copilot（個人またはOrganizationサブスクリプション）
- VS CodeまたはCopilot CLI
- 基本的なGit操作知識
- 対象技術スタック（導入するagents/skills/instructionsが対象とする言語・フレームワーク）の基礎知識

## 根拠

> 「A community-created collection of custom agents, instructions, skills, hooks, workflows, and plugins to supercharge your GitHub Copilot experience.」

> 「Agentic Workflows: AI-powered GitHub Actions automations written in markdown」
