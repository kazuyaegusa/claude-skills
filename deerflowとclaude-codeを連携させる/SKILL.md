# DeerFlowとClaude Codeを連携させる

> DeerFlowエージェントのコーディングタスクをClaude Code（claude CLI）に委譲し、ファイル操作・コード生成・実行を任せる。

- 出典: https://x.com/dify_base/status/2031190239885353023
- 投稿者: AX Base| AX情報発信メディア
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeはコーディングに特化しており、ファイルシステムへのアクセスやコード実行を得意とする。DeerFlowのオーケストレーション能力とClaude Codeの実装能力を組み合わせると、調査→実装→検証の自律サイクルが実現できる。

## いつ使うのか

DeerFlowの調査・計画エージェントが立案したコーディングタスクを、Claude Codeに実装させたいとき

### 具体的な適用場面

- 複数の専門エージェント（検索・コーディング・データ分析）を組み合わせた自律リサーチパイプラインを構築するとき
- LLMにコードを生成させてサンドボックス内で即座に実行・検証するコーディングエージェントを作るとき
- セッションをまたいで過去の調査結果や判断を参照する長期タスクエージェントを構築するとき

## やり方

1. Claude CLIをインストール: `npm install -g @anthropic-ai/claude-code`。2. DeerFlowの設定でClaude Codeをコーディングサブエージェントとして登録する（具体的な設定キーはDeerFlow公式参照）。3. タスクにコーディング要素が含まれると、DeerFlowが `claude -p` コマンド経由でClaude Codeを呼び出す。4. Claude Codeの実行結果がDeerFlowのパイプラインに返される。

### 入力

- コーディングタスクの仕様
- 対象ディレクトリのパス

### 出力

- 実装されたコードファイル
- 実行結果

## 使うツール・ライブラリ

- DeerFlow (ByteDance OSS)
- claude CLI (Claude Code)

## コード例

```
claude -p "${TASK_DESCRIPTION}" --output-format json
```

## 前提知識

- Pythonの基本的な実行環境（Python 3.x）
- LLMプロバイダーのAPIキー（OpenAI / Anthropic 等）
- マルチエージェントシステムの基本概念（オーケストレーター・サブエージェントの役割分担）
- DeerFlowのGitHubリポジトリへのアクセス（具体的な設定スキーマの確認に必要）

## 根拠

> 「ByteDanceがオープンソースのAIエージェント基盤『DeerFlow』を公開」

> 「サブエージェントの自動振り分け」

> 「サンドボックスでコード実行」

> 「長期メモリ搭載」

> 「Claude Code連携も対応」
