# LiteLLMを推論ゲートウェイとして利用する

> 複数のAI providerへのアクセスをLiteLLMで統一し、推論リクエストのルーティング・認証・レート制限を一元管理する

- 出典: https://x.com/rna4219/status/2035464954632093802
- 投稿者: ゲノムちゃん
- カテゴリ: other

## なぜ使うのか

各providerの認証方式やAPIエンドポイントが異なると、worker側で個別対応が必要になり保守が困難。LiteLLMで抽象化することで、providerの追加・変更が容易になる

## いつ使うのか

複数のAI providerを利用し、認証・ルーティング・レート制限を一元管理したいとき

### 具体的な適用場面

- 複数のAIコーディングエージェント（Codex, Claude Code, Antigravity等）を並行運用している
- AIエージェントのタスク進捗が不透明で、途中経過や責務境界が追えない
- plan/dev/acceptanceの区切りが曖昧で、失敗時の再実行や承認判断が属人化している
- agent-to-agentの無限委譲で制御が効かなくなるリスクを回避したい
- GitHub/tracker連携はあるが、状態と成果物の紐付けが散らばっている

## やり方

1. shipyard-cp backend内でLiteLLMを設定 2. 各provider（Claude, OpenAI, GLM-5等）のAPIキーをLiteLLM configに登録 3. worker側は統一されたLiteLLM APIエンドポイントを呼び出すだけ 4. LiteLLMがprovider選択・認証・レート制限を自動処理

### 入力

- 各providerのAPIキー
- LiteLLM config

### 出力

- 統一された推論APIエンドポイント
- provider横断のレート制限・audit log

## 使うツール・ライブラリ

- LiteLLM
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
