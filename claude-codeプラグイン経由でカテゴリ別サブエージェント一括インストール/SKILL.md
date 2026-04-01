# Claude Codeプラグイン経由でカテゴリ別サブエージェント一括インストール

> 127個以上のサブエージェントをカテゴリ別プラグイン（voltagent-lang, voltagent-infra等）として一括インストールする

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動で個別に.mdファイルをコピーするより効率的で、カテゴリ単位で必要なエージェント群をまとめて導入できるため。特にメタオーケストレーションエージェント（voltagent-meta）は他カテゴリがインストール済みの時に最大効果を発揮する

## いつ使うのか

複数の専門領域をカバーするサブエージェントを短時間で導入したい時、チーム全体で同じエージェントセットを標準化したい時

## やり方

1. `claude plugin marketplace add VoltAgent/awesome-claude-code-subagents` でマーケットプレイスに追加
2. `claude plugin install <plugin-name>` で必要なカテゴリをインストール（例: `claude plugin install voltagent-lang` で言語スペシャリスト全体）
3. インストールしたサブエージェントは自動的に `~/.claude/agents/` または `.claude/agents/` に配置される

### 入力

- Claude Code CLIがインストール済み
- プラグインマーケットプレイスへのアクセス権限

### 出力

- カテゴリ別サブエージェント群が ~/.claude/agents/ にインストールされる
- 全プロジェクトで利用可能なグローバルエージェント

## 使うツール・ライブラリ

- Claude Code CLI
- VoltAgent/awesome-claude-code-subagents plugin

## コード例

```
claude plugin marketplace add VoltAgent/awesome-claude-code-subagents
claude plugin install voltagent-lang
claude plugin install voltagent-infra
```

## 前提知識

- Claude Codeがインストール・セットアップ済み
- サブエージェントの概念理解（独立したコンテキストウィンドウ、ドメイン特化プロンプト、ツール権限管理）
- 基本的なCLI操作（curl, chmod, git clone等）
- YAMLフロントマター形式の理解（サブエージェント定義ファイルの編集時）
- Claude Codeの /agents コマンドとサブエージェント呼び出し構文の理解

## 根拠

> "This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks."

> "Each subagent includes a `model` field that automatically routes it to the right Claude model — balancing quality and cost"

> "Project Subagents: `.claude/agents/` Current project only, Higher precedence"

> "Global Subagents: `~/.claude/agents/` All projects, Lower precedence"

> "claude plugin marketplace add VoltAgent/awesome-claude-code-subagents"
