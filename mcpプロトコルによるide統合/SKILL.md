# MCPプロトコルによるIDE統合

> Model Context Protocol (MCP)を介してClaude Code、Cursor、Gemini CLI等のIDEから、自然言語でデータベース操作を可能にする

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: claude-code-workflow

## なぜ使うのか

開発者がコンテキストスイッチなくIDE内でデータベーススキーマ確認・クエリ実行・テストデータ生成等を行え、開発速度が向上する

## いつ使うのか

IDE内でデータベーススキーマを確認したい時、手作業でSQLを書かずにデータを取得したい時、スキーマに基づいたコード生成をAIに依頼したい時

## やり方

1. Toolboxサーバーを起動（MCP対応）
2. IDE側のMCP設定にToolboxサーバーのエンドポイントを追加
3. IDE内でAIアシスタントに自然言語で依頼（例: "2024年に配送された注文とその商品を教えて"）
4. AIアシスタントがToolboxのツールを自動選択・実行
5. 結果がIDE内に表示される

### 入力

- 自然言語での質問・依頼
- Toolboxサーバーのエンドポイント

### 出力

- クエリ結果、生成されたコード、スキーマ情報

## 使うツール・ライブラリ

- MCP Toolbox server
- Claude Code、Cursor、Gemini CLI等のMCP対応IDE

## コード例

```
# NPXで直接実行（実験用）
npx @toolbox-sdk/server --tools-file tools.yaml

# Gemini CLI Extensions経由
gemini extensions install https://github.com/gemini-cli-extensions/mcp-toolbox
```

## 前提知識

- Model Context Protocol (MCP)の基本概念
- AIエージェントフレームワーク（LangChain、LlamaIndex、Genkit等）の基礎知識
- データベース接続の基本（PostgreSQL、MySQL、Spanner、BigQuery等）
- YAML形式の読み書き
- Docker/コンテナ技術の基礎（本番デプロイ時）
- OpenTelemetryによる可観測性の概念（本番運用時）
