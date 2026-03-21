# mcpoでChatGPT等の非MCP対応クライアントに接続する

> MCPサーバーをOpenAPI経由で公開するmcpoツールを使い、MCP非対応だがツール呼び出し（Function Calling）対応のクライアントでSerenaを利用する

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: agent-orchestration

## なぜ使うのか

ChatGPT等はMCPに対応していないが、OpenAI Function Calling等のツール呼び出し機能は持つ。mcpoでMCPをOpenAPIに変換することで、既存クライアントでもSerenaを使える

## いつ使うのか

ChatGPTやMCP非対応だがツール呼び出し対応のLLMクライアントでSerenaを使いたい時

## やり方

1. mcpoをインストール（詳細はSerenaドキュメント参照）
2. mcpoにSerena MCPサーバーのエンドポイントを渡し、OpenAPIサーバーとして起動
3. ChatGPT等のクライアントからOpenAPI経由でSerenaツールを呼び出す
4. mcpoが内部でMCP呼び出しに変換し、Serenaと通信

### 入力

- mcpoツール
- Serena MCPサーバー
- OpenAPI/Function Calling対応クライアント（ChatGPT等）

### 出力

- OpenAPI経由でSerenaツールを呼び出せる環境

## 使うツール・ライブラリ

- mcpo

## 前提知識

- Model Context Protocol（MCP）の基本概念
- Language Server Protocol（LSP）の基礎知識
- LLMエージェントの動作原理（ツール呼び出し・Function Calling）
- Python環境構築（uv等のパッケージマネージャー）
- コードベースにおけるシンボル（関数・クラス・変数等）の概念
- （JetBrainsプラグイン利用時）JetBrains IDEの基本操作
