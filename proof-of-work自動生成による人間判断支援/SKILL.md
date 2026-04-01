# Proof of Work自動生成による人間判断支援

> エージェント完了時にCI結果、PRレビュー、複雑度分析、デモ動画を自動収集・提示し、人間が承認判断しやすくする

- 出典: https://x.com/gota_bara/status/2029298458855915897
- 投稿者: Gota@Data Analyst
- カテゴリ: agent-orchestration

## なぜ使うのか

人間がコード全体を読まずとも、客観的な証跡で品質を判断できるようにし、承認プロセスを高速化するため

## いつ使うのか

エージェント成果物の品質を人間が効率的にレビューしたい場合

### 具体的な適用場面

- 複数のタスクを並列実装したいが、各エージェントの進捗監視に時間を取られている
- Linear/GitHub Issuesに溜まったバックログを自動消化させたい
- CI失敗やPRレビュー指摘に対して自動で再試行・修正させたい
- チーム全体でエージェント活用を標準化し、人間は承認・レビューに集中したい

## やり方

1. Codex実行完了時にGitHub API経由でPRステータス、CI結果、レビューコメントを取得 2. コード複雑度分析ツール（radon, CodeClimate等）を実行結果に統合 3. デモ動画生成スクリプト（ffmpeg, puppeteer等）を実行し、GIF/MP4をPRコメントに添付 4. これらをLinearイシューにコメントバックまたはSlack通知で人間に提示

### 入力

- PR URL
- CIシステムAPI（GitHub Actions, CircleCI等）
- 複雑度分析設定、デモ生成スクリプト

### 出力

- CI結果サマリー
- PRレビュー指摘リスト
- 複雑度スコア
- デモ動画/GIF

## 使うツール・ライブラリ

- GitHub API
- radon/CodeClimate
- ffmpeg/puppeteer

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
