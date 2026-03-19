# Microsoft Graph API統合MCPサーバーのパターン

> Microsoft 365の各サービス(Calendar, Mail, Teams, Word等)をMicrosoft Graph API経由で操作するMCPサーバーを、Remote型エンドポイント(https://agent365.svc.cloud.microsoft/agents/tenants/{tenant_id}/servers/mcp_*)として提供する

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: agent-orchestration

## なぜ使うのか

M365データへのアクセスはマルチテナント認証・権限管理・監査ログが必須なため、クライアント側で認証情報を管理するよりもサーバー側で集中管理する方が安全かつスケーラブル。また、Graph APIの共通パターン(ページネーション、フィルタリング、トークン最適化)を各MCPサーバーで再実装するのを避けるため。

## いつ使うのか

M365データ(メール、カレンダー、Teams、SharePoint等)にLLMからアクセスさせたいが、認証・権限管理・監査をサーバー側で集中管理したい場合

## やり方

1. テナントIDをパスパラメータとして受け取るHTTPSエンドポイント(例: `https://agent365.svc.cloud.microsoft/agents/tenants/{tenant_id}/servers/mcp_CalendarTools`)を作成
2. Microsoft Entra ID(旧Azure AD)での認証を実装(OAuthトークン検証)
3. Microsoft Graph APIの該当エンドポイント(例: CalendarToolsなら`/me/calendar/events`)をラップしたMCP Toolsを定義
4. サーバー側でページネーション・フィルタリング・トークン最適化を実装(LLMへの応答サイズを削減)
5. VS Code等のインストールURLに`inputs`フィールドでテナントIDの入力を促す設定を含める
6. ドキュメント・トラブルシューティングガイドをbap-microsoft/MCP-Platformリポジトリで公開

### 入力

- Microsoft Entra tenant ID
- OAuthアクセストークン(認証済みユーザー)
- Graph APIクエリパラメータ(日付範囲、検索キーワード等)

### 出力

- MCP Tools経由でアクセス可能なM365データ(イベント、メール、チャット等)
- ページネーション・フィルタリング済みの結果

## 使うツール・ライブラリ

- Microsoft Graph API
- Microsoft Entra ID (認証)
- MCP SDK
- ASP.NET Core (推測、投稿に明記なし)

## コード例

```
// インストールURL例(Calendar Tools)
https://vscode.dev/redirect/mcp/install?name=agent365-calendartools&config={"type":"http","url":"https://agent365.svc.cloud.microsoft/agents/tenants/${input:tenant_id}/servers/mcp_CalendarTools"}&inputs=[{"id":"tenant_id","type":"promptString","description":"Microsoft Entra tenant ID (GUID)"}]
```

## 前提知識

- MCP (Model Context Protocol)の基本概念(Host, Client, Server, Tools, Resources)の理解
- VS Code/Visual Studio等のIDEでのMCP設定方法の基礎知識
- Microsoft Graph APIの基本的な知識(認証、スコープ、エンドポイント構造)
- Azure/M365のテナントID・組織名等の基本的な概念の理解
- npmまたはPython(uvx)を使ったパッケージインストールの経験

## 根拠

> "This repository contains core libraries, test frameworks, engineering systems, pipelines, and tooling for Microsoft MCP Server contributors to unify engineering investments; and reduce duplication and divergence"

> "CATEGORY: PRODUCTIVITY, TYPE: REMOTE - https://agent365.svc.cloud.microsoft/agents/tenants/{tenant_id}/servers/mcp_CalendarTools" (Microsoft 365 Calendar)

> "Calendar tools for creating, updating, deleting events, managing invites, and checking availability. Integrates with Microsoft Graph Calendar APIs."

> "inputs=[{\"id\":\"tenant_id\",\"type\":\"promptString\",\"description\":\"Microsoft Entra tenant ID (GUID)\"}]"
