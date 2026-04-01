# カテゴリー定義の明示による理解促進

> 各カテゴリーセクションの冒頭に、そのカテゴリーの定義を引用形式（>）で記載する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

ユーザーがClaude Codeエコシステムの構造を理解し、自分のニーズに最も適したカテゴリーを特定できるようにするため

## いつ使うのか

専門用語や概念が多いドキュメントで、読者の理解を助けたい場合

## やり方

1. 各カテゴリーセクション（## Agent Skills 🤖など）の直後に引用ブロックを追加
2. そのカテゴリーが何であるか、何に使われるかを1-2文で定義
3. 簡潔かつ明確な言葉で記述

### 入力

- カテゴリーの役割定義
- 対象読者の前提知識レベル

### 出力

- 各カテゴリーの定義文（引用形式）

## 使うツール・ライブラリ

- Markdown（引用記法）

## コード例

```
## Agent Skills 🤖

> Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.
```

## 前提知識

- Claude Codeの基本的な使い方（CLI、設定ファイル、コマンド実行）
- GitHubの基本操作（リポジトリのクローン、READMEの閲覧）
- Markdownの読解
- AI開発ツールの一般的な概念（エージェント、フック、プロンプト等）

## 根拠

> "A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow."

> "Agent Skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks" - カテゴリー定義の例

> 8つの主要カテゴリー: Agent Skills, Workflows & Knowledge Guides, Tooling, Status Lines, Hooks, Slash-Commands, CLAUDE.md Files, Alternative Clients
