# Claude CodeをDeerFlowに連携する

> DeerFlowのサブエージェントの一つとしてClaude Codeを呼び出し、コーディングタスクをClaude Codeに委譲するパイプラインを構成する

- 出典: https://x.com/dify_base/status/2031190239885353023
- 投稿者: AX Base| AX情報発信メディア
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeはファイル編集・テスト実行・git操作など実際の開発ワークフローに特化しており、DeerFlowのオーケストレーション層と組み合わせることで「リサーチ→設計→実装」の一気通貫自動化が可能になる

## いつ使うのか

DeerFlowのマルチエージェントパイプラインで、実際のコードベース変更・テスト実行・git操作を含むタスクをClaude Codeに任せたいとき

### 具体的な適用場面

- リサーチ・コード生成・データ分析など異種タスクが混在するAIワークフローを構築するとき
- エージェントにコードを実行させる必要があるが、ホストマシンを汚したくないとき
- 複数セッションにまたがる文脈（ユーザー履歴・過去の調査結果）をエージェントに保持させたいとき
- Claude Codeを既存のマルチエージェントパイプラインに組み込みたいとき

## やり方

1. Claude CLIをインストール: `npm install -g @anthropic-ai/claude-code`
2. DeerFlowのエージェント設定ファイルでClaude Codeをコーダーエージェントとして登録（具体的な設定構造は公式リポジトリのドキュメントを参照）
3. DeerFlowがコーディングタスクを検出した際にClaude Codeプロセスを呼び出す形で統合
4. 環境変数 `ANTHROPIC_AUTH_TOKEN` または Claude Code subscriptionで認証
5. 実行例のイメージ: DeerFlowのplanner → coderエージェントに振り分け → Claude Codeがファイル編集・テスト実行 → 結果をDeerFlowに返す

### 入力

- Claude CLI (npm install -g @anthropic-ai/claude-code)
- Anthropic認証情報
- DeerFlowのエージェント設定

### 出力

- Claude Codeによる実際のファイル変更・テスト結果

## 使うツール・ライブラリ

- DeerFlow (bytedance/deer-flow)
- Claude Code (claude CLI)
- Node.js

## 前提知識

- Python 3.10+ の実行環境
- LLMプロバイダー（OpenAI / Anthropic等）のAPIキー
- Docker（サンドボックス実行を使う場合）
- Node.js（Claude Code連携を使う場合）
- マルチエージェントアーキテクチャの基本概念（オーケストレーター・サブエージェント・ツール呼び出し）

## 根拠

> ByteDanceがオープンソースのAIエージェント基盤「DeerFlow」を公開

> タスクをエージェントが自律的に処理

> サブエージェントの自動振り分け

> サンドボックスでコード実行

> 長期メモリ搭載
