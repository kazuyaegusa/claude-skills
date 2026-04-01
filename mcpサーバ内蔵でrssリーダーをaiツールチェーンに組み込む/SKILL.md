# MCPサーバ内蔵でRSSリーダーをAIツールチェーンに組み込む

> RSSリーダー自体にModel Context Protocol (MCP)サーバを内蔵し、AIエージェントから記事検索・要約・翻訳を呼び出せるようにする

- 出典: https://x.com/ryuzee/status/2035210077725237424
- 投稿者: Ryutaro YOSHIBA
- カテゴリ: agent-orchestration

## なぜ使うのか

AIエージェントが記事データベースに直接アクセスできるようにし、ワークフロー自動化やチャットボット統合を可能にするため

## いつ使うのか

RSSリーダーの記事データをAIエージェントのワークフローに統合したい場合

### 具体的な適用場面

- SNSのフィルターバブルを避けて能動的に情報源を設計したい
- 複数ブログを統一UIで全文読みたいがCookieバナー・広告・ペイウォールを回避したい
- RSSフィードを提供していないサイトも自動購読したい
- 記事の翻訳・要約をRSSリーダー内で完結させたい
- 既読履歴・いいね・ブックマークを元にした記事スコアリングで情報優先度を管理したい

## やり方

1. RSSリーダーのバックエンドにMCPサーバを実装 2. 記事検索、要約、翻訳、ブックマーク追加等のエンドポイントをMCPツールとして公開 3. AIエージェント（Claude Code等）からMCPクライアントで接続 4. AIが「最近のAI関連記事を要約して」等のリクエストを受けたらMCP経由でRSSリーダーのDBを検索・要約して返す

### 入力

- MCPクライアントからのリクエスト（検索クエリ、記事ID等）

### 出力

- 検索結果、要約テキスト、翻訳テキスト等のJSON

## 使うツール・ライブラリ

- Model Context Protocol (MCP)
- Anthropic/Gemini/OpenAI API

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
