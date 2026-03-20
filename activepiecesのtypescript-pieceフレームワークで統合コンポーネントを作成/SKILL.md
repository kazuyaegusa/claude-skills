# ActivepiecesのTypeScript pieceフレームワークで統合コンポーネントを作成

> TypeScriptでtype-safeな統合コンポーネント(piece)を作成し、npmパッケージとして公開すると、自動的にActivepiecesのノーコードビルダーとMCPサーバーの両方で利用可能になる

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: automation-pipeline

## なぜ使うのか

統合コンポーネントをクローズドなプラグインシステムではなく、標準的なnpmエコシステムに乗せることで、(1)バージョン管理が容易、(2)コミュニティ貢献が促進される、(3)LLMからも同じツールを利用できる、という3つのメリットが得られる

## いつ使うのか

新しいSaaSやAPIをActivepiecesとLLMの両方から利用したい時、既存のMCPサーバーが存在しないサービスを統合したい時

## やり方

1. Activepiecesの公式ドキュメント (https://www.activepieces.com/docs/build-pieces/building-pieces/overview) に従ってpiece開発環境をセットアップする
2. TypeScriptでpieceのアクション・トリガーを定義（type-safeな引数・戻り値定義を含む）
3. ローカル開発時はホットリロードで動作確認
4. npmjs.comに @activepieces スコープでパッケージを公開
5. Activepiecesにコントリビュート（プルリクエスト）すると、自動的にMCPサーバーとしても利用可能になる

### 入力

- 統合したいサービスのAPI仕様
- TypeScript開発環境
- Activepiecesのpiece開発ドキュメント

### 出力

- npmパッケージとして公開されたpiece
- Activepiecesノーコードビルダーで使える統合コンポーネント
- Claude Desktop/Cursor/WindsurfでMCPサーバーとして利用可能なツール

## 使うツール・ライブラリ

- TypeScript
- Activepieces piece framework
- npm

## 前提知識

- TypeScript / npmの基礎知識（piece開発時）
- MCP (Model Context Protocol)の概念理解（LLM統合時）
- Claude Desktop / Cursor / Windsurfのいずれかの利用経験（LLMからの利用時）
- ワークフロー自動化ツール（Zapier等）の利用経験
