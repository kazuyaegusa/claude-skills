# JavaScript動的レンダリング対応でSPA爬取

> React/Vueなどクライアントサイドレンダリングされるサイトでも、DOM構築後のHTMLを取得

- 出典: https://x.com/xiaohu/status/2031921663751946646
- 投稿者: 小互
- カテゴリ: ui-ux

## なぜ使うのか

従来の爬虫はHTMLソースのみ取得。SPAではJavaScript実行前の空HTMLしか得られない。このAPIはJS実行後のDOMを返すため、動的コンテンツも取得可能

## いつ使うのか

爬取対象がReact/Vue/Angular等のSPAで、通常のHTTP GETでは中身が取れない時

### 具体的な適用場面

- 競合サイトの価格・在庫情報を定期的に収集したい時
- ニュースサイト・ブログ全体をアーカイブしたい時
- React/Vue等のSPAサイトから構造化データを抽出したい時
- 変更検知機能を実装したいが、毎回全ページ爬取するとコストが高い時
- HTML解析を避け、直接JSON形式でデータ取得したい時

## やり方

1. Cloudflare Scraping API呼び出し時、オプションでJS実行を有効化
2. APIはヘッドレスブラウザ相当の環境でページを読み込み、JS実行完了後のHTMLを返す
3. 取得したHTMLから必要データを抽出、またはJSON出力を指定

### 入力

- SPAサイトのURL
- JS実行有効化オプション

### 出力

- JavaScript実行後の完全なHTML/JSON

## 使うツール・ライブラリ

- Cloudflare Scraping API（JS rendering機能）

## 前提知識

- Cloudflareアカウントとアクティブなサブスクリプション（Scraping API利用可能プラン）
- HTTP APIの基本的な使い方（POST/GET、認証ヘッダー設定）
- JSONスキーマの基本理解（構造化データ抽出時）
- 対象サイトの利用規約確認（爬取が許可されているか）

## 根拠

> 给一个网址，自动爬完整站，返回HTML/Markdown/JSON

> 支持 JS 渲染（React/Vue 动态站也能爬）

> 增量爬取：只爬更新过的页面，省时省钱

> 要什么数据，直接返回结构化 JSON
