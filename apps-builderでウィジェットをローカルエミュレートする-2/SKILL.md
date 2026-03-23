# Apps Builderでウィジェットをローカルエミュレートする

> ChatGPT apps/MCP appsのウィジェットUIをローカル環境でリアルタイムプレビュー・テストする

- 出典: https://github.com/MCPJam/inspector
- 投稿者: MCPJam
- カテゴリ: dev-tool

## なぜ使うのか

ngrokやChatGPT有料サブスクなしで、デバイス種別・ロケール・テーマ・タッチ操作等を即座に検証できる

## いつ使うのか

ChatGPT Apps SDKやMCP ext-appsでウィジェットを実装している時、特にレスポンシブ対応やCSP設定を確認したい時

## やり方

1. MCPJam InspectorのApps Builder画面を開く
2. 対象のMCPサーバーに接続
3. ツールを手動実行するか、LLMとチャットしてウィジェット表示をトリガー
4. エミュレーターのデバイス種別（Desktop/Tablet/Mobile）を切り替え
5. locale、light/dark mode、CSP権限、safe area insetsを変更してテスト
6. JSON-RPC/window.openaiメッセージログで通信内容を確認

### 入力

- ChatGPT Apps SDK対応MCPサーバー、またはMCP ext-apps（SEP-1865）実装
- widgetState、structuredContentを返すツール定義

### 出力

- 各デバイス・設定でのウィジェット表示
- JSON-RPC/window.openai通信ログ

## 使うツール・ライブラリ

- MCPJam Inspector Apps Builder
- windows.openai API
- MCP ext-apps JSON-RPC (tools/call, ui/initialize, ui/message等)

## 前提知識

- MCPサーバーの基本概念（tools/resources/prompts）
- ChatGPT Apps SDKまたはMCP ext-apps（SEP-1865）の仕様理解
- OAuth 2.0の基本フロー（authorization code grant等）
- Node.js 20以上の実行環境（npx使用時）
- JSON-RPC通信の基礎知識

## 根拠

> 「No more ngrok or ChatGPT subscription needed. MCPJam is the fastest way to iterate on any MCP project.」

> 「npx @mcpjam/inspector@latest」

> 「Build and test your apps with a full widget emulator, chat with any LLM, and inspect your server's tools, resources, prompts, and OAuth flows.」

> 「Test your app's locale change, CSP permissions, light / dark mode, hover & touch, and safe area insets.」

> 「docker run -p 6274:6274 mcpjam/mcp-inspector」
