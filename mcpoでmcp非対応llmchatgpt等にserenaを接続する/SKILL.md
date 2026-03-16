# mcpoでMCP非対応LLM（ChatGPT等）にSerenaを接続する

> mcpo（MCP to OpenAPI変換ツール）を使ってSerena MCPサーバーをOpenAPIエンドポイント化し、ChatGPTや他のツール呼び出し対応LLMで利用する

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: agent-orchestration

## なぜ使うのか

ChatGPTはMCP非対応だがツール呼び出し（Function Calling）は対応しており、OpenAPI経由なら既存LLMでもSerenaツールを使える

## いつ使うのか

MCP非対応だがツール呼び出しは対応しているLLM（ChatGPT/Gemini等）でSerenaを使いたい場合

## やり方

1. Serena MCPサーバーを起動
2. mcpo（https://github.com/evalstate/mcpo）をインストール・起動し、SerenaをOpenAPIスキーマに変換
3. ChatGPT等のツール呼び出し設定にOpenAPIエンドポイントを追加
4. LLMがHTTP経由でSerenaツールを呼び出し

### 入力

- Serena MCPサーバー
- mcpo
- ツール呼び出し対応LLM

### 出力

- OpenAPI経由のSerenaツール呼び出し
- MCP非対応LLMでのシンボルレベルコード操作

## 使うツール・ライブラリ

- mcpo
- Serena

## 前提知識

- Model Context Protocol (MCP) の基本概念
- Language Server Protocol (LSP) の役割（IDE補完・参照解析の仕組み）
- LLMのツール呼び出し（Function Calling）の仕組み
- Python環境とuvパッケージマネージャーの使い方
- コーディングエージェント（Claude Code/Cursor等）の基本的な使用経験

## 根拠

> 「Serena provides essential semantic code retrieval and editing tools that are akin to an IDE's capabilities, extracting code entities at the symbol level」（シンボルレベル抽出がIDE相当）

> 「Most users report that Serena has strong positive effects ... described to be a game changer, providing an enormous productivity boost」（コミュニティ評価）

> 「Visual Studio Code team, together with Microsoft's Open Source Programs Office and GitHub Open Source have decided to sponsor Serena」（Microsoft公式スポンサー）

> 「Simply implement a new tool by subclassing serena.agent.Tool and implement the apply method」（カスタムツール追加方法）
