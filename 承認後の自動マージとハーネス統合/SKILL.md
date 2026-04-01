# 承認後の自動マージとハーネス統合

> 人間が承認したPRをSymphonyが自動でマージし、Harness Engineering環境（テスト、デプロイ自動化）に統合する

- 出典: https://x.com/gota_bara/status/2029298458855915897
- 投稿者: Gota@Data Analyst
- カテゴリ: agent-orchestration

## なぜ使うのか

承認後の手動マージ作業をなくし、エンドツーエンドで「イシュー登録→実装→承認→本番反映」を自動化するため

## いつ使うのか

承認フローが確立しており、人間判断後の作業を完全自動化したい場合

### 具体的な適用場面

- 複数のタスクを並列実装したいが、各エージェントの進捗監視に時間を取られている
- Linear/GitHub Issuesに溜まったバックログを自動消化させたい
- CI失敗やPRレビュー指摘に対して自動で再試行・修正させたい
- チーム全体でエージェント活用を標準化し、人間は承認・レビューに集中したい

## やり方

1. Linear/GitHub Webhook等で承認イベントを検知（ラベル追加、コメント「LGTM」等） 2. Symphony内でPR承認状態を確認、GitHub API経由で auto-merge または merge PR 実行 3. マージ後、Harness設定に従いCI/CDパイプラインを自動トリガー（GitHub Actions, ArgoCD等） 4. デプロイ完了をLinearに通知、イシューをクローズ

### 入力

- 承認トリガー（ラベル、コメント）
- GitHub merge設定（squash, rebase等）
- Harness CI/CD設定

### 出力

- マージ完了したPR
- デプロイ済み本番環境
- クローズされたLinearイシュー

## 使うツール・ライブラリ

- GitHub API
- Linear Webhook
- GitHub Actions/ArgoCD

## 前提知識

- Harness Engineering（エージェント実行環境の整備）を理解している
- Linear/GitHub等のイシュー管理ツールを使っている
- Codex app-serverまたは同等のコーディングエージェントAPIにアクセスできる
- Elixir/OTPの基本（Supervisor, GenServer）を知っている、または学ぶ意欲がある

## 根拠

> 「Symphony turns project work into isolated, autonomous implementation runs, allowing teams to manage work instead of supervising coding agents.」（GitHub README冒頭）

> 「In this demo video, Symphony monitors a Linear board for work and spawns agents to handle the tasks.」（README動画説明）

> 「The agents complete the tasks and provide proof of work: CI status, PR review feedback, complexity analysis, and walkthrough videos.」（README動画説明）

> 「Symphony works best in codebases that have adopted harness engineering.」（README Requirements）

> 「Elixir-based Symphony implementation」（README Option 2）
