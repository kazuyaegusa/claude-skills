# Local型とRemote型MCPサーバーを用途別に使い分ける

> Local型（stdio, コマンド実行）は開発者環境で直接実行、Remote型（HTTP, HTTPS URL）はクラウドサービスとして提供し、認証・スケーラビリティを考慮する

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: infrastructure

## なぜ使うのか

Local型は低レイテンシ・オフライン動作可能だが、スケールしづらい。Remote型は集中管理・認証・監査が容易だが、ネットワーク依存。用途に応じた選択で最適なUXとセキュリティを実現できる

## いつ使うのか

【Local】開発者ツール（Playwright, Azure DevOps CLI等）、オフライン必須、認証不要の場合
【Remote】エンタープライズサービス（M365 Copilot, Foundry）、集中管理・監査必須、SaaS型提供の場合

## やり方

【Local型】
1. MCPサーバーをCLIツール（npx, uvx等）としてパッケージング
2. VS Code等のMCPホスト設定で`{"type":"stdio", "command":"npx", "args":["-y", "@package/name"]}`形式で指定
3. ホストがサブプロセスとしてサーバー起動、stdin/stdoutでMCP通信

【Remote型】
1. MCPサーバーをHTTPSエンドポイントとしてデプロイ（例: https://mcp.ai.azure.com）
2. 認証（OAuth, API key等）を実装
3. ホスト設定で`{"type":"http", "url":"https://..."}` 指定
4. HTTP経由でMCPメッセージ送受信

### 入力

- Local: コマンドラインツール実装、パッケージマネージャ（npm, pip等）
- Remote: HTTPSサーバー環境、認証基盤、スケーラブルインフラ

### 出力

- Local: ローカルプロセスとして動作するMCPサーバー
- Remote: クラウドホストされたMCPエンドポイント

## 使うツール・ライブラリ

- Local: npx, uvx, stdio transport
- Remote: HTTP transport, OAuth/AAD, Azure App Service等

## コード例

```
# Local型設定例（VS Code mcp_settings.json）
{
  "mcpServers": {
    "playwright": {
      "type": "stdio",
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}

# Remote型設定例
{
  "mcpServers": {
    "foundry": {
      "type": "http",
      "url": "https://mcp.ai.azure.com"
    }
  }
}
```

## 前提知識

- Model Context Protocol (MCP)の基本概念（クライアント・サーバーアーキテクチャ、ツール・リソース・プロンプトの違い）
- MCPホスト（Claude Desktop, VS Code, GitHub Copilot等）の使用経験
- Azure/Microsoft 365の基本サービス理解（必要に応じてAzure subscription, M365 tenant）
- JSON設定ファイル編集、環境変数・認証の基礎知識
- （開発者向け）TypeScript/Python等のMCP SDK、npm/pip等パッケージマネージャ使用経験

## 根拠

> "TYPE: Local (stdio, npx/uvx) vs REMOTE (https://mcp.ai.azure.com, https://sentinel.microsoft.com/mcp/data-exploration)"
