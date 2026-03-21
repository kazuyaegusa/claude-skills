# Apps Builderでウィジェットをローカルエミュレートする

> ChatGPT appsやMCP appsのウィジェットをローカル環境で表示・操作テストする

- 出典: https://github.com/MCPJam/inspector
- 投稿者: MCPJam
- カテゴリ: dev-tool

## なぜ使うのか

ngrokやChatGPTサブスクリプションなしで、開発中のウィジェットの動作を即座に確認するため

## いつ使うのか

ChatGPT Apps SDKやMCP ext-appsのUI実装を開発・デバッグする時

## やり方

1. MCPJam InspectorのApps Builderタブを開く
2. MCPサーバーに接続
3. ツールを手動実行するか、LLMとチャットしてウィジェットを表示
4. エミュレーターでデスクトップ/タブレット/モバイルビューを切り替え
5. JSON-RPCメッセージと`window.openai`メッセージをログで確認
6. ライト/ダークモード、ロケール変更、CSPパーミッションをテスト

### 入力

- 開発中のMCPサーバー（ChatGPTアプリまたはMCP拡張アプリ対応）
- ウィジェット表示を行うツール実装

### 出力

- 各デバイスサイズでレンダリングされたウィジェット
- JSON-RPCおよびwindow.openai APIの通信ログ

## 使うツール・ライブラリ

- MCPJam Inspector Apps Builder
- ChatGPT Apps SDK API（widgetState, callTool, structuredContent等）
- MCP ext-apps API（tools/call, ui/initialize等）

## 前提知識

- Node.js 20以上の基礎知識とインストール済み環境
- TypeScript 5以上の基本的な理解
- MCP（Model Context Protocol）の基本概念
- ChatGPT Apps SDKまたはMCP ext-appsの基礎知識（アプリ開発の場合）
- OAuthの基本フロー理解（OAuth実装をテストする場合）

## 根拠

> 「No more ngrok or ChatGPT subscription needed. MCPJam is the fastest way to iterate on any MCP project.」

> 「npx @mcpjam/inspector@latest」

> 「Local development for ChatGPT Apps SDK support. Full support for the `windows.openai` API: `widgetState`, `callTool`, `structuredContent`, `sendFollowUpMessage`, `displayMode`, CSP, and more.」
