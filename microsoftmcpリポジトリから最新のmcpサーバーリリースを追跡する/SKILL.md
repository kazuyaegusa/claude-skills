# microsoft/mcpリポジトリから最新のMCPサーバーリリースを追跡する

> microsoft/mcpリポジトリのReleasesページで、Azure MCP・Fabric MCP等の最新バージョンとCHANGELOGを確認する

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: infrastructure

## なぜ使うのか

公式サーバーは頻繁に機能追加・バグ修正されるため、最新版を使わないとセキュリティリスクや互換性問題が発生する可能性があるため

## いつ使うのか

既存のMCPサーバーを運用中で、新機能やバグ修正を取り込みたい時

## やり方

1. https://github.com/microsoft/mcp にアクセス
2. README内のテーブルから対象サーバー（例: Azure MCP）の「Releases」列リンクをクリック
3. フィルタされたリリース一覧（例: `?q=Azure.Mcp.Server-`）を確認
4. 最新リリースのタグとCHANGELOGリンクを開き、変更内容を把握
5. 必要に応じてVS Code拡張機能を更新、またはnpm/uvx/NuGet等でパッケージを最新化

### 入力

- microsoft/mcpリポジトリURL
- 対象MCPサーバー名

### 出力

- 最新バージョン番号
- CHANGELOG記載の変更詳細
- 更新されたMCPサーバーパッケージ

## 使うツール・ライブラリ

- GitHub Releases API
- npm/uvx/NuGet（パッケージマネージャ）

## 前提知識

- MCPプロトコルの基本概念（Host/Client/Serverアーキテクチャ）
- VS Code/Claude Code/Copilot CLI等のMCPクライアントツール
- Azure CLI / Microsoft 365アカウント / GitHubアカウント（接続先サービスに応じて）
- Node.js/Python環境（ローカル実行型MCPサーバーを使う場合）

## 根拠

> 「Azure MCP Server can be used alone or with the GitHub Copilot for Azure extension in VS Code」（VS Code拡張機能として配布）

> 「Microsoft Foundry - TYPE: REMOTE - https://mcp.ai.azure.com」（リモートMCPサーバーの実例）

> 「Install Azure MCP in VS Code: vscode.dev/redirect?url=vscode:extension/ms-azuretools.vscode-azure-mcp-server」（ワンクリックインストールリンク）

> 「Azure MCP Documentation: https://learn.microsoft.com/azure/developer/azure-mcp-server/」（公式ドキュメント完備）
