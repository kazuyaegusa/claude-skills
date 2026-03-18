# Slash-Commands で定型プロンプトを再利用する

> 頻繁に使うプロンプトを `/commit`, `/tdd`, `/analyze-issue` などのコマンドとして登録し、1 行で呼び出せるようにする仕組み。各コマンドは `.claude/commands/` ディレクトリの Markdown ファイルとして定義される

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

同じ指示を毎回タイプすると時間がかかり、表現のブレによって AI の応答品質が不安定になる。Slash-Commands で定型化することで、チーム全体で一貫した指示を出せ、ベストプラクティスを共有できる

## いつ使うのか

Git コミット、PR 作成、GitHub Issue 対応、TDD サイクル実行、ドキュメント生成など、繰り返し実行する定型作業がある場合

## やり方

1. `.claude/commands/` ディレクトリに `<コマンド名>.md` ファイルを作成
2. ファイル内に詳細なプロンプトを記述（Claude にどう振る舞ってほしいかを明確に）
3. Claude Code セッション内で `/コマンド名` と入力すると、そのプロンプトが展開されて実行される
4. 例: `/commit` → コミットメッセージを自動生成して Git commit 実行

### 入力

- Markdown 形式のプロンプト定義
- パラメータ（コマンドによっては Issue 番号など）

### 出力

- 定型化された AI 応答
- 自動化されたタスク実行

## 使うツール・ライブラリ

- Claude Code Slash-Commands API

## コード例

```
# /commit.md

Create a git commit using conventional commit format with appropriate emojis, following project standards and creating descriptive messages that explain the purpose of changes.
```

## 前提知識

- Claude Code の基本的な使い方（インストール、セッション開始、ファイル操作）
- Git の基礎知識（ブランチ、コミット、PR）
- コマンドライン操作の基本（Bash, tmux など）
- 開発プロセスの基礎知識（TDD, CI/CD, コードレビュー）

## 根拠

> A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow.

> Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

> Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.

> Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task.

> CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards.
