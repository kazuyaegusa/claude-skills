# DockerでJaegerを5分で起動する

> docker-compose.yml 1ファイルでJaeger all-in-oneを立ち上げ、OTLP受信可能にする

- 出典: https://x.com/mk18/status/2035518245495804379
- 投稿者: mk18
- カテゴリ: claude-code-workflow

## なぜ使うのか

Jaegerのall-in-oneイメージはコレクター・UI・ストレージが全て入っており、開発環境ですぐ使える

## いつ使うのか

ローカルでOTelトレースを可視化したい時、開発環境にトレース基盤が欲しい時

### 具体的な適用場面

- Claude Codeが遅い・何度もBashを叩いている原因を特定したい
- サブエージェントの並列実行やツール呼び出しパターンを分析したい
- AIエージェントのパフォーマンスを定量的にモニタリングしたい
- チーム内でAIエージェントの動作ログを安全に共有・レビューしたい

## やり方

1. docker-compose.yml を以下の内容で作成:
   services:
     jaeger:
       image: jaegertracing/all-in-one:latest
       ports:
         - "16686:16686"  # Jaeger UI
         - "4317:4317"    # OTLP gRPC
         - "4318:4318"    # OTLP HTTP
       environment:
         COLLECTOR_OTLP_ENABLED: "true"
2. `docker compose up -d` で起動
3. ブラウザで http://localhost:16686 を開くとJaeger UIが表示される

### 入力

- Docker/Docker Compose実行環境

### 出力

- Jaeger UI (http://localhost:16686)
- OTLP gRPC endpoint (localhost:4317)
- OTLP HTTP endpoint (localhost:4318)

## 使うツール・ライブラリ

- Docker
- jaegertracing/all-in-one:latest

## コード例

```
# docker-compose.yml
services:
  jaeger:
    image: jaegertracing/all-in-one:latest
    ports:
      - "16686:16686"  # Jaeger UI
      - "4317:4317"    # OTLP gRPC
      - "4318:4318"    # OTLP HTTP
    environment:
      COLLECTOR_OTLP_ENABLED: "true"

# 起動
docker compose up -d
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
