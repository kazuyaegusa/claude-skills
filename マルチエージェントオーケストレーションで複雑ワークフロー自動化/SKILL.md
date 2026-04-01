# マルチエージェントオーケストレーションで複雑ワークフロー自動化

> voltagent-metaカテゴリのオーケストレーションエージェント（multi-agent-coordinator, workflow-orchestrator, pied-piper等）を使い、複数のサブエージェントを連携させてSDLCワークフロー全体を自動化する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

単一エージェントでは対応できない複雑なタスク（設計→実装→テスト→レビュー→デプロイ）を、専門エージェント間で役割分担・連携させることで、高品質かつ効率的に実行できる

## いつ使うのか

新機能開発・バグ修正・リファクタリングなど、複数フェーズにまたがるタスクを一貫したワークフローで自動化したい時。繰り返し発生するSDLCパターンをテンプレート化したい時

## やり方

1. `claude plugin install voltagent-meta` でオーケストレーションエージェントをインストール
2. 他カテゴリ（lang, infra, qa-sec等）も必要に応じてインストール
3. Claude Codeで「Use multi-agent-coordinator to design, implement, test, and deploy feature X」のように指示
4. コーディネーターエージェントが適切なサブエージェント（api-designer → backend-developer → test-automator → code-reviewer → deployment-engineer）を順次または並列で呼び出し、ワークフロー全体を管理

### 入力

- voltagent-metaとタスクに必要な他カテゴリのエージェントがインストール済み
- 実行したいワークフローの明確な定義（例: 設計→実装→テスト→デプロイ）

### 出力

- 複数エージェントが協調して完成させた機能・修正
- 各フェーズの成果物（設計ドキュメント、コード、テストレポート、デプロイログ）

## 使うツール・ライブラリ

- multi-agent-coordinator
- workflow-orchestrator
- pied-piper
- taskade

## コード例

```
# Claude Code内で
> Use multi-agent-coordinator to orchestrate: api-designer → backend-developer → test-automator → code-reviewer → deployment-engineer for implementing user authentication feature
```

## 前提知識

- Claude Codeがインストール・セットアップ済み
- サブエージェントの概念理解（独立したコンテキストウィンドウ、ドメイン特化プロンプト、ツール権限管理）
- 基本的なCLI操作（curl, chmod, git clone等）
- YAMLフロントマター形式の理解（サブエージェント定義ファイルの編集時）
- Claude Codeの /agents コマンドとサブエージェント呼び出し構文の理解

## 根拠

> "This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks."

> "Shared Across Projects: After creating a subagent, you can utilize it throughout various projects and distribute it among team members"

> "Each subagent includes a `model` field that automatically routes it to the right Claude model — balancing quality and cost"

> "Project Subagents: `.claude/agents/` Current project only, Higher precedence"

> "Global Subagents: `~/.claude/agents/` All projects, Lower precedence"
