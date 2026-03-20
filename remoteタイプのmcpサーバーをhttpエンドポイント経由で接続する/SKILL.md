# REMOTEタイプのMCPサーバーをHTTPエンドポイント経由で接続する

> サーバーレス実行されるMCPサーバー（例: Microsoft Foundry `https://mcp.ai.azure.com`）に、ローカルプロセスなしで接続する

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

ローカル環境にNode.js/Python等のランタイムやサーバープロセスを立てる必要がなく、認証・スケーリング・更新を全てクラウド側で管理できるため

## いつ使うのか

Azure Foundry・Microsoft 365 Calendar/Mail/Teams等、クラウドホストされたMCPサーバーを利用する時

## やり方

1. READMEから対象サーバーのTYPEカラムが `REMOTE` かつURLが記載されていることを確認
2. VS Code/Insidersのインストールリンクをクリック
3. `vscode:mcp/install?{"type":"http","url":"https://..."}` 形式のURLがMCPクライアントに登録される
4. 初回接続時に認証フロー（OAuth等）が走る場合は画面指示に従う
5. 接続成功後、リモートサーバーが提供するツール・リソースが利用可能になる

### 入力

- リモートMCPサーバーのHTTPS URL
- 認証情報（Microsoft Entra tenant ID等、必要に応じて）

### 出力

- MCPクライアントに登録されたリモートサーバー接続
- クラウド側でホストされるツール群（例: カレンダー作成、メール送信、Teams操作）

## 使うツール・ライブラリ

- MCPクライアント（VS Code/Claude Code等）
- HTTPベースMCPトランスポート

## 前提知識

- MCPプロトコルの基本概念（Host/Client/Serverアーキテクチャ）
- VS Code/Claude Code/Copilot CLI等のMCPクライアントツール
- Azure CLI / Microsoft 365アカウント / GitHubアカウント（接続先サービスに応じて）
- Node.js/Python環境（ローカル実行型MCPサーバーを使う場合）

## 根拠

> 「This repository contains core libraries, test frameworks, engineering systems, pipelines, and tooling for Microsoft MCP Server contributors to unify engineering investments; and reduce duplication and divergence」（単一リポジトリで統合管理）

> 「Microsoft Foundry - TYPE: REMOTE - https://mcp.ai.azure.com」（リモートMCPサーバーの実例）

> 「Azure MCP Documentation: https://learn.microsoft.com/azure/developer/azure-mcp-server/」（公式ドキュメント完備）
