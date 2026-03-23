# npxで即座にMCPJam Inspectorを起動する

> ローカルインストール不要で、最新版のMCPJam Inspectorをコマンド1つで起動する

- 出典: https://github.com/MCPJam/inspector
- 投稿者: MCPJam
- カテゴリ: ui-ux

## なぜ使うのか

グローバルインストールやバージョン管理の手間を省き、常に最新版を使用できる

## いつ使うのか

MCP開発を始める時、または他のマシンで一時的にテストしたい時

## やり方

1. ターミナルで `npx @mcpjam/inspector@latest` を実行
2. 自動的にポート6274でサーバーが起動
3. ブラウザでインターフェースにアクセス

### 入力

- Node.js 20以上がインストールされた環境

### 出力

- localhost:6274で動作するMCPJam Inspector UI

## 使うツール・ライブラリ

- npx
- @mcpjam/inspector

## コード例

```
npx @mcpjam/inspector@latest
```

## 前提知識

- MCPサーバーの基本概念（tools/resources/prompts）
- ChatGPT Apps SDKまたはMCP ext-apps（SEP-1865）の仕様理解
- OAuth 2.0の基本フロー（authorization code grant等）
- Node.js 20以上の実行環境（npx使用時）
- JSON-RPC通信の基礎知識
