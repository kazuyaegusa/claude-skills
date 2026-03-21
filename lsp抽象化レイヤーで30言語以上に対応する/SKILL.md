# LSP抽象化レイヤーで30言語以上に対応する

> Language Server Protocol（LSP）を抽象化し、30言語以上の言語サーバーを統一インターフェースで利用できるようにする（Solid-LSPライブラリ）

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: agent-orchestration

## なぜ使うのか

各言語専用のツールを個別実装するのではなく、LSP標準に準拠した言語サーバーを活用することで、最小の実装コストで多言語対応を実現できる

## いつ使うのか

対応言語を増やしたい、または既存のLSP対応言語でシンボルレベル操作を実装したい時

## やり方

1. multilspy（Microsoftのライブラリ）をベースに、Solid-LSPライブラリを構築
2. LSPの非同期呼び出しを同期化し、Pythonから扱いやすくする
3. シンボル検索・参照検索・定義取得等のLSP機能を統一APIで提供
4. 各言語の言語サーバー（rust-analyzerやpyright等）をSolid-LSP経由で呼び出す
5. Serenaのツール（find_symbol等）が内部でSolid-LSPを使い、言語非依存で動作

### 入力

- multilspy（LSPラッパー）
- 各言語の言語サーバー実装（例: rust-analyzer、pyright等）
- LSP標準仕様

### 出力

- Solid-LSPライブラリ（Serena内部モジュール）
- 30言語以上のシンボル検索・編集機能

## 使うツール・ライブラリ

- multilspy
- LSP実装各種（rust-analyzer、pyright、clangd等）

## コード例

```
# 概念的なSolid-LSP利用例（Serena内部）
# from solidlsp import LSPClient
# client = LSPClient(language='python', workspace_path='/path/to/project')
# symbols = client.find_symbol('MyClass')
# references = client.find_references(symbol_location)
```

## 前提知識

- Model Context Protocol（MCP）の基本概念
- Language Server Protocol（LSP）の基礎知識
- LLMエージェントの動作原理（ツール呼び出し・Function Calling）
- Python環境構築（uv等のパッケージマネージャー）
- コードベースにおけるシンボル（関数・クラス・変数等）の概念
- （JetBrainsプラグイン利用時）JetBrains IDEの基本操作

## 根拠

> 「support for over 30 programming languages」（LSP経由）

> 「The plugin naturally supports all programming languages and frameworks that are supported by JetBrains IDEs」
