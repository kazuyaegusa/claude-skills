# クエリバリエーションで検索カバレッジ向上

> 同一検索意図に対して複数のクエリ表現を生成し、並列実行後にマージ・重複排除

- 出典: https://github.com/exa-labs/exa-mcp-server
- 投稿者: exa-labs
- カテゴリ: other

## なぜ使うのか

Exaは表現が違うと異なる結果を返すため、1クエリだけでは見落としが発生する

## いつ使うのか

網羅性が重要な調査（競合分析、文献レビュー等）を行う場合

## やり方

1. 検索意図から2-3個のクエリバリエーションを生成
2. additionalQueries パラメータに指定、または並列に複数検索実行
3. 結果をマージして重複排除
4. ユーザーに統合結果を返す

### 入力

- 検索意図
- カテゴリ

### 出力

- マージ・重複排除済み検索結果

## 使うツール・ライブラリ

- web_search_advanced_exa
- additionalQueries parameter

## コード例

```
{
  "query": "machine learning engineer San Francisco",
  "category": "people",
  "additionalQueries": ["ML engineer SF", "AI engineer Bay Area"],
  "numResults": 25
}
```

## 前提知識

- MCP (Model Context Protocol) の基本概念
- 使用するAI環境（Cursor/VS Code/Claude Code等）の設定ファイル構造
- JSONフォーマットの編集能力
- Exa APIの検索カテゴリと用途の理解
