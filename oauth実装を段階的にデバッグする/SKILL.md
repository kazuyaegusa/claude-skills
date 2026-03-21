# OAuth実装を段階的にデバッグする

> MCPサーバーのOAuth認証フローを各ステップごとに可視化・検証する

- 出典: https://github.com/MCPJam/inspector
- 投稿者: MCPJam
- カテゴリ: dev-tool

## なぜ使うのか

OAuth実装のどの段階で問題が起きているかを特定し、複数プロトコルバージョンの互換性を確保するため

## いつ使うのか

MCPサーバーにOAuth認証を実装・デバッグする時、または複数バージョンのサポートを確認する時

## やり方

1. MCPJam InspectorのOAuth Debuggerを開く
2. テストするOAuthプロトコルバージョン（03-26, 06-18, 11-25）を選択
3. 認証方式（client pre-registration, DCR, CIMD）を指定
4. OAuthフローを開始し、各ステップ（認可リクエスト、トークン交換等）を実行
5. 各ステップのHTTPリクエスト/レスポンス、JSON-RPCメッセージを確認
6. エラーがあればガイド付き説明で原因を特定

### 入力

- OAuth対応MCPサーバー
- OAuthプロバイダー設定（例: Stytch）

### 出力

- 各認証ステップの詳細ログ
- エラー箇所の特定と修正ガイド

## 使うツール・ライブラリ

- MCPJam Inspector OAuth Debugger
- Stytch（推奨OAuthプロバイダー）

## 前提知識

- Node.js 20以上の基礎知識とインストール済み環境
- TypeScript 5以上の基本的な理解
- MCP（Model Context Protocol）の基本概念
- ChatGPT Apps SDKまたはMCP ext-appsの基礎知識（アプリ開発の場合）
- OAuthの基本フロー理解（OAuth実装をテストする場合）

## 根拠

> 「No more ngrok or ChatGPT subscription needed. MCPJam is the fastest way to iterate on any MCP project.」

> 「npx @mcpjam/inspector@latest」

> 「Debug your MCP server's OAuth implementation at every step. Visually inspect every network message. Supports all protocol versions (03-26, 06-18, and 11-25). Support for client pre-registration, DCR, and CIMD.」
