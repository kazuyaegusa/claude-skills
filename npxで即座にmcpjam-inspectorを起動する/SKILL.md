# npxで即座にMCPJam Inspectorを起動する

> インストール不要でMCPJam Inspectorをローカルで起動し、MCP開発環境を立ち上げる

- 出典: https://github.com/MCPJam/inspector
- 投稿者: MCPJam
- カテゴリ: ui-ux

## なぜ使うのか

グローバルインストールや環境構築の手間を省き、最新版を常に使えるようにするため

## いつ使うのか

MCPサーバーやChatGPTアプリの開発を始める時、または最新機能を試したい時

## やり方

1. ターミナルで `npx @mcpjam/inspector@latest` を実行
2. 自動的にローカルサーバーが起動（デフォルトポート6274）
3. ブラウザでインスペクターUIにアクセス

### 入力

- Node.js 20以上がインストールされた環境

### 出力

- ローカルで動作するMCPJam Inspectorのウェブインターフェース

## 使うツール・ライブラリ

- @mcpjam/inspector（npm package）
- npx

## コード例

```
npx @mcpjam/inspector@latest
```

## 前提知識

- Node.js 20以上の基礎知識とインストール済み環境
- TypeScript 5以上の基本的な理解
- MCP（Model Context Protocol）の基本概念
- ChatGPT Apps SDKまたはMCP ext-appsの基礎知識（アプリ開発の場合）
- OAuthの基本フロー理解（OAuth実装をテストする場合）
