# Hooksでライフサイクルを制御する

> Claude Codeのツール実行前後に自動でスクリプトを実行し、品質チェック・通知・承認フローを挿入する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

人間が毎回監視しなくても、TDD違反やセキュリティリスクを自動検出・ブロックできるため

## いつ使うのか

TDD強制、破壊的コマンドのブロック、シークレットスキャン、デスクトップ通知など、特定タイミングで自動介入したい時

## やり方

1. ~/.claude/hooks.json に hook定義を追加（event, command, approval等）
2. Write/Edit時にlint、Bash実行時にAST解析など、eventに応じたスクリプトを指定
3. approval=trueで人間承認を要求、falseで自動実行

### 入力

- hooks.json設定ファイル
- 実行するスクリプト（Bash, Python, etc.）
- eventトリガー（Write, Edit, Bash, etc.）

### 出力

- hook実行結果（承認/ブロック/通知）
- Claudeへのフィードバックメッセージ

## 使うツール・ライブラリ

- hooks.json
- 各種linter（ESLint, Prettier, etc.）
- AST解析ツール（Dippy等）

## コード例

```
{
  "hooks": [
    {
      "event": "Write",
      "command": "eslint --fix {file_path}",
      "approval": false
    }
  ]
}
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
