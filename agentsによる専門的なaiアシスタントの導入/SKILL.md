# Agentsによる専門的なAIアシスタントの導入

> MCP server（Model Context Protocol）と連携し、外部API、データベース、開発ツールにアクセスできる専門的なagentをインストールする

- 出典: https://github.com/github/awesome-copilot
- 投稿者: github
- カテゴリ: agent-orchestration

## なぜ使うのか

標準Copilotの能力を超えて、実行環境への直接操作、外部サービス連携、複雑なワークフロー自動化が可能になる

## いつ使うのか

セキュリティ監査、データベーススキーマ管理、Infrastructure as Code生成など高度な専門タスクをAI支援したい時

## やり方

1. https://awesome-copilot.github.com/agents でAgentを検索
2. AgentのドキュメントでMCP server要件を確認
3. 必要なMCP serverをセットアップ
4. `copilot plugin install <agent-name>@awesome-copilot` でAgentをインストール
5. Copilot Chat内でAgentを呼び出し（例: `@security-audit`）

### 入力

- Agent定義ファイル
- MCP server（必要に応じて）
- 外部サービス認証情報

### 出力

- 専門領域に特化したAI支援（例: 脆弱性検出、スキーマ最適化提案）
- 外部ツール・サービスと連携した自動化

## 使うツール・ライブラリ

- GitHub Copilot
- MCP servers
- Awesome Copilot Agents collection

## 前提知識

- GitHub Copilot（個人またはOrganizationサブスクリプション）
- VS CodeまたはCopilot CLI
- 基本的なGit操作知識
- 対象技術スタック（導入するagents/skills/instructionsが対象とする言語・フレームワーク）の基礎知識

## 根拠

> 「A community-created collection of custom agents, instructions, skills, hooks, workflows, and plugins to supercharge your GitHub Copilot experience.」

> 「copilot plugin install <plugin-name>@awesome-copilot」

> 「Agents: Specialized Copilot agents that integrate with MCP servers」

> 「Hooks: Automated actions triggered during Copilot agent sessions」
