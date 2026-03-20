# Agent Installerサブエージェントによるメタ管理

> Claude Code内から `agent-installer` サブエージェント自身を使い、他のエージェントを検索・インストールする

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

ターミナル操作なしで、自然言語で「PHP専門エージェントを探してインストールして」と指示できるため、開発フローを中断せずにエージェント管理ができる

## いつ使うのか

開発中にClaude Code内から即座に新しい専門エージェントを追加したい場合

## やり方

1. `curl -s https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/categories/09-meta-orchestration/agent-installer.md -o ~/.claude/agents/agent-installer.md` でagent-installerをインストール
2. Claude Codeで「agent-installerでPHP関連エージェントを探して」と指示
3. agent-installerがGitHub APIを使ってリポジトリを検索し、候補を提示
4. 「php-proをグローバルにインストールして」と指示すると、自動的に `~/.claude/agents/` に配置される

### 入力

- agent-installer.md（メタエージェント定義）
- GitHubへのネットワークアクセス

### 出力

- 検索結果リスト
- 指定したエージェント定義ファイルの自動配置

## 使うツール・ライブラリ

- Claude Code
- GitHub API
- curl

## コード例

```
# agent-installerのインストール
curl -s https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/categories/09-meta-orchestration/agent-installer.md -o ~/.claude/agents/agent-installer.md

# Claude Code内での利用例
"agent-installerでRust専門のエージェントを検索して"
"rust-engineerをプロジェクトローカルにインストールして"
```

## 前提知識

- Claude Codeの基本操作（CLI起動、エージェント呼び出し）
- サブエージェントの概念理解（独立コンテキスト、ツール権限、モデル選択）
- YAML frontmatter形式の基本構造
- Git操作（クローン、ファイルコピー）またはcurlコマンドの使用
- 対象領域（言語・インフラ・QA等）の基礎知識（各エージェントを活用する場合）

## 根拠

> 「This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.」

> 「Independent Context Windows: Every subagent operates within its own isolated context space」

> 「Smart Model Routing: Each subagent includes a `model` field that automatically routes it to the right Claude model — balancing quality and cost」

> 「Tool Assignment Philosophy: Each subagent's `tools` field specifies Claude Code built-in tools, optimized for their role」

> 「Project Subagents: `.claude/agents/` Current project only, Higher precedence」
