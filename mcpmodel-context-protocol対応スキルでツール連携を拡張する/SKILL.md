# MCP（Model Context Protocol）対応スキルでツール連携を拡張する

> Linear、Google Workspace、PostgreSQL、NotebookLM等の外部サービスと連携するMCP対応スキルをインストールし、Claude Code から直接データ操作・クエリ実行を可能にする

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

SKILL.md だけでは不可能な「外部システムへの実際のアクセス」をMCPサーバー経由で実現し、AIを単なるコード生成ツールから「実行可能なワークフロー自動化エージェント」に昇格させるから

## いつ使うのか

外部サービス（Linear、Jira、Google Workspace、データベース等）との統合が必要なとき、AIに「読み取り専用」ではなく「書き込み・実行」能力を持たせたいとき

## やり方

1. awesome-claude-skills の該当カテゴリ（Data & Analysis, Collaboration等）からMCP対応スキルを特定（説明に「MCP」「API」の記載があるもの）
2. リポジトリのREADMEに従ってMCPサーバーをインストール（通常 npx/pip でインストール）
3. 認証情報（API キー、OAuth トークン等）を設定
4. Claude Code の MCP 設定ファイルにサーバーを追加
5. SKILL.md を ~/.claude/skills/ に配置
6. Claude セッションでツールが認識されることを確認（例: 'list Linear issues' コマンドが動作）

### 入力

- 外部サービスのAPI認証情報
- MCPサーバーのインストール要件（Node.js, Python等）
- Claude Code の MCP 設定ファイル

### 出力

- 外部サービスへの読み書きアクセス機能
- 自動化されたワークフロー（例: Linear チケット作成、DB クエリ実行、Google Docs 更新等）

## 使うツール・ライブラリ

- linear-claude-skill + MCP server
- postgres skill + MCP server
- google-workspace-skills + OAuth
- notebooklm skill + Google API

## コード例

```
# 例: Linear MCP スキルのセットアップ
git clone https://github.com/wrsmith108/linear-claude-skill
cd linear-claude-skill
npm install

# .env に Linear API キーを設定
echo "LINEAR_API_KEY=your_api_key_here" > .env

# Claude Code の MCP 設定に追加（~/.claude/mcp.json）
{
  "mcpServers": {
    "linear": {
      "command": "node",
      "args": ["/path/to/linear-claude-skill/server.js"],
      "env": {
        "LINEAR_API_KEY": "your_api_key_here"
      }
    }
  }
}

# SKILL.md を配置
cp SKILL.md ~/.claude/skills/linear/

# Claude セッションでテスト
# "List all open issues assigned to me in Linear" → MCP経由でAPIコール→結果表示
```

## 前提知識

- Claude Code の基本的な使い方（セットアップ、セッション開始、基本的なプロンプト）
- ~/.claude/skills/ ディレクトリの役割とスキル読み込みの仕組み
- SKILL.md の基本構造（name, description, 使用条件等のフロントマター）
- git の基本操作（clone, pull）
- ターミナル/コマンドラインの基本操作
- （MCP利用時）Node.js/Python環境、API認証の基礎知識

## 根拠

> 「A curated list of Claude Skills」 - awesome-claude-skills リポジトリの冒頭文

> 「If you use Claude to build web applications, do yourself a favor and use VibeSec-Skill to avoid getting hacked」 - セキュリティスキルの重要性を強調

> 「test-driven-development - Use when implementing any feature or bugfix, before writing implementation code」 - TDDスキルの説明

> 「linear-claude-skill - Manage Linear issues, projects, and teams with MCP tools, SDK scripts, and GraphQL fallbacks」 - MCP連携スキルの例

> 「claude-starter - Production-ready Claude Code configuration template with 40 auto-activating skills across 8 domains, TOON format support for 30-60% token savings」 - 大規模スキルコレクションの例
