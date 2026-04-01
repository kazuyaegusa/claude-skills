# DeerFlowとClaude Codeを連携させる

> DeerFlowエージェント基盤のバックエンドとしてClaude Codeを使用し、コーディング能力の高いエージェントを構築する

- 出典: https://x.com/dify_base/status/2031190239885353023
- 投稿者: AX Base| AX情報発信メディア
- カテゴリ: claude-code-workflow

## なぜ使うのか

DeerFlowのオーケストレーション能力とClaude Codeのコーディング能力を組み合わせることで、複雑なソフトウェア開発タスクを自律処理できるようになるため

## いつ使うのか

コード生成・リファクタリング・デバッグを含む複合タスクをDeerFlowで自動化したいとき

### 具体的な適用場面

- 複数の専門エージェント（コード生成・検索・分析）を自動選択して一連のリサーチタスクを処理したいとき
- AIエージェントにコードを実行させる必要があるが、ホスト環境を汚染したくないとき
- 複数セッションにまたがる長期プロジェクトで文脈を保持しながらエージェントを動かしたいとき

## やり方

1. DeerFlowの設定でLLMバックエンドとしてClaude Codeを指定
2. `ANTHROPIC_API_KEY` または Claude Code subscription認証を設定
3. DeerFlowのエージェントがコーディングタスクを受け取った際にClaude Codeへルーティング
※具体的な設定キー名は投稿に記載なし。リポのREADMEで確認要

### 入力

- Claude Code API認証情報
- DeerFlow設定ファイル

### 出力

- Claude Codeが処理したコード生成・修正結果

## 使うツール・ライブラリ

- DeerFlow (ByteDance OSS)
- Claude Code (Anthropic)

## 前提知識

- AIエージェントの基本概念（LLM・ツール呼び出し・エージェントループ）
- Pythonまたはエージェントフレームワークの基礎
- Dockerまたはコンテナの基礎（サンドボックス利用時）
- Claude Code または Anthropic API の利用環境（Claude Code連携時）

## 根拠

> 「ByteDanceがオープンソースのAIエージェント基盤「DeerFlow」を公開」

> 「サブエージェントの自動振り分け」

> 「サンドボックスでコード実行」

> 「長期メモリ搭載」

> 「Claude Code連携も対応」
