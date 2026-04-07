# 独立コンテキストウィンドウ活用

> 各サブエージェントが独立したコンテキスト空間で動作し、メイン会話とタスク詳細を分離する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

複数タスクを並行処理してもコンテキスト汚染が起きず、メインスレッドがクリーンに保たれ、専門タスクの精度が向上する

## いつ使うのか

複雑なタスクを分割して並列処理したい時、メイン会話を散らかさずに専門作業を行いたい時

## やり方

1. `/agents` コマンドでサブエージェントマネージャーを起動
2. プロジェクト固有（.claude/agents/）またはグローバル（~/.claude/agents/）でエージェントを作成
3. 詳細な目的・起動トリガー・ツールアクセス権限を設定
4. システムプロンプトをエディタ（`e`キー）でカスタマイズ
5. Claude Codeが自動的に適切なエージェントを起動、または明示的に指定: `> Have the code-reviewer subagent analyze my latest commits`

### 入力

- サブエージェント定義（役割、トリガー、ツール権限）

### 出力

- 独立コンテキストで動作するサブエージェント
- メインスレッドに影響しないタスク実行結果

## 使うツール・ライブラリ

- Claude Code /agents コマンド

## コード例

```
/agents
# Then in editor:
---
name: code-reviewer
description: When code review is needed
tools: Read, Grep, Glob
model: sonnet
---
You are a code quality guardian...
```

## 前提知識

- Claude Codeの基本操作とサブエージェント概念の理解
- 開発タスクのカテゴリ分類（言語/インフラ/品質等）に関する知識
- Claude APIのモデル違い（opus/sonnet/haiku）の理解
- Markdownとフロントマター（YAML）の基礎知識
- Claude Code組み込みツール（Read, Write, Edit, Bash等）の把握

## 根拠

> 「This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.」

> 「Independent Context Windows: Every subagent operates within its own isolated context space, preventing cross-contamination between different tasks」

> 「Tool Assignment Philosophy: Read-only agents (reviewers, auditors): Read, Grep, Glob - analyze without modifying」

> 「Project Subagents (.claude/agents/): Current project only, Higher precedence」「Global Subagents (~/.claude/agents/): All projects, Lower precedence」

> 「130+ subagents across 10 categories: Core Development, Language Specialists, Infrastructure, Quality & Security, Data & AI, Developer Experience, Specialized Domains, Business & Product, Meta & Orchestration, Research & Analysis」
