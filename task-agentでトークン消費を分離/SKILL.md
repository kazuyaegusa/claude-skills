# Task agentでトークン消費を分離

> Exa検索を常にTask agent（fork context）で実行し、メインコンテキストに検索結果全体を流さない

- 出典: https://github.com/exa-labs/exa-mcp-server
- 投稿者: exa-labs
- カテゴリ: claude-code-workflow

## なぜ使うのか

検索結果は大量のテキストを含むため、メインコンテキストに全て入れるとトークン枯渇する。agentで要約・フィルタしてから返すことでトークン効率化

## いつ使うのか

大量検索結果を扱う場合、トークン制限が厳しい環境で動作させる場合

## やり方

1. Claude Skillに「Token Isolation (Critical)」ルールを記載
2. 検索クエリ実行時、必ずTask agentを起動
3. agent内でExa検索を実行
4. agent内でLLMにより結果をマージ・重複排除・要約
5. agentはメインに対してコンパクトなJSON/markdownのみ返却

### 入力

- 検索クエリ
- numResults（結果数）

### 出力

- 要約済み検索結果（メインコンテキストに負荷をかけない形式）

## 使うツール・ライブラリ

- Task agent（Claude Code）
- Exa MCP Server

## コード例

```
# In Claude Skill:
## Token Isolation (Critical)
Never run Exa searches in main context. Always spawn Task agents:
- Agent runs Exa search internally
- Agent processes results using LLM intelligence
- Agent returns only distilled output (compact JSON or brief markdown)
- Main context stays clean
```

## 前提知識

- MCP (Model Context Protocol) の基本概念
- 使用するAI環境（Cursor/VS Code/Claude Code等）の設定ファイル構造
- JSONフォーマットの編集能力
- Exa APIの検索カテゴリと用途の理解

## 根拠

> Never run Exa searches in main context. Always spawn Task agents: Agent runs Exa search internally, Agent processes results using LLM intelligence, Agent returns only distilled output
