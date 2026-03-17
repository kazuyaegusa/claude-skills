# GitHub Copilot CLIプラグインとしてMCPサーバーを配布する

> Copilot CLI (/plugin install形式) でMCPサーバーの機能を提供し、ターミナルからAzureリソース操作・スキル参照を可能にする

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: automation-pipeline

## なぜ使うのか

VS Code拡張だけでなく、CLIからもMCP機能を使いたいユースケース（CI/CD, スクリプト自動化等）がある。Copilot CLIプラグインとして配布すれば、コマンドライン中心の開発者もカバーできる

## いつ使うのか

Copilot CLIユーザーにAzure操作機能を提供したいとき、またはCI/CDパイプラインで自然言語ベース自動化を実現したいとき

## やり方

1. Copilot CLIプラグインmarketplaceを追加: `/plugin marketplace add microsoft/skills`
2. Azure pluginインストール: `/plugin install azure-skills@skills`
3. プラグインがMCPサーバー（Azure MCP等）のツールとスキルを参照
4. Copilot CLIで自然言語コマンド実行（例: `copilot "deploy app to Azure"`）
5. プラグインが背後でMCPサーバー呼び出し、Azureリソース操作
6. 結果をターミナルに返す

### 入力

- Copilot CLIインストール済み環境
- MCPサーバー（azure-skills等）
- Azure認証情報

### 出力

- ターミナルから自然言語でAzure操作可能な環境
- CopilotがMCPサーバー経由で実行したコマンド結果

## 使うツール・ライブラリ

- GitHub Copilot CLI
- microsoft/skills marketplace
- Azure MCP Server

## コード例

```
# プラグインインストール
$ copilot /plugin marketplace add microsoft/skills
$ copilot /plugin install azure-skills@skills

# 使用例
$ copilot "list all resource groups in my subscription"
# → Azure MCPサーバー経由でaz group list実行
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

> "Get started with the Azure plugin, which connects GitHub Copilot CLI or Claude Code to your Azure account. /plugin marketplace add microsoft/skills, /plugin install azure-skills@skills"
