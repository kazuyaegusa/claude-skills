# Claude SkillでMCPツールの使用パターンを定型化

> Exa MCP用のClaude Skillを作成し、カテゴリ別の最適な検索パターン・フィルタ制限・トークン管理を文書化

- 出典: https://github.com/exa-labs/exa-mcp-server
- 投稿者: exa-labs
- カテゴリ: claude-code-workflow

## なぜ使うのか

カテゴリごとのフィルタ制限を毎回調べる必要がなくなり、AIが自動的に正しいパラメータで検索できる

## いつ使うのか

特定の検索カテゴリを頻繁に使う場合、チーム内で検索パターンを標準化したい場合

## やり方

1. 目的別にSkillファイルを作成（company-research/code-search/people-research等）
2. Skill内で「Tool Restriction」「Token Isolation」「Filter Restrictions」等のセクションを明記
3. カテゴリ固有のフィルタ制限を列挙
4. 典型的なクエリ例をコード例として記載
5. MCPエンドポイントURLにtools パラメータを付与してSkillで使うツールを限定
6. Claude Codeでスキルファイルを読み込み

### 入力

- 検索カテゴリ（company/code/people等）
- 頻出するクエリパターン
- フィルタ制限の文書

### 出力

- Claude Skillファイル（SKILL.md形式）
- MCPエンドポイントURL（tools パラメータ付き）

## 使うツール・ライブラリ

- Claude Code skill system
- Exa MCP Server

## コード例

```
---
name: company-research
description: Company research using Exa search
context: fork
---

## Tool Restriction
ONLY use `web_search_advanced_exa`.

## Filter Restrictions
When using `category: "company"`, these cause 400 errors:
- includeDomains / excludeDomains
- startPublishedDate / endPublishedDate
```

## 前提知識

- MCP (Model Context Protocol) の基本概念
- 使用するAI環境（Cursor/VS Code/Claude Code等）の設定ファイル構造
- JSONフォーマットの編集能力
- Exa APIの検索カテゴリと用途の理解

## 根拠

> Connect to Exa's hosted MCP server: https://mcp.exa.ai/mcp

> Never run Exa searches in main context. Always spawn Task agents: Agent runs Exa search internally, Agent processes results using LLM intelligence, Agent returns only distilled output

> Exa returns different results for different phrasings. For coverage: Generate 2-3 query variations, Run in parallel, Merge and deduplicate
