# VS Code拡張機能としてMCPサーバーをワンクリックインストールする

> 公式READMEのINSTALLバッジリンク（vscode:extension/...）をクリックし、MCPサーバーをVS Codeに直接追加する

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動の設定ファイル編集やCLIコマンド実行を不要にし、非技術者でも公式MCPサーバーを即座に利用可能にするため

## いつ使うのか

Azure MCP・GitHub MCP・Microsoft 365 MCP等、公式提供のサーバーを初めて導入する時

## やり方

1. README内の対象MCPサーバーの行を確認
2. INSTALLカラムのVS Codeバッジをクリック
3. ブラウザが `vscode://extension/...` URLを開き、VS Codeが起動
4. 拡張機能インストールダイアログで承認
5. VS Code再起動後、MCPクライアント（Claude Code等）から当該サーバーが利用可能になる

### 入力

- VS Codeがインストール済みの環境
- 対象MCPサーバーのREADMEリンク

### 出力

- VS Codeに統合されたMCPサーバー
- Claude Code等のMCPクライアントから呼び出し可能なツール群

## 使うツール・ライブラリ

- VS Code
- vscode:extensionプロトコルハンドラ

## 前提知識

- MCPプロトコルの基本概念（Host/Client/Serverアーキテクチャ）
- VS Code/Claude Code/Copilot CLI等のMCPクライアントツール
- Azure CLI / Microsoft 365アカウント / GitHubアカウント（接続先サービスに応じて）
- Node.js/Python環境（ローカル実行型MCPサーバーを使う場合）
