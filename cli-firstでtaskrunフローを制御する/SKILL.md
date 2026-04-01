# CLI-firstでtask/runフローを制御する

> Web UIは補助的に留め、主要な操作（task作成、進捗確認、ステージ移行）をCLIコマンドで完結させる

- 出典: https://x.com/rna4219/status/2035464954632093802
- 投稿者: ゲノムちゃん
- カテゴリ: automation-pipeline

## なぜ使うのか

実務ではCLI操作が速く、スクリプト化・自動化しやすい。UIは状態確認の補助に留めることで、運用の属人化を防ぐ

## いつ使うのか

AIワーカーの運用を自動化・スクリプト化したい、または属人化を防ぎたいとき

### 具体的な適用場面

- 複数のAIコーディングエージェント（Codex, Claude Code, Antigravity等）を並行運用している
- AIエージェントのタスク進捗が不透明で、途中経過や責務境界が追えない
- plan/dev/acceptanceの区切りが曖昧で、失敗時の再実行や承認判断が属人化している
- agent-to-agentの無限委譲で制御が効かなくなるリスクを回避したい
- GitHub/tracker連携はあるが、状態と成果物の紐付けが散らばっている

## やり方

1. `.claude/commands/run.md`を参照してtask作成コマンドを実行 2. `status`コマンドで進捗確認: 現在のステージ（plan/dev/acceptance等）と状態を表示 3. `pipeline`コマンドでフロー全体を可視化: plan→dev→acceptance→integrate→publishの流れを追跡 4. 必要時のみWeb UIで補助確認（http://localhost:3000）

### 入力

- task定義
- 実行したいコマンド（run/status/pipeline等）

### 出力

- CLIからのtask作成・進捗確認・フロー追跡結果
- スクリプト化可能な操作履歴

## 使うツール・ライブラリ

- shipyard-cp CLI
- Claude Code commands
- Codex commands

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
