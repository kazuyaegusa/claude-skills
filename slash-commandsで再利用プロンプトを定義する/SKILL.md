# Slash Commandsで再利用プロンプトを定義する

> .claude/commands/{name}.md にプロンプトを記述し、/name で呼び出せるショートカットを作る

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

長いプロンプトを毎回入力する手間を省き、チーム全体で標準化されたワークフローを共有できるため

## いつ使うのか

git操作（commit, PR作成）、ドキュメント生成、コンテキスト読み込みなど、定型プロンプトがある時

## やり方

1. .claude/commands/commit.md など、タスク名.md を作成
2. プロンプト本文をmarkdownで記述（引数は {arg} で受け取り可能）
3. Claude Codeで /commit と入力すると展開・実行される

### 入力

- タスクの目的・手順を記述したmarkdownファイル
- （オプション）引数定義

### 出力

- .claude/commands/{name}.md
- /name コマンドとしてClaude Codeから呼び出し可能

## 使うツール・ライブラリ

- markdown
- Claude Code SlashCommand tool

## コード例

```
<!-- .claude/commands/commit.md -->
Conventional Commit形式でコミットメッセージを生成し、git commitを実行する。

1. git diff を確認
2. type(scope): subject 形式でメッセージ作成
3. git commit -m "..."
```

## 前提知識

- Claude Codeの基本的な使い方（CLI起動、プロンプト入力、ツール実行）
- markdown記法
- JSON記法（hooks.json等の設定ファイル）
- Bash/シェルスクリプトの基礎
- Git基本操作
- （Agent Teams利用時）マルチエージェントの概念理解

## 根拠

> "Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities."

> "Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle."

> "Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task"

> "CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards"

> "A well-designed desktop app that provides detailed observability into your Claude Code sessions by analyzing the session logs. Provides turn-based context data across numerous categories, compaction visualization, subagent execution trees, and custom notification triggers."
