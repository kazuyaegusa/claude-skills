# セルフホスト可能なノーコード×プロコードハイブリッドアーキテクチャ

> ノーコードビルダーでワークフローを構築しつつ、TypeScriptによるカスタム拡張を可能にし、全体をセルフホストできるアーキテクチャを設計する

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: automation-pipeline

## なぜ使うのか

非技術者でも使えるUXを提供しつつ、開発者にはフルカスタマイズ性を保証するため。セルフホストによりセキュリティとデータ主権を確保する

## いつ使うのか

Zapierのような自動化をオンプレミスで実現したい場合、ノーコードとプロコードの両方のユーザーをサポートする必要がある場合

## やり方

1. Loops、Branches、Auto Retriesなどの基本フローコントロールをノーコードで提供
2. Code with NPMピースでTypeScriptコードを直接実行可能にする
3. ASK AI in Code Pieceで非技術者でもAIの助けを借りてデータクレンジング等を実施できるようにする
4. すべてのフローをバージョン管理する
5. セルフホスト可能なデプロイメント（network-gapped環境対応）を提供する
6. 開発者がカスタムpiecesをローカルでhot reloadしながら開発できる環境を提供する

### 入力

- ワークフロー要件
- 統合対象サービス
- セキュリティ・コンプライアンス要件

### 出力

- セルフホスト可能な自動化プラットフォーム
- ノーコードビルダーUI
- カスタムTypeScript pieces

## 使うツール・ライブラリ

- Activepieces
- TypeScript
- Docker（セルフホスト用）

## 前提知識

- TypeScriptの基本知識
- Model Context Protocol（MCP）の概念理解
- Claude DesktopやCursorなどMCP対応ツールの使用経験
- npmパッケージの作成・公開方法
- ワークフロー自動化の基本概念（トリガー、アクション、データ変換）
- Docker/コンテナ技術の基本（セルフホスト時）

## 根拠

> "When you contribute pieces to Activepieces they become automatically available as MCP servers that you can use with LLMs through Claude Desktop, Cursor or Windsurf!"

> "🛠️ Largest open source MCP toolkit: All our pieces (280+) are available as MCP that you can use with LLMs on Claude Desktop, Cursor or Windsurf."

> "🛠️ Pieces are written in Typescript: Pieces are npm packages in TypeScript, offering full customization with the best developer experience, including **hot reloading** for **local** piece development on your machine."

> "As an **open ecosystem**, all integration source code is accessible in our repository. These integrations are versioned and [published](https://www.npmjs.com/search?q=%40activepieces) directly to npmjs.com upon contribution."
