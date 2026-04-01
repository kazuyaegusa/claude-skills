# SPECドキュメント駆動での独自実装

> OpenAIが公開したSPEC.mdに従い、好きな言語でSymphonyを自作する

- 出典: https://x.com/gota_bara/status/2029298458855915897
- 投稿者: Gota@Data Analyst
- カテゴリ: agent-orchestration

## なぜ使うのか

既存の言語スタック（Python, Go等）に統合したい、またはElixir以外で運用したい場合に対応するため

## いつ使うのか

Elixir環境がない、または既存のPython/Go等エコシステムに統合したい場合

### 具体的な適用場面

- 複数のタスクを並列実装したいが、各エージェントの進捗監視に時間を取られている
- Linear/GitHub Issuesに溜まったバックログを自動消化させたい
- CI失敗やPRレビュー指摘に対して自動で再試行・修正させたい
- チーム全体でエージェント活用を標準化し、人間は承認・レビューに集中したい

## やり方

1. https://github.com/openai/symphony/blob/main/SPEC.md を読み、必要な機能要件を把握 2. お気に入りのコーディングエージェント（Codex, Cursor等）に「SPEC.mdに従ってSymphonyを[言語]で実装して」と指示 3. Linear API連携、Codex API呼び出し、タスク監視、Proof of Work生成の各モジュールを実装 4. ローカルテスト後、本番環境で運用

### 入力

- SPEC.mdファイル
- 対象言語のHTTPクライアント、並行処理ライブラリ

### 出力

- 独自言語で実装されたSymphonyプロセス

## 使うツール・ライブラリ

- SPEC.md
- 任意のプログラミング言語
- Codex/Cursorなどのコーディングエージェント

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
