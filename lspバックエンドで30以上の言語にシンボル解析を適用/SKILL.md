# LSPバックエンドで30以上の言語にシンボル解析を適用

> Language Server Protocol実装をSerena経由で利用し、多言語プロジェクト（Python、JS/TS、Rust、Go、Java等30以上）のシンボル定義・参照・編集を統一的に処理する

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: agent-orchestration

## なぜ使うのか

各言語専用ツールを個別に統合するコストを避け、LSPという標準プロトコルで一貫したコード解析機能を提供するため

## いつ使うのか

無料・オープンソースの解析ツールで多言語対応したい、またはJetBrains IDEを使っていない場合

## やり方

1. プロジェクトで使う言語のLanguage Serverが必要に応じてインストールされているか確認（https://oraios.github.io/serena/01-about/020_programming-languages.html）
2. SerenaがLSPサーバーと通信して自動的にシンボル情報を取得
3. LLMがfind_symbol等のツールを呼び出すと、Serenaが内部でLSPリクエストを送り結果を返す

### 入力

- 対象言語のLanguage Server（例: pylsp、typescript-language-server、rust-analyzer）
- プロジェクトソースコード

### 出力

- シンボル定義位置、参照一覧、型情報等のLSP解析結果

## 使うツール・ライブラリ

- Solid-LSP（Serenaに内蔵、multilspyベース）
- 各言語のLSP実装

## 前提知識

- MCPの概念と動作原理
- Language Server Protocol（LSP）の基礎知識
- LLMエージェントのツール呼び出しメカニズム
- Python環境管理（uv）の基本操作
- 対象言語のLanguage Serverインストール方法（LSPバックエンド使用時）
- JetBrains IDE操作の基礎（JetBrainsバックエンド使用時）

## 根拠

> support for over 30 programming languages, including AL, Ansible, Bash, C#, C/C++, Clojure, Dart, Elixir, Elm, Erlang, Fortran, GLSL, Go, Groovy, Haskell, HLSL, Java, Javascript, Julia, Kotlin, Lean 4, Lua, Luau, Markdown, MATLAB, Nix, OCaml, Perl, PHP, PowerShell, Python, R, Ruby, Rust, Scala, Solidity, Swift, TOML, TypeScript, WGSL, YAML, and Zig.

> The Serena JetBrains Plugin leverages the powerful code analysis capabilities of your JetBrains IDE. The plugin naturally supports all programming languages and frameworks that are supported by JetBrains IDEs.
