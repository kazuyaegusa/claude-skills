# メタオーケストレーションエージェントで複数subagentを連携させる

> voltagent-metaカテゴリのエージェント（multi-agent-coordinator, workflow-orchestrator等）を使い、複数の専門subagentを協調動作させる

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

複雑なタスクは単一の専門家では解決できないため、タスク分割→適切なsubagent割り当て→結果統合のフローを自動化することで、大規模ワークフローを効率的に実行できる

## いつ使うのか

アーキテクチャ設計→実装→テスト→デプロイのような複数フェーズのタスク時、複数の専門領域にまたがる大規模リファクタリング時

## やり方

1. `claude plugin install voltagent-meta`でメタオーケストレーションエージェントを導入
2. 他カテゴリ（voltagent-lang, voltagent-infra等）のsubagentも併せてインストール
3. メタエージェント（multi-agent-coordinator等）に複雑なタスクを依頼
4. メタエージェントが自動的にタスクを分解し、適切な専門subagentを起動・調整
5. 結果を統合してユーザーに返す

### 入力

- 複雑なマルチステップタスク
- 複数の専門領域にまたがる要件

### 出力

- coordinated subagent群による統合的な成果物
- タスク分割と進捗管理の自動化

## 使うツール・ライブラリ

- voltagent-meta plugin
- multi-agent-coordinator
- workflow-orchestrator
- task-distributor

## コード例

```
# メタオーケストレーションプラグインをインストール
claude plugin install voltagent-meta

# 他の専門家プラグインも導入
claude plugin install voltagent-lang
claude plugin install voltagent-infra

# メタエージェントに複雑なタスクを依頼
> Use multi-agent-coordinator to refactor this monolith into microservices with full test coverage
```

## 前提知識

- Claude Codeの基本的な使用経験
- subagentの概念理解（独立したコンテキストを持つ専門AIアシスタント）
- YAML frontmatterの基本構文
- コマンドラインツール（curl, git）の基本操作
- 対象言語・フレームワークの基礎知識（各subagent活用時）

## 根拠

> 「claude plugin marketplace add VoltAgent/awesome-claude-code-subagents」「claude plugin install voltagent-lang」
