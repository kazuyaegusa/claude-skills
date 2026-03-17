# MCPクライアント・サーバーアーキテクチャでLLMコンテキスト提供を標準化する

> Model Context Protocol (MCP)を使い、LLMアプリケーション（MCPホスト）とデータソース・ツール（MCPサーバー）を1:1クライアント・サーバー接続で統合する

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: prompt-engineering

## なぜ使うのか

各サービスが独自APIを持つと、LLMごとに統合コードを書く必要がある。MCPで標準化すれば、サーバー側が一度実装すれば全てのMCP対応LLMクライアントから利用可能になり、開発効率と相互運用性が向上する

## いつ使うのか

LLMに外部ツール・データソースへのアクセス能力を持たせたいが、個別統合コードを書きたくないとき

## やり方

1. MCPホスト（Claude Desktop, VS Code, GitHub Copilot等）を用意
2. MCPクライアント（ホスト内のコネクタ）を初期化
3. MCPサーバー（Azure MCP, GitHub MCP等）に接続
4. サーバーが公開するツール・リソース・プロンプトをLLMから呼び出し可能にする
5. LLMの推論結果に基づいてサーバー側でAPI実行・データ取得
6. 結果をLLMにコンテキストとして返す

### 入力

- MCP対応LLMクライアント（Claude Desktop, VS Code extension等）
- MCPサーバーのエンドポイント情報（Local: コマンド+引数、Remote: HTTPS URL）
- 必要に応じて認証情報（Azure subscription, GitHub PAT, M365 tenant ID等）

### 出力

- LLMから呼び出し可能なツール・リソース一覧
- API実行結果のコンテキストデータ（JSON等）

## 使うツール・ライブラリ

- Model Context Protocol (MCP) 仕様
- MCP SDK (TypeScript/Python等)
- 各種MCPホスト（Claude Desktop, VS Code, GitHub Copilot CLI, Visual Studio）

## 前提知識

- Model Context Protocol (MCP)の基本概念（クライアント・サーバーアーキテクチャ、ツール・リソース・プロンプトの違い）
- MCPホスト（Claude Desktop, VS Code, GitHub Copilot等）の使用経験
- Azure/Microsoft 365の基本サービス理解（必要に応じてAzure subscription, M365 tenant）
- JSON設定ファイル編集、環境変数・認証の基礎知識
- （開発者向け）TypeScript/Python等のMCP SDK、npm/pip等パッケージマネージャ使用経験

## 根拠

> "Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to large language models (LLMs). It allows AI applications to connect with various data sources and tools in a consistent manner"

> "MCP Hosts: Applications like AI assistants or IDEs that initiate connections. MCP Clients: Connectors within the host application that maintain 1:1 connections with servers. MCP Servers: Services that provide context and capabilities through the standardized MCP"

> "Get started with the Azure plugin, which connects GitHub Copilot CLI or Claude Code to your Azure account. /plugin marketplace add microsoft/skills, /plugin install azure-skills@skills"
