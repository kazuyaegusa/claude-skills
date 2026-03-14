# OTel CollectorでResource AttributeをLog Attributeにコピー

> OTel CollectorのTransform Processorを使い、Resource Attributeの情報をLog Attributeにコピーした上でCloud Loggingに送信する

- 出典: https://x.com/horie1024/status/2032315539008479554
- 投稿者: ホリエ
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude CodeがResource AttributeとしてOTelに送信したメタデータ（user.email等）がCloud Loggingにそのままでは保存されないため、Log Attribute側にコピーしてログ本体と一緒に保存する必要がある

## いつ使うのか

OTelのResource Attributeに含まれる情報（user.email、サービスメタデータ等）がCloud Loggingに保存されないことに気づいたとき

### 具体的な適用場面

- 数十〜数百名規模でClaude Code / AI開発ツールを展開しており、利用状況を組織として把握したい場合
- 個人ごとのAIツールコストを集計し、最適プラン（固定 vs 従量課金）の振り分けを自動化したい場合
- MDM（Intune等）を導入済みの企業がmacOS/Windowsの設定を一元管理している場合
- 既存のBigQuery/Cloud Logging分析基盤にAIツールの利用ログを統合したい場合

## やり方

1. OTel CollectorのYAML設定のprocessorsセクションにtransformプロセッサーを追加する
2. log_statementsに以下の変換ルールを記述する
   - set(body, {"message": body}) where IsString(body)  # bodyを構造化
   - merge_maps(attributes, resource.attributes, "upsert")  # Resource→Attributeにコピー
   - merge_maps(body, attributes, "upsert")  # Attributeをbodyにもマージ
3. pipelinesのlogsにtransformプロセッサーを追加する

### 入力

- OTel Collector設定YAML
- Cloud Loggingエクスポーター設定

### 出力

- Resource Attributeの情報がCloud Loggingのjson_payloadフィールドに含まれたログ
- BigQueryからuser.emailなどのメタデータをJSONクエリで取得可能な状態

## 使うツール・ライブラリ

- OpenTelemetry Collector
- otelcol-contrib
- googlecloudexporter

## コード例

```
processors:
  transform:
    error_mode: ignore
    log_statements:
      - context: log
        statements:
          - 'set(body, {"message": body}) where IsString(body)'
          - 'merge_maps(attributes, resource.attributes, "upsert")'
          - 'merge_maps(body, attributes, "upsert")'
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
