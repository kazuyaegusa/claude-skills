# 4種のインストール方法提供

> plugin/manual/interactive installer/agent installerの4通りの導入経路を用意し、ユーザーの習熟度・環境に応じて選択可能にする

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

初心者は対話的インストーラーで段階的に導入、上級者はcurlでスタンドアロン実行、CI/CDではmanual installでスクリプト化、という使い分けが必要。単一の方法では全ユーザーをカバーできない

## いつ使うのか

多様なユーザー層に対してsubagentを配布するとき

## やり方

1. Plugin方式: `claude plugin install voltagent-lang` でカテゴリ一括導入
2. Manual: リポジトリをclone→`~/.claude/agents/` にコピー
3. Interactive installer: `./install-agents.sh` で対話的に選択
4. Standalone installer: `curl -sO ...install-agents.sh && ./install-agents.sh`（clone不要）
5. Agent installer: agent-installer.mdを導入し、Claude Codeに「Find PHP agents and install」と指示

### 入力

- GitHubリポジトリURL
- agent定義ファイル群

### 出力

- ~/.claude/agents/ または .claude/agents/ に配置されたagent
- インストール完了メッセージ

## 使うツール・ライブラリ

- claude CLI
- curl
- bash script

## コード例

```
# Plugin方式
claude plugin install voltagent-lang

# Standalone installer（clone不要）
curl -sO https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/install-agents.sh
chmod +x install-agents.sh
./install-agents.sh
```

## 前提知識

- Claude Codeの基本操作（subagent作成・呼び出し）
- YAML frontmatterの理解
- Claude APIのモデル種別（opus/sonnet/haiku）の特性
- ~/.claude/agents/ と .claude/agents/ の違い（global/project-specific）
- 最小権限の原則（Principle of Least Privilege）

## 根拠

> This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.

> 130+ subagents covering a wide range of development use cases

> 4 installation methods: Plugin (claude plugin install), Manual, Interactive installer (./install-agents.sh), Agent installer (via Claude Code)

> Standard template with YAML frontmatter: name, description, tools, model

> subagent-catalog skill: /subagent-catalog:search, :fetch, :list, :invalidate
