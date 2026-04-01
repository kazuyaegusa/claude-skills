# Claude Codeでクラウドベース定期タスクを設定する

> Claude Codeに対象リポジトリ、スケジュール、実行プロンプトを設定して、クラウドインフラ上で定期実行させる

- 出典: https://x.com/noahzweben/status/2035122989533163971
- 投稿者: Noah Zweben
- カテゴリ: claude-code-workflow

## なぜ使うのか

ローカルマシンを常時起動する必要がなくなり、安定した定期実行環境を確保できる

## いつ使うのか

定期的なコードチェック、レポート生成、自動メンテナンスなど、時間ベースで繰り返し実行したいタスクがある場合

### 具体的な適用場面

- 毎日決まった時刻にリポジトリの状態をチェックして問題を検出したい
- 週次でコードベースの分析レポートを自動生成したい
- 複数リポジトリに対して定期的なメンテナンスタスクを実行したい
- ローカルマシンを常時起動できない環境でAIエージェントを定期実行したい

## やり方

1. Claude Codeで対象リポジトリ（単数または複数）を指定 2. cronライクなスケジュール形式で実行頻度を設定 3. 実行させたいタスク内容をプロンプトとして記述 4. クラウドインフラが指定スケジュールで自動実行

### 入力

- 対象リポジトリのパスまたはURL
- 実行スケジュール（cron形式など）
- 実行させたいタスクを記述したプロンプト

### 出力

- スケジュール通りに実行されるクラウドベースのタスク
- 実行結果の通知またはログ

## 使うツール・ライブラリ

- Claude Code

## 前提知識

- Claude Codeの基本的な使い方
- 対象リポジトリへのアクセス権限
- 定期実行させたいタスクの明確な定義

## 根拠

> You can now schedule recurring cloud-based tasks on Claude Code.

> Set a repo (or repos), a schedule, and a prompt.

> Claude runs it via cloud infra on your schedule, so you don't need to keep Claude Code running on your local machine.
