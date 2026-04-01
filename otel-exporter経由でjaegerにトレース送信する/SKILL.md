# OTel Exporter経由でJaegerにトレース送信する

> opentelemetry-exporter-otlp-proto-grpc を使ってPythonからJaegerにSpanを送る

- 出典: https://x.com/mk18/status/2035518245495804379
- 投稿者: mk18
- カテゴリ: claude-code-workflow

## なぜ使うのか

OTLP（OpenTelemetry Protocol）はベンダー中立な標準プロトコルで、Jaeger・Grafana Tempo・Honeycombなど多様なバックエンドに送信できる

## いつ使うのか

Python製のアプリケーション・スクリプトからOTelトレースを送りたい時

### 具体的な適用場面

- Claude Codeが遅い・何度もBashを叩いている原因を特定したい
- サブエージェントの並列実行やツール呼び出しパターンを分析したい
- AIエージェントのパフォーマンスを定量的にモニタリングしたい
- チーム内でAIエージェントの動作ログを安全に共有・レビューしたい

## やり方

1. `pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp-proto-grpc`
2. Pythonコードで OTLPSpanExporter を初期化（endpoint="localhost:4317"）
3. TracerProvider に BatchSpanProcessor(exporter) を追加
4. tracer.start_as_current_span() でSpanを生成・送信

### 入力

- Jaegerのendpoint (localhost:4317)
- Span階層設計

### 出力

- Jaeger UIに表示されるトレース

## 使うツール・ライブラリ

- opentelemetry-api
- opentelemetry-sdk
- opentelemetry-exporter-otlp-proto-grpc

## コード例

```
pip install opentelemetry-api opentelemetry-sdk \
  opentelemetry-exporter-otlp-proto-grpc
```

## 前提知識

- OpenTelemetryの基本概念（Trace, Span, Exporter）
- Dockerの基本操作
- Pythonの基本文法（JSONパース、ファイルI/O）
- Claude Codeのセッションログがどこに保存されているか

## 根拠

> Claude Code は ~/.claude/projects/ 以下にセッションごとの JSONL ログを自動保存している

> 今回使うのは 1 日分（約 24 時間）のセッション。148 ターン、130 回のツール呼び出し

> session = リクエスト全体 / turn = ミドルウェア層 / tool_call = 外部 API 呼び出し

> サイズだけ記録して中身は捨てる のが正解だ

> docker compose up -d # → http://localhost:16686 で Jaeger UI が開く
