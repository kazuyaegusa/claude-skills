# LSPとJetBrains Pluginから選択する

> バックエンドとしてLSP（無償・オープンソース、40+言語対応）またはJetBrains Plugin（IDE解析、最強だが有償IDE必要）のどちらかを選ぶ

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: other

## なぜ使うのか

LSPは広範な言語をカバーし無償で使えるが、JetBrains Pluginはより高度な解析とフレームワーク対応（Spring/Django等）が可能だから

## いつ使うのか

無償で広範囲の言語を扱いたいならLSP、最高精度でフレームワーク対応が欲しいならJetBrains Plugin

## やり方

1. LSPを使う場合：Serena起動時に自動で各言語のLSPサーバーがダウンロード・起動される（一部言語は追加依存あり）
2. JetBrains Pluginを使う場合：JetBrains Marketplace から Serena Plugin をインストールし、IDE起動後にSerena MCPサーバーと接続
3. どちらか一方を選ぶか、プロジェクトごとに切り替え可能

### 入力

- LSP：言語ごとのLSP実装（pyright/rust-analyzer等、Serenaが自動管理）
- JetBrains Plugin：IntelliJ/PyCharm/WebStorm等のIDE

### 出力

- シンボル解析・参照解決結果
- コード補完・リファクタリング情報

## 使うツール・ライブラリ

- multilspy（LSPラッパー）
- Solid-LSP（Serenaの同期LSPレイヤー）
- Serena JetBrains Plugin

## コード例

```
# LSP版のインストール例（デフォルト）
uvx --from git+https://github.com/oraios/serena serena start-mcp-server

# JetBrains Plugin版のセットアップ
# 1. IDEで Preferences > Plugins > Marketplace から "Serena" を検索してインストール
# 2. MCPクライアント設定でSerenaサーバーを指定（LSP版と同じコマンド）
# 3. IDE起動時にPluginが自動でコード解析機能を提供
```

## 前提知識

- MCPの基本概念（Model Context Protocolとは何か）
- LSPの基本（Language Server Protocolとは何か、なぜシンボルレベル解析ができるか）
- コーディングエージェントの基本的な動作原理（ツール呼び出し、ファイル読み書き等）
- Python/uvの基本（uvxコマンドでPythonツールを実行できる知識）
- JSONベースの設定ファイル編集（クライアント設定でMCPサーバーを登録するため）

## 根拠

> 「Serena provides essential semantic code retrieval and editing tools that are akin to an IDE's capabilities, extracting code entities at the symbol level and exploiting relational structure.」

> 「The plugin naturally supports all programming languages and frameworks that are supported by JetBrains IDEs, including IntelliJ IDEA, PyCharm, Android Studio, WebStorm, PhpStorm, RubyMine, GoLand」

> 「Most users report that Serena has strong positive effects on the results of their coding agents, even when used within very capable agents like Claude Code. Serena is often described to be a game changer, providing an enormous productivity boost.」

> 「We are proud to announce that the Visual Studio Code team, together with Microsoft's Open Source Programs Office and GitHub Open Source have decided to sponsor Serena with a one-time contribution!」
