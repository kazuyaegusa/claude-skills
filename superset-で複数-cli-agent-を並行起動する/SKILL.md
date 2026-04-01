# Superset で複数 CLI agent を並行起動する

> Claude Code、Codex CLI、Gemini CLI など CLI 型 coding agent を同一プロジェクト内で 10個以上並行実行する

- 出典: https://x.com/laogui/status/2035229908134502833
- 投稿者: 老鬼
- カテゴリ: claude-code-workflow

## なぜ使うのか

単一 agent では処理しきれない大規模タスクを分割し、複数 agent で同時進行させることで開発速度を大幅に向上できる

## いつ使うのか

複数の独立したタスクを AI agent に同時依頼したい時、または単一 agent では時間がかかりすぎるタスクを分割処理したい時

### 具体的な適用場面

- Claude Code、Codex CLI、Gemini CLI など複数の異なる AI agent を同じプロジェクトで並行稼働させたい時
- AI agent が長時間実行するタスクを複数走らせ、途中で画面を閉じても進捗を失いたくない時
- 複数 agent による変更を一箇所で diff 確認・approve・merge したい時
- 10個以上の AI agent を同時起動して大規模タスクを並列処理したい時

## やり方

1. Superset をインストール（具体的なコマンドは投稿未記載）
2. プロジェクトディレクトリで複数の agent CLI を起動（例: `claude -p`、`codex`、`gemini` など）
3. Superset の dashboard で各 agent セッションを登録・起動
4. 各 agent に異なるタスク（例: フロントエンド実装、バックエンド API、テスト追加）を並行指示
5. dashboard で全 agent の進捗・ログ・diff を一覧表示

### 入力

- 複数の CLI 型 coding agent（Claude Code、Codex CLI、Gemini CLI 等）
- 並行実行したいタスクリスト
- 対象プロジェクトディレクトリ

### 出力

- 複数 agent による並行実装結果
- 統一 dashboard での進捗・ログ表示
- 各 agent による変更 diff

## 使うツール・ライブラリ

- Superset (https://superset.sh/)
- Claude Code
- Codex CLI
- Gemini CLI

## 前提知識

- Claude Code、Codex CLI、Gemini CLI など CLI 型 AI coding agent の基本的な使い方
- ターミナル操作と複数プロセス管理の基礎知識
- Git による変更管理・diff 確認・merge の基本

## 根拠

> 本质上是多 agent 并行命令行工具，帮你解决多 agent 并行时的隔离、冲突和可视化管理问题

> 可以同时起十几个 Claude Code、Codex CLI、Gemini CLI 等，让它们在同一项目里并行做不同任务

> 再用统一的 dashboard 显示所有 agent 的进度、日志和改动 diff，支持在应用内直接 review 和合并

> 终端 session 是跑在一个后台 daemon 里，你关掉应用、甚至崩溃重启，再打开时所有会话和滚动缓冲都能恢复
