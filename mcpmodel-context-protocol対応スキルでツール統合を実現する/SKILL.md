# MCP（Model Context Protocol）対応スキルでツール統合を実現する

> Linear, NotebookLM, Google Workspace, VideoDB など、MCP対応スキルを導入し、Claude CodeからSaaS APIを直接呼び出せるようにする

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

MCPはClaude Codeとサードパーティツールを標準化されたプロトコルで接続する仕組み。MCP対応スキルを使うと、認証・APIリクエスト・レスポンス処理が抽象化され、自然言語命令だけで外部サービスを操作できる

## いつ使うのか

Linear、NotebookLM、Gmail、Googleカレンダーなど、外部SaaSとClaude Codeを連携させたい時

## やり方

1. 使いたいサービスのMCP対応スキルを検索（例: linear-claude-skill, notebooklm, google-workspace-skills）
2. リポジトリのセットアップ手順に従ってMCPサーバーを起動（多くはnpm/Docker）
3. Claude CodeのMCP設定ファイル（~/.claude/mcp.json等）にサーバーエンドポイントを登録
4. スキルのSKILL.mdを `~/.claude/skills/` に配置
5. Claude Codeに「Linearで新しいissueを作って」と指示すると、MCPサーバー経由でLinear APIが呼ばれる

### 入力

- 連携したいSaaSサービス
- API認証情報（OAuth token, API key等）

### 出力

- SaaSサービス上に作成されたリソース（issue, ドキュメント, イベント等）
- Claude Code上での操作結果確認

## 使うツール・ライブラリ

- Model Context Protocol (MCP)
- linear-claude-skill
- notebooklm skill
- google-workspace-skills
- npm / Docker

## 前提知識

- Claude Codeの基本的な使い方（スキルの配置場所 ~/.claude/skills/ の理解）
- GitHubリポジトリのクローン方法
- npm/npx の基本操作（一部スキルのインストールに必要）
- MCP（Model Context Protocol）の概念（外部ツール連携スキルを使う場合）

## 根拠

> 投稿タイトル: 'BehiSecc/awesome-claude-skills - A curated list of Claude Skills.'

> 収録スキル例: 'docx - Create, edit, analyze Word docs with tracked changes', 'test-driven-development - Use when implementing any feature or bugfix', 'VibeSec-Skill - VibeSec helps Claude write secure code and prevent common vulnerabilities', 'pm-skills - 24 product management skills across the Triple Diamond lifecycle'

> コレクション例: 'OpenPaw - 38-skill bundle that turns Claude Code into a personal assistant. Run via npx pawmode', 'agentskill.sh - Browse and install 69,000+ AI agent skills'

> Tip: 'If you use Claude to build web applications, do yourself a favor and use VibeSec-Skill to avoid getting hacked.'

> GitHub URL: https://github.com/BehiSecc/awesome-claude-skills
