# Hybrid Search（FTS5 + Chroma統合）

> SQLite FTS5のキーワード検索とChromaベクトルDBのセマンティック検索を組み合わせ、ハイブリッド検索を実現する

- 出典: https://github.com/thedotmack/claude-mem
- 投稿者: thedotmack
- カテゴリ: claude-code-workflow

## なぜ使うのか

キーワード検索だけでは同義語や意味の類似性を拾えず、ベクトル検索だけでは正確なキーワードマッチが弱い。両者を統合することで検索精度が向上する

## いつ使うのか

「認証周りのバグ修正」のような自然言語クエリで、過去の関連コードや議論を広く拾いたい場合

## やり方

1. uvでChroma依存をインストール（auto-install） 2. ObservationをChromaにembedding保存 3. 検索時にFTS5結果とChroma類似度スコアをマージ 4. スコアリングでランキング統合

### 入力

- 自然言語クエリ
- SQLite Observationテーブル
- Chroma embeddingインデックス

### 出力

- 統合スコアでランク付けされた検索結果

## 使うツール・ライブラリ

- Chroma
- uv（Python package manager）
- SQLite FTS5

## コード例

```
// Worker内部（概念）
const ftsResults = db.query('SELECT * FROM observations_fts WHERE content MATCH ?', query);
const chromaResults = await chroma.query({ queryTexts: [query], nResults: 10 });
const merged = mergeAndRank(ftsResults, chromaResults);
```

## 前提知識

- Claude Codeの基本的な使い方（ツール使用、セッション概念）
- Node.js 18+のインストール
- SQLiteの基本知識（オプション：データ構造理解のため）
- MCP（Model Context Protocol）の概念（オプション：検索ツール理解のため）

## 根拠

> 「Hybrid Search with Chroma vector database」
