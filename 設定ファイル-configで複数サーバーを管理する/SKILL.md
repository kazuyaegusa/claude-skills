# 設定ファイル（--config）で複数サーバーを管理する

> mcp.json形式の設定ファイルを用意し、`--config`と`--server`オプションで特定サーバーをInspectorに読み込む。単一サーバーまたは"default-server"なら--server省略可能

- 出典: https://github.com/modelcontextprotocol/inspector
- 投稿者: modelcontextprotocol
- カテゴリ: other

## なぜ使うのか

複数のMCPサーバーを開発・運用する際、各サーバーのコマンド・環境変数・引数を一元管理でき、再現性の高いテスト環境を構築できる

## いつ使うのか

複数のMCPサーバーを開発している、チームで統一された設定ファイルを共有したい、環境ごとに異なるサーバーを切り替えたい場合

## やり方

1. mcp.jsonに複数サーバー定義を記述（mcpServersオブジェクト）
2. `npx @modelcontextprotocol/inspector --config mcp.json --server myserver` で起動
3. 単一サーバーまたはdefault-serverの場合は `--server` 省略可能
4. トランスポートタイプ（stdio/sse/streamable-http）は自動検出

### 入力

- mcp.json形式の設定ファイル（mcpServersオブジェクトにサーバー定義）
- 起動したいサーバーの名前（--serverオプション、単一/default-serverなら省略可）

### 出力

- 指定サーバーがInspectorに接続された状態
- 再現可能な開発・テスト環境

## 使うツール・ライブラリ

- npx
- @modelcontextprotocol/inspector

## コード例

```
# mcp.json例
{
  "mcpServers": {
    "everything": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-everything"],
      "env": {"hello": "Hello MCP!"}
    },
    "my-server": {
      "command": "node",
      "args": ["build/index.js"],
      "env": {"key": "value"}
    },
    "sse-server": {
      "type": "sse",
      "url": "http://localhost:3000/sse"
    }
  }
}

# 起動コマンド
npx @modelcontextprotocol/inspector --config mcp.json --server everything

# 単一サーバーの場合（--server省略可）
npx @modelcontextprotocol/inspector --config mcp.json
```

## 前提知識

- Node.js ^22.7.5以上
- MCPサーバーの基本概念（tools/resources/prompts）の理解
- MCPのトランスポート種別（stdio/SSE/Streamable HTTP）の違い
- JSON形式の設定ファイル記述能力（mcp.json）

## 根拠

> 「npx @modelcontextprotocol/inspector node build/index.js」— インストール不要でMCPサーバーを起動

> 「The MCP Inspector provides convenient buttons to export server launch configurations for use in clients such as Cursor, Claude Code, or the Inspector's CLI. The file is usually called mcp.json.」
