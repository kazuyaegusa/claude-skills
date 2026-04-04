# Subagentのカテゴリ別プラグイン化

> 130種以上のSubagentを10カテゴリに分類し、それぞれをClaude Code Pluginとして配布する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

タスク領域ごとに必要なSubagentだけをインストールでき、不要なコンテキスト汚染を防ぐため

## いつ使うのか

プロジェクトで必要な専門領域が明確で、全Subagentをインストールするとコンテキストが肥大化する場合

## やり方

1. GitHubリポジトリをカテゴリディレクトリで構造化（01-core-development, 02-language-specialists等）
2. 各カテゴリをvoltagent-*という名前のプラグインとして登録
3. claude plugin marketplace add VoltAgent/awesome-claude-code-subagents
4. claude plugin install voltagent-lang（言語専門家群のみ導入）のように選択インストール

### 入力

- 必要なタスク領域（言語、インフラ、セキュリティ等）

### 出力

- ~/.claude/agents/または.claude/agents/に配置されたSubagent定義ファイル群

## 使うツール・ライブラリ

- Claude Code Plugin system
- GitHub repository

## コード例

```
claude plugin marketplace add VoltAgent/awesome-claude-code-subagents
claude plugin install voltagent-lang    # 言語専門家のみ
claude plugin install voltagent-infra   # インフラ系のみ
```

## 前提知識

- Claude Codeの基本的な使用経験
- Subagentの概念（独立したコンテキストウィンドウ、専門性、ツール権限）の理解
- GitHubからのリポジトリクローンまたはcurlでのファイル取得方法
- ~/.claude/agents/と.claude/agents/の違い（グローバル vs プロジェクト固有）

## 根拠

> This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.

> Each subagent includes a `model` field that automatically routes it to the right Claude model — balancing quality and cost

> Code writers (developers, engineers): Read, Write, Edit, Bash, Glob, Grep - create and execute

> Option 1: Manual Installation / Option 2: Interactive Installer / Option 3: Standalone Installer / Option 4: Agent Installer

> claude plugin marketplace add VoltAgent/awesome-claude-code-subagents
