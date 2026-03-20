# カテゴリ別フィルタ制限を考慮したクエリ設計

> Exa検索のcategoryパラメータに応じて、利用可能/不可能なフィルタを使い分ける

- 出典: https://github.com/exa-labs/exa-mcp-server
- 投稿者: exa-labs
- カテゴリ: data-processing

## なぜ使うのか

カテゴリごとにフィルタのサポート状況が異なり、サポート外のフィルタを使うと400/500エラーになるため

## いつ使うのか

Exa検索でエラーを回避し確実に結果を得たい場合、カテゴリ固有の検索最適化をしたい場合

## やり方

1. 検索目的に応じてカテゴリを選択（company/people/news/tweet/research paper/financial report等）
2. 各カテゴリのフィルタ制限を確認
   - company: includeDomains/excludeDomains/日付フィルタ不可
   - people: 日付フィルタ/includeText/excludeText不可、includeDomainsはLinkedInのみ
   - tweet: includeText/excludeText/includeDomains/excludeDomains/moderation不可
   - financial report: excludeText不可
   - research paper/personal site: 全フィルタ利用可
3. includeText/excludeTextは全カテゴリで単一要素配列のみ対応
4. 制限に従ってパラメータを構成

### 入力

- 検索目的（企業調査/人材検索/学術論文等）
- フィルタ要件（ドメイン指定、日付範囲、テキスト含有等）

### 出力

- エラーの起きないクエリパラメータセット

## 使うツール・ライブラリ

- web_search_advanced_exa tool

## コード例

```
// company category - ドメイン・日付フィルタ不可
{
  "query": "AI infrastructure startups",
  "category": "company",
  "numResults": 20
}

// research paper - 全フィルタ利用可
{
  "query": "transformer attention",
  "category": "research paper",
  "includeDomains": ["arxiv.org"],
  "startPublishedDate": "2024-01-01",
  "includeText": ["LLM"]
}
```

## 前提知識

- MCP (Model Context Protocol) の基本概念
- 使用するAI環境（Cursor/VS Code/Claude Code等）の設定ファイル構造
- JSONフォーマットの編集能力
- Exa APIの検索カテゴリと用途の理解
