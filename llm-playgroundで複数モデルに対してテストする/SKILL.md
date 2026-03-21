# LLM Playgroundで複数モデルに対してテストする

> 開発中のMCPサーバーを複数のLLMモデル（GPT-5, Claude Sonnet, Gemini 2.5等）で動作検証する

- 出典: https://github.com/MCPJam/inspector
- 投稿者: MCPJam
- カテゴリ: prompt-engineering

## なぜ使うのか

異なるLLMでの互換性とツール呼び出しの挙動を確認し、トークン使用量を把握するため

## いつ使うのか

MCPサーバーが複数のLLMで正しく動作するか検証したい時、またはトークン効率を最適化したい時

## やり方

1. MCPJam InspectorのLLM Playgroundを開く
2. MCPサーバーを接続
3. テストしたいLLMモデルを選択（無料提供のフロンティアモデルまたは自分のAPIキー）
4. プロンプトを入力してMCPツールを呼び出させる
5. 応答、ツール実行結果、トークン使用量を確認
6. 必要に応じて別のモデルで同じテストを実行

### 入力

- MCPサーバー
- テスト用プロンプト
- （オプション）自分のLLM APIキー

### 出力

- 各LLMモデルでの応答結果
- ツール呼び出しログ
- トークン使用量統計

## 使うツール・ライブラリ

- MCPJam Inspector LLM Playground
- GPT-5, Claude Sonnet, Gemini 2.5等の各種LLM API

## 前提知識

- Node.js 20以上の基礎知識とインストール済み環境
- TypeScript 5以上の基本的な理解
- MCP（Model Context Protocol）の基本概念
- ChatGPT Apps SDKまたはMCP ext-appsの基礎知識（アプリ開発の場合）
- OAuthの基本フロー理解（OAuth実装をテストする場合）

## 根拠

> 「No more ngrok or ChatGPT subscription needed. MCPJam is the fastest way to iterate on any MCP project.」

> 「npx @mcpjam/inspector@latest」

> 「We provide frontier models such as GPT-5 and Claude Sonnet for free, or bring your own API key.」
