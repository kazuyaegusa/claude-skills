# Gemini CLI Extensionsによるコマンドライン直接操作

> Gemini CLIの拡張機能として事前定義済みツール（AlloyDB/BigQuery/Cloud SQL等）またはカスタムツールを導入し、ターミナルから自然言語でデータベースを操作する

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: automation-pipeline

## なぜ使うのか

IDE外での作業（CI/CD、サーバーSSH操作、スクリプト実行）でもAIによるデータベース支援が必要な場合に、Gemini CLIの拡張機能として即座にツールを追加できる

## いつ使うのか

IDE外での運用作業（ログ調査、データパッチ、スキーマ確認）をAIに支援させたい時、またはCI/CDパイプライン内で自然言語によるデータベース操作を自動化したい時

## やり方

1. 事前定義済みツールの場合: `gemini extensions install https://github.com/gemini-cli-extensions/<service-name>`
2. カスタムツールの場合: `gemini extensions install https://github.com/gemini-cli-extensions/mcp-toolbox`を実行し、自分のtools.yamlを参照
3. ターミナルで`gemini`コマンドを実行し、自然言語でクエリ（例: 「last 100 error logs in AlloyDB」）
4. Gemini CLIがMCP Toolbox経由でクエリを実行し、結果を返す

### 入力

- Gemini CLI
- インストールする拡張機能のURL
- カスタムツールの場合はtools.yaml

### 出力

- ターミナルでの自然言語によるデータベース操作結果

## 使うツール・ライブラリ

- Gemini CLI
- gemini-cli-extensions（MCP Toolbox, AlloyDB, BigQuery, Cloud SQL等）

## コード例

```
# 事前定義済みツール（AlloyDB）をインストール
gemini extensions install https://github.com/gemini-cli-extensions/alloydb

# カスタムツールをインストール
gemini extensions install https://github.com/gemini-cli-extensions/mcp-toolbox

# ターミナルで自然言語クエリ
gemini "Show me last 100 error logs in production database"
```

## 前提知識

- MCP（Model Context Protocol）の基本概念
- LLMエージェントフレームワーク（LangChain/LlamaIndex/Genkit等）の基礎知識
- SQL、データベース接続（ホスト/ポート/認証）の基本
- YAML設定ファイルの読み書き
- Docker/コンテナの基本操作（コンテナ版を使う場合）
- 各言語のパッケージマネージャー（pip, npm, go get）の使用経験

## 根拠

> Gemini CLI Extensionsの公式サポート（事前定義済みツール: AlloyDB, BigQuery, Cloud SQL等）
