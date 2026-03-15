# /loopで定期監視タスクをスケジュールする

> Claude Codeの `/loop` コマンドで最大3日間、定期的なプロンプト実行をスケジュールし、デプロイ監視・PR確認・ビルドチェックを自動化する

- 出典: https://x.com/labelmake/status/2032652943250338098
- 投稿者: Kyohei - OSS, 外資IT
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動でのポーリングが不要になり、Claude自身が変化を検知して対応できる。CronタスクをLLM理解で実行できる

## いつ使うのか

CI/CDの完了待ち、PRのレビュー待ち、デプロイ後の動作確認など、繰り返しチェックが必要な場合

## やり方

1. `/loop 5m /check-deployment` のようにインターバルとコマンドを指定
2. または自然言語で「30分ごとにPRのCIステータスを確認して失敗したら教えて」と伝える
3. 最大3日間実行可能
4. バックグラウンドで実行され、条件を満たしたら通知

### 入力

- 監視対象の条件
- チェック間隔（例: 5m, 1h）

### 出力

- 定期実行レポート
- 条件達成時の通知

## 使うツール・ライブラリ

- /loop
- Scheduled Tasks機能

## コード例

```
/loop 10m /btw はCIが通ったか確認して
```

## 前提知識

- Claude Code CLIの基本操作（起動、プロンプト入力、コマンド実行）
- GitおよびGitHubの基本知識
- CLAUDE.md、.claude/ディレクトリ構造の理解
- Claude CodeのPlan Mode、Command、Agent、Skillの概念的な区別

## 根拠

> 「公式・コミュニティのClaude Codeベストプラクティスを1箇所にまとめたリポジトリがGitHub月間トレンド入り」

> "CLAUDE.md should target under 200 lines per file"

> "use Esc Esc or /rewind to undo when Claude goes off-track instead of trying to fix it in the same context"
