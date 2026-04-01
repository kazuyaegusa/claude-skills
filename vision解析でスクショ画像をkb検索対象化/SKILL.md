# Vision解析でスクショ画像をKB検索対象化

> ブックマークに添付された画像・GIF・動画サムネイルをVision AI（マルチモーダルモデル）で解析し、1枚あたり30〜40個の視覚タグを生成して全文検索に組み込む。

- 出典: https://x.com/l_go_mrk/status/2037749522021892427
- 投稿者: AI駆動塾
- カテゴリ: other

## なぜ使うのか

Xには画像だけで情報を伝える投稿（スクリーンショット、図解、コードキャプチャなど）が多いが、テキスト検索では画像内容がヒットしない。Vision解析でOCR＋オブジェクト認識のタグを付与することで、「あのコードのスクショ」「ダッシュボードの画像」も検索対象になる。

## いつ使うのか

スクリーンショット・図解・コードキャプチャ含む投稿をブックマークしていて、その内容で後から検索したいとき

### 具体的な適用場面

- Xのブックマークが数百件以上あり「あの投稿どこだっけ」が頻発している
- スクリーンショット付き投稿をブックマークしているがOCRなしで内容検索できずにいる
- API課金を避けながらClaude CLIサブスク認証でローカルAIアプリを動かしたい

## やり方

1. パイプラインのStage 2（Vision Analysis）で自動実行される
2. Claude/OpenAIのVisionモデル（例: claude-3-5-sonnet, gpt-4o）へ画像URLを送信
3. 返却されたテキスト・オブジェクト・コンテキスト情報を30〜40タグに変換してDBに保存
4. Stage 3のSemantic Taggingでこれらのビジョンタグも含めたセマンティック検索インデックスを構築
5. 検索クエリ「スクショ付きのPython エラー解説」のように画像内容で検索できる

### 入力

- ブックマークに添付された画像・GIF・動画サムネイルのURL
- VisionモデルAPIアクセス（Claude/OpenAI）

### 出力

- 1画像あたり30〜40個の視覚タグ（テキスト、オブジェクト、コンテキスト）
- 画像内容で検索可能なSQLiteインデックス

## 使うツール・ライブラリ

- Claude claude-3-5-sonnet（Vision）
- OpenAI gpt-4o（Vision）
- SQLite

## コード例

```
// Vision Analysis stage output example
// 30-40 visual tags per image including:
// - OCR text extracted from image
// - Objects detected (charts, code, screenshots)
// - Context tags ("programming", "error message", "UI design")
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
