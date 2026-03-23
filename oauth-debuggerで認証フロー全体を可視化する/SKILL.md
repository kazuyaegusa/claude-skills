# OAuth Debuggerで認証フロー全体を可視化する

> MCPサーバーのOAuth実装を各ステップごとに詳細表示し、ネットワークメッセージを検査する

- 出典: https://github.com/MCPJam/inspector
- 投稿者: MCPJam
- カテゴリ: dev-tool

## なぜ使うのか

OAuth handshakeは複雑で、どこで失敗したか特定しにくい。各ステップのリクエスト/レスポンスを見ることで、実装ミスを即座に発見できる

## いつ使うのか

MCPサーバーにOAuth認証を実装・デバッグする時、特に異なるプロトコルバージョン間の挙動差異を確認したい時

## やり方

1. MCPJam InspectorでOAuth Debugger画面を開く
2. MCPサーバーのOAuth設定（プロトコルバージョン: 03-26/06-18/11-25、client pre-registration/DCR/CIMDのいずれか）を入力
3. 認証フローを開始
4. 各ステップ（authorization request、token exchange、refresh等）のHTTPリクエスト/レスポンスをビジュアル表示で確認
5. エラーがあればその段階で詳細を調査

### 入力

- OAuth対応MCPサーバー
- 認可エンドポイント・トークンエンドポイントURL
- client IDまたはDCR/CIMD設定

### 出力

- 各OAuthステップのHTTPリクエスト/レスポンス詳細
- 認証成功/失敗の診断結果

## 使うツール・ライブラリ

- MCPJam Inspector OAuth Debugger
- OAuth 2.0仕様（03-26, 06-18, 11-25対応）
- DCR (Dynamic Client Registration)
- CIMD (Client ID Metadata Documents)

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

> 「Debug your MCP server's OAuth implementation at every step. Visually inspect every network message. Supports all protocol versions (03-26, 06-18, and 11-25). Support for client pre-registration, DCR, and CIMD.」

> 「docker run -p 6274:6274 mcpjam/mcp-inspector」
