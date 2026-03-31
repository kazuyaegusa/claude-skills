# MCPによる永続的ブラウザコンテキスト管理

> Model Context Protocol (MCP)サーバーを使ってブラウザ自動化を行い、永続的な状態と豊富なイントロスペクションを活用する

- 出典: https://github.com/microsoft/playwright-mcp
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

探索的自動化、セルフヒーリングテスト、長時間実行される自律ワークフローでは、ページ構造に対する反復的推論と継続的なブラウザコンテキストの維持がトークンコストの懸念を上回る価値を持つ。MCPは構造化されたアクセシビリティスナップショットとステートフルな接続を提供する。

## いつ使うのか

探索的な自動化、ページ構造の反復的分析が必要な場合、セルフヒーリングテスト、長時間実行される自律ワークフローなど、継続的なブラウザコンテキストの維持が重要な場合。

## やり方

1. Playwright MCPサーバーを各MCPクライアント（VS Code, Claude Desktop, Cursor等）の設定に追加
2. 標準設定（`npx @playwright/mcp@latest`）またはカスタム設定を使用
3. LLMがMCPツール（browser_navigate, browser_click, browser_snapshot等）を呼び出してブラウザを操作
4. アクセシビリティツリーを使った構造化スナップショットで要素を特定（スクリーンショット不要）
5. 永続的なブラウザセッションで状態を維持

### 入力

- MCP対応クライアント（VS Code, Claude Code, Cursor等）
- Playwright MCPサーバー設定
- Node.js 18以上

### 出力

- 構造化されたアクセシビリティスナップショット
- 永続的なブラウザセッション
- 豊富なイントロスペクション機能

## 使うツール・ライブラリ

- @playwright/mcp
- Node.js
- MCP対応クライアント

## コード例

```
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
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

> 「This makes CLI + SKILLs better suited for high-throughput coding agents that must balance browser automation with large codebases, tests, and reasoning within limited context windows.」

> 「Fast and lightweight. Uses Playwright's accessibility tree, not pixel-based input.」

> 「LLM-friendly. No vision models needed, operates purely on structured data.」
