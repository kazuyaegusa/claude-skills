# JSON-RPCメッセージを詳細監視する

> MCPサーバーとクライアント間のすべてのJSON-RPC通信を記録・検査する

- 出典: https://github.com/MCPJam/inspector
- 投稿者: MCPJam
- カテゴリ: prompt-engineering

## なぜ使うのか

ツール、リソース、プロンプトの呼び出しが正しく行われているか、エラーの原因を特定するため

## いつ使うのか

MCPツールが期待通りに動作しない時、またはプロトコル実装を検証する時

## やり方

1. MCPJam Inspectorで任意の機能（Tools, Resources, Prompts等）を実行
2. Logsタブまたは各機能画面のメッセージビューを開く
3. JSON-RPCリクエスト/レスポンスの生データを確認
4. エラーメッセージやパラメータの不整合を特定
5. 必要に応じてサーバー実装を修正

### 入力

- 動作中のMCPサーバー
- 実行したいMCP操作（ツール呼び出し、リソース取得等）

### 出力

- タイムスタンプ付きJSON-RPCメッセージログ
- エラーの詳細情報

## 使うツール・ライブラリ

- MCPJam Inspector
- MCP JSON-RPC protocol

## 前提知識

- Node.js 20以上の基礎知識とインストール済み環境
- TypeScript 5以上の基本的な理解
- MCP（Model Context Protocol）の基本概念
- ChatGPT Apps SDKまたはMCP ext-appsの基礎知識（アプリ開発の場合）
- OAuthの基本フロー理解（OAuth実装をテストする場合）

## 根拠

> 「No more ngrok or ChatGPT subscription needed. MCPJam is the fastest way to iterate on any MCP project.」

> 「npx @mcpjam/inspector@latest」
