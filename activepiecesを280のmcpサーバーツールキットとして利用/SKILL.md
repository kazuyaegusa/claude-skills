# Activepiecesを280+のMCPサーバーツールキットとして利用

> Activepiecesに既に存在する280以上のpiece（Google Sheets, OpenAI, Discord, RSS等）を、Claude Desktop/Cursor/Windsurf等のLLMから直接MCPサーバーとして呼び出す

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: agent-orchestration

## なぜ使うのか

個別のMCPサーバーを探して設定する手間を省き、すでにコミュニティでメンテナンスされている統合を即座に利用できる。Activepiecesのpieceはnpmjsで公開されており、バージョン管理もされている

## いつ使うのか

LLMエージェントに外部API統合機能を追加したいが、各サービスのMCPサーバーを個別に探す手間を省きたい時、すでにActivepiecesでメンテナンスされている統合を活用したい時

## やり方

1. Activepiecesをセルフホストまたはクラウド版にサインアップ
2. 必要なpieceをActivepiecesのpiece一覧 (https://www.activepieces.com/pieces) から確認
3. Claude Desktop/Cursor/Windsurfの設定ファイルでActivepiecesのMCPサーバーを指定
4. LLMのプロンプトから直接pieceのアクションを呼び出す

### 入力

- Activepiecesのインスタンス（セルフホストまたはクラウド）
- Claude Desktop/Cursor/WindsurfのMCP設定

### 出力

- LLMから直接呼び出せる280+の外部サービス統合

## 使うツール・ライブラリ

- Activepieces
- Claude Desktop / Cursor / Windsurf
- MCP (Model Context Protocol)

## 前提知識

- TypeScript / npmの基礎知識（piece開発時）
- MCP (Model Context Protocol)の概念理解（LLM統合時）
- Claude Desktop / Cursor / Windsurfのいずれかの利用経験（LLMからの利用時）
- ワークフロー自動化ツール（Zapier等）の利用経験

## 根拠

> All-in-one AI automation designed to be extensible through a type-safe pieces framework written in TypeScript. When you contribute pieces to Activepieces they become automatically available as MCP servers that you can use with LLMs through Claude Desktop, Cursor or Windsurf!

> 🛠️ Largest open source MCP toolkit: All our pieces (280+) are available as MCP that you can use with LLMs on Claude Desktop, Cursor or Windsurf.
