# MCPサーバーのカタログ化と分類

> 20以上のMCPサーバーをREADME・ソースコード・CHANGELOG・ドキュメント・トラブルシューティング・サポート情報の6要素で統一管理し、カテゴリ(CLOUD/DEVELOPER TOOLS/PRODUCTIVITY/DATA/SECURITY)とタイプ(Local/Remote)で分類する

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: infrastructure

## なぜ使うのか

開発者が目的に応じて適切なMCPサーバーを素早く発見でき、導入後のトラブルシューティングも一貫した体験で行えるようにするため。エコシステム全体の保守性と発見可能性を向上させる。

## いつ使うのか

複数のMCPサーバーを提供するエコシステムを構築し、開発者が目的別に選択・導入できるようにしたい場合

## やり方

1. 各MCPサーバーごとにREADME/CHANGELOG/Source Code/Releases/Documentation/Troubleshooting/Supportの7つのリンクを含むテーブル行を作成
2. カテゴリ(CLOUD AND INFRASTRUCTURE, DEVELOPER TOOLS, PRODUCTIVITY, DATA AND ANALYTICS, SECURITY)を付与
3. タイプをLocal(ローカル実行)またはRemote(URL指定、例: https://mcp.ai.azure.com)で明記
4. INSTALLカラムに各IDE(VS Code/VS Code Insiders/Visual Studio/IntelliJ/Eclipse)向けのワンクリックインストールボタンを配置
5. github.com/microsoft/mcp リポジトリで一元管理し、各サーバーのサブディレクトリ(servers/Azure.Mcp.Server等)にソースコードを配置

### 入力

- 各MCPサーバーのソースコード、ドキュメント、リリースノート
- 対象IDE(VS Code, Visual Studio等)のMCPインストールプロトコルURL仕様

### 出力

- README.mdに記載された統一フォーマットのMCPサーバーカタログテーブル
- 各IDE向けのワンクリックインストールリンク
- カテゴリ・タイプ別に分類されたサーバー一覧

## 使うツール・ライブラリ

- GitHub Repository (microsoft/mcp)
- Markdown Table
- VS Code MCP Install Protocol (vscode:mcp/install?{config})
- Visual Studio MCP Install Protocol (aka.ms/vs/mcp-install?{config})

## コード例

```
[![Install Azure MCP in VS Code](badge)](https://vscode.dev/redirect?url=vscode:extension/ms-azuretools.vscode-azure-mcp-server)
```

## 前提知識

- MCP (Model Context Protocol)の基本概念(Host, Client, Server, Tools, Resources)の理解
- VS Code/Visual Studio等のIDEでのMCP設定方法の基礎知識
- Microsoft Graph APIの基本的な知識(認証、スコープ、エンドポイント構造)
- Azure/M365のテナントID・組織名等の基本的な概念の理解
- npmまたはPython(uvx)を使ったパッケージインストールの経験

## 根拠

> "This repository contains core libraries, test frameworks, engineering systems, pipelines, and tooling for Microsoft MCP Server contributors to unify engineering investments; and reduce duplication and divergence"

> "Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to large language models (LLMs)"

> "MCP Hosts: Applications like AI assistants or IDEs that initiate connections. MCP Clients: Connectors within the host application that maintain 1:1 connections with servers. MCP Servers: Services that provide context and capabilities through the standardized MCP."

> "Azure MCP Server can be used alone or with the GitHub Copilot for Azure extension in VS Code."

> "CATEGORY: CLOUD AND INFRASTRUCTURE, TYPE: Local" (Azure MCP)
