# VS Code拡張の一括インストールリンクを提供する

> MCPサーバーのインストールをワンクリック化するため、vscode://mcp/install スキーマを使ったディープリンクをREADME/ドキュメントに埋め込む

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: infrastructure

## なぜ使うのか

ユーザーが手動で設定ファイルを編集する必要がなくなり、導入障壁が劇的に下がる。特に非技術ユーザーや初学者にとって重要

## いつ使うのか

MCPサーバーの利用者にセットアップ手順を簡略化したい場合。特にOSS公開時やドキュメント作成時

## やり方

1. インストール設定をJSON形式で定義（name, type, command/url, args, inputs等） 2. JSONをURLエンコード 3. `vscode://mcp/install?{encoded_json}` 形式のURLを生成 4. README.mdにバッジ形式でリンクを埋め込む 5. ユーザーがクリックすると VS Code が起動し、自動的にMCPサーバー設定が追加される

### 入力

- MCPサーバーの接続設定（JSON）
- 対象IDE（VS Code / VS Code Insiders / Visual Studio等）

### 出力

- クリック可能なインストールリンク（URLまたはバッジ画像）
- VS Code設定ファイルへの自動追記

## 使うツール・ライブラリ

- URLエンコーダー
- shields.io（バッジ画像生成）
- VS Code Deep Link API

## コード例

```
// インストールリンク生成例
const config = {
  name: "azure-mcp",
  type: "stdio",
  command: "npx",
  args: ["-y", "@azure/mcp-server"]
};
const encoded = encodeURIComponent(JSON.stringify(config));
const link = `https://vscode.dev/redirect?url=vscode:mcp/install?${encoded}`;

// Markdown埋め込み例
[![Install in VS Code](https://img.shields.io/badge/VS_Code-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect?url=vscode:mcp/install?%7B...%7D)
```

## 前提知識

- Model Context Protocol (MCP) の基本概念（Host / Client / Server アーキテクチャ）の理解
- VS Code / Visual Studio / Claude Desktop 等の MCP Host 対応アプリケーションの使用経験
- Microsoft Azure / Microsoft 365 / GitHub 等のサービスへのアクセス権限（該当サーバーを利用する場合）
- Node.js / Python / .NET 等のランタイム環境（Local型MCPサーバーを利用する場合）
- OAuth 2.0 / Microsoft Entra ID 等の認証フローの基礎知識（Remote型MCPサーバーを利用する場合）

## 根拠

> 「INSTALL: vscode.dev/redirect?url=vscode:extension/... (VS Code), vscode-insiders:extension/... (VS Code Insiders), aka.ms/vs/mcp-install?... (Visual Studio)」
