# MCPサーバーのマルチクライアント対応設定

> Playwright MCPサーバーを複数のMCPクライアント（VS Code, Claude Desktop, Cursor, Windsurf等）で共通の設定方法で導入する

- 出典: https://github.com/microsoft/playwright-mcp
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

各クライアントで設定方法が異なる可能性があるが、標準設定を使うことで統一的な導入が可能になり、ドキュメント参照や移行が容易になる。

## いつ使うのか

複数のMCPクライアントでPlaywright自動化を利用したい場合、チーム内で統一的な設定を共有したい場合。

## やり方

1. 各クライアントのMCP設定ファイルまたはUIを開く
2. 標準設定を追加: command="npx", args=["@playwright/mcp@latest"]
3. VS Code/Cursor等ではワンクリックインストールボタンを使用可能
4. Claude CodeではCLI: `claude mcp add playwright npx @playwright/mcp@latest`
5. クライアントを再起動してMCPサーバーを有効化

### 入力

- MCP対応クライアント
- Node.js 18以上

### 出力

- 有効化されたPlaywright MCPサーバー
- ブラウザ自動化ツールへのアクセス

## 使うツール・ライブラリ

- npx
- @playwright/mcp

## コード例

```
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

## 前提知識

- Model Context Protocol (MCP)の基本概念
- Playwrightブラウザ自動化フレームワークの基礎知識
- LLMエージェントのコンテキストウィンドウとトークン制限の理解
- CLIとSKILLSの概念（コーディングエージェント向け）
- Node.jsとnpxの基本的な使い方

## 根拠

> 「Modern coding agents increasingly favor CLI–based workflows exposed as SKILLs over MCP because CLI invocations are more token-efficient: they avoid loading large tool schemas and verbose accessibility trees into the model context」

> 「MCP remains relevant for specialized agentic loops that benefit from persistent state, rich introspection, and iterative reasoning over page structure」

> 「Fast and lightweight. Uses Playwright's accessibility tree, not pixel-based input.」
