# Local型とRemote型MCPサーバーの使い分け

> MCPサーバーをLocal型(ローカルプロセスとして起動、stdio通信)とRemote型(HTTPSエンドポイント経由、クラウドホスト)の2種類に分け、用途に応じて選択させる

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: agent-orchestration

## なぜ使うのか

Local型は認証情報を開発者のマシンに保持でき、Remote型はサーバー側で認証・スケーリング・ログ管理が可能。セキュリティ要件・運用負荷・マルチテナント対応の有無に応じて最適なアーキテクチャを提供するため。

## いつ使うのか

セキュリティ要件が高く認証情報をローカル管理したい場合はLocal型、マルチテナント対応やサーバー側でのログ・監視が必要な場合はRemote型を選択

## やり方

1. **Local型の場合**: npmパッケージ(例: @azure-devops/mcp)またはuvx(Python)でインストール可能にし、`{"type":"stdio","command":"npx","args":["-y","@azure-devops/mcp"]}` 形式の設定をVS Code等に渡す
2. **Remote型の場合**: HTTPSエンドポイント(例: https://agent365.svc.cloud.microsoft/agents/tenants/{tenant_id}/servers/mcp_CalendarTools)を公開し、`{"type":"http","url":"https://..."}` 形式で設定
3. Remote型ではテナントID等のパラメータを`inputs`フィールドで動的に入力させる(例: `{"id":"tenant_id","type":"promptString"}`)
4. インストールボタンのURLに`quality=insiders`パラメータを追加することでVS Code Insidersにも対応

### 入力

- Local型: npmパッケージまたはPython実行可能ファイル、開発者ローカルの認証情報
- Remote型: HTTPSエンドポイントURL、テナントID等の動的パラメータ

### 出力

- Local型: ローカルプロセスとして起動されたMCPサーバー(stdio通信)
- Remote型: クラウドでホストされたMCPエンドポイント(HTTPS通信)

## 使うツール・ライブラリ

- npx (Node.js)
- uvx (Python)
- VS Code MCP Extension
- Microsoft Graph API (Remote型で使用)
- Azure Active Directory (認証)

## コード例

```
// Local型インストール例
{
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "@azure-devops/mcp", "${input:ado_org}"]
}

// Remote型インストール例
{
  "type": "http",
  "url": "https://agent365.svc.cloud.microsoft/agents/tenants/${input:tenant_id}/servers/mcp_CalendarTools"
}
```

## 前提知識

- MCP (Model Context Protocol)の基本概念(Host, Client, Server, Tools, Resources)の理解
- VS Code/Visual Studio等のIDEでのMCP設定方法の基礎知識
- Microsoft Graph APIの基本的な知識(認証、スコープ、エンドポイント構造)
- Azure/M365のテナントID・組織名等の基本的な概念の理解
- npmまたはPython(uvx)を使ったパッケージインストールの経験

## 根拠

> "Azure MCP Server can be used alone or with the GitHub Copilot for Azure extension in VS Code."

> "Install buttons: [![Install Azure MCP in VS Code](badge)](url)"
