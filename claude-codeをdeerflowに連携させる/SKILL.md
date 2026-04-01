# Claude CodeをDeerFlowに連携させる

> DeerFlowのコーダーサブエージェントとしてClaude Codeを呼び出し、コーディングタスクをClaude Codeに委譲する

- 出典: https://x.com/dify_base/status/2031190239885353023
- 投稿者: AX Base| AX情報発信メディア
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeはファイル読み書き・コマンド実行・コードベース横断操作に特化しており、DeerFlowのオーケストレーション層と組み合わせることで、調査→実装→検証の全サイクルを自動化できる

## いつ使うのか

DeerFlowのワークフロー内でコードベース操作・実装・テスト実行を自律的に行わせたいとき

### 具体的な適用場面

- 複数ステップの調査・コード生成・検証を含む自律ワークフローをPythonで構築したいとき
- Claude Codeを既存のマルチエージェントパイプラインに組み込んでコーディングタスクを委譲したいとき
- エージェントが生成したコードをホスト環境に影響させず安全に実行したいとき

## やり方

1. conf.yamlのコーダーサブエージェント設定でClaude Codeのエンドポイントを指定
2. `claude -p` コマンド（非対話モード）を呼び出すアダプターをDeerFlowに登録
3. オーケストレーターがコーディングタスクを検知した際にClaude Codeサブエージェントへルーティングされる
※ANTHROPIC_API_KEYは使わず、Claude Codeのsubscription認証（setup-token）を使用

### 入力

- コーディングタスク記述
- Claude Code CLI（インストール済み）
- conf.yamlのclaude-code連携設定

### 出力

- 実装コード
- テスト結果
- ファイル変更差分

## 使うツール・ライブラリ

- DeerFlow (bytedance/deer-flow)
- Claude Code CLI
- claude -p（非対話モード）

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
