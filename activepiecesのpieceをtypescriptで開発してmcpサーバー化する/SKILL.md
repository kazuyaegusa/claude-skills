# ActivepiecesのpieceをTypeScriptで開発してMCPサーバー化する

> TypeScriptでActivepieces用のpiece（統合コンポーネント）を作成し、npmに公開することで、自動的にMCPサーバーとしてClaude Desktop等から利用可能にする

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: agent-orchestration

## なぜ使うのか

LLMエージェントが外部サービスと連携するためのMCPサーバーを個別に開発するのは手間がかかる。Activepiecesのエコシステムに乗ることで、ワークフロー自動化とMCPサーバーを一度に手に入れられる

## いつ使うのか

既存のMCPサーバーに欲しい統合が無い場合、またはワークフロー自動化とLLM統合を同時に実現したい場合

## やり方

1. Activepiecesのドキュメント（https://www.activepieces.com/docs/build-pieces/building-pieces/overview）を参照してpiece開発環境を構築
2. TypeScriptでpieceを実装（型安全、hot reload対応）
3. コントリビューターガイドに従いプルリクエストを送る
4. マージされるとnpmjs.comに自動公開され、同時にMCPサーバーとして登録される
5. Claude Desktop、Cursor、WindsurfでMCPサーバーとして呼び出せる

### 入力

- TypeScriptの知識
- 統合したいサービスのAPI仕様

### 出力

- npmjs.comに公開されたActivepieces piece
- Claude Desktop等で利用可能なMCPサーバー

## 使うツール・ライブラリ

- Activepieces framework
- TypeScript
- npmjs.com

## 前提知識

- TypeScriptの基礎知識（piece開発の場合）
- Docker/Kubernetesの基本操作（セルフホストの場合）
- ワークフロー自動化の概念理解
- MCPプロトコルの基本理解（LLM統合の場合）

## 根拠

> When you contribute pieces to Activepieces they become automatically available as MCP servers that you can use with LLMs through Claude Desktop, Cursor or Windsurf!

> Largest open source MCP toolkit: All our pieces (280+) are available as MCP that you can use with LLMs on Claude Desktop, Cursor or Windsurf.
