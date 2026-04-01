# X-Trackerでバースト拡散を検知する

> X-Tracker機能で投稿のフォロワー増減・エンゲージメント変化率を時系列追跡し、バースト（急拡散）を検知する

- 出典: https://x.com/liangwenhao3/status/2033170553469882799?s=20
- 投稿者: Noise
- カテゴリ: other

## なぜ使うのか

トレンド投稿やバズを即時検知してコンテンツ戦略に反映したい場合、手動確認では遅延が発生する。自動バースト検知により早期アクションが可能

## いつ使うのか

競合アカウントや注目インフルエンサーの急成長投稿を早期発見したいとき、または自分の投稿の拡散パターンを分析したいとき

### 具体的な適用場面

- AIエージェントにX投稿URLを渡してコンテキストとして活用したいとき（現状は手動コピペ必須）
- 特定アカウントのタイムラインを定期監視してトレンド検知・日次レポート生成するCronジョブを組むとき
- X投稿のスレッド（返信ツリー）ごと取得して会話の文脈を丸ごと分析したいとき
- フォロワー増減・エンゲージメント拡散パターンをトラッキングしてバースト検知したいとき

## やり方

1. `python x-tweet-fetcher.py --track @username --output track_data.json` で追跡開始
2. Cronで定期実行して時系列データを蓄積
3. 出力のburst_detectionフィールドを確認: `jq '.burst_detection' track_data.json`
4. propagation_analysisフィールドで拡散経路（RT連鎖）を分析

### 入力

- 追跡対象の@ユーザー名またはX投稿URL
- 定期実行環境（Cron推奨）

### 出力

- JSON: burst_detection（バースト有無・スコア）, propagation_analysis（拡散経路グラフ）

## 使うツール・ライブラリ

- x-tweet-fetcher (X-Tracker機能, 追加依存なし)

## コード例

```
python x-tweet-fetcher.py --track @username --output track_data.json
jq '.burst_detection' track_data.json
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
