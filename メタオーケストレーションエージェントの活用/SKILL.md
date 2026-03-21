# メタオーケストレーションエージェントの活用

> multi-agent-coordinator等のメタエージェントを使い、複数の専門エージェントを動的に起動・調整して複雑なタスクを分散処理する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

単一エージェントでは手に負えない大規模タスク（例：フルスタック機能開発、セキュリティ監査+修正）を、専門家チームとして効率的に処理できる

## いつ使うのか

複数ドメインにまたがる大規模機能開発、エンドツーエンドのワークフロー自動化、複数専門家の意見を統合したい時

## やり方

1. `voltagent-meta` カテゴリから `multi-agent-coordinator` や `workflow-orchestrator` をインストール
2. 他のカテゴリ（voltagent-lang、voltagent-infra等）も併せてインストール（メタエージェントが起動する専門家が必要なため）
3. Claude Codeで「この機能をフロントエンド・バックエンド・インフラに分けて実装」のように依頼
4. multi-agent-coordinatorが自動的にfrontend-developer、backend-developer、devops-engineer等を起動・調整
5. 各エージェントの成果物を統合して最終成果物を返す

### 入力

- 高レベルのタスク記述（例：「認証機能を追加してCI/CDまで設定」）
- 利用可能な専門エージェント群（他カテゴリからインストール済み）

### 出力

- 複数エージェントが協調した成果物
- 各エージェントの作業履歴（トレーサビリティ）

## 使うツール・ライブラリ

- multi-agent-coordinator
- workflow-orchestrator
- task-distributor

## コード例

```
# メタエージェントのインストール
claude plugin install voltagent-meta

# 専門家エージェントも併せてインストール
claude plugin install voltagent-lang
claude plugin install voltagent-infra

# Claude Codeでの使用例
> "Have multi-agent-coordinator implement a full-stack user authentication feature with frontend, backend, and database migration"
```

## 前提知識

- Claude Codeの基本的な使い方（サブエージェント機能の理解）
- YAMLフロントマターとMarkdownの読み書き
- コマンドラインツール（claude CLI、curl、bash）の操作経験
- 開発ドメイン知識（各サブエージェントを効果的に使うため、対象領域の基礎理解が必要）

## 根拠

> 「This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.」

> 「model field that automatically routes it to the right Claude model — balancing quality and cost: opus (Deep reasoning), sonnet (Everyday coding), haiku (Quick tasks)」

> 「Project Subagents: .claude/agents/ (Current project only, Higher precedence) / Global Subagents: ~/.claude/agents/ (All projects, Lower precedence)」
