# Azure MCPサーバーをローカルで実行しAzure CLIの資格情報を再利用する

> Azure MCPサーバーをnpx/uvx経由でローカル起動し、既存のAzure CLI認証（`az login`）を使ってAzureリソースを操作する

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

追加の認証設定なしで、開発者がすでに使っているAzure CLI credentialをそのまま活用でき、セキュアかつ迅速にMCP統合を開始できるため

## いつ使うのか

Azure開発者が既存のCLI認証を使ってMCPをすぐに試したい時

## やり方

1. Azure CLIで `az login` 済みであることを確認
2. VS CodeのINSTALLリンクをクリックするか、手動で `npx -y @azure/mcp` を実行
3. MCPクライアント（Claude Code等）の設定に `{"command": "npx", "args": ["-y", "@azure/mcp"]}` を追加
4. MCPクライアントを再起動し、Azure MCPサーバーが起動することを確認
5. LLMに「Azureのリソースグループ一覧を取得」等の指示を出し、Azure CLIトークンでアクセスできることを検証

### 入力

- Azure CLI認証済み環境（`az login`）
- Node.js/npm環境（npx実行可能）

### 出力

- ローカル起動されたAzure MCPサーバープロセス
- Azureリソースへの自然言語操作結果

## 使うツール・ライブラリ

- Azure CLI
- npx
- @azure/mcpパッケージ

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
