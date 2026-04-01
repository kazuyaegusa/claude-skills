# ブックマークレットでX認証不要インポート

> ブラウザ拡張機能やOAuth認証なしに、ブックマークレット（またはコンソールスクリプト）でXのブックマークデータをJSON形式でエクスポートする。

- 出典: https://x.com/l_go_mrk/status/2037749522021892427
- 投稿者: AI駆動塾
- カテゴリ: data-processing

## なぜ使うのか

X APIはアクセス制限が厳しく、公式APIでブックマーク取得は有料プラン必須。ブラウザのDOMから直接データを取得するアプローチにより、API契約なしで自分のブックマークを取り出せる。

## いつ使うのか

X APIの有料プランなしにブックマークデータをローカルアプリに取り込みたいとき

### 具体的な適用場面

- Xのブックマークが数百件以上あり「あの投稿どこだっけ」が頻発している
- スクリーンショット付き投稿をブックマークしているがOCRなしで内容検索できずにいる
- API課金を避けながらClaude CLIサブスク認証でローカルAIアプリを動かしたい

## やり方

1. Xにログインしたブラウザでブックマークページ（x.com/i/bookmarks）を開く
2. SiftlyのUIからブックマークレットコードをコピー、またはGitHubのコンソールスクリプトを使用
3. ブラウザのコンソール（F12→Console）にスクリプトを貼り付けて実行
4. スクロールして全ブックマークを読み込んだ後、JSONファイルがダウンロードされる
5. SiftlyのImport画面からそのJSONをアップロード

### 入力

- Xログイン済みブラウザセッション
- SiftlyのブックマークレットコードまたはコンソールスクリプトURL

### 出力

- ブックマークデータのJSONファイル

## 使うツール・ライブラリ

- ブラウザコンソール（Chrome/Firefox）

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
