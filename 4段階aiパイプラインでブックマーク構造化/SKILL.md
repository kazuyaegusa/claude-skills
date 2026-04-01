# 4段階AIパイプラインでブックマーク構造化

> Twitterブックマークを Entity Extraction → Vision Analysis → Semantic Tagging → Categorization の4段階で処理し、検索可能な構造データに変換する

- 出典: https://x.com/l_go_mrk/status/2037749522021892427
- 投稿者: AI駆動塾
- カテゴリ: automation-pipeline

## なぜ使うのか

単純なキーワードマッチでは画像内テキストや意味的類似性を拾えない。Entity Extractionを無料（APIコールなし）の前処理として分離することで、コストのかかるLLM処理への入力品質を上げつつAPI呼び出し回数を最小化できる

## いつ使うのか

大量のTwitterブックマーク（数十件以上）を整理して、後から自然言語で検索・再発見したいとき

### 具体的な適用場面

- 数百〜数千のTwitterブックマークが溜まり、後から目的の投稿が見つからなくなっている状況
- スクリーンショット付きの技術投稿をブックマークしているが、画像内のコードや図表が検索できない状況
- 技術情報・ツール情報をジャンル別に整理してマインドマップで全体把握したい場合

## やり方

1. リポジトリをクローン: `git clone https://github.com/viperrcrypto/Siftly && cd Siftly`
2. 依存インストール: `npm install`
3. `.env` に LLM APIキーを設定（Claude CLI セッションがあれば不要）
4. `npm run dev` でローカルサーバー起動
5. ブラウザで localhost:3000 を開き、ブックマークレット or コンソールスクリプトでブックマークをインポート
6. UI から「Analyze」を実行すると4段階パイプラインが自動的に順次実行され、ブックマークにタグ・カテゴリが付与される

### 入力

- Twitter/X のブックマークデータ（ブックマークレット経由でエクスポート）
- LLM APIキー（Claude CLI セッションがあれば不要）

### 出力

- タグ付き・カテゴリ分類済みブックマーク（SQLite）
- 自然言語検索インデックス
- マインドマップ可視化
- CSV / JSON / ZIP エクスポートデータ

## 使うツール・ライブラリ

- Next.js 16
- TypeScript 5
- SQLite
- Tailwind CSS v4
- Claude CLI または LLM API

## コード例

```
// 4段階パイプラインの構成（READMEより）
📥 Import (bookmarklet or console script — no extensions needed)
    ↓
🏷️  Entity Extraction   — mines hashtags, URLs, mentions, and 100+ known tools from raw tweet data (free, zero API calls)
    ↓
👁️  Vision Analysis      — reads text, objects, and context from every image/GIF/video thumbnail (30–40 visual tags per image)
    ↓
🧠 Semantic Tagging     — generates 25–35 searchable tags per bookmark for AI-powered search
    ↓
📂 Categorization       — assigns each bookmark to 1–3 categories with confidence scores
```

## 前提知識

- Node.js（Next.js 16が動作するバージョン、v18以上推奨）
- Git（リポジトリのクローン用）
- LLM APIキー（Claude / OpenAI等）、またはClaude CLIの有効セッション
- Twitter/Xアカウントのブックマーク機能を使っていること

## 根拠

> It runs a 4-stage AI pipeline on your bookmarks: Entity Extraction → Vision Analysis → Semantic Tagging → Categorization

> Claude CLIセッションを自動検出するから、Claude使ってる人はAPIキー設定すら不要。

> Vision Analysis — reads text, objects, and context from every image/GIF/video thumbnail (30–40 visual tags per image)

> Semantic Tagging — generates 25–35 searchable tags per bookmark for AI-powered search

> Categorization — assigns each bookmark to 1–3 categories with confidence scores
