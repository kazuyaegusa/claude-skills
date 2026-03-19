# HooksでClaude Codeの動作をリアルタイム制御する

> Hooksカテゴリのリソース（例: TDD Guard、parry、Dippy）をインストールし、Claude Codeがファイルを書き込む前やBashコマンドを実行する前に検証・承認・ブロックを自動実行する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeは強力だが、TDD違反、プロンプトインジェクション、危険なBashコマンド実行のリスクがある。Hooksはライフサイクルイベント（tool_use、write、bash等）にスクリプトを挿入し、リアルタイムでガードレールを提供する

## いつ使うのか

Claude CodeがTDDを守らない、危険なコマンドを実行しようとする、プロンプトインジェクションのリスクがある時

## やり方

1. awesome-claude-codeの「Hooks 🪝」セクションから目的に合うフックを選択（例: TDD Guard）
2. フックのリポジトリをクローン: `git clone https://github.com/nizos/tdd-guard`
3. `.claude/hooks.json` に設定を追加（多くのフックはREADMEに設定例を記載）
4. Claude Codeを再起動してフックを有効化
5. Claude Codeが該当操作（例: ファイル書き込み）を実行する際、フックが自動起動し、ブロック or 警告を出す

### 入力

- 監視したいClaude Codeの操作（write、bash、tool_use等）
- 検証ロジック（TDDチェック、AST解析、シークレットスキャン等）

### 出力

- Claude Codeの操作がブロック or 承認される
- 違反時のエラーメッセージ or 警告

## 使うツール・ライブラリ

- TDD Guard
- parry
- Dippy
- TypeScript Quality Hooks

## コード例

```
# .claude/hooks.json 例（TDD Guard）
{
  "hooks": [
    {
      "event": "tool_use",
      "command": "python ~/.claude/hooks/tdd_guard.py",
      "description": "TDD違反をブロック"
    }
  ]
}
```

## 前提知識

- Claude Codeの基本的な使い方（インストール、起動、プロンプト入力）
- Claude Codeの設定ファイル構造（.claude/ディレクトリ、hooks.json、commands/、skills/）
- GitHubの基本操作（リポジトリのクローン、READMEの読解）
- JSON、Markdown、Bashの基礎知識

## 根拠

> # Awesome Claude Code - A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow.

> ## Agent Skills 🤖 - Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

> ## Hooks 🪝 - Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.

> ## Slash-Commands 🔪 - Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task.

> ## Tooling 🧰 - Tooling denotes applications that are built on top of Claude Code and consist of more components than slash-commands and CLAUDE.md files.
