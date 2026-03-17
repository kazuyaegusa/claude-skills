# Azure Developer CLI (azd) テンプレートとMCPサーバーを連携させ、インフラ付きでデプロイ可能にする

> azd templates（Bicep/Terraform等のIaC含む）にMCP統合を組み込み、`azd up`一発でMCPサーバー+必要なAzureリソースを一括デプロイできるようにする

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: context-management

## なぜ使うのか

MCPサーバーを手動セットアップすると、インフラ構築・認証設定・環境変数管理が煩雑。azdテンプレートで自動化すれば、開発者は数分でエンドツーエンド環境を立ち上げられる

## いつ使うのか

MCPサーバーをAzure上で本番運用したいが、手動インフラ構築を避けたいとき

## やり方

1. azdテンプレートリポジトリ作成（azure.yaml, infra/ディレクトリ含む）
2. MCPサーバーをコンテナ化またはApp Serviceとして定義
3. Bicep/TerraformでAzure OpenAI, Key Vault, App Service等を宣言
4. 環境変数・認証（Managed Identity等）をテンプレート内で自動設定
5. azure.yamlでMCPサーバーをserviceとして登録
6. azd upでインフラ+アプリを一括デプロイ
7. README内でMCPクライアント接続設定を案内

### 入力

- azdテンプレート（azure.yaml, IaCコード）
- MCPサーバー実装（Dockerfile or App Serviceデプロイ可能コード）
- 必要なAzureリソース定義（OpenAI, Storage等）

### 出力

- デプロイ済みMCPサーバー（HTTPS endpoint）
- 自動構成されたAzureリソース（認証・ネットワーク含む）
- 接続設定情報（.envまたはoutput）

## 使うツール・ライブラリ

- Azure Developer CLI (azd)
- Bicep or Terraform
- Azure App Service / Container Apps
- Azure OpenAI / Key Vault等

## コード例

```
# azure.yaml例
name: my-mcp-server
services:
  mcp:
    project: ./src
    language: python
    host: appservice

# azd upでデプロイ
$ azd up
# 出力例: MCP endpoint = https://my-mcp.azurewebsites.net
```

## 前提知識

- Model Context Protocol (MCP)の基本概念（クライアント・サーバーアーキテクチャ、ツール・リソース・プロンプトの違い）
- MCPホスト（Claude Desktop, VS Code, GitHub Copilot等）の使用経験
- Azure/Microsoft 365の基本サービス理解（必要に応じてAzure subscription, M365 tenant）
- JSON設定ファイル編集、環境変数・認証の基礎知識
- （開発者向け）TypeScript/Python等のMCP SDK、npm/pip等パッケージマネージャ使用経験

## 根拠

> "Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to large language models (LLMs). It allows AI applications to connect with various data sources and tools in a consistent manner"

> "MCP Hosts: Applications like AI assistants or IDEs that initiate connections. MCP Clients: Connectors within the host application that maintain 1:1 connections with servers. MCP Servers: Services that provide context and capabilities through the standardized MCP"

> "TYPE: Local (stdio, npx/uvx) vs REMOTE (https://mcp.ai.azure.com, https://sentinel.microsoft.com/mcp/data-exploration)"

> "INSTALL: 1-click install links for VS Code (vscode:mcp/install?...), VS Code Insiders, Visual Studio, IntelliJ, Eclipse"

> "CATEGORY: CLOUD AND INFRASTRUCTURE, DEVELOPER TOOLS, PRODUCTIVITY, DATA AND ANALYTICS, SECURITY"
