# Agent Skillによる専門知識の注入

> Claude Codeに特定タスク用の知識・手順・ツールをパッケージ化して提供する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

汎用LLMだけでは不足する専門領域（セキュリティ監査、IaC生成、科学計算等）の知識を補完し、再現性のある高品質な出力を得るため

## いつ使うのか

特定ドメインの専門知識が必要で、プロンプトだけでは品質・再現性が不足するとき

## やり方

1. `~/.claude/skills/{skill-name}/SKILL.md`にタスク定義・手順・コード例を記述
2. 必要に応じてスクリプト・設定ファイルを同梱
3. `/skill-name`コマンドまたは自動選択で起動
4. Trail of Bits Security Skills（CodeQL/Semgrep統合）、cc-devops-skills（IaC生成）等の既存スキルを参考に構築

### 入力

- タスク定義（SKILL.md）
- 補助スクリプト・設定ファイル（任意）

### 出力

- 専門化されたClaude Codeの振る舞い
- タスク固有の成果物（コード・ドキュメント・分析レポート等）

## 使うツール・ライブラリ

- SKILL.mdフォーマット
- Claude Code CLI

## コード例

```
# SKILL.md例
---
name: security-audit
description: CodeQLとSemgrepで脆弱性スキャン
---

## 手順
1. CodeQL databaseを生成
2. 既知の脆弱性パターンをクエリ
3. Semgrepでカスタムルール実行
4. レポート生成
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

> "Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task"

> "Ralph Wiggum Loop - continuously running an AI agent against a prompt file until the task is marked as complete or limits are reached"

> "CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards"
