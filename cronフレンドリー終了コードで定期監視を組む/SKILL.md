# Cronフレンドリー終了コードで定期監視を組む

> x-tweet-fetcherの終了コードを使ってCronジョブで「新着あり/なし」を判定し、新着時のみ後続処理を走らせる

- 出典: https://x.com/liangwenhao3/status/2033170553469882799?s=20
- 投稿者: Noise
- カテゴリ: automation-pipeline

## なぜ使うのか

毎回全件処理せず差分のみ処理することで、@mentions監視・タイムライン監視を効率化できる。標準的なUnix終了コード規約に従うためシェルスクリプトと直接統合できる

## いつ使うのか

特定アカウントへの@mentionsや特定キーワード投稿を定期監視して、新着があったときだけDiscord通知・DB保存・LLM分析をトリガーしたいとき

### 具体的な適用場面

- AIエージェントにX投稿URLを渡してコンテキストとして活用したいとき（現状は手動コピペ必須）
- 特定アカウントのタイムラインを定期監視してトレンド検知・日次レポート生成するCronジョブを組むとき
- X投稿のスレッド（返信ツリー）ごと取得して会話の文脈を丸ごと分析したいとき
- フォロワー増減・エンゲージメント拡散パターンをトラッキングしてバースト検知したいとき

## やり方

1. `python x-tweet-fetcher.py --mentions @username` を実行
2. 終了コード0 = 新着あり（JSONをstdoutに出力）、終了コード1 = 新着なし
3. cronに登録: `*/10 * * * * python /path/to/x-tweet-fetcher.py --mentions @username >> /tmp/mentions.json && process_mentions.sh`
4. `&&` で新着ありの場合のみ後続スクリプトを実行する

### 入力

- 監視対象の@ユーザー名またはキーワード
- 前回取得時刻（内部でインクリメンタル管理）

### 出力

- 新着あり: 終了コード0 + JSON to stdout
- 新着なし: 終了コード1 + 空出力

## 使うツール・ライブラリ

- x-tweet-fetcher
- cron (launchd or systemd)

## コード例

```
# crontab例: 10分ごとにmentions監視
*/10 * * * * python /path/to/x-tweet-fetcher.py --mentions @username && python process_mentions.py
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
