# api_requestイベントのcost_usdを集計して最適プランを自動判定

> OTelで収集したapi_requestイベントのcost_usdフィールドをユーザー別・日別に集計し、固定料金プランと従量課金プランのどちらが最適かを判断する

- 出典: https://x.com/horie1024/status/2032315539008479554
- 投稿者: ホリエ
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeの利用量が少ないユーザーにProプランを適用するとコストパフォーマンスが悪い。実使用コストを定量化することで、プランの最適化を自動的・継続的に行える

## いつ使うのか

Claude Codeを複数の課金プラン（固定/従量課金）で運用しており、コスト最適化のためにプラン振り分けを定期的に行いたいとき

### 具体的な適用場面

- 数十〜数百名規模でClaude Code / AI開発ツールを展開しており、利用状況を組織として把握したい場合
- 個人ごとのAIツールコストを集計し、最適プラン（固定 vs 従量課金）の振り分けを自動化したい場合
- MDM（Intune等）を導入済みの企業がmacOS/Windowsの設定を一元管理している場合
- 既存のBigQuery/Cloud Logging分析基盤にAIツールの利用ログを統合したい場合

## やり方

1. BigQueryのLinked DatasetからClaude Codeログを参照するVIEWを作成する
2. WHERE条件でevent.name='api_request'のみ抽出する
3. user_email・日付でGROUP BYし、SUM(cost_usd)とCOUNT(*)を集計する
4. 月次コストの閾値（例: 固定プランの月額）と実コストを比較し、超過ユーザーにはProプラン、以下ユーザーには従量課金プランへの移行を通知する

### 入力

- BigQueryに蓄積されたapi_requestイベントログ（cost_usdフィールド含む）
- 各課金プランの月額固定費

### 出力

- ユーザー別月次コスト集計テーブル
- 最適プラン移行の通知リスト

## 使うツール・ライブラリ

- BigQuery
- Claude Code OTel（api_requestイベント）

## コード例

```
SELECT
  DATE(event_timestamp, "Asia/Tokyo") AS date,
  user_email,
  SUM(cost_usd) AS cost_usd,
  COUNT(*) AS api_call_count
FROM <linked_dataset_view>
WHERE event_name = 'api_request'
GROUP BY ALL
```

## 前提知識

- Claude CodeのOpenTelemetry機能の基本概念（OTEL_EXPORTER系環境変数）
- MDMツール（Intuneまたは同等）の管理者権限と設定配布の操作方法
- OpenTelemetry Collectorの設定YAML（receivers/processors/exporters/pipelines）の基本構造
- Google Cloud（Cloud Run、Cloud Logging、BigQuery、Cloud Load Balancing）の基本操作
- Terraformの基本的な記述・適用方法

## 根拠

> 「全社員に対して設定を入れるように依頼をしたとしても、どうしても漏れが生じてしまうため、そのような依頼ベースの手法に頼らず、ファイルを配布することを考えます」

> 「この場所に配置したJSON設定ファイルはManaged settingsと呼ばれ、優先順位が最も高い設定ファイルとして認識されます」

> 「Resource Attributeの情報を全て抜き出してLog Attributeにコピーしています」

> 「Cloud LoggingとBigQueryはかなり高度に統合されています。Cloud Loggingに保存されたデータに対して直接BigQueryからクエリを実行できます」

> 「api_requestイベントのcost_usdフィールドを集計して、各自に最も適したプランをアナウンスしています」
