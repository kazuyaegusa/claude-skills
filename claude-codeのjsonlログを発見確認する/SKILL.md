# Claude CodeのJSONLログを発見・確認する

> ~/.claude/projects/ 以下に自動保存されているセッションログ（JSONL形式）を特定する

- 出典: https://x.com/mk18/status/2035518245495804379
- 投稿者: mk18
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeは全セッションをJSONL形式で自動保存しており、これが計装対象のデータソースになる

## いつ使うのか

Claude Codeの実行履歴を解析したい時、どのセッションが長かったか確認したい時

### 具体的な適用場面

- Claude Codeが遅い・何度もBashを叩いている原因を特定したい
- サブエージェントの並列実行やツール呼び出しパターンを分析したい
- AIエージェントのパフォーマンスを定量的にモニタリングしたい
- チーム内でAIエージェントの動作ログを安全に共有・レビューしたい

## やり方

1. ターミナルで `ls -lhS ~/.claude/projects/-home-{ユーザー名}-*/*.jsonl | head -5` を実行
2. サイズの大きい順にファイルが表示される
3. 対象ファイルを `cat` や `jq` で内容確認
4. 各行が1イベント（ターン開始、ツール呼び出し、応答等）のJSON

### 入力

- ~/.claude/projects/ 以下のディレクトリ構造

### 出力

- セッションごとのJSONLファイルパス
- ファイルサイズ（ツール呼び出し量の目安）

## 使うツール・ライブラリ

- ls
- jq

## コード例

```
ls -lhS ~/.claude/projects/-home-yuto-*/*.jsonl | head -5
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
