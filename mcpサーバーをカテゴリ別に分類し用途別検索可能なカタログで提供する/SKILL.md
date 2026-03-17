# MCPサーバーをカテゴリ別に分類し、用途別検索可能なカタログで提供する

> CLOUD AND INFRASTRUCTURE, DEVELOPER TOOLS, PRODUCTIVITY, DATA AND ANALYTICS, SECURITY等のカテゴリでMCPサーバーを整理し、README表形式でリポジトリ・説明・インストールリンクを一覧化する

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: infrastructure

## なぜ使うのか

MCPサーバーが増えると、ユーザーは自分のニーズに合うものを見つけにくくなる。カテゴリ分類とメタデータ（説明、タイプ、リンク）の標準化で、発見性と再利用性が向上する

## いつ使うのか

複数のMCPサーバーを提供し、ユーザーが適切なものを素早く選べるようにしたいとき

## やり方

1. MCPサーバーを機能領域でカテゴリ分類（例: DEVELOPER TOOLS, PRODUCTIVITY等）
2. 各サーバーのメタデータ収集（REPOSITORY, DESCRIPTION, CATEGORY, TYPE, INSTALL）
3. README.mdで表形式またはセクション形式で一覧化
4. 各エントリにロゴ・バッジ・インストールリンクを付与
5. ドキュメントサイトやazd templatesとのクロスリンク追加

### 入力

- MCPサーバーのメタデータ（名前、リポジトリURL、説明、カテゴリ、タイプ、インストールURL）
- カテゴリ定義（組織の分類基準）

### 出力

- カテゴリ別MCPサーバーカタログ（README.md）
- 検索可能なメタデータベース（JSON/YAML等）

## 使うツール・ライブラリ

- Markdown表形式
- shields.ioバッジ
- GitHub Pages等ドキュメントホスティング

## コード例

```
# カタログ例（README.md抜粋）
### <img height="18" width="18" src="..." alt="Azure Logo" /> Azure
- **REPOSITORY**: [microsoft/mcp](https://github.com/microsoft/mcp/tree/main/servers/Azure.Mcp.Server#readme)
- **DESCRIPTION**: All Azure MCP tools in a single server...
- **CATEGORY**: `CLOUD AND INFRASTRUCTURE`
- **TYPE**: `Local`
- **INSTALL**: [![Install Azure MCP in VS Code](...)](#)
```

## 前提知識

- Model Context Protocol (MCP)の基本概念（クライアント・サーバーアーキテクチャ、ツール・リソース・プロンプトの違い）
- MCPホスト（Claude Desktop, VS Code, GitHub Copilot等）の使用経験
- Azure/Microsoft 365の基本サービス理解（必要に応じてAzure subscription, M365 tenant）
- JSON設定ファイル編集、環境変数・認証の基礎知識
- （開発者向け）TypeScript/Python等のMCP SDK、npm/pip等パッケージマネージャ使用経験

## 根拠

> "Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to large language models (LLMs). It allows AI applications to connect with various data sources and tools in a consistent manner"

> "This repository contains core libraries, test frameworks, engineering systems, pipelines, and tooling for Microsoft MCP Server contributors to unify engineering investments; and reduce duplication and divergence"

> "MCP Hosts: Applications like AI assistants or IDEs that initiate connections. MCP Clients: Connectors within the host application that maintain 1:1 connections with servers. MCP Servers: Services that provide context and capabilities through the standardized MCP"

> "TYPE: Local (stdio, npx/uvx) vs REMOTE (https://mcp.ai.azure.com, https://sentinel.microsoft.com/mcp/data-exploration)"

> "CATEGORY: CLOUD AND INFRASTRUCTURE, DEVELOPER TOOLS, PRODUCTIVITY, DATA AND ANALYTICS, SECURITY"
