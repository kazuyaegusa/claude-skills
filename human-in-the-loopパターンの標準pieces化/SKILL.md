# Human-in-the-loopパターンの標準pieces化

> 承認待ち、遅延実行、人間入力（チャット、フォーム）をpiecesとして標準実装し、AIワークフローに組み込めるようにする

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: automation-pipeline

## なぜ使うのか

完全自動化できない業務や、人間の判断が必要な場面でもAIワークフローを活用できるようにするため

## いつ使うのか

AIが判断できない場面で人間の介入が必要な場合、段階的な自動化を進めたい場合、コンプライアンス上の承認が必要な場合

## やり方

1. Delay Executionピースで指定時間の待機を実装
2. Require Approvalピースで承認フローを実装
3. Chat Interfaceピースで対話的な入力を受け付ける
4. Form Interfaceピースで構造化データを入力する
5. これらをpiecesフレームワーク上に構築することで、他のpiecesと同様にワークフローに組み込めるようにする

### 入力

- 承認条件、遅延時間、入力フォームスキーマ

### 出力

- 人間の承認結果、入力データ、遅延後の実行継続

## 使うツール・ライブラリ

- Activepieces pieces framework
- Chat Interface piece
- Form Interface piece

## 前提知識

- TypeScriptの基本知識
- Model Context Protocol（MCP）の概念理解
- Claude DesktopやCursorなどMCP対応ツールの使用経験
- npmパッケージの作成・公開方法
- ワークフロー自動化の基本概念（トリガー、アクション、データ変換）
- Docker/コンテナ技術の基本（セルフホスト時）

## 根拠

> "🧠 Human in the Loop: Delay execution for a period of time or require approval. These are just pieces built on top of the piece framework"

> "💻 Human Input Interfaces: Built-in support for human input triggers like 'Chat Interface' 💬 and 'Form Interface' 📝"
