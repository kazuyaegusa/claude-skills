# MCP Serverでスキルを動的に拡張する

> Model Context Protocol（MCP）Serverを実装して、Claude Codeの機能を動的にAPI経由で拡張する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

静的なスキルファイルだけでは、外部APIとの連携やリアルタイムデータ取得が難しい。MCPを使うことで、Linear, Jira, Google Workspace, データベースなどの外部システムと統合できる

## いつ使うのか

Claude Codeを外部サービス（プロジェクト管理ツール、データベース、クラウドサービス）と連携させたい時

## やり方

1. MCPに対応したスキルを選択（例: linear-claude-skill, google-workspace-skills, postgres）
2. スキルのREADMEに従ってMCP Serverをセットアップ
3. 認証情報（OAuth, API Key）を設定
4. Claude Code設定でMCP Serverを有効化
5. Claude Codeから自然言語でMCP経由の操作を指示

### 入力

- 対象サービスのAPI認証情報
- MCPに対応したスキルリポジトリ

### 出力

- 外部サービスとの双方向連携
- リアルタイムデータの取得・操作

## 使うツール・ライブラリ

- Model Context Protocol（MCP）
- linear-claude-skill
- google-workspace-skills
- postgres / mysql / mssql skills
- outline skill

## 前提知識

- Claude Codeの基本的な使い方（スキルのインストール・有効化方法）
- Gitの基本操作（clone, pull）
- Markdown記法の読み書き
- （スキル開発の場合）Python, Node.js, Bashのいずれかの基礎知識
- （MCP Server利用の場合）API認証（OAuth, API Key）の基本理解

## 根拠

> "A curated list of Claude Skills."

> "If you use Claude to build web applications, do yourself a favor and use VibeSec-Skill to avoid getting hacked."

> "skill-creator - Template / helper to build new Claude skills."

> "agentskill.sh - Browse and install 69,000+ AI agent skills for Claude Code, Cursor, Copilot, Windsurf, Zed, and 20+ AI tools."

> "linear-claude-skill - Manage Linear issues, projects, and teams with MCP tools"
