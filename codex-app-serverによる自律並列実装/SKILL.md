# Codex app-serverによる自律並列実装

> 取得したタスクをCodex app-serverに渡し、独立したエージェント実行として並列起動・完了まで自律実行させる

- 出典: https://x.com/gota_bara/status/2029298458855915897
- 投稿者: Gota@Data Analyst
- カテゴリ: agent-orchestration

## なぜ使うのか

人間が各エージェントの進捗を個別に監視するコストを排除し、複数タスクを同時並行で処理してスループットを上げるため

## いつ使うのか

複数タスクを同時進行させたい、かつエージェントが独立して完結できる場合

### 具体的な適用場面

- 複数のタスクを並列実装したいが、各エージェントの進捗監視に時間を取られている
- Linear/GitHub Issuesに溜まったバックログを自動消化させたい
- CI失敗やPRレビュー指摘に対して自動で再試行・修正させたい
- チーム全体でエージェント活用を標準化し、人間は承認・レビューに集中したい

## やり方

1. Codex app-serverをローカルまたはリモートで起動（codex server start） 2. Symphony設定でCodex APIエンドポイントとモデル（o1/o3等）を指定 3. Linearから取得したイシュー本文をプロンプトとして、Codex APIに POST /runs でリクエスト 4. 各実行をSymphony内でプロセス（Elixir GenServer等）として追跡、並列実行

### 入力

- Codex APIエンドポイント
- 実行対象タスクのプロンプト
- 並列実行数上限（リソース管理）

### 出力

- 各タスクの実行ID（Codex run ID）
- 実行結果（成功/失敗、生成されたPR URL等）

## 使うツール・ライブラリ

- Codex app-server
- Symphony Elixir実装（GenServer for task supervision）

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
