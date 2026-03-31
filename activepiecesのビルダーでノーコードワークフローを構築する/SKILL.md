# Activepiecesのビルダーでノーコードワークフローを構築する

> Activepiecesのビルダー（ノーコードUI）を使い、Loops、Branches、Auto Retries、HTTP、Code with NPMなどの機能を組み合わせてワークフローを作成する

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: automation-pipeline

## なぜ使うのか

開発者がpieceを用意すれば、非技術者でもビルダーUIから200以上の統合を使ってワークフローを組み立てられる。AIによるコード補助（ASK AI in Code Piece）により、プログラミング知識なしでデータ処理も可能

## いつ使うのか

非技術者がワークフロー自動化を行いたい、または技術者が迅速にプロトタイプを作りたい場合

## やり方

1. Activepiecesにログイン（セルフホストまたはクラウド版）
2. ビルダーUIでTriggerを選択（例：RSS、Chat Interface、Form Interface）
3. Actionsを追加（例：Google Sheets書き込み、Discord通知）
4. Loops、Branchesで条件分岐・繰り返しを設定
5. ASK AI in Code Pieceで自然言語指示からコードを生成
6. Auto Retriesで障害時自動リトライ設定
7. Human-in-the-loopで承認フローを挟む
8. フローをバージョン管理し、テンプレート化

### 入力

- 統合したいサービスのアカウント情報
- ワークフローの要件

### 出力

- 実行可能なワークフロー
- 再利用可能なテンプレート

## 使うツール・ライブラリ

- Activepiecesビルダー
- 200+ pieces（Google Sheets、OpenAI、Discord、RSS等）

## 前提知識

- TypeScriptの基礎知識（piece開発の場合）
- Docker/Kubernetesの基本操作（セルフホストの場合）
- ワークフロー自動化の概念理解
- MCPプロトコルの基本理解（LLM統合の場合）

## 根拠

> All-in-one AI automation designed to be extensible through a type-safe pieces framework written in TypeScript.

> When you contribute pieces to Activepieces they become automatically available as MCP servers that you can use with LLMs through Claude Desktop, Cursor or Windsurf!

> Largest open source MCP toolkit: All our pieces (280+) are available as MCP that you can use with LLMs on Claude Desktop, Cursor or Windsurf.

> Pieces are npm packages in TypeScript, offering full customization with the best developer experience, including hot reloading for local piece development on your machine.

> ASK AI in Code Piece (Non technical user can clean data without knowing to code)
