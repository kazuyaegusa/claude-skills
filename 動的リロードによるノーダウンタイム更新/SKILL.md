# 動的リロードによるノーダウンタイム更新

> toolboxサーバー起動時にデフォルトで有効化される設定変更の自動検出・リロード機能

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: agent-orchestration

## なぜ使うのか

ツールのSQL文やパラメータを修正するたびにサーバー再起動すると開発サイクルが遅くなり、本番環境ではダウンタイムが発生する

## いつ使うのか

開発中にツール定義を頻繁に調整する時、本番環境でツールを無停止更新したい時

## やり方

1. toolbox --config tools.yamlで起動（--disable-reloadを付けなければデフォルトで有効）
2. tools.yamlを編集
3. toolboxが自動的にファイル変更を検知して設定を再読み込み
4. エージェントは次回ツールロード時に新定義を取得

### 入力

- 編集されたtools.yaml

### 出力

- 更新されたツール定義（再起動なし）

## 使うツール・ライブラリ

- toolbox CLI（デフォルト機能）

## コード例

```
# デフォルトで有効
toolbox --config tools.yaml

# 無効化する場合
toolbox --config tools.yaml --disable-reload
```

## 前提知識

- MCPプロトコルの基本概念（Model Context Protocol）
- LLMエージェントフレームワークの基礎（LangChain/LlamaIndex/Genkit等のいずれか）
- データベース接続の基本（PostgreSQL/MySQL等の接続文字列）
- YAMLの基本文法
- ツール呼び出しの仕組み（Function Calling）

## 根拠

> MCP Toolbox for Databases is an open source MCP server for databases. It enables you to develop tools easier, faster, and more securely by handling the complexities such as connection pooling, authentication, and more.

> Toolbox sits between your application's orchestration framework and your database, providing a control plane that is used to modify, distribute, or invoke tools.

> npx @toolbox-sdk/server --config tools.yaml - This runs the latest version of the toolbox server with your configuration file.

> Toolbox enables dynamic reloading by default. To disable, use the --disable-reload flag.

> By connecting your IDE to your databases with MCP Toolbox, you can delegate complex and time-consuming database tasks, allowing you to build faster and focus on what matters.
