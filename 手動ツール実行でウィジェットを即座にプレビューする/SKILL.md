# 手動ツール実行でウィジェットを即座にプレビューする

> LLMを介さず、MCPツールを直接実行してウィジェット/リソース/プロンプトの表示を確認する

- 出典: https://github.com/MCPJam/inspector
- 投稿者: MCPJam
- カテゴリ: prompt-engineering

## なぜ使うのか

LLMの応答待ちやプロンプト調整なしで、ツールの出力（特にwidgetState/structuredContent）を即座に検証できる

## いつ使うのか

ツール単体の動作確認時、ウィジェットUIの見た目を素早く調整したい時

## やり方

1. MCPJam InspectorでMCPサーバーに接続
2. Tools/Resources/Promptsセクションでテスト対象を選択
3. 必要なパラメータを入力
4. 「Invoke」ボタンで手動実行
5. Apps Builderでウィジェット表示を即座に確認
6. JSON-RPC通信ログで詳細を検証

### 入力

- MCPサーバーのツール/リソース/プロンプト定義
- ツール実行に必要なパラメータ

### 出力

- ツールのレスポンス（JSON）
- ウィジェット表示（Apps Builder）
- JSON-RPC通信ログ

## 使うツール・ライブラリ

- MCPJam Inspector MCP Tools/Resources/Prompts UI

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

> 「docker run -p 6274:6274 mcpjam/mcp-inspector」
