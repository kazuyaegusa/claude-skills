# NPXでの即座起動によるプロトタイピング

> バイナリのダウンロード・インストールなしに、npxコマンド1行でMCP Toolboxサーバーを起動する

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: dev-tool

## なぜ使うのか

ローカル検証や実験段階ではインストール手順を省略し、設定ファイルがあればすぐにサーバーを立ち上げたい

## いつ使うのか

初回試行時、CIでの一時的な起動、複数バージョンを切り替えながら検証したい時（本番環境では非推奨）

## やり方

1. tools.yamlを用意
2. `npx @toolbox-sdk/server --config tools.yaml`を実行
3. 最新版のtoolboxサーバーが自動ダウンロードされて起動

### 入力

- tools.yaml設定ファイル
- Node.js実行環境

### 出力

- 起動したMCPサーバー（ポート5000）

## 使うツール・ライブラリ

- npx
- @toolbox-sdk/server

## コード例

```
npx @toolbox-sdk/server --config tools.yaml
```

## 前提知識

- MCPプロトコルの基本概念（Model Context Protocol）
- LLMエージェントフレームワークの基礎（LangChain/LlamaIndex/Genkit等のいずれか）
- データベース接続の基本（PostgreSQL/MySQL等の接続文字列）
- YAMLの基本文法
- ツール呼び出しの仕組み（Function Calling）

## 根拠

> npx @toolbox-sdk/server --config tools.yaml - This runs the latest version of the toolbox server with your configuration file.
