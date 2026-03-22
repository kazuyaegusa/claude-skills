# FastMCPで3層アーキテクチャ構築

> Servers（ツール公開）・Apps（UI統合）・Clients（サーバー接続）の3つのコンポーネントを組み合わせてMCPアプリを構築する

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: prompt-engineering

## なぜ使うのか

単なるツール公開だけでなく、会話内レンダリング可能なUIや、他のMCPサーバーとの統合が必要な複雑なユースケースに対応できる

## いつ使うのか

ツールだけでなくリソース（データ）やプロンプトテンプレートも提供したい時、または既存MCPサーバーを統合したクライアントを作りたい時

## やり方

1. Serversで`@mcp.tool`・`@mcp.resource`・`@mcp.prompt`を使いLLMに公開する機能を定義
2. Appsでツールにインタラクティブなチャット内UIを追加（会話中に直接レンダリング）
3. ClientsでURL指定により他のMCPサーバー（ローカル/リモート）に接続
4. トランスポート・認証・プロトコルライフサイクルは自動管理される

### 入力

- Pythonで実装したツール/リソース/プロンプトロジック
- （Clients使用時）接続先MCPサーバーのURL

### 出力

- MCP準拠のサーバー（tools/resources/prompts公開）
- チャット内レンダリング可能なアプリUI
- 他サーバーと連携するMCPクライアント

## 使うツール・ライブラリ

- fastmcp（Servers/Apps/Clients全て含む）

## コード例

```
# Serverの例は上記参照
# Clientはドキュメント参照（gofastmcp.com/clients/client）
# Appsはドキュメント参照（gofastmcp.com/apps/overview）
```

## 前提知識

- Python 3.x基礎知識
- 型ヒント（Type Hints）の理解
- デコレータの基本概念
- Model Context Protocol (MCP)の概要理解
- 非同期プログラミング（async/await）の基礎（応用時）
