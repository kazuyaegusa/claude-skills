# subagent-catalogスキルで会話形式のエージェント検索・取得

> Claude Codeスキルとしてsubagent-catalogを導入し、`/subagent-catalog:search <query>`でエージェントを検索、`/subagent-catalog:fetch <name>`で定義を取得する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

READMEやGitHubを開かずに、会話内でエージェントカタログを検索・ブラウズでき、見つけたエージェントの完全な定義をその場で取得して即座に利用開始できる

## いつ使うのか

開発中にリアルタイムでエージェントを探したい時、エージェントの詳細（ツール権限、モデル、プロンプト内容）を確認してから使いたい時

## やり方

1. `cp -r tools/subagent-catalog ~/.claude/commands/` でスキルをインストール
2. Claude Codeで `/subagent-catalog:search python` のように検索（名前・説明・カテゴリでマッチング）
3. `/subagent-catalog:fetch python-pro` で完全なエージェント定義を取得
4. `/subagent-catalog:list` で全カテゴリ一覧、`/subagent-catalog:invalidate` でキャッシュリフレッシュ

### 入力

- subagent-catalogスキルがインストール済み
- 検索クエリ（エージェント名、説明キーワード、カテゴリ）

### 出力

- マッチしたエージェントのリストまたは完全な定義

## 使うツール・ライブラリ

- subagent-catalog skill

## コード例

```
/subagent-catalog:search kubernetes
/subagent-catalog:fetch kubernetes-specialist
/subagent-catalog:list
/subagent-catalog:invalidate
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
