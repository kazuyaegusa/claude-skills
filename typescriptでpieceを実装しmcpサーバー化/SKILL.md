# TypeScriptでpieceを実装しMCPサーバー化

> Activepiecesのpiece frameworkでTypeScriptのnpmパッケージとして統合を実装すると、それがMCPサーバーとして自動公開される

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: automation-pipeline

## なぜ使うのか

1つのコードベースでノーコードビルダーとLLM(Claude/Cursor/Windsurf)の両方から統合を利用可能にし、重複開発を避けるため

## いつ使うのか

LLMから外部サービスを操作したいが、既存MCPサーバーが存在しない場合、かつノーコードビルダーでも同じ統合を使いたい場合

## やり方

1. Activepiecesリポジトリをcloneし、piece frameworkのドキュメント(https://www.activepieces.com/docs/build-pieces/building-pieces/overview)を参照
2. TypeScriptでactionやtriggerを定義(type-safe APIを使用)
3. npmパッケージとしてビルド・バージョン管理
4. npmjs.comに@activepiecesスコープで公開
5. Activepiecesがpiece定義を読み取り、MCPサーバー仕様に自動変換
6. Claude Desktop/Cursor/Windsurfの設定でMCPサーバーとして追加

### 入力

- 対象サービスのAPI仕様
- TypeScript開発環境
- Activepiecesのpiece framework

### 出力

- npmパッケージとして公開された統合
- MCPサーバー仕様に準拠したエンドポイント
- Activepiecesビルダーで利用可能なアクション/トリガー

## 使うツール・ライブラリ

- Activepieces piece framework
- TypeScript
- npmjs.com
- Claude Desktop/Cursor/Windsurf

## コード例

```
// 公式ドキュメント参照
// pieceはTypeScriptでaction/triggerを定義し、
// Activepiecesが自動でMCP仕様に変換
```

## 前提知識

- TypeScript基礎知識
- REST API統合の基本理解
- Docker/npmの基本操作
- MCPプロトコルの概念(Claude Desktop等LLMツールとの統合前提)
- ワークフロー自動化の基礎(トリガー、アクション、条件分岐)
- オープンソースプロジェクトへのコントリビューション経験(任意)

## 根拠

> When you contribute pieces to Activepieces they become automatically available as MCP servers that you can use with LLMs through Claude Desktop, Cursor or Windsurf!

> **🛠️ Largest open source MCP toolkit**: All our pieces (280+) are available as MCP that you can use with LLMs on Claude Desktop, Cursor or Windsurf.
