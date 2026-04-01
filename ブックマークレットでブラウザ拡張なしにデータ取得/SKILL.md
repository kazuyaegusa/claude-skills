# ブックマークレットでブラウザ拡張なしにデータ取得

> ブラウザ拡張機能をインストールせず、ブックマークレット（JavaScriptブックマーク）またはコンソールスクリプトを使ってTwitterブックマークをエクスポートする

- 出典: https://x.com/l_go_mrk/status/2037749522021892427
- 投稿者: AI駆動塾
- カテゴリ: data-processing

## なぜ使うのか

ブラウザ拡張はストア審査・権限要求・セキュリティリスクがある。ブックマークレットならインストール不要で即座に使え、ユーザーへの摩擦を最小化できる

## いつ使うのか

ブラウザ拡張機能をインストールしたくない場合、または会社のマシンで拡張が制限されている場合

### 具体的な適用場面

- 数百〜数千のTwitterブックマークが溜まり、後から目的の投稿が見つからなくなっている状況
- スクリーンショット付きの技術投稿をブックマークしているが、画像内のコードや図表が検索できない状況
- 技術情報・ツール情報をジャンル別に整理してマインドマップで全体把握したい場合

## やり方

1. Siftly（localhost:3000）の設定ページからブックマークレットのJavaScriptコードを取得する
2. ブラウザのブックマークバーに新規ブックマークを作成し、URLフィールドにそのコード（`javascript:...`）を貼り付ける
3. Twitter/Xの自分のブックマークページ（x.com/i/bookmarks）を開いた状態でそのブックマークレットをクリックする
4. スクリプトがページ上のブックマークデータを収集してSiftlyのローカルサーバーに送信する
（代替: ブラウザのDevToolsコンソールに直接スクリプトを貼り付けて実行）

### 入力

- Siftlyローカルサーバー（localhost:3000）が起動していること
- Twitter/Xにログインしてブックマークページを開いていること

### 出力

- ブックマークデータがSiftlyにインポートされた状態

## 使うツール・ライブラリ

- ブラウザのブックマークレット機能

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
