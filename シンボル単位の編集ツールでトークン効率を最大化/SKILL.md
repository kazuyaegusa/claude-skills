# シンボル単位の編集ツールでトークン効率を最大化

> replace_symbol_body, insert_after_symbol, insert_before_symbol, safe_deleteなどのシンボル単位編集ツールを提供

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: agent-orchestration

## なぜ使うのか

行番号ベースやテキスト検索ベースの編集は脆弱でトークンを浪費する。シンボル単位の操作により、エラー率低減とトークン削減を同時達成。

## いつ使うのか

大規模ファイルで特定シンボルのみを編集したい時、または既存コードを壊さず安全に変更したい時

## やり方

1. エージェントがfind_symbolで対象シンボルを特定 2. replace_symbol_bodyで関数本体を置換、またはinsert_after_symbolで新規メソッドを追加 3. safe_deleteで未使用コードを安全に削除

### 入力

- シンボル名（関数名、クラス名等）
- 新規コード

### 出力

- 編集済みソースコード

## 使うツール・ライブラリ

- Serena MCP server

## 前提知識

- Model Context Protocol (MCP)の基本的な理解
- Language Server Protocol (LSP)の概念
- uv (Pythonパッケージマネージャ)の使い方
- シンボル・参照・型階層などのIDE概念
- Claude Code/Codex/Claude Desktop等のMCP対応クライアント
