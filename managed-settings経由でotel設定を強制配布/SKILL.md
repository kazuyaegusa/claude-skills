# Managed Settings経由でOTel設定を強制配布

> Claude CodeのManaged Settings JSONファイルをMDMツール（Intune等）で全社員の端末に配置し、OTel設定を強制的に有効化する

- 出典: https://x.com/horie1024/status/2032315539008479554
- 投稿者: ホリエ
- カテゴリ: claude-code-workflow

## なぜ使うのか

依頼ベースの設定では漏れが発生し継続的モニタリングが不可能。Managed Settingsはユーザー設定より優先順位が高く、上書き不可のため確実に全員に適用できる

## いつ使うのか

MDMを導入済みの組織でClaude Codeを複数名に展開しており、全員のログを漏れなく収集したいとき

### 具体的な適用場面

- 数十〜数百名規模でClaude Code / AI開発ツールを展開しており、利用状況を組織として把握したい場合
- 個人ごとのAIツールコストを集計し、最適プラン（固定 vs 従量課金）の振り分けを自動化したい場合
- MDM（Intune等）を導入済みの企業がmacOS/Windowsの設定を一元管理している場合
- 既存のBigQuery/Cloud Logging分析基盤にAIツールの利用ログを統合したい場合

## やり方

1. MDMツール（Intune等）のスクリプト/プロファイル配布機能を使い以下パスにJSONを配置する
   - macOS: /Library/Application Support/ClaudeCode/managed-settings.json
   - Windows: C:\Program Files\ClaudeCode\managed-settings.json
2. JSONの内容にenvブロックとして以下を記述する
   - CLAUDE_CODE_ENABLE_TELEMETRY=1
   - OTEL_METRICS_EXPORTER=otlp
   - OTEL_LOGS_EXPORTER=otlp
   - OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
   - OTEL_EXPORTER_OTLP_ENDPOINT=<収集サーバーのURL>
   - OTEL_EXPORTER_OTLP_HEADERS=Authorization=Bearer <トークン>
   - OTEL_RESOURCE_ATTRIBUTES=user.email=<ユーザーのメールアドレス>
3. MDMで配布後、Claude Code起動時に自動的にOTelが有効化されることを確認する

### 入力

- MDMツール（Intune等）の管理者権限
- OTelコレクターのエンドポイントURL
- Bearer認証トークン
- ユーザーのメールアドレス（OTEL_RESOURCE_ATTRIBUTESに設定）

### 出力

- 全社員のClaude CodeからOTelエンドポイントへ自動的にログが送信される状態
- managed-settings.jsonが各端末の指定パスに配置された状態

## 使うツール・ライブラリ

- Microsoft Intune（または他のMDMツール）
- Claude Code Managed Settings機能

## コード例

```
{
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp",
    "OTEL_LOGS_EXPORTER": "otlp",
    "OTEL_EXPORTER_OTLP_PROTOCOL": "http/protobuf",
    "OTEL_EXPORTER_OTLP_ENDPOINT": "https://<your-collector-endpoint>",
    "OTEL_EXPORTER_OTLP_HEADERS": "Authorization=Bearer <token>",
    "OTEL_RESOURCE_ATTRIBUTES": "user.email=<user@example.com>",
    "OTEL_METRICS_INCLUDE_VERSION": "true"
  }
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
