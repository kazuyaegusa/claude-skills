# LSPベースのシンボルレベル抽出をMCPツール化

> Language Server Protocol (LSP)を抽象化レイヤーで統合し、シンボル検索・参照検索・型階層などをMCPツールとして提供する

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: claude-code-workflow

## なぜ使うのか

エージェントがファイル全体を読まずにコード構造と関係性を理解でき、トークン効率と信頼性が向上する。40以上の言語に対応可能。

## いつ使うのか

オープンソース・無料で多言語対応のコーディングエージェント基盤を作りたい時

## やり方

1. LSP実装をラップする抽象化レイヤーを設計 2. find_symbol, symbol_overview, find_referencing_symbolsなどのMCPツールを実装 3. uvでパッケージ化し `serena init` でセットアップ 4. クライアントのMCP設定に起動コマンドを追加

### 入力

- LSP実装（各言語のLanguage Server）
- MCPクライアント（Claude Code, Codex, Claude Desktop等）

### 出力

- シンボル検索結果
- ファイルアウトライン
- 参照一覧

## 使うツール・ライブラリ

- Language Server Protocol (LSP)
- MCP (Model Context Protocol)
- uv (Pythonパッケージマネージャ)

## コード例

```
uvx -p 3.13 --from git+https://github.com/oraios/serena serena init
```

## 前提知識

- Model Context Protocol (MCP)の基本的な理解
- Language Server Protocol (LSP)の概念
- uv (Pythonパッケージマネージャ)の使い方
- シンボル・参照・型階層などのIDE概念
- Claude Code/Codex/Claude Desktop等のMCP対応クライアント

## 根拠

> support for over 40 programming languages, including AL, Ansible, Bash, C#, C/C++, Clojure, Dart, Elixir, Elm, Erlang, Fortran, F#, GLSL, Go, Groovy, Haskell, HLSL, Java, JavaScript, Julia, Kotlin, Lean 4, Lua, Luau, Markdown, MATLAB, Nix, OCaml, Perl, PHP, PowerShell, Python, R, Ruby, Rust, Scala, Solidity, Swift, TOML, TypeScript, WGSL, YAML, and Zig.
