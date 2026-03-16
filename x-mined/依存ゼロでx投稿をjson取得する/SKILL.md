# 依存ゼロでX投稿をJSON取得する

> 追加ライブラリなしで単一X投稿のテキスト・統計・メディア・引用ツイートをJSONで取得する

- 出典: https://x.com/liangwenhao3/status/2033170553469882799?s=20
- 投稿者: Noise
- カテゴリ: agent-orchestration

## なぜ使うのか

APIキー取得・ログインが不要なため、エージェントや自動化スクリプトにゼロ設定で組み込める

## いつ使うのか

AIエージェントやスクリプトにX投稿URLが渡され、内容をコンテキストとして取得したいとき。単一投稿のみ必要でCamofox不要の軽量環境

### 具体的な適用場面

- AIエージェントにX投稿URLを渡してコンテキストとして活用したいとき（現状は手動コピペ必須）
- 特定アカウントのタイムラインを定期監視してトレンド検知・日次レポート生成するCronジョブを組むとき
- X投稿のスレッド（返信ツリー）ごと取得して会話の文脈を丸ごと分析したいとき
- フォロワー増減・エンゲージメント拡散パターンをトラッキングしてバースト検知したいとき

## やり方

1. `git clone https://github.com/ythx-101/x-tweet-fetcher` でクローン
2. `cd x-tweet-fetcher`
3. `python x-tweet-fetcher.py --tweet https://x.com/user/status/123456` を実行
4. stdout にJSON出力される（text, stats, media, quotes フィールドを含む）
5. エージェントから呼ぶ場合: `subprocess.run(['python', 'x-tweet-fetcher.py', '--tweet', url], capture_output=True)` でJSONを受け取る

### 入力

- X投稿URL (https://x.com/user/status/数字形式)

### 出力

- JSON: text（本文）, stats（likes/RT/views）, media（画像URL）, quotes（引用元）

## 使うツール・ライブラリ

- x-tweet-fetcher (Python 3.7+, 標準ライブラリのみ)

## コード例

```
python x-tweet-fetcher.py --tweet https://x.com/user/status/123456
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
