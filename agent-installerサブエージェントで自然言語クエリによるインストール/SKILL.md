# agent-installerサブエージェントで自然言語クエリによるインストール

> Claude Code内で自然言語（「PHPエージェントを見つけてグローバルにインストール」）でサブエージェントを検索・インストールする

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

CLIコマンドやスクリプトを覚える必要がなく、会話形式でエージェントを発見・導入できるため、UXが向上する。カテゴリ名やエージェント名を正確に知らなくても検索可能

## いつ使うのか

エージェントカタログを探索しながら、試行錯誤的に必要なものを見つけたい時。CLIに不慣れなユーザーがGUI的に操作したい時

## やり方

1. `curl -s https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/categories/09-meta-orchestration/agent-installer.md -o ~/.claude/agents/agent-installer.md`
2. Claude Codeで「Use the agent-installer to show me available categories」や「Find PHP agents and install php-pro globally」と指示
3. agent-installerがGitHub APIを経由してカタログを検索・取得・インストール

### 入力

- agent-installer.md がインストール済み
- Claude Codeセッション起動中

### 出力

- 自然言語リクエストに応じて適切なサブエージェントが自動インストールされる

## 使うツール・ライブラリ

- agent-installer.md
- GitHub API

## コード例

```
curl -s https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/categories/09-meta-orchestration/agent-installer.md -o ~/.claude/agents/agent-installer.md
```

## 前提知識

- Claude Codeがインストール・セットアップ済み
- サブエージェントの概念理解（独立したコンテキストウィンドウ、ドメイン特化プロンプト、ツール権限管理）
- 基本的なCLI操作（curl, chmod, git clone等）
- YAMLフロントマター形式の理解（サブエージェント定義ファイルの編集時）
- Claude Codeの /agents コマンドとサブエージェント呼び出し構文の理解

## 根拠

> "This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks."

> "Domain-Specific Intelligence: Subagents come equipped with carefully crafted instructions tailored to their area of expertise"

> "Shared Across Projects: After creating a subagent, you can utilize it throughout various projects and distribute it among team members"

> "Each subagent includes a `model` field that automatically routes it to the right Claude model — balancing quality and cost"

> "Project Subagents: `.claude/agents/` Current project only, Higher precedence"
