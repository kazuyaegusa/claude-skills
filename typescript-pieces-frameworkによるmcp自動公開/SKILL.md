# TypeScript pieces frameworkによるMCP自動公開

> TypeScriptでワークフロー統合（pieces）を作成すると、それが自動的にMCPサーバーとしてClaude DesktopやCursor等から利用可能になる仕組みを構築する

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: automation-pipeline

## なぜ使うのか

手動でMCPサーバーを実装する手間を省き、開発者がビジネスロジックに集中できるようにするため。また、npmパッケージとして公開することでコミュニティが容易に貢献でき、エコシステムを急速に拡大できる

## いつ使うのか

LLMから呼び出せる統合パーツを大量に作成・公開したい場合、コミュニティによる統合拡張を促進したい場合

## やり方

1. TypeScriptでtype-safeなpieces frameworkを定義する
2. 開発者がこのフレームワークに従ってnpmパッケージとして統合を実装する（hot reload対応でローカル開発可能）
3. npmjs.comにpublishする
4. Activepiecesプラットフォームが自動的にこれらをMCPサーバーとして公開する
5. Claude DesktopやCursor等の設定ファイルからこのMCPサーバーを参照する

### 入力

- TypeScriptによるpieces実装
- npmjs.comへのパッケージ公開

### 出力

- MCPサーバーとして動作する統合パーツ
- Claude Desktop/Cursor等から呼び出し可能なアクション

## 使うツール・ライブラリ

- TypeScript
- npm
- Activepieces pieces framework
- Model Context Protocol (MCP)

## コード例

```
// TypeScript pieces frameworkの例（推測）
import { createPiece } from '@activepieces/pieces-framework';

export const googleSheetsPiece = createPiece({
  name: 'google-sheets',
  actions: [
    {
      name: 'addRow',
      displayName: 'Add Row to Sheet',
      async run(context) {
        // Google Sheets APIを呼び出す実装
      }
    }
  ]
});
```

## 前提知識

- TypeScriptの基本知識
- Model Context Protocol（MCP）の概念理解
- Claude DesktopやCursorなどMCP対応ツールの使用経験
- npmパッケージの作成・公開方法
- ワークフロー自動化の基本概念（トリガー、アクション、データ変換）
- Docker/コンテナ技術の基本（セルフホスト時）

## 根拠

> "All-in-one AI automation designed to be **extensible** through a **type-safe** pieces framework written in **TypeScript**."

> "When you contribute pieces to Activepieces they become automatically available as MCP servers that you can use with LLMs through Claude Desktop, Cursor or Windsurf!"

> "🛠️ Largest open source MCP toolkit: All our pieces (280+) are available as MCP that you can use with LLMs on Claude Desktop, Cursor or Windsurf."

> "🌐 Open Ecosystem: All pieces are open source and available on npmjs.com, **60% of the pieces are contributed by the community**."

> "🛠️ Pieces are written in Typescript: Pieces are npm packages in TypeScript, offering full customization with the best developer experience, including **hot reloading** for **local** piece development on your machine."
