# IDEワンクリックインストールURLの生成

> VS Code/Visual Studio等のIDEが直接解釈できるMCPインストールプロトコルURLを生成し、バッジボタンとしてREADMEに埋め込む

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: prompt-engineering

## なぜ使うのか

開発者が手動でJSON設定ファイルを編集する手間を省き、1クリックでMCPサーバーをIDEに追加できるようにすることで、導入ハードルを大幅に下げるため。

## いつ使うのか

MCPサーバーをエンドユーザーに配布し、IDE設定の手動編集なしでインストールさせたい場合

## やり方

1. VS Code用: `vscode:mcp/install?{JSON_CONFIG}` または `vscode:extension/{EXTENSION_ID}` 形式のURLを作成
2. VS Code Insiders用: 同じURLで`vscode-insiders:`スキームに変更し、`quality=insiders`パラメータを追加
3. Visual Studio用: `https://aka.ms/vs/mcp-install?{JSON_CONFIG}` 形式のURLを作成
4. JSON_CONFIGには`{"name":"server_name","type":"stdio|http","command":"...","args":[...]}` を含める
5. 動的入力が必要な場合、`inputs`配列に`{"id":"param_name","type":"promptString","description":"説明"}`を追加
6. Markdown badgeとして`[![Install in VS Code](badge_url)](install_url)`形式で埋め込む

### 入力

- MCPサーバーのインストール設定(type, command, args等)
- 動的パラメータ(テナントID、組織名等)の入力定義

### 出力

- 各IDE向けのワンクリックインストールURL
- Markdown badge付きインストールボタン

## 使うツール・ライブラリ

- VS Code MCP Install Protocol
- Visual Studio MCP Install Protocol
- URL encoding
- shields.io (badge生成)

## コード例

```
// VS Codeインストール例
https://vscode.dev/redirect?url=vscode:mcp/install?%7B%22name%22%3A%22ado%22%2C%22type%22%3A%22stdio%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure-devops%2Fmcp%22%2C%22%24%7Binput%3Aado_org%7D%22%5D%2C%22inputs%22%3A%5B%7B%22id%22%3A%22ado_org%22%2C%22type%22%3A%22promptString%22%2C%22description%22%3A%22Azure%20DevOps%20organization%20name%22%7D%5D%7D
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
