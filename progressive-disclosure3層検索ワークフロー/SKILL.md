# Progressive Disclosure（3層検索ワークフロー）

> 検索を3段階に分け、トークンコストを10分の1に削減しながら必要な情報のみ取得する

- 出典: https://github.com/thedotmack/claude-mem
- 投稿者: thedotmack
- カテゴリ: claude-code-workflow

## なぜ使うのか

全Observationの全文をプロンプトに注入するとトークン爆発するが、関連性不明のまま要約だけ注入すると精度が落ちる。段階的に詳細度を上げることで、コストと精度を両立できる

## いつ使うのか

過去のプロジェクト履歴から特定の情報を検索する際（mem-searchスキル使用時）

## やり方

1. `search(query, type, limit)`でインデックスのみ取得（ID+タイトル、50-100トークン/結果） 2. `timeline(observationId)`で時系列前後の文脈を確認 3. 関連性が高いIDだけ`get_observations(ids)`で全文取得（500-1,000トークン/結果）

### 入力

- 検索クエリ（自然言語）
- フィルタ条件（type/date/project）

### 出力

- Layer 1: 検索結果インデックス（ID+タイトル配列）
- Layer 2: 時系列コンテキスト（前後のObservation）
- Layer 3: 選択されたObservationの全文

## 使うツール・ライブラリ

- SQLite FTS5（全文検索）
- Chroma Vector Database（セマンティック検索）
- MCP Tools（search/timeline/get_observations）

## コード例

```
// Layer 1
const index = await search({ query: 'auth bug', type: 'bugfix', limit: 10 });
// Layer 2
const context = await timeline({ observationId: index[0].id });
// Layer 3
const details = await get_observations({ ids: [123, 456] });
```

## 前提知識

- Claude Codeの基本的な使い方（ツール使用、セッション概念）
- Node.js 18+のインストール
- SQLiteの基本知識（オプション：データ構造理解のため）
- MCP（Model Context Protocol）の概念（オプション：検索ツール理解のため）

## 根拠

> 「Progressive Disclosure - Layered memory retrieval with token cost visibility」
