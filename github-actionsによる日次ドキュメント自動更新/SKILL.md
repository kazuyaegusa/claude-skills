# GitHub Actionsによる日次ドキュメント自動更新

> `.github/workflows/` でスクレイピングスクリプトを毎日実行し、`docs/llms.txt` と `docs/llms-full.txt` を最新のMicrosoft Learnドキュメントから自動生成する

- 出典: https://github.com/microsoft/skills
- 投稿者: microsoft
- カテゴリ: agent-orchestration

## なぜ使うのか

スキルが参照するドキュメントを常に最新に保ち、手動更新の負担を排除する

## いつ使うのか

スキルカタログが参照する外部ドキュメントを常に最新に保ちたい場合。llms.txt形式でLLM向けドキュメントを配布したい場合

## やり方

1. `.github/scripts/` にドキュメントスクレイピングスクリプトを配置 2. `.github/workflows/` で日次スケジュール実行 3. 生成された `docs/llms.txt` をGitHub Pages公開

### 入力

- スクレイピング対象URL
- GitHub Actions workflow定義

### 出力

- docs/llms.txt（リンク+要約）
- docs/llms-full.txt（全文）

## 使うツール・ライブラリ

- GitHub Actions
- Puppeteer/Playwright等（スクレイピング）

## コード例

```
# .github/workflows/test-harness.yml
on:
  schedule:
    - cron: '0 0 * * *'
```

## 前提知識

- AI coding agent（GitHub Copilot、Claude Code、Copilot CLI等）の基本操作
- Markdown形式のドキュメント構造理解
- Symlink（シンボリックリンク）の概念
- YAML形式の設定ファイル
- GitHub Actionsの基本（日次更新ワークフローを活用する場合）
- MCP（Model Context Protocol）の概要（外部ツール統合を使う場合）

## 根拠

> 「132 skills in `.github/skills/` — flat structure with language suffixes for automatic discovery」（Skill Catalog）

> 「Skills are installed to your chosen agent's directory (e.g., `.github/skills/` for GitHub Copilot) and symlinked if you use multiple agents.」（Quick Start）

> 「Reference configurations in `.vscode/mcp.json`: Documentation (microsoft-docs, context7, deepwiki), Development (github, playwright, terraform), Utilities (sequentialthinking, memory, markitdown)」（MCP Servers）

> 「GitHub Actions (daily doc updates)」（Repository Structure）

> 「Create acceptance criteria in `.github/skills/<skill>/references/acceptance-criteria.md` — Document correct/incorrect import patterns, authentication patterns, async variants」（Contributing）
