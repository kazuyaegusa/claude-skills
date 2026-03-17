# IDE拡張とMCPサーバーを1クリックインストール可能にする

> VS Code/Visual Studio/IntelliJ用のインストールリンク（vscode:mcp/install?...形式）を提供し、ユーザーがREADMEのバッジクリックだけでMCPサーバーを導入できるようにする

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: prompt-engineering

## なぜ使うのか

手動設定（JSON編集、コマンド実行）はエラーが発生しやすく、導入障壁が高い。1クリックリンクで自動設定すれば、開発者のオンボーディング時間を劇的に短縮できる

## いつ使うのか

MCPサーバーを公開する際、ユーザー体験を最大化したいとき

## やり方

1. MCPサーバーの設定情報（name, type, command/url, args, inputs等）をJSON定義
2. URLエンコードして`vscode:mcp/install?{...}`形式のリンク生成
3. README.mdにバッジ形式（shields.io等）で埋め込み
4. ユーザーがクリックするとVS Codeが起動し、設定ダイアログ表示
5. 必要に応じてinput（tenant ID等）をプロンプト
6. 自動的にmcp_settings.jsonに追記・サーバー起動

### 入力

- MCPサーバーのメタデータ（name, type, command, args, url等）
- 必要な環境変数・認証情報の入力定義

### 出力

- 1クリックインストールURL
- READMEバッジ（VS Code, VS Code Insiders, Visual Studio, IntelliJ, Eclipse等）

## 使うツール・ライブラリ

- VS Code URL scheme (vscode://, vscode-insiders://)
- Visual Studio URL scheme
- shields.io（バッジ生成）

## コード例

```
# インストールURL例（Azure DevOps MCP）
https://insiders.vscode.dev/redirect/mcp/install?name=ado&type=stdio&command=npx&args=%5B%22-y%22%2C%22%40azure-devops%2Fmcp%22%2C%22%24%7Binput%3Aado_org%7D%22%5D&inputs=%5B%7B%22id%22%3A%22ado_org%22%2C%22type%22%3A%22promptString%22%2C%22description%22%3A%22Azure%20DevOps%20organization%20name%20(e.g.%20contoso)%22%7D%5D

# バッジMarkdown
[![Install in VS Code](https://img.shields.io/badge/VS_Code-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect?url=vscode:mcp/install?...)
```

## 前提知識

- Model Context Protocol (MCP)の基本概念（クライアント・サーバーアーキテクチャ、ツール・リソース・プロンプトの違い）
- MCPホスト（Claude Desktop, VS Code, GitHub Copilot等）の使用経験
- Azure/Microsoft 365の基本サービス理解（必要に応じてAzure subscription, M365 tenant）
- JSON設定ファイル編集、環境変数・認証の基礎知識
- （開発者向け）TypeScript/Python等のMCP SDK、npm/pip等パッケージマネージャ使用経験
