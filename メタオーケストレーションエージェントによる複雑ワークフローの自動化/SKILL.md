# メタオーケストレーションエージェントによる複雑ワークフローの自動化

> Meta & Orchestrationカテゴリのエージェント（multi-agent-coordinator, workflow-orchestrator, task-distributor等）を使い、複数のサブエージェントを組み合わせた複雑なワークフローを自動化する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

単一のタスクではなく、「設計→実装→テスト→レビュー→デプロイ」のような多段階プロセスを一括で実行したい場合、各段階に最適なエージェントを順次起動し、前段の出力を次段の入力として連携させることで、手動調整の手間を削減し、再現性と品質を向上できる

## いつ使うのか

反復的なSDLCワークフローを自動化したい場合、複数の専門家エージェントの知見を統合して意思決定したい場合、大規模リファクタリングやマイクレーション等の長期プロジェクトを段階的に進める場合

## やり方

1. `voltagent-meta`プラグインをインストールして、オーケストレーション用エージェント群を利用可能にする
2. 実行したいワークフローを定義（例: APIエンドポイント追加 = api-designer → backend-developer → test-automator → code-reviewer → deployment-engineer）
3. multi-agent-coordinatorまたはworkflow-orchestratorに対して、ワークフロー全体を記述した指示を与える
4. オーケストレーターが各段階で適切なサブエージェントを起動し、出力を次の段階に渡す
5. 最終結果をメイン会話に統合

### 入力

- ワークフロー定義（各段階とそれに対応するエージェント）
- 各段階の入力・出力仕様

### 出力

- 多段階ワークフローの自動実行結果
- 各段階の中間成果物
- 統合された最終成果物

## 使うツール・ライブラリ

- voltagent-meta プラグイン
- multi-agent-coordinator, workflow-orchestrator, task-distributor等のエージェント
- Pied Piper（SDLC反復ワークフロー専用）
- Taskade MCP（リアルタイムコラボレーション対応）

## コード例

```
# メタオーケストレーションエージェントの利用例
> Use the workflow-orchestrator to:
> 1. Have api-designer create OpenAPI spec for user registration
> 2. Have backend-developer implement the endpoint
> 3. Have test-automator write integration tests
> 4. Have security-auditor review for vulnerabilities
> 5. Have code-reviewer check code quality
> 6. Have deployment-engineer prepare deployment config
```

## 前提知識

- Claude Code CLI がインストールされていること
- Claude Codeの基本操作（エージェント起動、ツール実行）の理解
- YAMLフロントマターの基本構文知識（エージェントカスタマイズ時）
- gitの基本操作（リポジトリクローン、ファイルコピー）
- 対象プロジェクトの技術スタックと開発フローの把握

## 根拠

> 「127+ subagents across 10 categories: Core Development, Language Specialists, Infrastructure, Quality & Security, Data & AI, Developer Experience, Specialized Domains, Business & Product, Meta & Orchestration, Research & Analysis」
