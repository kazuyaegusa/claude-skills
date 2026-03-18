# HNSW索引による超高速ベクトル検索

> Hierarchical Navigable Small World（HNSW）アルゴリズムで384次元ベクトルを<1ms（最大12,500倍高速）で検索し、類似パターンを瞬時に取得

- 出典: https://github.com/ruvnet/ruflo
- 投稿者: ruvnet
- カテゴリ: agent-orchestration

## なぜ使うのか

線形検索は10万ベクトルで数秒かかるが、HNSWはグラフ構造で探索経路を絞り込み、サブミリ秒で結果を返す。これにより大規模パターンDBでもリアルタイム応答が可能

## いつ使うのか

大量のパターン（1万件以上）から類似例を高速に見つけたい場合、またはリアルタイム推論が必要な場合

## やり方

1. `npx ruflo memory init --force`でAgentDB初期化
2. パターン保存時に自動でHNSW索引構築（M=16、efConstruction=200）
3. `npx ruflo memory search -q "authentication" --build-hnsw`で検索
4. 内部的にHNSWグラフを辿って最近傍k件を取得（~61µs）
5. コサイン類似度でランキング、上位5件を返却

### 入力

- クエリベクトル（またはクエリテキスト、自動埋め込み）
- k（上位k件取得）
- 最小類似度閾値（例: 0.7）

### 出力

- 類似パターン配列（key、similarity、content）
- 検索時間（通常<1ms）

## 使うツール・ライブラリ

- @claude-flow/memory（AgentDB、HnswLite）
- ONNX Runtime（ローカル埋め込み生成）
- RuVector（オプション、ネイティブ高速化）

## コード例

```
const db = new AgentDB({ path: './data/memory', hnsw: { m: 16, efConstruction: 200 } });
await db.store('auth-pattern', { content: 'JWT authentication flow', embedding: await db.embed('JWT auth') });
const results = await db.search('how to authenticate users', { topK: 5, minSimilarity: 0.7 });
// 結果: [{ key: 'auth-pattern', similarity: 0.92, content: '...' }]、時間: <1ms
```

## 前提知識

- Node.js 20+とnpm 9+
- Claude Code CLIのインストール（`npm install -g @anthropic-ai/claude-code`）
- Anthropic APIキー（Claude利用時）またはClaude Codeサブスクリプション
- 基本的なTypeScript/JavaScriptの知識
- （オプション）Docker（RuVector PostgreSQL利用時）
- （オプション）Git、GitHub CLI（GitHub統合時）
- マルチエージェントシステムの基本概念理解（推奨）

## 根拠

> 「150x-12,500x faster search」「HNSW (sub-millisecond retrieval)」
