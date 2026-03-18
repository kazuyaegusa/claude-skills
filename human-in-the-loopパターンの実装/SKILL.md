# Human-in-the-Loopパターンの実装

> ワークフロー実行中に承認待ちや遅延を挿入し、人間の判断を介入させるpieceを実装

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: automation-pipeline

## なぜ使うのか

完全自動化が危険な場合や、人間の判断が必要なケース(支払い承認、重要データ削除等)で、自動化と人間制御を両立するため

## いつ使うのか

金融取引、データ削除、外部公開、権限変更等、誤実行がリスクを伴う自動化を行う場合

## やり方

1. Activepiecesビルダーで承認ステップ用のpieceを追加(公式提供)
2. フロー中で承認トリガーを設定(例: 「金額>10万円なら承認待ち」)
3. 承認待ち時にメール/Slack等で通知
4. 承認者がActivepieces UIまたはAPI経由で承認/却下
5. 承認後、フローが後続ステップを実行
6. 却下時はフロー停止またはエラーハンドリング

### 入力

- 承認対象のデータ(金額、操作内容等)
- 承認者の連絡先(メール/Slack等)

### 出力

- 承認/却下の結果
- 承認ログ

## 使うツール・ライブラリ

- Activepieces approval piece
- メール/Slack通知piece

## コード例

```
// フロー例(疑似コード)
if (amount > 100000) {
  await approvalPiece.requestApproval({
    message: `${amount}円の支払いを承認しますか?`,
    approvers: ['admin@example.com']
  });
}
// 承認後のみ後続実行
```

## 前提知識

- TypeScript基礎知識
- REST API統合の基本理解
- Docker/npmの基本操作
- MCPプロトコルの概念(Claude Desktop等LLMツールとの統合前提)
- ワークフロー自動化の基礎(トリガー、アクション、条件分岐)
- オープンソースプロジェクトへのコントリビューション経験(任意)
