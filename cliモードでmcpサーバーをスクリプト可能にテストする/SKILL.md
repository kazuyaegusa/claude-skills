# CLIモードでMCPサーバーをスクリプト可能にテストする

> MCP Inspectorをコマンドラインから実行し、tools/resources/promptsの操作を標準出力に出力することで、CI/CDやAIアシスタントと統合する

- 出典: https://github.com/modelcontextprotocol/inspector
- 投稿者: modelcontextprotocol
- カテゴリ: prompt-engineering

## なぜ使うのか

UI操作では自動化できないテストシナリオを実現し、コード変更→テスト実行→結果確認のフィードバックループをAIコーディングアシスタント（Cursor等）から直接実行できるようにする

## いつ使うのか

CI/CDパイプラインでのMCPサーバー自動テスト、AIコーディングアシスタントとの統合、バッチ処理でのリソース一括取得時

## やり方

1. `npx @modelcontextprotocol/inspector --cli node build/index.js` で起動
2. `--method tools/list` でツール一覧を取得
3. `--method tools/call --tool-name mytool --tool-arg key=value` でツール実行
4. JSON出力を標準出力から取得してログ解析やCI/CD統合

### 入力

- MCPサーバーのコマンド（stdio）またはURL（SSE/HTTP）
- メソッド指定（--method tools/list | tools/call | resources/list等）
- ツール引数（--tool-name, --tool-arg key=value形式）

### 出力

- JSON形式の標準出力（ツール実行結果、リソース一覧など）
- スクリプトやCIパイプラインで解析可能な機械可読データ

## 使うツール・ライブラリ

- npx
- @modelcontextprotocol/inspector --cli

## コード例

```
# ツール一覧取得
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list

# ツール実行
npx @modelcontextprotocol/inspector --cli node build/index.js \
  --method tools/call \
  --tool-name mytool \
  --tool-arg key=value \
  --tool-arg 'options={"format": "json"}'

# リモートサーバー（Streamable HTTP）
npx @modelcontextprotocol/inspector --cli https://my-server.com \
  --transport http \
  --method tools/list \
  --header "X-API-Key: xxx"

# 設定ファイル経由
npx @modelcontextprotocol/inspector --cli --config mcp.json --server myserver
```

## 前提知識

- Node.js ^22.7.5以上
- MCPサーバーの基本概念（tools/resources/prompts）の理解
- MCPのトランスポート種別（stdio/SSE/Streamable HTTP）の違い
- JSON形式の設定ファイル記述能力（mcp.json）

## 根拠

> 「The MCP inspector is a developer tool for testing and debugging MCP servers.」

> 「npx @modelcontextprotocol/inspector node build/index.js」— インストール不要でMCPサーバーを起動

> 「CLI mode enables programmatic interaction with MCP servers from the command line, ideal for scripting, automation, and integration with coding assistants. This creates an efficient feedback loop for MCP server development.」

> 「The MCP Inspector provides convenient buttons to export server launch configurations for use in clients such as Cursor, Claude Code, or the Inspector's CLI. The file is usually called mcp.json.」
