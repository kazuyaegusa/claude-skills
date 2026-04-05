# Agent Teamsによる並列タスク分解

> 複雑なタスクを複数のサブエージェントに分割し、並列実行で高速化する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

大規模タスクを効率的に処理し、各エージェントの専門性を活かすため

## いつ使うのか

並列化可能なサブタスクが複数あり、高速化が必要なとき

## やり方

1. タスクを独立したサブタスクに分解
2. AGENTS.mdでサブエージェント定義（役割・ツール・モデル）
3. 依存関係を設定
4. 並列実行 → 結果統合
5. Harness（メタスキルによるチーム自動生成）、Auto-Claude（SDLC統合）等を参考に実装

### 入力

- タスク全体の仕様
- サブタスク分割計画
- エージェント定義（AGENTS.md）

### 出力

- 各サブタスクの成果物
- 統合された最終成果物

## 使うツール・ライブラリ

- AGENTS.mdフォーマット
- Claude Code Agent SDK

## コード例

```
# AGENTS.md例
agents:
  - name: researcher
    role: 調査
    model: haiku
  - name: implementer
    role: 実装
    model: sonnet
    depends_on: [researcher]
```

## 前提知識

- Claude Codeの基本操作（CLI使用・セッション管理）
- マークダウンフォーマットの理解
- Bash/Python/TypeScriptのいずれかでスクリプト作成経験
- Git・GitHub CLIの基礎知識
- LLMエージェントの基本概念（プロンプトエンジニアリング・コンテキスト管理）

## 根拠

> "Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities."

> "Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle."

> "Ralph Wiggum Loop - continuously running an AI agent against a prompt file until the task is marked as complete or limits are reached"

> "Agent Teams - Launch Claude Code session that is connected to a swarm of Claude Code Agents"
