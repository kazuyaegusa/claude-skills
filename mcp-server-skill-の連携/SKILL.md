# MCP server + Skill の連携

> Model Context Protocol(MCP) serverでドキュメント検索・GitHub操作等のツールを提供し、Skillでそれらツールの使い方をAgentに教える

- 出典: https://github.com/microsoft/skills
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

MCPは「何ができるか(ツール定義)」、Skillは「いつ・どう使うか(ベストプラクティス)」を提供する。両者を組み合わせることで、Agentはドキュメント検索やAPI呼び出しを適切に実行できる

## いつ使うのか

外部API/ドキュメント/GitHub/ブラウザ操作をAgentに組み込みたい時。特にAzure SDK等のドキュメント参照が頻繁な開発

## やり方

1. `.vscode/mcp.json` (または `.claude/mcp.json`)にMCP server設定を記述(例: microsoft-docs, github, playwright) 2. 対応するSkillを `.github/skills/` に配置(例: `mcp-builder`, `github-issue-creator`) 3. SkillのYAMLフロントマターに `triggers` を設定(例: "search documentation", "create issue") 4. Agentがユーザー入力に応じてMCPツールを呼び出し、Skillのガイドに従って操作 5. 例: 「Cosmos DBのパーティションキー戦略を調べて」→ microsoft-docs MCPで検索 → azure-cosmos-db-py Skillで実装

### 入力

- MCP server設定(mcp.json)
- 対応Skill(SKILL.md)

### 出力

- Agentが外部ツールを自律的に活用
- ドキュメント参照→コード生成のワンストップ化

## 使うツール・ライブラリ

- MCP servers (microsoft-docs, github, playwright, context7等)
- Copilot SDK / Claude MCP client

## コード例

```
// .vscode/mcp.json
{
  "mcpServers": {
    "microsoft-docs": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-microsoft-docs"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" }
    }
  }
}

// Skillで使い方を指示
// .github/skills/github-issue-creator/SKILL.md
---
triggers:
  - create issue
  - file bug
---
Use `github` MCP server's `create_issue` tool with title, body, labels.
```

## 前提知識

- AI Coding Agent(GitHub Copilot/Claude/Gemini等)の基本操作
- Git/シンボリックリンクの理解
- YAMLフロントマターの読み書き
- Azure SDK/Foundry SDK(対象ドメイン)の基礎知識
- CI/CD(GitHub Actions等)でのテスト自動化経験(テストハーネス活用時)

## 根拠

> "Skills, custom agents, AGENTS.md templates, and MCP configurations for AI coding agents working with Azure SDKs and Microsoft AI Foundry."

> "132 skills in `.github/skills/` — flat structure with language suffixes for automatic discovery"

> "Use skills selectively. Loading all skills causes context rot: diluted attention, wasted tokens, conflated patterns."

> "Sensei-style Scoring — Skills are evaluated on frontmatter compliance: Low(Basic description only) / Medium(Description > 150 chars, has trigger keywords) / Medium-High(Has triggers AND anti-triggers) / High(Triggers + anti-triggers + compatibility field)"

> "128 skills with 1158 test scenarios — all skills have acceptance criteria and test scenarios."
