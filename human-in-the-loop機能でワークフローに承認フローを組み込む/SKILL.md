# Human-in-the-Loop機能でワークフローに承認フローを組み込む

> Activepiecesの「遅延実行」「承認待ち」「チャットインターフェース」「フォームインターフェース」pieceを使って、自動化の途中で人間の判断を挟む

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: automation-pipeline

## なぜ使うのか

完全自動化できない・すべきでない業務（契約承認、高額決済、顧客対応等）において、適切なタイミングで人間の判断を挟むことで、自動化と制御のバランスを取る

## いつ使うのか

高リスクな操作（決済、削除、公開等）の前に承認を挟みたい時、顧客や上司からの追加情報が必要な時

## やり方

1. Activepiecesのノーコードビルダーでワークフローを作成
2. 承認が必要なポイントで「Approval」pieceを挿入
3. または「Delay」pieceで一定時間待機させる
4. 「Chat Interface」または「Form Interface」pieceで人間からの入力を受け付ける
5. 入力内容に基づいて後続のワークフローを分岐

### 入力

- 承認を必要とするワークフローのトリガー
- 承認者のメールアドレスまたはチャット連絡先

### 出力

- 承認・却下の判断結果
- 人間が入力したフォームデータ

## 使うツール・ライブラリ

- Activepieces Approval piece
- Activepieces Delay piece
- Activepieces Chat Interface piece
- Activepieces Form Interface piece

## 前提知識

- TypeScript / npmの基礎知識（piece開発時）
- MCP (Model Context Protocol)の概念理解（LLM統合時）
- Claude Desktop / Cursor / Windsurfのいずれかの利用経験（LLMからの利用時）
- ワークフロー自動化ツール（Zapier等）の利用経験
