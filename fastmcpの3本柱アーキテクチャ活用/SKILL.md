# FastMCPの3本柱アーキテクチャ活用

> Servers（ツール公開）、Apps（対話的UI）、Clients（サーバー接続）の3つのコンポーネントを組み合わせて使う

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: prompt-engineering

## なぜ使うのか

MCPの全ユースケース（サーバー実装、クライアント実装、UI統合）を単一のフレームワークで統一的に扱うことで、学習コストを削減し、コンポーネント間の相互運用性を保証する

## いつ使うのか

ツール公開だけでなく、クライアント実装や対話的UIが必要な時、フルスタックのMCPアプリケーションを構築する時

## やり方

1. Servers: `@mcp.tool`、`@mcp.resource`、`@mcp.prompt`でLLMにツール・リソース・プロンプトを公開
2. Apps: 対話的UIを会話内に直接レンダリング（詳細はドキュメント参照）
3. Clients: URLでサーバーに接続し、プロトコル管理を自動化

### 入力

- Servers: Python関数
- Clients: MCPサーバーのURL
- Apps: UIコンポーネント定義

### 出力

- Servers: MCP準拠のサーバー
- Clients: サーバーとの接続
- Apps: 会話内レンダリングされるUI

## 使うツール・ライブラリ

- fastmcp

## 前提知識

- Pythonの基本的な関数定義・型ヒント・デコレータの知識
- Model Context Protocol（MCP）の概念理解（LLMがツールを呼び出すプロトコル）
- LLMツール統合の基本的な理解
