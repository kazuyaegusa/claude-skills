# Linear連携による自動タスク取得

> LinearボードからイシューをポーリングまたはWebhookで取得し、エージェント実行タスクに変換する

- 出典: https://x.com/gota_bara/status/2029298458855915897
- 投稿者: Gota@Data Analyst
- カテゴリ: agent-orchestration

## なぜ使うのか

人間がタスクをエージェントに手動で投げる手間を省き、イシューが登録された時点で自動実行パイプラインに乗せるため

## いつ使うのか

Linearでタスク管理しており、エージェント実行を自動化したい場合

### 具体的な適用場面

- 複数のタスクを並列実装したいが、各エージェントの進捗監視に時間を取られている
- Linear/GitHub Issuesに溜まったバックログを自動消化させたい
- CI失敗やPRレビュー指摘に対して自動で再試行・修正させたい
- チーム全体でエージェント活用を標準化し、人間は承認・レビューに集中したい

## やり方

1. Linear APIキーを環境変数に設定 2. Symphony設定ファイルでLinearボードIDとフィルタ条件（ラベル、ステータス）を指定 3. Symphonyプロセス起動で定期的にLinear APIをポーリング、新規/更新イシューを検出 4. イシュー内容をプロンプトとしてCodexに渡し、実行タスクを生成

### 入力

- Linear APIキー
- ボードID、フィルタ条件（ラベル、ステータス等）
- Codexへのプロンプトテンプレート

### 出力

- Symphonyが監視する実行タスクのキュー
- 各タスクの進捗状態（running, failed, completed）

## 使うツール・ライブラリ

- Linear API
- Elixir HTTPクライアント（httpoison等）
- Symphony Elixir実装

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
