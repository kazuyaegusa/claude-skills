# FastMCPの3本柱アーキテクチャを活用する

> Server（ツール提供）、Client（MCP接続）、App（対話UI）の3機能を統合的に使う

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: dev-tool

## なぜ使うのか

MCPサーバーだけでなく、クライアント側の接続や対話UIまで同じフレームワークで統一でき、フルスタックMCPアプリケーションが作れる

## いつ使うのか

単なるツール提供を超えて、複数MCPサーバーを統合したり、ユーザー操作UIを提供したい時

## やり方

1. Server: @mcp.toolで関数をツール化
2. Client: FastMCP Clientで他のMCPサーバーに接続（ローカル/リモート）
3. App: ツールに対話UIを追加し、会話内でレンダリング
4. 必要に応じて3つを組み合わせて実装

### 入力

- FastMCPライブラリ
- MCP対応LLMクライアント（Claude Desktop等）

### 出力

- フルスタックMCPアプリケーション（サーバー+クライアント+UI）

## 使うツール・ライブラリ

- fastmcp

## 前提知識

- Python 3.x の基本文法（関数定義、デコレータ）
- 型ヒント（type hints）の理解
- MCP（Model Context Protocol）の概念（LLMとツールを接続するプロトコル）
- FastAPIやFlaskのようなPythonフレームワークの使用経験があると理解が早い

## 根拠

> 「FastMCP 1.0 was incorporated into the official MCP Python SDK in 2024」（公式SDK採用）

> 「some version of FastMCP powers 70% of MCP servers across all languages」（70%シェア）

> 「We recommend installing FastMCP with uv」（公式推奨インストール方法）

> 「Prefect Horizon offers free hosting for FastMCP users」（無料ホスティング）
