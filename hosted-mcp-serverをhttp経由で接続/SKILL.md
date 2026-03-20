# hosted MCP serverをHTTP経由で接続

> Exa MCPサーバー（https://mcp.exa.ai/mcp）にHTTPトランスポートで接続し、AI assistantに検索機能を追加する

- 出典: https://github.com/exa-labs/exa-mcp-server
- 投稿者: exa-labs
- カテゴリ: other

## なぜ使うのか

ローカルサーバー起動が不要で、設定ファイルの変更だけで機能追加できるため導入コストが低い

## いつ使うのか

MCPサーバーをローカルで管理したくない場合、複数環境で同じMCP機能を使いたい場合

## やり方

1. 利用するAI環境の設定ファイルパスを確認
2. mcpServersセクションにexaエントリを追加、urlに https://mcp.exa.ai/mcp を指定
3. AI環境を再起動して反映
4. 必要に応じてtools パラメータでツールを選択（例: ?tools=web_search_exa,get_code_context_exa）

### 入力

- AI環境の設定ファイルパス
- Exa API Key（オプション、deep_search_exa等の一部機能で必須）

### 出力

- AI assistantで利用可能な検索ツール（web_search_exa, get_code_context_exa等）

## 使うツール・ライブラリ

- Exa MCP Server (https://mcp.exa.ai/mcp)
- MCP protocol compatible AI environments

## コード例

```
{
  "mcpServers": {
    "exa": {
      "url": "https://mcp.exa.ai/mcp"
    }
  }
}
```

## 前提知識

- MCP (Model Context Protocol) の基本概念
- 使用するAI環境（Cursor/VS Code/Claude Code等）の設定ファイル構造
- JSONフォーマットの編集能力
- Exa APIの検索カテゴリと用途の理解

## 根拠

> Connect to Exa's hosted MCP server: https://mcp.exa.ai/mcp

> Never run Exa searches in main context. Always spawn Task agents: Agent runs Exa search internally, Agent processes results using LLM intelligence, Agent returns only distilled output

> Exa returns different results for different phrasings. For coverage: Generate 2-3 query variations, Run in parallel, Merge and deduplicate
