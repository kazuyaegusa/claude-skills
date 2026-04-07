# 複数MCPクライアントに標準設定で配布する

> VS Code, Cursor, Claude Desktop, Goose等、10種類以上のMCPクライアントに対して標準的なJSON設定を提供し、ワンクリックインストールリンクを併記する

- 出典: https://github.com/microsoft/playwright-mcp
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

MCPサーバーの利用障壁を下げ、クライアント間の設定差異を吸収して広範なエコシステムでの採用を促進する

## いつ使うのか

MCPサーバーを公開し、多様なクライアント環境での採用を促進する場合

## やり方

1. 標準設定（command: npx, args: [@playwright/mcp@latest]）を定義
2. 各MCPクライアント用のドキュメントセクションを作成
3. ワンクリックインストール用のディープリンクを生成（vscode:mcp/install等）
4. CLI経由のインストールコマンドも併記（claude mcp add等）

### 入力

- MCPサーバーのnpmパッケージ
- 各クライアントのMCP設定仕様

### 出力

- クライアント別インストール手順
- ディープリンク
- 標準JSON設定

## 使うツール・ライブラリ

- npx
- 各MCPクライアントCLI

## コード例

```
# VS Code CLI
code --add-mcp '{"name":"playwright","command":"npx","args":["@playwright/mcp@latest"]}'

# Claude Code CLI
claude mcp add playwright npx @playwright/mcp@latest
```

## 前提知識

- Model Context Protocol（MCP）の基本概念
- Playwrightの基本的な使い方
- コーディングエージェント（Claude Code/Copilot等）のアーキテクチャ
- トークン消費とコンテキストウィンドウの制約に関する理解
- アクセシビリティツリーの概念

## 根拠

> 「Modern coding agents increasingly favor CLI–based workflows exposed as SKILLs over MCP because CLI invocations are more token-efficient」（READMEより）

> 「they avoid loading large tool schemas and verbose accessibility trees into the model context」（MCPのトークンコスト説明）

> 「MCP remains relevant for specialized agentic loops that benefit from persistent state, rich introspection, and iterative reasoning over page structure」（MCP適用場面の明示）
