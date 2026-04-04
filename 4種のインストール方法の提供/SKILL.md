# 4種のインストール方法の提供

> Manual, Interactive Script, Standalone Installer, Agent Installerの4通りでSubagentをインストール可能にする

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

ユーザーの環境・スキルレベル・用途に応じて最適な導入方法を選択できるようにするため

## いつ使うのか

1. Manual: 特定のSubagentだけ導入したい / 2. Interactive: 複数カテゴリを対話的に選択したい / 3. Standalone: CI/CDで自動化したい / 4. Agent Installer: Claude Codeから検索・インストールまで完結させたい

## やり方

1. Manual: git clone → cp categories/*/agent.md ~/.claude/agents/
2. Interactive Script: ./install-agents.sh → カテゴリ選択 → インストール
3. Standalone: curl -sO install-agents.sh → chmod +x → 実行（リポジトリクローン不要）
4. Agent Installer: agent-installer.mdをダウンロード → Claude Code上で"Find PHP agents and install php-pro globally"と指示

### 入力

- インストール方法の選択（Manual/Interactive/Standalone/Agent Installer）

### 出力

- ~/.claude/agents/（グローバル）または.claude/agents/（プロジェクト固有）に配置されたSubagent定義

## 使うツール・ライブラリ

- git
- curl
- bash
- Claude Code

## コード例

```
# Option 3: Standalone Installer
curl -sO https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/install-agents.sh
chmod +x install-agents.sh
./install-agents.sh

# Option 4: Agent Installer
curl -s https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/categories/09-meta-orchestration/agent-installer.md -o ~/.claude/agents/agent-installer.md
```

## 前提知識

- Claude Codeの基本的な使用経験
- Subagentの概念（独立したコンテキストウィンドウ、専門性、ツール権限）の理解
- GitHubからのリポジトリクローンまたはcurlでのファイル取得方法
- ~/.claude/agents/と.claude/agents/の違い（グローバル vs プロジェクト固有）

## 根拠

> This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.

> Independent Context Windows: Every subagent operates within its own isolated context space

> Each subagent includes a `model` field that automatically routes it to the right Claude model — balancing quality and cost

> Read-only agents (reviewers, auditors): Read, Grep, Glob - analyze without modifying

> Code writers (developers, engineers): Read, Write, Edit, Bash, Glob, Grep - create and execute
