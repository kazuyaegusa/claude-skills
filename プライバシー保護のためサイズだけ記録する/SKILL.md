# プライバシー保護のためサイズだけ記録する

> tool.input_size / tool.output_size は記録するが、中身（テキスト・ファイルパス・コマンド）は記録しない

- 出典: https://x.com/mk18/status/2035518245495804379
- 投稿者: mk18
- カテゴリ: claude-code-workflow

## なぜ使うのか

OTelトレースは社内共有されることが多く、会話内容・コードベース構造・API キーが漏れるリスクがある。サイズだけでもレイテンシやボトルネック分析には十分

## いつ使うのか

AIエージェントログをチーム内で共有する時、社内監査要件がある時

### 具体的な適用場面

- Claude Codeが遅い・何度もBashを叩いている原因を特定したい
- サブエージェントの並列実行やツール呼び出しパターンを分析したい
- AIエージェントのパフォーマンスを定量的にモニタリングしたい
- チーム内でAIエージェントの動作ログを安全に共有・レビューしたい

## やり方

1. tool.input_size: len(tool_input_text) を記録
2. tool.output_size: len(tool_output_text) を記録
3. tool.name / tool.category のみ記録（例: "Bash", "file_read"）
4. ❌ 記録しない: 会話テキスト、ファイルパス、コマンド内容、環境変数
5. Spanの attributes に `{"tool.input_size": 1234, "tool.output_size": 5678}` のみセット

### 入力

- ツール呼び出しの入力・出力テキスト

### 出力

- サイズ（文字数）のみを含むOTel attributes
- 機密情報を含まないトレース

## 使うツール・ライブラリ

- opentelemetry-api

## コード例

```
# ✅ 記録するもの
"tool.name"         # ツール名（Bash, Read, Write...）
"tool.category"     # カテゴリ（shell, file_read, web...）
"tool.input_size"   # 入力サイズ（文字数）
"tool.output_size"  # 出力サイズ（文字数）
"tool.error"        # エラーかどうか
"turn.input_tokens" # トークン使用量

# ❌ 意図的に記録しないもの
# - 会話テキスト（業務情報が含まれる）
# - ファイルパス（プロジェクト構造が漏れる）
# - コマンド内容（認証情報が含まれうる）
# - 環境変数
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
