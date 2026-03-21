# MCP経由でシンボルレベルコード操作を提供する

> LSPまたはJetBrainsプラグインを使い、ファイルではなくシンボル（関数・クラス・変数等）単位でコードを検索・編集するツールをMCPサーバーとして公開する

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: claude-code-workflow

## なぜ使うのか

LLMがファイル全体を読まずに必要なシンボルだけ取得・編集できるため、トークン消費を削減し、大規模コードベースでも効率的に動作する。IDEのような構造理解により、文字列置換より正確な編集が可能になる

## いつ使うのか

LLMエージェントがファイル全体を読んでトークン超過する、grepで関連コードを見逃す、文字列置換で誤編集する等の問題が発生した時

## やり方

1. uvをインストール（uv公式サイト参照）
2. `uvx --from git+https://github.com/oraios/serena serena start-mcp-server --help` で起動オプション確認
3. クライアント（Claude Code、Codex、Claude Desktop等）の設定ファイルにSerena MCPサーバーの起動コマンドを追加
4. LLMがfind_symbol、find_referencing_symbols、insert_after_symbol等のツールを使えるようになる
5. エージェントがシンボル名で検索・編集を実行し、ファイル全体読み込みを回避

### 入力

- uv（パッケージマネージャー）
- MCP対応クライアント（Claude Code、Codex、VSCode+Cline等）
- 対象プロジェクトのコードベース
- （LSP利用時）言語サーバーの依存関係
- （JetBrainsプラグイン利用時）対応IDE

### 出力

- シンボル検索結果（関数・クラス定義等）
- 参照元シンボルのリスト
- シンボル単位での編集操作（insert_after_symbol等）の結果
- トークン消費削減とコード品質向上

## 使うツール・ライブラリ

- Serena（MCPサーバー）
- uv（Pythonパッケージマネージャー）
- LSP実装（各言語のlanguage server）
- Serena JetBrainsプラグイン（オプション）
- multilspy（LSPラッパー、Serenaの内部依存）
- Python MCP SDK

## コード例

```
# Serena MCP起動例（uvx経由）
uvx --from git+https://github.com/oraios/serena serena start-mcp-server

# クライアント設定例（概念的）
# Claude Codeの設定でMCPサーバーコマンドを指定
# {
#   "mcpServers": {
#     "serena": {
#       "command": "uvx",
#       "args": ["--from", "git+https://github.com/oraios/serena", "serena", "start-mcp-server"]
#     }
#   }
# }
```

## 前提知識

- Model Context Protocol（MCP）の基本概念
- Language Server Protocol（LSP）の基礎知識
- LLMエージェントの動作原理（ツール呼び出し・Function Calling）
- Python環境構築（uv等のパッケージマネージャー）
- コードベースにおけるシンボル（関数・クラス・変数等）の概念
- （JetBrainsプラグイン利用時）JetBrains IDEの基本操作

## 根拠

> 「Serena provides essential semantic code retrieval and editing tools that are akin to an IDE's capabilities, extracting code entities at the symbol level」

> 「Serena's tool implementation is decoupled from the framework-specific code and can thus easily be adapted to any agent framework」

> 「Visual Studio Code team, together with Microsoft's Open Source Programs Office and GitHub Open Source have decided to sponsor Serena」

> 「Most users report that Serena has strong positive effects ... often described to be a game changer, providing an enormous productivity boost」
