# 有限ネストで責務境界を制御する

> agent-to-agentの委譲を無限に許さず、有限ネストを前提にtaskの深さと責務を制御する

- 出典: https://x.com/rna4219/status/2035464954632093802
- 投稿者: ゲノムちゃん
- カテゴリ: agent-orchestration

## なぜ使うのか

無限委譲を許すと制御が効かなくなり、どのagentがどこまで担当しているか不明瞭になり、失敗時の切り分けや再実行が困難になるため

## いつ使うのか

agentがagentを呼ぶような構成で、委譲の深さや責務境界が曖昧になりやすい場合

### 具体的な適用場面

- 複数のAIコーディングエージェント（Codex, Claude Code, Antigravity等）を並行運用している
- AIエージェントのタスク進捗が不透明で、途中経過や責務境界が追えない
- plan/dev/acceptanceの区切りが曖昧で、失敗時の再実行や承認判断が属人化している
- agent-to-agentの無限委譲で制御が効かなくなるリスクを回避したい
- GitHub/tracker連携はあるが、状態と成果物の紐付けが散らばっている

## やり方

1. shipyard-cpでtaskを作成時に、ネスト深さの上限を設定 2. control planeが委譲階層を追跡し、上限到達時は自動でエスカレーションまたはエラー通知 3. 各ステージ（plan/dev/acceptance等）で責務を明確に区切り、委譲先agentの範囲を制限

### 入力

- task定義（ネスト深さ上限含む）
- 委譲先agentの仕様

### 出力

- 制御された委譲階層
- 責務境界が明確なtask構造

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
