# 複数のMicrosoft公式MCPサーバーを組み合わせて企業ワークフローを構築する

> Azure MCP + Microsoft 365 Mail MCP + GitHub MCP等、複数の公式サーバーを同時接続し、横断的なAIエージェントフローを実現する

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

単一サービスの操作では完結しない実務タスク（例: GitHub PRレビュー結果をTeamsに通知、Azureリソース状態を定期メール送信）を、LLMが自律的に実行できるようにするため

## いつ使うのか

GitHub→Azure→Microsoft 365のような複数サービスを跨ぐ自動化をAIエージェントで実現したい時

## やり方

1. 必要なMCPサーバー（例: Azure MCP, Microsoft 365 Mail, GitHub MCP）を全てVS Codeにインストール
2. 各サーバーに必要な認証（Azure CLI, Microsoft 365 OAuth, GitHub token等）を設定
3. MCPクライアントから複数サーバーのツールが同時に利用可能になることを確認（例: `list_tools` 呼び出し）
4. LLMに「GitHubのPR一覧を取得し、レビュー待ちをTeamsに投稿」等の複合タスクを指示
5. LLMが複数MCPサーバーのツールを組み合わせて実行する様子を観察・デバッグ

### 入力

- 各MCPサーバーへの認証情報
- MCPクライアント（Claude Code/Copilot CLI等）
- 実行したいワークフローの自然言語記述

### 出力

- 複数サービスを横断した自動化フロー
- 各サービスの操作ログ（メール送信、Teams投稿、Azureリソース更新等）

## 使うツール・ライブラリ

- Azure MCP
- Microsoft 365 Mail/Calendar/Teams MCP
- GitHub MCP

## 前提知識

- MCPプロトコルの基本概念（Host/Client/Serverアーキテクチャ）
- VS Code/Claude Code/Copilot CLI等のMCPクライアントツール
- Azure CLI / Microsoft 365アカウント / GitHubアカウント（接続先サービスに応じて）
- Node.js/Python環境（ローカル実行型MCPサーバーを使う場合）

## 根拠

> 「This repository contains core libraries, test frameworks, engineering systems, pipelines, and tooling for Microsoft MCP Server contributors to unify engineering investments; and reduce duplication and divergence」（単一リポジトリで統合管理）

> 「Azure MCP Server can be used alone or with the GitHub Copilot for Azure extension in VS Code」（VS Code拡張機能として配布）

> 「Microsoft Foundry - TYPE: REMOTE - https://mcp.ai.azure.com」（リモートMCPサーバーの実例）

> 「Install Azure MCP in VS Code: vscode.dev/redirect?url=vscode:extension/ms-azuretools.vscode-azure-mcp-server」（ワンクリックインストールリンク）

> 「Azure MCP Documentation: https://learn.microsoft.com/azure/developer/azure-mcp-server/」（公式ドキュメント完備）
