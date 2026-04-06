# Agent Skillsで専門知識を注入する

> SKILL.mdファイルに特定タスクの手順・知識・ツールを記述し、Claude Codeが専門エージェントとして振る舞えるようにする

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

毎回プロンプトで指示するのではなく、再利用可能な知識パッケージとして管理することで一貫性と品質を保つため

## いつ使うのか

TDD、セキュリティ監査、デプロイ、ドキュメント生成など、繰り返し実行する専門タスクがある時

## やり方

1. ~/.claude/skills/{skill-name}/SKILL.md を作成
2. name, description, 手順、ツール、コード例を記述
3. Claudeがタスクに応じて自動選択、またはユーザーが明示的に呼び出し

### 入力

- タスクの目的・手順の明確な定義
- 使用するツール・ライブラリのリスト
- コード例・テンプレート

### 出力

- SKILL.mdファイル
- ~/.claude/skills/_index.md への登録

## 使うツール・ライブラリ

- Claude Code Skill tool
- markdown

## コード例

```
---
name: skill-name
description: 何をするスキルか
---

# 手順
1. ...
2. ...
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

> "Ralph Orchestrator implements the simple but effective 'Ralph Wiggum' technique for autonomous task completion, continuously running an AI agent against a prompt file until the task is marked as complete or limits are reached."

> "A well-designed desktop app that provides detailed observability into your Claude Code sessions by analyzing the session logs. Provides turn-based context data across numerous categories, compaction visualization, subagent execution trees, and custom notification triggers."

> "Harness - A meta-skill that designs domain-specific agent teams, defines specialized agents, and generates the skills they use."
