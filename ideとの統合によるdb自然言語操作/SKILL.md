# IDEとの統合によるDB自然言語操作

> Claude Code/Cursor等のAI IDEにMCP ToolboxをMCPサーバーとして接続し、コーディング中にDBへ自然言語でクエリできるようにする

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: claude-code-workflow

## なぜ使うのか

IDE外部のDBクライアントに切り替えることなく、AIアシスタントに「2024年の注文件数は？」と聞くだけでSQL生成・実行・結果取得まで完結できる

## いつ使うのか

開発中にDBスキーマ確認やデータ検証を頻繁に行う時、SQLを書かずに素早くデータを確認したい時

## やり方

1. toolbox --config tools.yamlでサーバー起動
2. IDEのMCP設定にtoolboxサーバーのエンドポイントを追加
3. IDE内でAIアシスタントに自然言語でDB操作を依頼
4. AIがツールを選択・実行し結果を返す

### 入力

- 起動済みのMCP Toolboxサーバー
- IDEのMCP設定

### 出力

- 自然言語クエリに対するDB実行結果
- スキーマ情報を踏まえたコード生成

## 使うツール・ライブラリ

- Claude Code/Cursor等MCP対応IDE
- MCP Toolbox

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
