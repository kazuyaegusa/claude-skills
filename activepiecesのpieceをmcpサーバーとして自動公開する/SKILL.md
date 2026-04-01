# ActivepiecesのpieceをMCPサーバーとして自動公開する

> Activepiecesにcontributeしたpiece（統合モジュール）が、自動的にMCPサーバーとしてClaude Desktop、Cursor、Windsurf等のLLMツールで利用可能になる仕組みを活用する

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: agent-orchestration

## なぜ使うのか

ワークフロー自動化とLLMエージェントのツール統合を二重開発せずに済み、コミュニティのcontributionを最大限活用できる。280以上のサービス統合を一度に手に入れられる

## いつ使うのか

既存のMCPサーバーでカバーできないサービスと統合したい、かつそのサービスをワークフロー自動化でも使いたい場合。コミュニティ主導で拡張したい場合

## やり方

1. Activepiecesをセットアップ（セルフホストまたはクラウド利用）
2. TypeScriptでpieceを開発（npmパッケージとして作成、公式ドキュメント https://www.activepieces.com/docs/build-pieces/building-pieces/overview を参照）
3. Activepiecesリポジトリにpieceをcontribute（PRマージ後、自動的にnpmjs.comに公開）
4. 公開されたpieceは自動的にMCPサーバーとして認識され、Claude Desktop等の設定に追加可能
5. LLMツール側で該当MCPサーバーを有効化

### 入力

- 統合したいサービスのAPI仕様
- TypeScript開発環境
- Activepieces環境（セルフホストまたはクラウド）

### 出力

- npmパッケージとして公開されたpiece
- MCPサーバーとして利用可能な統合モジュール
- Activepiecesビルダー上で利用可能なアクション・トリガー

## 使うツール・ライブラリ

- Activepieces framework (TypeScript)
- npmjs.com
- Claude Desktop / Cursor / Windsurf (MCP client)

## コード例

```
// Activepiecesのpiece開発例（公式ドキュメントより）
import { createPiece } from '@activepieces/pieces-framework';

export const myPiece = createPiece({
  name: 'my-service',
  displayName: 'My Service',
  actions: [
    // アクション定義（hot reloading対応）
  ],
  triggers: [
    // トリガー定義
  ]
});
```

## 前提知識

- TypeScriptの基本知識（piece開発時）
- Docker/Kubernetesの基本（セルフホスト時）
- MCP（Model Context Protocol）の概念理解
- npmパッケージ管理の基礎
- REST API / Webhook の基本知識
