# UI Exportボタンでmcp.json設定を自動生成する

> Inspector UIで動作確認したサーバー設定を「Server Entry」「Servers File」ボタンでクリップボードにコピーし、Cursor/Claude Code等のクライアントに即座に適用可能なmcp.json形式で取得する

- 出典: https://github.com/modelcontextprotocol/inspector
- 投稿者: modelcontextprotocol
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動でのJSON記述ミスを防ぎ、Inspector上で検証済みの設定を確実にクライアントへ移行できるため、設定ファイルの品質とデプロイ速度が向上する

## いつ使うのか

MCPサーバーの動作確認後、Cursor/Claude Codeに統合する直前。複数サーバーを管理する設定ファイルを整備する際

## やり方

1. Inspector UIでサーバーを起動し、動作を確認
2. UIの「Server Entry」ボタンをクリック→単一サーバーエントリがクリップボードにコピーされる
3. または「Servers File」ボタンで完全なmcp.json構造をコピー
4. クリップボードの内容をmcp.jsonに貼り付け

### 入力

- Inspector UIで接続済みのMCPサーバー設定（command, args, env, または url）

### 出力

- Server Entry: 単一サーバーのJSON設定（mcpServersオブジェクト内に貼り付け可能）
- Servers File: 完全なmcp.json構造（default-serverとして設定済み）

## 使うツール・ライブラリ

- MCP Inspector UI

## コード例

```
# Server Entry出力例（STDIO）
{
  "command": "node",
  "args": ["build/index.js", "--debug"],
  "env": {
    "API_KEY": "your-api-key",
    "DEBUG": "true"
  }
}

# Servers File出力例（完全版）
{
  "mcpServers": {
    "default-server": {
      "command": "node",
      "args": ["build/index.js"],
      "env": {
        "API_KEY": "xxx"
      }
    }
  }
}

# SSE/Streamable HTTPの場合
{
  "type": "sse",
  "url": "http://localhost:3000/events"
}
```

## 前提知識

- Node.js ^22.7.5以上
- MCPサーバーの基本概念（tools/resources/prompts）の理解
- MCPのトランスポート種別（stdio/SSE/Streamable HTTP）の違い
- JSON形式の設定ファイル記述能力（mcp.json）

## 根拠

> 「The MCP inspector is a developer tool for testing and debugging MCP servers.」

> 「npx @modelcontextprotocol/inspector node build/index.js」— インストール不要でMCPサーバーを起動

> 「The MCP Inspector provides convenient buttons to export server launch configurations for use in clients such as Cursor, Claude Code, or the Inspector's CLI. The file is usually called mcp.json.」

> 「Client-side timeout (ms) - Inspector will cancel the request if no response is received within this time. Note: servers may have their own timeouts」— タイムアウト設定の明示的説明
