# Elixir/OTPによる実行監視と自動再起動

> Elixir OTPのSupervisorを使い、エージェント実行の失敗検知・再起動・状態管理を自動化する

- 出典: https://x.com/gota_bara/status/2029298458855915897
- 投稿者: Gota@Data Analyst
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェントがCI失敗やAPI制限等で途中停止しても、人間が手動で再実行する必要をなくし、完了まで自律的にリトライさせるため

## いつ使うのか

エージェント実行が不安定で途中失敗することがあり、自動リトライさせたい場合

### 具体的な適用場面

- 複数のタスクを並列実装したいが、各エージェントの進捗監視に時間を取られている
- Linear/GitHub Issuesに溜まったバックログを自動消化させたい
- CI失敗やPRレビュー指摘に対して自動で再試行・修正させたい
- チーム全体でエージェント活用を標準化し、人間は承認・レビューに集中したい

## やり方

1. mix new symphony でElixirプロジェクト作成 2. lib/symphony/run_supervisor.ex にSupervisor定義、子プロセスとして各Codex実行を起動 3. GenServerで各実行の状態（running, failed, completed）を管理 4. 失敗時はSupervisor戦略（:one_for_one, :rest_for_one等）で自動再起動、最大リトライ回数を設定 5. mix run --no-halt で常駐プロセスとして起動

### 入力

- Supervisor起動設定（application.ex）
- 各実行タスクの初期状態
- リトライポリシー（最大回数、バックオフ戦略）

### 出力

- 常駐プロセスとして動作するSymphonyサーバー
- 各実行の状態変化ログ

## 使うツール・ライブラリ

- Elixir
- OTP Supervisor/GenServer

## コード例

```
defmodule Symphony.RunSupervisor do
  use Supervisor

  def start_link(init_arg) do
    Supervisor.start_link(__MODULE__, init_arg, name: __MODULE__)
  end

  def init(_init_arg) do
    children = [
      {Symphony.RunWorker, []}
    ]
    Supervisor.init(children, strategy: :one_for_one, max_restarts: 3)
  end
end
```

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
