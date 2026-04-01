# Vision解析で画像内テキストを検索対象化

> ブックマークに添付された画像・GIF・動画サムネイルをVision APIで解析し、画像内のテキスト・オブジェクト・コンテキストをタグとして抽出して検索インデックスに含める

- 出典: https://x.com/l_go_mrk/status/2037749522021892427
- 投稿者: AI駆動塾
- カテゴリ: context-management

## なぜ使うのか

スクリーンショット付きの技術投稿には画像内にコードや図表が含まれるが、テキスト検索では拾えない。Vision解析で1画像あたり30〜40個の視覚タグを生成することで、画像コンテンツも意味検索の対象になる

## いつ使うのか

コードスクリーンショット・UIデモ・図解を含む投稿を多数ブックマークしており、画像の内容でも検索したいとき

### 具体的な適用場面

- 数百〜数千のTwitterブックマークが溜まり、後から目的の投稿が見つからなくなっている状況
- スクリーンショット付きの技術投稿をブックマークしているが、画像内のコードや図表が検索できない状況
- 技術情報・ツール情報をジャンル別に整理してマインドマップで全体把握したい場合

## やり方

1. Siftly パイプラインの Vision Analysis ステージはAI分析実行時に自動で走る（個別設定不要）
2. 各ブックマーク内の画像が設定済みのVision対応LLM API（Claude / GPT-4o等）に送られる
3. 返ってきた視覚タグ（30〜40個）がSQLiteに保存され、後続のSemantic Taggingステージの入力に合流する
4. 検索クエリを投げると画像内テキストに由来するタグもヒット対象になる

### 入力

- ブックマークに添付された画像・GIF・動画サムネイル
- Vision機能付きLLM API（Claude / GPT-4o等）

### 出力

- 画像1枚あたり30〜40個の視覚タグ
- 画像内テキスト・コンテキストが検索可能な状態

## 使うツール・ライブラリ

- LLM Vision API（Claude / GPT-4o）
- SQLite

## コード例

```
// READMEより
// Vision Analysis — reads text, objects, and context from every image/GIF/video thumbnail
// Output: 30–40 visual tags per image
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
