# hot reloadでローカルpiece開発

> Activepiecesはローカルマシンでpieceを開発中、変更を保存すると即座にビルダーに反映されるhot reload機能を提供

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: automation-pipeline

## なぜ使うのか

統合開発のフィードバックループを高速化し、デバッグとテストを効率化するため

## いつ使うのか

新規pieceを開発中、またはデバッグ中で、頻繁にコード変更とテストを繰り返す必要がある場合

## やり方

1. Activepiecesをローカル環境でセットアップ(Docker/npm)
2. pieces/packages/以下に新規pieceディレクトリを作成
3. npm run watch等でホットリロードモードで起動
4. TypeScriptコードを編集・保存
5. ビルダーUIで即座に変更を確認
6. デバッグログとエラーをリアルタイム確認

### 入力

- ローカルActivepieces環境
- piece開発用TypeScriptコード

### 出力

- リアルタイムでビルダーに反映された統合
- デバッグログ

## 使うツール・ライブラリ

- Activepieces CLI
- npm/Docker
- TypeScript watch mode

## コード例

```
# ローカル開発環境起動例
npm run watch
# コード変更→自動reload→ビルダーで即座に確認
```

## 前提知識

- TypeScript基礎知識
- REST API統合の基本理解
- Docker/npmの基本操作
- MCPプロトコルの概念(Claude Desktop等LLMツールとの統合前提)
- ワークフロー自動化の基礎(トリガー、アクション、条件分岐)
- オープンソースプロジェクトへのコントリビューション経験(任意)

## 根拠

> **🛠️  Pieces are written in Typescript**: Pieces are npm packages in TypeScript, offering full customization with the best developer experience, including **hot reloading** for **local** piece development on your machine.

> **🌐 Open Ecosystem:** All pieces are open source and available on npmjs.com, **60% of the pieces are contributed by the community**.

> As an **open ecosystem**, all integration source code is accessible in our repository. These integrations are versioned and [published](https://www.npmjs.com/search?q=%40activepieces) directly to npmjs.com upon contribution.
