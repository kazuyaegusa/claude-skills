# MCPを永続状態管理・探索的自動化に使う

> ページ構造への反復的推論、セルフヒーリングテスト、長時間実行の自律ワークフロー等にはMCPサーバーを選択する

- 出典: https://github.com/microsoft/playwright-mcp
- 投稿者: microsoft
- カテゴリ: agent-orchestration

## なぜ使うのか

MCPは永続的な状態、豊富なイントロスペクション、ページ構造への反復的推論を提供し、継続的なブラウザコンテキスト維持がトークンコストを上回る場合に有効

## いつ使うのか

探索的自動化、セルフヒーリングテスト、長時間実行の自律ワークフローなど、継続的なブラウザコンテキスト維持が重要な場合

## やり方

1. MCPクライアント（Claude Desktop/Cursor/VS Code等）の設定ファイルにPlaywright MCPサーバーを追加
2. `npx @playwright/mcp@latest`で起動
3. エージェントがMCPツール（browser_snapshot, browser_click等）を呼び出してページ構造を解析
4. 反復的にページ状態を取得しながら自律的にワークフローを実行

### 入力

- MCPクライアント設定（JSON）
- Playwright MCPサーバー（@playwright/mcp）
- 対象ブラウザ

### 出力

- 永続的なブラウザセッション
- 構造化されたアクセシビリティスナップショット
- 反復的な推論結果

## 使うツール・ライブラリ

- @playwright/mcp
- MCP SDK

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

- Model Context Protocol（MCP）の基本概念
- Playwrightの基本的な使い方
- コーディングエージェント（Claude Code/Copilot等）のアーキテクチャ
- トークン消費とコンテキストウィンドウの制約に関する理解
- アクセシビリティツリーの概念
