# MCP ServerとSkillを併用して機能を拡張する

> MCP（Model Context Protocol）サーバーとClaude Skillsを組み合わせ、外部API（Linear, Google Workspace, NotebookLM等）とのシームレスな統合を実現する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

MCPは低レベルのAPI呼び出しを担当し、Skillは高レベルのワークフロー（例: Linear issueの作成→コミット→PR作成）を記述する。両者を分離することで、再利用性とメンテナンス性が向上

## いつ使うのか

外部SaaS（Linear, Jira, Google Workspace）と連携する時、API呼び出しとビジネスロジックを分離したい時

## やり方

1. MCP ServerをClaude Codeに接続（例: @modelcontextprotocol/server-linear）
2. Skillで高レベルワークフローを定義（例: linear-claude-skill）
3. Skill内でMCP toolsを呼び出し（例: `linear.createIssue()`）
4. GraphQL/REST APIのフォールバックを記述（MCP障害時）
5. CLAUDE.mdでスキルとMCPの依存関係を文書化

### 入力

- MCP Serverのエンドポイント設定
- Skillのワークフロー定義

### 出力

- 外部サービスとの自動連携
- エラーハンドリング付きフォールバック

## 使うツール・ライブラリ

- Model Context Protocol
- linear-claude-skill
- google-workspace-skills

## 前提知識

- Claude Codeの基本的な使い方（スキルのインストール・実行）
- GitHubでのリポジトリ検索・クローン操作
- ~/.claude/skills/ ディレクトリ構造の理解
- （オプション）MCP（Model Context Protocol）の概念
