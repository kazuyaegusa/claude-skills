# JSONLログをパースしてSpanに変換する

> Claude CodeのJSONLログを1行ずつ読み、イベント種別に応じてsession/turn/tool_call Spanを生成する

- 出典: https://x.com/mk18/status/2035518245495804379
- 投稿者: mk18
- カテゴリ: claude-code-workflow

## なぜ使うのか

JSONL形式のログはイベントストリームであり、時系列順に処理することで親子関係を持つSpan階層を構築できる

## いつ使うのか

構造化ログ（JSONL）からOTelトレースを生成したい時

### 具体的な適用場面

- Claude Codeが遅い・何度もBashを叩いている原因を特定したい
- サブエージェントの並列実行やツール呼び出しパターンを分析したい
- AIエージェントのパフォーマンスを定量的にモニタリングしたい
- チーム内でAIエージェントの動作ログを安全に共有・レビューしたい

## やり方

1. JSONLファイルを1行ずつ読み、`json.loads()` でパース
2. イベント種別（session開始、turn開始、tool呼び出し、応答等）を判定
3. session開始時: root Spanを作成
4. turn開始時: session Spanの子として turn Spanを作成
5. tool呼び出し時: turn Spanの子として tool_call Spanを作成
6. 各Spanにtimestamp・duration・attributesをセット
7. BatchSpanProcessor経由でJaegerに送信

### 入力

- Claude CodeのJSONLログファイル

### 出力

- 階層構造を持つOTel trace（session → turn → tool_call）

## 使うツール・ライブラリ

- Python json module
- opentelemetry-api

## コード例

```
def build_turns(events: list[dict]):
    # JSONLイベントをパースしてturn/tool_call Spanに変換
    # （記事には核心部分のみ抜粋とあるため、詳細は元記事参照）
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
