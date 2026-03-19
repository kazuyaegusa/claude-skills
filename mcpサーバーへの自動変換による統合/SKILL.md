# MCPサーバーへの自動変換による統合

> Activepiecesで開発された280以上のpieceを自動的にMCP（Model Context Protocol）サーバーに変換し、Claude Desktop、Cursor、WindsurfなどのLLMツールから直接呼び出せるようにする

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: claude-code-workflow

## なぜ使うのか

LLMエージェントがコード生成だけでなく、実際のシステム統合・外部サービス操作を実行できるようにするため。MCPプロトコルを介することで、LLMは構造化されたツール呼び出しとして統合機能を利用できる

## いつ使うのか

Claude Code等のLLMツールから直接Google Sheets更新、Discord通知、OpenAI呼び出し等の実務タスクを実行したい時、AIエージェントに複数サービスをまたがるワークフローを実行させたい時

## やり方

1. Activepiecesにpieceをコントリビュート（npmパッケージとして公開）
2. Activepiecesがpieceメタデータを解析し、MCPサーバーのインターフェース定義を自動生成
3. Claude Desktop、Cursor、WindsurfのMCP設定ファイルにActivepiecesのMCPサーバーを登録
4. LLMが自然言語でリクエストすると、Activepiecesが該当pieceを実行
5. 実行結果をLLMにフィードバックして次のアクションを決定

### 入力

- Activepiecesに登録されたpiece（npmパッケージ）
- MCP対応LLMツール（Claude Desktop/Cursor/Windsurf）
- MCP設定ファイル

### 出力

- LLMから呼び出し可能な統合機能一覧
- LLMによる自動化タスクの実行結果

## 使うツール・ライブラリ

- Model Context Protocol (MCP)
- Claude Desktop
- Cursor
- Windsurf
- Activepieces

## 前提知識

- TypeScriptの基礎知識（型システム、非同期処理）
- npmパッケージ管理の理解
- REST API/Webhook等の統合パターンの知識
- Model Context Protocol (MCP)の基本概念（LLMがツールを呼び出す仕組み）
- ワークフロー自動化ツール（Zapier等）の利用経験があると理解が早い

## 根拠

> When you contribute pieces to Activepieces they become automatically available as MCP servers that you can use with LLMs through Claude Desktop, Cursor or Windsurf!

> **🛠️ Largest open source MCP toolkit**: All our pieces (280+) are available as MCP that you can use with LLMs on Claude Desktop, Cursor or Windsurf.
