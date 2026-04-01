# Claude CodeをDeerFlowに連携

> DeerFlowのサブエージェントとしてClaude Codeを呼び出し、コーディングタスクをClaude Codeに委任する。

- 出典: https://x.com/dify_base/status/2031190239885353023
- 投稿者: AX Base| AX情報発信メディア
- カテゴリ: claude-code-workflow

## なぜ使うのか

DeerFlowのオーケストレーションとClaude Codeのコーディング能力を組み合わせることで、調査→コード生成→実行の自律ループをより高精度に構築できるため。

## いつ使うのか

DeerFlowワークフロー内でコード生成・修正・デバッグが必要な場面

### 具体的な適用場面

- コード生成・実行を含む複合タスクをAIに自律処理させたい場合
- 過去の調査結果や判断履歴をエージェントに持続的に参照させたいワークフロー構築時

## やり方

1. DeerFlowの設定ファイルにClaude Code用のサブエージェント定義を追加 2. `ANTHROPIC_API_KEY` または Claude Code CLIのパスを環境変数で渡す 3. コーディングタスクが検出されると自動的にClaude Codeサブエージェントへルーティングされる 4. Claude Codeの出力がオーケストレーターに返され、後続ステップへ渡される

### 入力

- コーディングタスクの指示テキスト
- ANTHROPIC_API_KEY または Claude Code CLI

### 出力

- 生成・修正されたコード、またはコード実行結果

## 使うツール・ライブラリ

- DeerFlow (bytedance/deer-flow)
- Claude Code CLI
- Anthropic SDK

## 前提知識

- Python 3.x および pip の基本操作
- Dockerの基本知識（サンドボックス実行を使う場合）
- LLMエージェント・ツール呼び出しの概念理解
- Claude Code CLI または Anthropic APIキー（Claude Code連携を使う場合）

## 根拠

> ByteDanceがオープンソースのAIエージェント基盤「DeerFlow」を公開。

> サブエージェントの自動振り分け

> サンドボックスでコード実行

> 長期メモリ搭載

> Claude Code連携も対応
