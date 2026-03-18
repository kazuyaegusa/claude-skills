# MCPサーバーによるツールの中央管理と動的リロード

> tools.yamlの変更を検知し、サーバー再起動なしでツール定義を自動更新する

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: agent-orchestration

## なぜ使うのか

ツールの修正・追加時にアプリケーション本体やエージェントの再デプロイが不要になり、開発サイクルが高速化する

## いつ使うのか

開発中に頻繁にツール定義を調整する必要がある時、または本番環境でツールロジックのA/Bテストを行いたい時

## やり方

1. Toolboxサーバーをデフォルト設定で起動（動的リロード有効）
2. tools.yamlを編集（新しいツール追加、既存ツールのSQL変更等）
3. サーバーが変更を自動検知し、次回のload_toolset()呼び出し時に新しい定義を返す
4. 動的リロードを無効化したい場合は`--disable-reload`フラグを付与

### 入力

- 編集されたtools.yaml

### 出力

- 更新されたツール定義（エージェント側での追加のデプロイ作業なし）

## 使うツール・ライブラリ

- MCP Toolbox Server（デフォルトで動的リロード有効）

## コード例

```
# 動的リロード有効（デフォルト）
./toolbox --tools-file tools.yaml

# 動的リロード無効
./toolbox --tools-file tools.yaml --disable-reload
```

## 前提知識

- MCP（Model Context Protocol）の基本概念
- LLMエージェントフレームワーク（LangChain/LlamaIndex/Genkit等）の基礎知識
- SQL、データベース接続（ホスト/ポート/認証）の基本
- YAML設定ファイルの読み書き
- Docker/コンテナの基本操作（コンテナ版を使う場合）
- 各言語のパッケージマネージャー（pip, npm, go get）の使用経験
