# Dockerでポータブルなテスト環境を構築する

> MCPJam InspectorをDockerコンテナで起動し、チーム全体で統一されたテスト環境を提供する

- 出典: https://github.com/MCPJam/inspector
- 投稿者: MCPJam
- カテゴリ: automation-pipeline

## なぜ使うのか

ローカル環境の差異（Node.jsバージョン、依存関係等）を排除し、CI/CDやチーム開発で再現性の高いテストを実現する

## いつ使うのか

CI/CD環境でMCPサーバーのE2Eテストを自動化したい時、またはチーム全員が同一バージョンのInspectorを使いたい時

## やり方

1. Dockerがインストールされた環境で以下を実行
   `docker run -p 6274:6274 mcpjam/mcp-inspector`
2. ポート6274でMCPJam Inspectorが起動
3. ブラウザでlocalhost:6274にアクセス

### 入力

- Docker環境

### 出力

- コンテナ化されたMCPJam Inspector（ポート6274）

## 使うツール・ライブラリ

- Docker
- mcpjam/mcp-inspector イメージ

## コード例

```
docker run -p 6274:6274 mcpjam/mcp-inspector
```

## 前提知識

- MCPサーバーの基本概念（tools/resources/prompts）
- ChatGPT Apps SDKまたはMCP ext-apps（SEP-1865）の仕様理解
- OAuth 2.0の基本フロー（authorization code grant等）
- Node.js 20以上の実行環境（npx使用時）
- JSON-RPC通信の基礎知識

## 根拠

> 「No more ngrok or ChatGPT subscription needed. MCPJam is the fastest way to iterate on any MCP project.」

> 「npx @mcpjam/inspector@latest」

> 「docker run -p 6274:6274 mcpjam/mcp-inspector」
