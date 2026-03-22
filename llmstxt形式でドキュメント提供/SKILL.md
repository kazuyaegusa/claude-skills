# llms.txt形式でドキュメント提供

> FastMCPのドキュメントをllms.txt標準に従ってLLM可読形式で公開する

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: context-management

## なぜ使うのか

LLMがドキュメント全体を直接読み込み可能にすることで、コーディング時のコンテキスト参照が容易になる

## いつ使うのか

LLMにFastMCP APIやパターンを質問させたい時、または開発中にAI補完でドキュメント参照させたい時

## やり方

1. llms.txt（サイトマップ）をgofastmcp.com/llms.txtで公開
2. llms-full.txt（全文）をgofastmcp.com/llms-full.txtで公開
3. LLMツールから直接参照可能に

### 入力

- FastMCPドキュメントサイト

### 出力

- llms.txt（サイトマップ）
- llms-full.txt（全ドキュメント）

## 使うツール・ライブラリ

- llmstxt.org標準

## コード例

```
# LLMから参照する例
# "Read https://gofastmcp.com/llms.txt to understand FastMCP API"
```

## 前提知識

- Python 3.x基礎知識
- 型ヒント（Type Hints）の理解
- デコレータの基本概念
- Model Context Protocol (MCP)の概要理解
- 非同期プログラミング（async/await）の基礎（応用時）
