# カテゴリー別リソース分類によるエコシステム整理

> Claude Code拡張を8つの明確なカテゴリー（Agent Skills、Workflows、Tooling、Status Lines、Hooks、Slash-Commands、CLAUDE.md Files、Alternative Clients）に分類し、各リソースに説明と作者情報を付与する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

ユーザーが自分のニーズに最も適したリソースを素早く発見できるようにするため。また、各カテゴリーの定義を明示することで、リソースの役割と使用場面を理解しやすくする

## いつ使うのか

大規模なツールエコシステムを整理し、ユーザーが目的に応じてリソースを発見できるようにしたい場合

## やり方

1. リソースを機能・用途に基づいて分類する
2. 各カテゴリーに明確な定義を提供する（例："Agent Skills are model-controlled configurations..."）
3. 各リソースにGitHubリンク、作者名、簡潔な説明（1-3文）を記載
4. サブカテゴリーを設けて更に細分化（例：Slash-Commandsを"Version Control & Git"、"Code Analysis & Testing"などに分割）
5. 定期的に更新し、"Latest Additions"セクションで新規追加を強調

### 入力

- 各リソースのGitHubリポジトリURL
- リソースの機能説明
- 作者情報

### 出力

- 階層化されたMarkdownリスト
- カテゴリー別目次
- 検索可能なREADME構造

## 使うツール・ライブラリ

- GitHub
- Markdown
- awesome.re badge

## コード例

```
## Agent Skills 🤖

> Agent skills are model-controlled configurations...

### General

- [AgentSys](https://github.com/avifenesh/agentsys) by [avifenesh](https://github.com/avifenesh) - Workflow automation system for Claude with...
```

## 前提知識

- Claude Codeの基本的な使い方（CLI、設定ファイル、コマンド実行）
- GitHubの基本操作（リポジトリのクローン、READMEの閲覧）
- Markdownの読解
- AI開発ツールの一般的な概念（エージェント、フック、プロンプト等）

## 根拠

> "A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow."

> "Latest Additions" セクションに claude-devtools, agnix, Codebase to Course, Ruflo を掲載

> "Agent Skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks" - カテゴリー定義の例

> "Please do not open a PR to submit a recommendation - the only person who is allowed to submit PRs to this repo is Claude" - 品質管理方針

> 8つの主要カテゴリー: Agent Skills, Workflows & Knowledge Guides, Tooling, Status Lines, Hooks, Slash-Commands, CLAUDE.md Files, Alternative Clients
