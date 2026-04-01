# 3段階フォールバックでRSSのないサイトをフィード化する

> RSS Auto-discovery → RSS Bridge → LLMセレクタ推論の3段階でフィードを自動生成する

- 出典: https://x.com/ryuzee/status/2035210077725237424
- 投稿者: Ryutaro YOSHIBA
- カテゴリ: other

## なぜ使うのか

RSSフィードを提供していないサイトも購読可能にし、手動でのスクレイピング設定を不要にするため

## いつ使うのか

購読したいサイトがRSSフィードを提供していない場合

### 具体的な適用場面

- SNSのフィルターバブルを避けて能動的に情報源を設計したい
- 複数ブログを統一UIで全文読みたいがCookieバナー・広告・ペイウォールを回避したい
- RSSフィードを提供していないサイトも自動購読したい
- 記事の翻訳・要約をRSSリーダー内で完結させたい
- 既読履歴・いいね・ブックマークを元にした記事スコアリングで情報優先度を管理したい

## やり方

1. RSS Auto-discoveryでlink[type="application/rss+xml"]を探す 2. 見つからなければRSS Bridgeに問い合わせ 3. それでも失敗したらLLMにページのaタグ構造（5階層分の祖先、class、href、テキスト）を渡し、1行のJSONでCSSセレクタを返させる 4. 取得したセレクタで記事リストを抽出してフィード化

### 入力

- 購読したいサイトのURL
- ページのaタグDOMツリー（祖先5階層分のclass、href、テキスト）

### 出力

- CSSセレクタを含む1行JSON
- 生成されたRSSフィード

## 使うツール・ライブラリ

- RSS Bridge
- Anthropic/Gemini/OpenAI API
- DOM parser

## 前提知識

- TypeScriptでのバックエンド・フロントエンド開発経験
- Readability.jsやDOM操作の基礎知識
- Meilisearch等の全文検索エンジンの基本的な使い方
- Anthropic/Gemini/OpenAI APIの基本的な呼び出し方
- MCPプロトコルの概要理解
- PWA・Service Worker・Cache APIの基礎知識

## 根拠

> 全記事の自動フルテキスト取得 - Readability.js と 独自に入れた600パターンのノイズ除去

> RSSのないサイトのフィード自動生成（LLMによるCSSセレクタ推論） - RSS Auto-discovery → RSS Bridge → LLMセレクタ推論の3段階フォールバック

> LLMにはページのaタグ構造（5階層分の祖先、class、href、テキスト）を渡し、1行のJSONでCSSセレクタを返させる

> いいねやブックマークは記事のengagement scoreに反映される（いいね +10、ブックマーク +5、翻訳済み +3、既読 +2） スコアは時間減衰と掛け合わせて算出

> MCPサーバ内蔵
