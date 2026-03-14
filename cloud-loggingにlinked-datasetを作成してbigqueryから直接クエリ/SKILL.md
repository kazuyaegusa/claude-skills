# Cloud LoggingにLinked Datasetを作成してBigQueryから直接クエリ

> Cloud LoggingのログバケットにLinked Datasetを作成し、BigQueryから直接SQL クエリでログを参照できる構成にする

- 出典: https://x.com/horie1024/status/2032315539008479554
- 投稿者: ホリエ
- カテゴリ: claude-code-workflow

## なぜ使うのか

Cloud LoggingとBigQueryのLinked Dataset機能を使うと、ログのエクスポートジョブ不要でBigQueryからCloud Loggingのデータをリアルタイムにクエリできる。パイプラインの複雑さを削減できる

## いつ使うのか

Cloud LoggingにOTelログを送信しており、BigQueryの既存分析基盤からそのログをSQLでクエリしたいとき

### 具体的な適用場面

- 数十〜数百名規模でClaude Code / AI開発ツールを展開しており、利用状況を組織として把握したい場合
- 個人ごとのAIツールコストを集計し、最適プラン（固定 vs 従量課金）の振り分けを自動化したい場合
- MDM（Intune等）を導入済みの企業がmacOS/Windowsの設定を一元管理している場合
- 既存のBigQuery/Cloud Logging分析基盤にAIツールの利用ログを統合したい場合

## やり方

1. Claude Code専用のCloud Loggingバケットを作成する（retention_days=3650等で保持期限を設定）
2. Log RouterでClaude Codeのログ（logName=".../claude-code-telemetry"）を専用バケットに流すSinkを作成する
3. Linked Datasetリソースを作成しCloud LoggingバケットとBigQueryを紐付ける
4. BigQueryからLinked Datasetを参照し、json_payloadに対してJSON_VALUE関数でフィールド抽出するVIEWを作成する

### 入力

- Cloud Loggingへのログ書き込み権限
- BigQueryのLinked Dataset作成権限
- TerraformまたはGCPコンソールのアクセス

### 出力

- BigQueryから`JSON_VALUE(json_payload, '$.cost_usd')`のようなクエリでClaude Codeログが参照可能な状態
- Cloud Logging保持期限を長期（例: 3650日）に設定した専用ログバケット

## 使うツール・ライブラリ

- Google Cloud Logging
- BigQuery
- Terraform
- google_logging_linked_dataset

## コード例

```
resource "google_logging_linked_dataset" "claude_code_logs" {
  bucket      = google_logging_project_bucket_config.claude_code_logs.id
  link_id     = "claude_code_logs_bq_link"
  description = "Linked dataset for querying Claude Code logs from BigQuery"
}
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
