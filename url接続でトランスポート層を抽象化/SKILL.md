# URL接続でトランスポート層を抽象化

> Clientsを使う際、MCPサーバーへの接続をURLで指定するだけで、トランスポート（stdio/SSE/WebSocket）・認証・プロトコルライフサイクルが自動処理される

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: dev-tool

## なぜ使うのか

MCP低レベルSDKでは、stdioトランスポートとHTTPトランスポートで異なる初期化コードが必要で、認証トークンやヘッダーの管理も手動。これをURL1つで抽象化することで、サーバー側の実装変更（例: stdioからHTTPへ移行）に影響されない

## いつ使うのか

他のMCPサーバーをプログラムから利用したいとき。ローカル開発ではstdio、本番ではHTTP/SSEに切り替える場合でも、URLを変えるだけでコード変更不要

## やり方

1. `from fastmcp import Client`をインポート
2. `client = Client("<サーバーURL>")`でインスタンス化
3. `await client.connect()`で接続確立（トランスポート自動判定）
4. `await client.call_tool("ツール名", 引数)`でツール実行
5. 切断は`await client.disconnect()`

### 入力

- MCPサーバーのURL（例: stdio://path, http://host:port）

### 出力

- 接続済みClientインスタンス
- ツール呼び出し結果

## 使うツール・ライブラリ

- fastmcp

## 前提知識

- Pythonの基本文法（関数定義、デコレータ、型ヒント）
- MCPの基本概念（ツール・リソース・プロンプトの役割）
- 非同期プログラミングの基礎（Clientsを使う場合）

## 根拠

> 「FastMCP 1.0 was incorporated into the official MCP Python SDK in 2024.」（公式SDK統合実績）

> 「downloaded a million times a day, and some version of FastMCP powers 70% of MCP servers across all languages」（採用実績）

> 「We recommend installing FastMCP with uv: uv pip install fastmcp」（推奨インストール方法）

> 「When you're ready to deploy, Prefect Horizon offers free hosting for FastMCP users.」（無料ホスティング提供）
