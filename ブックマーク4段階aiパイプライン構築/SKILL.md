# ブックマーク4段階AIパイプライン構築

> XブックマークデータをEntity抽出→Vision解析→セマンティックタグ付け→カテゴリ分類の4段階で処理し、検索可能なSQLite DBを構築する。

- 出典: https://x.com/l_go_mrk/status/2037749522021892427
- 投稿者: AI駆動塾
- カテゴリ: automation-pipeline

## なぜ使うのか

生のブックマークJSONはハッシュタグ・URL・メンション程度しか構造化されておらず、意味検索・画像検索・カテゴリ横断検索が不可能なため、AI処理で多次元のメタデータを付加する必要がある。

## いつ使うのか

Xブックマークが100件を超えており、内容ベースの再検索や整理をしたいとき

### 具体的な適用場面

- Xのブックマークが数百件以上あり「あの投稿どこだっけ」が頻発している
- スクリーンショット付き投稿をブックマークしているがOCRなしで内容検索できずにいる
- API課金を避けながらClaude CLIサブスク認証でローカルAIアプリを動かしたい

## やり方

1. `git clone https://github.com/viperrcrypto/Siftly && cd Siftly && npm install` でセットアップ
2. `.env` にAIプロバイダー設定（Claude CLI利用者はスキップ可）
3. ブラウザのコンソールまたはブックマークレット経由でXブックマークJSONをエクスポート
4. UIからJSONをインポートして「Run Pipeline」を実行
   - Stage 1 Entity Extraction: ハッシュタグ・URL・メンション・100以上の既知ツール名を無料で抽出（APIコール不要）
   - Stage 2 Vision Analysis: 各画像/GIF/サムネイルから30〜40の視覚タグを生成
   - Stage 3 Semantic Tagging: ブックマーク1件あたり25〜35の検索用セマンティックタグを生成
   - Stage 4 Categorization: 信頼スコア付きで1〜3カテゴリに分類
5. `npm run dev` でUI起動後、自然言語クエリで検索

### 入力

- Xブックマークデータ（ブックマークレット or コンソールスクリプトで取得）
- AIプロバイダーのAPIキー（Claude CLI使用者は不要）

### 出力

- タグ・カテゴリ付きSQLiteローカルDB
- 自然言語検索インターフェース
- マインドマップ可視化
- CSV/JSON/ZIPエクスポート

## 使うツール・ライブラリ

- Next.js 16
- TypeScript 5
- SQLite
- Tailwind CSS v4
- Claude API / OpenAI API / Ollama（選択式）

## コード例

```
// 4-stage pipeline (from README)
📥 Import (bookmarklet or console script)
    ↓
🏷️  Entity Extraction   — 100+ known tools, hashtags, URLs (free, zero API calls)
    ↓
👁️  Vision Analysis      — 30–40 visual tags per image/GIF/thumbnail
    ↓
🧠 Semantic Tagging     — 25–35 searchable tags per bookmark
    ↓
📂 Categorization       — 1–3 categories with confidence scores
```

## 前提知識

- Node.js / npm の基本操作
- Xにログイン済みのブラウザ環境
- Claude CLIセッション or Claude/OpenAI APIキー（いずれか）
- git clone・npm install・npm run dev が実行できる環境

## 根拠

> 「4段階AIパイプライン: Import → Entity Extraction → Vision Analysis → Semantic Tagging → Categorization」（README）

> 「Entity Extraction — mines hashtags, URLs, mentions, and 100+ known tools from raw tweet data (free, zero API calls)」（README）

> 「Vision Analysis — reads text, objects, and context from every image/GIF/video thumbnail (30–40 visual tags per image)」（README）

> 「Semantic Tagging — generates 25–35 searchable tags per bookmark for AI-powered search」（README）

> 「Categorization — assigns each bookmark to 1–3 categories with confidence scores」（README）
