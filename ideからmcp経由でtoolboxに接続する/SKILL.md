# IDEからMCP経由でToolboxに接続する

> Claude CodeやCursor等のMCP対応IDEにToolboxサーバーを接続し、AI assistantに自然言語でデータベース操作をさせる

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: claude-code-workflow

## なぜ使うのか

コンテキストスイッチを減らし、AIアシスタントを真の共同開発者にするため。SQLを書かずに自然言語でクエリを実行し、スキーマを参照してコード生成できる

## いつ使うのか

IDE内でデータベーススキーマを参照しながらコード生成したい時、SQLを書かずにデータ分析したい時、データベース管理タスクをAIに委譲したい時

## やり方

1. Toolboxサーバーを起動（tools.yamlで必要なデータベースとツールを定義）
2. IDEのMCP設定でToolboxサーバーのエンドポイント（http://127.0.0.1:5000）を追加
3. IDE内でAIアシスタントに自然言語で指示（例: 「2024年に配送された注文数と商品を教えて」）
4. アシスタントが適切なToolboxツールを呼び出してクエリ実行・結果を返す

### 入力

- 稼働中のToolboxサーバー
- MCP対応IDE（Claude Code, Cursor等）

### 出力

- 自然言語でのクエリ結果
- リアルタイムスキーマを反映したコード生成

## 使うツール・ライブラリ

- MCP対応IDE（Claude Code, Cursor等）
- Toolbox MCP server

## コード例

```
# IDE設定例（概念的）
# .mcp/settings.json等でToolboxサーバーを追加
{
  "mcpServers": {
    "toolbox": {
      "url": "http://127.0.0.1:5000"
    }
  }
}

# IDE内で自然言語で指示
# 「2024年に配送された注文数と商品を教えて」
# → アシスタントがToolboxのツールを呼び出してクエリ実行
```

## 前提知識

- MCPプロトコルの基本概念（サーバー・クライアント・ツール）
- 使用するデータベース（PostgreSQL/MySQL/BigQuery等）の接続情報
- AIフレームワーク（LangChain/LlamaIndex/Genkit等）の基本的な使い方
- YAML形式の理解
- 非同期処理（async/await）の理解（Python/JS SDKを使う場合）
