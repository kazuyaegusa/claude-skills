# Agent Teamsで並列処理を自動化する

> 複数の独立したサブタスクをClaude Code subagentに分割し、並列実行させる

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

複数ファイルの実装や調査+実装の並行実行で、シーケンシャル実行よりも高速化できるため

## いつ使うのか

並列化可能な独立サブタスクが2つ以上ある、複数ファイルにまたがる実装、調査+実装が必要な時

## やり方

1. タスクを独立した単位に分解（調査、実装A、実装B等）
2. AGENTS.md または Task tool で各エージェントの役割・ツールを定義
3. 依存関係を設定し、並列実行可能な部分は同時起動
4. 全タスク完了後、統合レポート生成

### 入力

- タスクの分解計画
- 各エージェントの役割定義
- 依存関係グラフ

### 出力

- 並列実行されたサブタスク結果
- 統合レポート

## 使うツール・ライブラリ

- Claude Code Task tool
- AGENTS.md

## コード例

```
// 疑似コード
Task({
  type: 'general-purpose',
  prompt: 'ファイルAを実装',
  model: 'sonnet'
})
Task({
  type: 'general-purpose',
  prompt: 'ファイルBを実装',
  model: 'sonnet'
})
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

> "Ralph Orchestrator implements the simple but effective 'Ralph Wiggum' technique for autonomous task completion, continuously running an AI agent against a prompt file until the task is marked as complete or limits are reached."
