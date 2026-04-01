# OTelのSpan階層を3層設計する

> session（root）→ turn → tool_call の3層でSpanを構造化する

- 出典: https://x.com/mk18/status/2035518245495804379
- 投稿者: mk18
- カテゴリ: claude-code-workflow

## なぜ使うのか

Webサービスの「リクエスト→ミドルウェア→API呼び出し」と同じ階層構造にすることで、既存のOTel可視化ツール（Jaeger/Grafana）がそのまま使える

## いつ使うのか

AIエージェントのログをOTelに変換する設計を行う時

### 具体的な適用場面

- Claude Codeが遅い・何度もBashを叩いている原因を特定したい
- サブエージェントの並列実行やツール呼び出しパターンを分析したい
- AIエージェントのパフォーマンスを定量的にモニタリングしたい
- チーム内でAIエージェントの動作ログを安全に共有・レビューしたい

## やり方

1. session span: セッション全体を1つのroot spanにする（trace ID固定）
2. turn span: ユーザー発言→AI応答の1往復を1 spanにする（parent: session）
3. tool_call span: Bash/Read/Write等の各ツール呼び出しを1 spanにする（parent: turn）
4. Pythonの opentelemetry-api で `tracer.start_as_current_span()` をネストして生成

### 入力

- セッションID、ターンID、ツール呼び出しID

### 出力

- 階層構造を持つOTel trace（Jaegerで親子関係が表示される）

## 使うツール・ライブラリ

- opentelemetry-api
- opentelemetry-sdk

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
