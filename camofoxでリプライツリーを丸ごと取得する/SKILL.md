# Camofoxでリプライツリーを丸ごと取得する

> CamofoxブラウザをバックエンドとしてX投稿へのコメント（スレッド形式）・ユーザータイムライン・Xアーティクルの全文を取得する

- 出典: https://x.com/liangwenhao3/status/2033170553469882799?s=20
- 投稿者: Noise
- カテゴリ: other

## なぜ使うのか

X公式APIではリプライ取得は高額プランのみ。Camofoxはブラウザ偽装でブロックを回避しつつ階層化されたコメントツリーを返す

## いつ使うのか

投稿への反応（賛否・補足情報）や特定アカウントの発言履歴をまとめて分析したいとき。単一投稿だけでなく文脈が必要な場合

### 具体的な適用場面

- AIエージェントにX投稿URLを渡してコンテキストとして活用したいとき（現状は手動コピペ必須）
- 特定アカウントのタイムラインを定期監視してトレンド検知・日次レポート生成するCronジョブを組むとき
- X投稿のスレッド（返信ツリー）ごと取得して会話の文脈を丸ごと分析したいとき
- フォロワー増減・エンゲージメント拡散パターンをトラッキングしてバースト検知したいとき

## やり方

1. Camofoxをインストール（READMEのCamofox setupセクション参照）
2. `python x-tweet-fetcher.py --comments https://x.com/user/status/123456` でコメント取得
3. `python x-tweet-fetcher.py --timeline @username --limit 200` でタイムライン取得（最大200件）
4. `python x-tweet-fetcher.py --article https://x.com/i/articles/xxx` でXアーティクル全文取得
5. 出力はすべてJSON（threaded comment tree形式）

### 入力

- X投稿URL または @ユーザー名
- Camofoxのインストール済み環境

### 出力

- JSON: threaded comment tree（コメント）, paginated tweet list（タイムライン200件まで）, full article text（アーティクル）

## 使うツール・ライブラリ

- x-tweet-fetcher
- Camofox（ブラウザバックエンド）

## コード例

```
python x-tweet-fetcher.py --comments https://x.com/user/status/123456
python x-tweet-fetcher.py --timeline @username --limit 200
```

## 前提知識

- Python 3.7以上
- 高度な機能（コメント取得・タイムライン・アーティクル）にはCamofoxのセットアップが必要
- 基本的なJSON処理知識（jq または Python json モジュール）

## 根拠

> 「Fetch tweets, comments, timelines, and articles from X/Twitter — without login or API keys.」

> 「Zero config · Agent-first JSON output · Cron-friendly exit codes」

> 機能表: Single tweet（Zero Deps✅）, Reply comments（Camofox✅）, User timeline up to 200件（Camofox✅）

> 「X-Tracker (growth): burst detection, propagation analysis（Zero Deps✅）」

> 「X has no free API. Scraping gets you blocked. Browser automation is fragile.」
