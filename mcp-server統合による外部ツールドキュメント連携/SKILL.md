# MCP server統合による外部ツール・ドキュメント連携

> `.vscode/mcp.json` でMCPサーバー（microsoft-docs、GitHub、Playwright等）を定義し、スキル内から `microsoft-docs` MCP経由でドキュメントを参照させる

- 出典: https://github.com/microsoft/skills
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

スキル内に全ドキュメントを埋め込むとトークンを消費するため、MCP経由で必要な箇所のみをLLMに与える

## いつ使うのか

公式ドキュメント・GitHub・ブラウザ操作をエージェントに実行させたい場合。スキルのトークンを削減したい場合

## やり方

1. `.vscode/mcp.json` にサーバー定義（例: microsoft-docs） 2. SKILL.md 内で「Reference official docs via `microsoft-docs` MCP」と記載 3. エージェントが必要時にMCPツールを呼び出し

### 入力

- MCPサーバー名
- ツール名
- 呼び出しパラメータ

### 出力

- ドキュメント断片
- GitHub issue/PR情報
- ブラウザ操作結果

## 使うツール・ライブラリ

- MCP protocol
- microsoft-docs MCP
- github MCP
- playwright MCP

## コード例

```
{
  "mcpServers": {
    "microsoft-docs": { "command": "npx", "args": ["@modelcontextprotocol/server-docs"] }
  }
}
```

## 前提知識

- AI coding agent（GitHub Copilot、Claude Code、Copilot CLI等）の基本操作
- Markdown形式のドキュメント構造理解
- Symlink（シンボリックリンク）の概念
- YAML形式の設定ファイル
- GitHub Actionsの基本（日次更新ワークフローを活用する場合）
- MCP（Model Context Protocol）の概要（外部ツール統合を使う場合）

## 根拠

> 「Reference configurations in `.vscode/mcp.json`: Documentation (microsoft-docs, context7, deepwiki), Development (github, playwright, terraform), Utilities (sequentialthinking, memory, markitdown)」（MCP Servers）
