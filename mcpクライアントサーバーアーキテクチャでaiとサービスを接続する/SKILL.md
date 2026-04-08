# MCPクライアント・サーバーアーキテクチャでAIとサービスを接続する

> MCP Host（AI assistant/IDE）、MCP Client（Host内のコネクタ）、MCP Server（データソース・ツール提供サービス）の3層構造を構築し、標準化されたプロトコルでLLMにコンテキストと実行能力を提供する

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

各AIアプリケーションが独自のAPIラッパーを実装する必要がなくなり、MCPサーバーを追加するだけで新しいデータソース・ツールを利用可能になるため、開発コストと保守負担が削減される

## いつ使うのか

AIエージェントに外部サービスへのアクセス権限を与える必要がある場合。特に複数サービスを横断利用したい場合に有効

## やり方

1. MCP Hostとなるアプリケーション（VS Code/Claude Desktop等）をセットアップ 2. Host内にMCP Clientを組み込む（多くの場合は拡張機能として提供） 3. MCPサーバーの接続情報（stdio/http、command/url、認証情報）を設定ファイルに記述 4. Host起動時にClientがServerと1:1接続を確立 5. AIエージェントが自然言語でリクエストすると、ClientがServerのツール・リソースを呼び出して結果を返す

### 入力

- MCP Host対応アプリケーション（VS Code/Visual Studio/Claude Desktop等）
- MCPサーバーの接続情報（type: stdio/http、command/url、args、認証情報）
- 必要に応じてアクセストークン・API Key等の認証情報

### 出力

- AIエージェントから自然言語で外部サービスを操作可能な環境
- MCP Serverが提供するツール・リソースのカタログ
- 実行結果（データ取得、CRUD操作、検索結果等）

## 使うツール・ライブラリ

- MCP SDK
- VS Code拡張（例: ms-azuretools.vscode-azure-mcp-server）
- claude-desktop設定ファイル
- GitHub Copilot CLI / Claude Code

## コード例

```
// MCP Client設定例（VS Code settings.json）
{
  "mcpServers": {
    "azure-mcp": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@azure/mcp-server"]
    },
    "foundry-mcp": {
      "type": "http",
      "url": "https://mcp.ai.azure.com"
    }
  }
}
```

## 前提知識

- Model Context Protocol (MCP) の基本概念（Host / Client / Server アーキテクチャ）の理解
- VS Code / Visual Studio / Claude Desktop 等の MCP Host 対応アプリケーションの使用経験
- Microsoft Azure / Microsoft 365 / GitHub 等のサービスへのアクセス権限（該当サーバーを利用する場合）
- Node.js / Python / .NET 等のランタイム環境（Local型MCPサーバーを利用する場合）
- OAuth 2.0 / Microsoft Entra ID 等の認証フローの基礎知識（Remote型MCPサーバーを利用する場合）

## 根拠

> 「Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to large language models (LLMs)」

> 「MCP follows a client-server architecture: MCP Hosts (Applications like AI assistants or IDEs), MCP Clients (Connectors within the host application), MCP Servers (Services that provide context and capabilities)」

> 「This repository contains core libraries, test frameworks, engineering systems, pipelines, and tooling for Microsoft MCP Server contributors to unify engineering investments; and reduce duplication and divergence」

> 「Azure MCP Server implements the MCP specification to create a seamless connection between AI agents and Azure services」

> 「INSTALL: vscode.dev/redirect?url=vscode:extension/... (VS Code), vscode-insiders:extension/... (VS Code Insiders), aka.ms/vs/mcp-install?... (Visual Studio)」
