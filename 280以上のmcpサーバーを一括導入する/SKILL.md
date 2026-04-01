# 280以上のMCPサーバーを一括導入する

> Activepiecesが提供する280以上のpiece（Google Sheets、OpenAI、Discord、RSS等）をMCPサーバーとしてClaude Desktop等に一括導入する

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: agent-orchestration

## なぜ使うのか

個別にMCPサーバーを探して設定する手間を省き、幅広いサービス統合を即座に利用可能にする。コミュニティの60%がcontributeしているエコシステムの恩恵を受けられる

## いつ使うのか

LLMエージェントで多様な外部サービスと連携したい場合。MCPサーバーを個別に構築・管理するリソースがない場合

## やり方

1. Activepiecesの公式リポジトリまたはnpmjs.comから利用可能なpieceリストを確認（https://www.activepieces.com/pieces）
2. 必要なpieceをActivepiecesインスタンスに追加（セルフホストの場合は設定ファイル、クラウドの場合はUI経由）
3. Claude Desktop等のMCP client設定ファイルに、利用したいpieceのMCPサーバー情報を追加
4. LLMツール再起動後、追加したサービス統合が利用可能

### 入力

- Activepiecesインスタンス（セルフホストまたはクラウド）
- Claude Desktop / Cursor / Windsurf等のMCP client
- 利用したいサービスのAPI認証情報

### 出力

- 280以上のサービスと連携可能なLLMエージェント環境
- 統一されたワークフロー自動化とMCP統合

## 使うツール・ライブラリ

- Activepieces
- Claude Desktop
- Cursor
- Windsurf

## 前提知識

- TypeScriptの基本知識（piece開発時）
- Docker/Kubernetesの基本（セルフホスト時）
- MCP（Model Context Protocol）の概念理解
- npmパッケージ管理の基礎
- REST API / Webhook の基本知識

## 根拠

> When you contribute pieces to Activepieces they become automatically available as MCP servers that you can use with LLMs through Claude Desktop, Cursor or Windsurf!

> Largest open source MCP toolkit: All our pieces (280+) are available as MCP that you can use with LLMs on Claude Desktop, Cursor or Windsurf.
