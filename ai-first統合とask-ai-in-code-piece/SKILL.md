# AI-First統合とASK AI in Code Piece

> ビルダーのCodeピース内で「ASK AI」機能を使い、非技術者がコード不要でデータクリーニング等を実行

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: automation-pipeline

## なぜ使うのか

非技術者が複雑なデータ変換やクリーニングをノーコードで実現し、技術者の介入なしに自動化を完結させるため

## いつ使うのか

非技術者がデータクリーニング、フォーマット変換、条件分岐等をコード不要で実現したい場合

## やり方

1. Activepiecesビルダーでフローを作成
2. Codeピースを追加
3. 「ASK AI」ボタンをクリック
4. 自然言語で指示(例: 「このリストから重複を削除し、メールアドレスを小文字に統一」)
5. AIがTypeScript/JavaScriptコードを生成
6. コードをレビュー・実行
7. 結果を確認し、必要に応じて再指示

### 入力

- 自然言語での指示
- 入力データ(JSON/CSV等)

### 出力

- AIが生成したコード
- 実行結果

## 使うツール・ライブラリ

- Activepieces Code Piece
- AI SDK(OpenAI等)

## コード例

```
// ユーザー指示: "重複削除してメールを小文字に"
// AIが生成するコード例:
const unique = [...new Set(data.map(d => d.email.toLowerCase()))];
return unique;
```

## 前提知識

- TypeScript基礎知識
- REST API統合の基本理解
- Docker/npmの基本操作
- MCPプロトコルの概念(Claude Desktop等LLMツールとの統合前提)
- ワークフロー自動化の基礎(トリガー、アクション、条件分岐)
- オープンソースプロジェクトへのコントリビューション経験(任意)

## 根拠

> All-in-one AI automation designed to be **extensible** through a **type-safe** pieces framework written in **TypeScript**.

> When you contribute pieces to Activepieces they become automatically available as MCP servers that you can use with LLMs through Claude Desktop, Cursor or Windsurf!

> **🛠️ Largest open source MCP toolkit**: All our pieces (280+) are available as MCP that you can use with LLMs on Claude Desktop, Cursor or Windsurf.

> **🛠️  Pieces are written in Typescript**: Pieces are npm packages in TypeScript, offering full customization with the best developer experience, including **hot reloading** for **local** piece development on your machine.

> **🌐 Open Ecosystem:** All pieces are open source and available on npmjs.com, **60% of the pieces are contributed by the community**.
