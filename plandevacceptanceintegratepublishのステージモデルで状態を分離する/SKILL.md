# plan→dev→acceptance→integrate→publishのステージモデルで状態を分離する

> taskをplan（計画）、dev（開発）、acceptance（受入）、integrate（統合）、publish（公開）の5ステージに分割し、各ステージで状態と成果物を明確に管理する

- 出典: https://x.com/rna4219/status/2035464954632093802
- 投稿者: ゲノムちゃん
- カテゴリ: other

## なぜ使うのか

曖昧な「途中経過」ではなく、明確なステージで区切ることで、どこまで進んでいるか、どこで失敗したかが追いやすくなり、再実行や承認判断が属人化しない

## いつ使うのか

AIエージェントの作業過程が不透明で、途中経過や失敗箇所が追えないとき

### 具体的な適用場面

- 複数のAIコーディングエージェント（Codex, Claude Code, Antigravity等）を並行運用している
- AIエージェントのタスク進捗が不透明で、途中経過や責務境界が追えない
- plan/dev/acceptanceの区切りが曖昧で、失敗時の再実行や承認判断が属人化している
- agent-to-agentの無限委譲で制御が効かなくなるリスクを回避したい
- GitHub/tracker連携はあるが、状態と成果物の紐付けが散らばっている

## やり方

1. task作成時にplanステージから開始 2. planで要件定義・設計を完了したらdevステージへ移行 3. devで実装完了後、acceptanceステージで受入テスト 4. acceptanceパス後、integrateステージでmain branchへの統合 5. publishステージでリリース・デプロイ 6. 各ステージの状態と成果物は`status`コマンドで確認可能

### 入力

- task定義
- 各ステージの完了条件

### 出力

- 各ステージの状態（pending/in-progress/completed/failed等）
- ステージごとの成果物（plan文書、コード、テスト結果等）

## 使うツール・ライブラリ

- shipyard-cp

## 前提知識

- Node.js 20以上の環境
- pnpmパッケージマネージャ
- Claude CodeまたはCodexの基本的な使い方
- LiteLLMの概要理解
- task/runベースのワークフロー概念

## 根拠

> 「複数の AI provider / worker を上流でオーケストレーションするためのツール」

> 「Codex / Claude Code などを task / run ベースで扱い、実務フローに載せやすくすることを狙っています」

> 「LiteLLM を推論ゲートウェイとして使い、Codex / Claude Code / Google Antigravity / GLM-5 系ワーカーを、共通の task / run / gate / audit モデル上で制御します」

> 「どの task が今どこまで進んでいるか分からない」「plan / dev / acceptance の区切りが曖昧」「agent に agent を呼ばせるような構成で、委譲の深さや責務境界が曖昧になりやすい」

> 「無限委譲ではなく有限ネストを前提にして、task の深さと責務を制御する」
