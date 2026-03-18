# オープンエコシステムでのpiece共有

> 開発したpieceをnpmjs.comに公開し、コミュニティと共有する。60%の統合がコミュニティ貢献

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: automation-pipeline

## なぜ使うのか

重複開発を避け、エコシステム全体で統合資産を共有・再利用し、開発速度を加速させるため

## いつ使うのか

自社で開発した統合を他社・他開発者と共有し、エコシステムに貢献したい場合

## やり方

1. pieceを開発・テスト
2. package.jsonでバージョン管理
3. npmjs.comに@activepiecesスコープで公開
4. ActivepiecesリポジトリにPR提出(任意)
5. ドキュメント作成(README, 使用例)
6. コミュニティフィードバックを受け、イテレーション
7. Activepiecesカタログ(https://www.activepieces.com/pieces)に自動追加

### 入力

- 開発済みpiece
- npmアカウント
- ドキュメント

### 出力

- npmパッケージ
- Activepiecesカタログへの掲載
- コミュニティからのフィードバック

## 使うツール・ライブラリ

- npm
- GitHub
- Activepieces Contributor's Guide

## コード例

```
# npm公開例
npm publish --access public
# @activepieces/piece-example として公開
```

## 前提知識

- TypeScript基礎知識
- REST API統合の基本理解
- Docker/npmの基本操作
- MCPプロトコルの概念(Claude Desktop等LLMツールとの統合前提)
- ワークフロー自動化の基礎(トリガー、アクション、条件分岐)
- オープンソースプロジェクトへのコントリビューション経験(任意)
