# MCPサーバーをカテゴリ別・型別に整理してカタログ化する

> 提供するMCPサーバー群を「CATEGORY（CLOUD AND INFRASTRUCTURE / DEVELOPER TOOLS / PRODUCTIVITY / DATA AND ANALYTICS / SECURITY）」と「TYPE（Local / Remote）」で分類し、表形式またはセクション形式でドキュメント化する

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: infrastructure

## なぜ使うのか

ユーザーが自分のユースケースに最適なMCPサーバーを素早く見つけられるようにするため。特に20種類以上のサーバーがある場合、カテゴリ分けがないと探索コストが高い

## いつ使うのか

複数のMCPサーバーを提供する場合。特にエコシステム全体を俯瞰可能なカタログページを作成したい場合

## やり方

1. 各MCPサーバーのユースケース・提供機能を分析 2. カテゴリ軸とタイプ軸で分類 3. README.mdに見出し（### カテゴリ名）+ 説明リスト（REPOSITORY / DESCRIPTION / CATEGORY / TYPE / INSTALL）の形式で記載 4. インストールリンクを複数IDE向けに並列提供（VS Code / VS Code Insiders / Visual Studio / IntelliJ / Eclipse等） 5. Remote型の場合はエンドポイントURLも明記

### 入力

- MCPサーバーのメタデータ（名前、説明、リポジトリURL、カテゴリ、タイプ、インストールコマンド等）

### 出力

- 構造化されたMCPサーバーカタログドキュメント（README.md等）
- カテゴリ別・タイプ別のナビゲーション

## 使うツール・ライブラリ

- Markdown
- GitHub README badges（shields.io）

## コード例

```
// カタログ構成例（Markdown）
### ☸️ Azure Kubernetes Service (AKS)
- **REPOSITORY**: [Azure/aks-mcp](https://github.com/Azure/aks-mcp)
- **DESCRIPTION**: An MCP server that enables AI assistants to interact with AKS clusters...
- **CATEGORY**: `CLOUD AND INFRASTRUCTURE`
- **TYPE**: `Local`
- **INSTALL**: [![VS Code](...)](#) [![VS Code Insiders](...)](#) [![Visual Studio](...)](#)
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

> 「TYPE: Local (stdio) / Remote (https://...)」
