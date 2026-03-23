# LLM Playgroundで複数モデルに対してサーバーをテストする

> GPT-5、Claude Sonnet、Gemini 2.5等のフロンティアモデルを使い、MCPサーバーの応答を無料でテストする

- 出典: https://github.com/MCPJam/inspector
- 投稿者: MCPJam
- カテゴリ: prompt-engineering

## なぜ使うのか

本番環境で使われる複数のLLMに対して、ツール呼び出しやプロンプト応答が期待通りか検証する必要があるが、各APIキーを用意してテストするのは手間とコストがかかる

## いつ使うのか

MCPサーバーを複数LLMプロバイダーに対応させたい時、またはモデル間の挙動差異を比較検証したい時

## やり方

1. MCPJam InspectorのLLM Playgroundを開く
2. テスト対象のMCPサーバーに接続
3. モデル選択（GPT-5/Claude Sonnet/Gemini 2.5等）
4. チャットでサーバーのツール・プロンプトを実行
5. トークン使用量と応答品質を確認
6. 必要に応じて自分のAPIキーを設定して他モデルもテスト

### 入力

- MCPサーバー（tools/resources/prompts定義）
- （オプション）自分のLLM APIキー

### 出力

- 各LLMモデルでの応答結果
- トークン使用量統計

## 使うツール・ライブラリ

- MCPJam Inspector LLM Playground
- GPT-5
- Claude Sonnet
- Gemini 2.5

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
