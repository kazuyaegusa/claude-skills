# DeerFlowでサブエージェントを自動振り分ける

> タスクの種別（調査・コード生成・レポート作成など）をオーケストレーターが判定し、対応する専門サブエージェントへ自動的にルーティングする

- 出典: https://x.com/dify_base/status/2031190239885353023
- 投稿者: AX Base| AX情報発信メディア
- カテゴリ: agent-orchestration

## なぜ使うのか

タスクごとに異なるツール・プロンプト・モデルを持つ専門エージェントに委譲することで、単一の汎用エージェントより精度と効率が上がる

## いつ使うのか

1タスクの中に調査・実装・要約など複数の専門処理が混在しており、シングルエージェントでは精度が落ちるとき

### 具体的な適用場面

- 複数ステップの調査・コード生成・検証を含む自律ワークフローをPythonで構築したいとき
- Claude Codeを既存のマルチエージェントパイプラインに組み込んでコーディングタスクを委譲したいとき
- エージェントが生成したコードをホスト環境に影響させず安全に実行したいとき

## やり方

1. `git clone https://github.com/bytedance/deer-flow && cd deer-flow` でリポ取得
2. `pip install -r requirements.txt`（またはuvなら `uv sync`）
3. `conf.yaml` にLLMプロバイダー設定を記述（例: model: claude-3-5-sonnet）
4. `python main.py` で起動するとオーケストレーターが入力タスクを受け取り、researcher/coder/reporter等のサブエージェントへ自動割り当て

### 入力

- タスク記述テキスト
- conf.yaml（LLMプロバイダー設定）

### 出力

- 各サブエージェントの処理結果を統合した最終レスポンス

## 使うツール・ライブラリ

- DeerFlow (bytedance/deer-flow)
- Python 3.10+

## 前提知識

- Python 3.10以上の実行環境
- git によるリポジトリクローン操作の知識
- LLMプロバイダーのAPIキーまたはClaude Code subscription認証
- Dockerの基礎知識（サンドボックス実行を使う場合）

## 根拠

> 「ByteDanceがオープンソースのAIエージェント基盤「DeerFlow」を公開」

> 「サブエージェントの自動振り分け」

> 「サンドボックスでコード実行」

> 「長期メモリ搭載」

> 「Claude Code連携も対応」
