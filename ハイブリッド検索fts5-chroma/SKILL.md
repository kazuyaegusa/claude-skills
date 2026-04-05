# ハイブリッド検索（FTS5 + Chroma）

> SQLite FTS5によるキーワード検索とChroma vectorDBによるセマンティック検索を組み合わせ、文脈的に関連する過去履歴を高精度で発見する

- 出典: https://github.com/thedotmack/claude-mem
- 投稿者: thedotmack
- カテゴリ: claude-code-workflow

## なぜ使うのか

完全一致検索だけでは類似表現を見逃し、ベクトル検索だけではキーワード特定性が弱い。両者の統合で想起精度を最大化

## いつ使うのか

「認証周りの過去の失敗」等、キーワードと意味の両方で検索したい時

## やり方

1. ユーザークエリをFTS5で全文検索（高速）
2. 同じクエリをChromaでベクトル類似検索（意味的関連性）
3. スコアを統合してランキング
4. mem-searchスキル経由でClaude Codeに結果提供

### 入力

- 自然言語クエリ
- 観測データのベクトル埋め込み

### 出力

- 関連度スコア付き検索結果

## 使うツール・ライブラリ

- SQLite FTS5（全文検索エンジン）
- Chroma（ベクトルDB、Pythonバックエンド）
- uv（Python環境管理、自動インストール）

## コード例

```
// 検索API疑似コード
const ftsResults = await db.query(`SELECT * FROM observations_fts WHERE content MATCH ?`, [query]);
const chromaResults = await chroma.query({ queryTexts: [query], nResults: 10 });
const merged = mergeAndRank(ftsResults, chromaResults);
```

## 前提知識

- Claude Codeの基本操作とプラグインシステムの理解
- Node.js 18.0.0+の実行環境
- SQLiteの基本概念（テーブル、クエリ）
- ベクトル検索・埋め込みの基礎知識（Chroma理解のため）
- ライフサイクルフック・イベント駆動設計の概念
- TypeScript/JavaScript（カスタマイズ時）

## 根拠

> 「SQLite Database - Stores sessions, observations, summaries」
