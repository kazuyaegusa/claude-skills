# Local (stdio) とRemote (https) MCPサーバーを使い分ける

> MCPサーバーの実行形態を Local (stdioでプロセス起動) と Remote (https endpoint) の2種類から選択し、セキュリティ要件・認証フロー・実行環境に応じて適切な方式を採用する

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: prompt-engineering

## なぜ使うのか

Local型はユーザーのマシン上で実行されるため認証情報の管理が容易で低レイテンシだが、依存関係インストールが必要。Remote型は認証を中央管理でき複数クライアントで共有可能だが、ネットワーク経由のため遅延がある。用途に応じた使い分けでセキュリティと利便性を両立

## いつ使うのか

機密情報を扱う場合はLocal型（認証情報がローカルに閉じる）、複数環境で共有したい場合やサーバーサイドでデータ処理が必要な場合はRemote型

## やり方

1. Local型: `"type": "stdio"` + `"command": "npx/uvx/dotnet"` + `"args": [パッケージ名]` を設定。初回実行時に依存パッケージが自動インストールされる 2. Remote型: `"type": "http"` + `"url": "https://..."` を設定。認証はサーバー側でOAuth/Entra ID等で管理 3. テナントID等の動的パラメータは `"inputs"` フィールドで実行時プロンプトを定義

### 入力

- サーバータイプの決定（stdio / http）
- Local型: コマンド実行環境（Node.js / Python / .NET等）
- Remote型: エンドポイントURL、認証情報

### 出力

- Local型: ローカルプロセスとして起動したMCPサーバー
- Remote型: HTTPSエンドポイント経由でアクセス可能なMCPサーバー

## 使うツール・ライブラリ

- npx (Node.js パッケージ実行)
- uvx (Python パッケージ実行)
- dotnet run (.NET アプリ実行)
- OAuth 2.0 / Microsoft Entra ID (Remote型認証)

## コード例

```
// Local型設定例
{
  "name": "azure-devops",
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "@azure-devops/mcp", "${input:ado_org}"],
  "inputs": [{
    "id": "ado_org",
    "type": "promptString",
    "description": "Azure DevOps organization name"
  }]
}

// Remote型設定例
{
  "name": "foundry-mcp",
  "type": "http",
  "url": "https://mcp.ai.azure.com"
}
```

## 前提知識

- Model Context Protocol (MCP) の基本概念（Host / Client / Server アーキテクチャ）の理解
- VS Code / Visual Studio / Claude Desktop 等の MCP Host 対応アプリケーションの使用経験
- Microsoft Azure / Microsoft 365 / GitHub 等のサービスへのアクセス権限（該当サーバーを利用する場合）
- Node.js / Python / .NET 等のランタイム環境（Local型MCPサーバーを利用する場合）
- OAuth 2.0 / Microsoft Entra ID 等の認証フローの基礎知識（Remote型MCPサーバーを利用する場合）

## 根拠

> 「TYPE: Local (stdio) / Remote (https://...)」

> 「Microsoft 365 Calendar / Mail / User / Teams / Word / Admin Center / Copilot Chat 等の M365系MCPサーバーは全て Remote型（https://agent365.svc.cloud.microsoft/agents/tenants/{tenant_id}/servers/...）」

> 「Azure DevOps MCP / AKS MCP / Playwright MCP / Markitdown MCP 等は Local型（stdio）」
