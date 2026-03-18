# IDE統合によるAIアシスタントへのデータベース操作委譲

> Claude Code、Cursor、Windsurf等のIDE内AIアシスタントをMCP Toolbox経由でデータベースに接続し、自然言語でのクエリ実行・スキーマ管理・コード生成を可能にする

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: claude-code-workflow

## なぜ使うのか

IDE↔データベース間のコンテキストスイッチを削減し、「2024年の注文数と商品は?」のような自然言語クエリでデータ取得、テーブル作成、インデックス追加をAIに委譲できる。また、AIがリアルタイムのスキーマを参照するため、生成されるコードやクエリの精度が向上する

## いつ使うのか

データベーススキーマを頻繁に参照しながらコードを書く時、または手動でSQLを書く時間を削減したい時

## やり方

1. MCP Toolboxサーバーをローカルまたはリモートで起動
2. IDE（Claude Code/Cursor/Windsurf等）のMCP設定ファイルにToolboxサーバーのエンドポイントを追加
3. IDE内でAIアシスタントに自然言語でデータベース操作を依頼（例: 「usersテーブルにemailカラムを追加して」）
4. AIがMCP Toolbox経由でスキーマを取得し、適切なSQLを生成・実行

### 入力

- 起動中のMCP Toolboxサーバー
- IDEのMCP設定ファイル
- 自然言語でのデータベース操作指示

### 出力

- AIが生成・実行したSQLクエリ
- データベーススキーマに基づいて生成されたアプリケーションコード・テスト

## 使うツール・ライブラリ

- Claude Code、Cursor、Windsurf等のMCP対応IDE
- MCP Toolbox Server

## コード例

```
# IDE（Claude Code）のMCP設定例（推測）
# claude_desktop_config.json
{
  "mcpServers": {
    "toolbox": {
      "command": "npx",
      "args": ["@toolbox-sdk/server", "--tools-file", "/path/to/tools.yaml"]
    }
  }
}

# IDE内での自然言語操作例
"How many orders were delivered in 2024, and what items were in them?"
→ AIがMCP Toolbox経由でSQLを生成・実行し、結果を返す
```

## 前提知識

- MCP（Model Context Protocol）の基本概念
- LLMエージェントフレームワーク（LangChain/LlamaIndex/Genkit等）の基礎知識
- SQL、データベース接続（ホスト/ポート/認証）の基本
- YAML設定ファイルの読み書き
- Docker/コンテナの基本操作（コンテナ版を使う場合）
- 各言語のパッケージマネージャー（pip, npm, go get）の使用経験

## 根拠

> 「MCP Toolbox for Databases is an open source MCP server for databases. It enables you to develop tools easier, faster, and more securely by handling the complexities such as connection pooling, authentication, and more.」

> 「By connecting your IDE to your databases with MCP Toolbox, you can delegate complex and time-consuming database tasks, allowing you to build faster and focus on what matters.」

> 「This solution was originally named 'Gen AI Toolbox for Databases' as its initial development predated MCP, but was renamed to align with recently added MCP compatibility.」

> Python/JS/Go向けの複数SDKとコードサンプル（toolbox-langchain, @toolbox-sdk/core, mcp-toolbox-sdk-go等）
