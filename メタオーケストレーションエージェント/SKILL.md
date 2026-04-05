# メタオーケストレーションエージェント

> agent-installerなどのメタエージェントがGitHubから他のエージェントを検索・インストールし、マルチエージェント協調を自動化する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

エージェント導入自体をエージェント化することで、自然言語で「PHPエージェントをインストール」と指示するだけで適切なエージェントが自動配置される。複雑なワークフローの組み立てもメタエージェントに委譲できる

## いつ使うのか

大量のエージェントを管理したい時、または複雑なマルチエージェントワークフローを構築したい時

## やり方

1. `agent-installer.md`をダウンロード：`curl -s https://raw.githubusercontent.com/.../agent-installer.md -o ~/.claude/agents/agent-installer.md`
2. Claude Codeで「agent-installerでPHPエージェントを探してグローバルにインストール」と指示
3. agent-installerがGitHub APIでリポジトリを検索し、該当エージェントを`~/.claude/agents/`に自動配置
4. multi-agent-coordinatorやworkflow-orchestratorで複数エージェントを協調動作させる

### 入力

- インストールしたいエージェントの条件（言語、ドメイン等）
- オーケストレーションするタスクの定義

### 出力

- 自動インストールされたエージェント群
- 協調動作するマルチエージェントワークフロー

## 使うツール・ライブラリ

- agent-installer
- multi-agent-coordinator
- workflow-orchestrator
- GitHub API

## コード例

```
# agent-installerのインストール
curl -s https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/categories/09-meta-orchestration/agent-installer.md -o ~/.claude/agents/agent-installer.md

# Claude Codeでの使用例
> Use agent-installer to find PHP agents and install php-pro globally
> Use multi-agent-coordinator to orchestrate research-analyst and backend-developer
```

## 前提知識

- Claude Code CLIがインストールされている
- claude plugin機能の基本的な理解
- サブエージェントの概念（独立したコンテキストウィンドウ、ドメイン特化型プロンプト）
- Markdown/YAMLの基本文法

## 根拠

> This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.

> 130+ specialized Claude Code subagents covering a wide range of development use cases

> claude plugin marketplace add VoltAgent/awesome-claude-code-subagents

> Each subagent's `tools` field specifies Claude Code built-in tools, optimized for their role

> Smart Model Routing: Each subagent includes a `model` field that automatically routes it to the right Claude model
