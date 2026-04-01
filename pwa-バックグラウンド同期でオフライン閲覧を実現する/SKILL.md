# PWA + バックグラウンド同期でオフライン閲覧を実現する

> Progressive Web App化し、Service WorkerでオフラインキャッシュとバックグラウンドでのRSSフィード同期を実装する

- 出典: https://x.com/ryuzee/status/2035210077725237424
- 投稿者: Ryutaro YOSHIBA
- カテゴリ: other

## なぜ使うのか

ネットワーク接続が不安定な環境でも記事を読み続けられるようにし、スマホアプリのような体験を提供するため

## いつ使うのか

モバイルデバイスでのオフライン閲覧や、ネットワークが不安定な環境での利用を想定する場合

### 具体的な適用場面

- SNSのフィルターバブルを避けて能動的に情報源を設計したい
- 複数ブログを統一UIで全文読みたいがCookieバナー・広告・ペイウォールを回避したい
- RSSフィードを提供していないサイトも自動購読したい
- 記事の翻訳・要約をRSSリーダー内で完結させたい
- 既読履歴・いいね・ブックマークを元にした記事スコアリングで情報優先度を管理したい

## やり方

1. manifest.jsonとService Workerを設定してPWA化 2. 記事本文・画像をService WorkerのCacheAPIでキャッシュ 3. Background Sync APIで定期的にRSSフィードを取得・更新 4. オフライン時はキャッシュから記事を表示、オンライン復帰時に未読記事を同期

### 入力

- キャッシュ対象の記事リスト
- RSSフィードURL

### 出力

- オフラインで閲覧可能な記事キャッシュ
- バックグラウンド同期された最新記事

## 使うツール・ライブラリ

- Service Worker
- Cache API
- Background Sync API

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
