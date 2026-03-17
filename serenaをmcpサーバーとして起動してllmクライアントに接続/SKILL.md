# SerenaをMCPサーバーとして起動してLLMクライアントに接続

> Serenaを各種LLMクライアント（Claude Code/Desktop、VSCode、Cursor、Cline等）のMCPサーバーとして起動し、シンボルレベルのコードツールをLLMに提供する

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: claude-code-workflow

## なぜ使うのか

ファイル全体の読み込みやgrep検索の代わりに、find_symbol/insert_after_symbol等のツールを使うことでトークン消費を削減し、コード生成精度を向上させるため

## いつ使うのか

コードベースが数百ファイル以上で構造が複雑、またはLLMが頻繁に無関係なファイルを読む時

## やり方

1. uvをインストール（https://docs.astral.sh/uv/getting-started/installation/）
2. uvx --from git+https://github.com/oraios/serena serena start-mcp-server --help で起動オプション確認
3. クライアント（Claude Code等）の設定ファイルにSerena起動コマンドを追加（https://oraios.github.io/serena/02-usage/030_clients.html 参照）
4. クライアントを再起動してSerenaツールが利用可能になることを確認

### 入力

- uv（Pythonパッケージマネージャー）
- 対応LLMクライアント（Claude Code、Claude Desktop、VSCode+Cline等）
- 対象プロジェクトのパス

### 出力

- MCPサーバープロセス
- LLMから利用可能なfind_symbol、find_referencing_symbols、insert_after_symbol等のツール

## 使うツール・ライブラリ

- uv
- Serena（https://github.com/oraios/serena）
- MCP対応クライアント

## コード例

```
uvx --from git+https://github.com/oraios/serena serena start-mcp-server
```

## 前提知識

- MCPの概念と動作原理
- Language Server Protocol（LSP）の基礎知識
- LLMエージェントのツール呼び出しメカニズム
- Python環境管理（uv）の基本操作
- 対象言語のLanguage Serverインストール方法（LSPバックエンド使用時）
- JetBrains IDE操作の基礎（JetBrainsバックエンド使用時）

## 根拠

> Serena is a powerful coding agent toolkit capable of turning an LLM into a fully-featured agent that works directly on your codebase.

> Serena provides essential semantic code retrieval and editing tools that are akin to an IDE's capabilities, extracting code entities at the symbol level and exploiting relational structure.

> The Serena JetBrains Plugin leverages the powerful code analysis capabilities of your JetBrains IDE. The plugin naturally supports all programming languages and frameworks that are supported by JetBrains IDEs.

> Most users report that Serena has strong positive effects on the results of their coding agents, even when used within very capable agents like Claude Code. Serena is often described to be a game changer, providing an enormous productivity boost.

> We are proud to announce that the Visual Studio Code team, together with Microsoft's Open Source Programs Office and GitHub Open Source have decided to sponsor Serena with a one-time contribution!
