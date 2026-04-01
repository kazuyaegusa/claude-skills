# Superset daemon で agent セッションを永続化する

> Superset の後背 daemon でターミナルセッションを管理し、アプリ終了・クラッシュ後も会話履歴とスクロールバッファを復元できるようにする

- 出典: https://x.com/laogui/status/2035229908134502833
- 投稿者: 老鬼
- カテゴリ: agent-orchestration

## なぜ使うのか

AI agent の長時間タスク実行中にアプリを閉じたりクラッシュすると、従来は全セッションが失われた。daemon 化により状態を保持し、再接続で作業を継続できる

## いつ使うのか

AI agent に長時間タスクを依頼した後、他の作業のためにアプリを閉じたい時、またはシステムが不安定で途中クラッシュのリスクがある時

### 具体的な適用場面

- Claude Code、Codex CLI、Gemini CLI など複数の異なる AI agent を同じプロジェクトで並行稼働させたい時
- AI agent が長時間実行するタスクを複数走らせ、途中で画面を閉じても進捗を失いたくない時
- 複数 agent による変更を一箇所で diff 確認・approve・merge したい時
- 10個以上の AI agent を同時起動して大規模タスクを並列処理したい時

## やり方

1. Superset を起動すると自動的に後背 daemon が立ち上がる
2. 各 agent セッションは daemon プロセス内で実行される
3. Superset アプリを閉じる・クラッシュさせる
4. 再度 Superset を開くと、daemon から全セッションの状態（会話履歴、スクロールバッファ、実行中タスク）が復元される

### 入力

- Superset アプリ
- 実行中の agent セッション

### 出力

- アプリ再起動後も復元される agent セッション
- 保持された会話履歴とスクロールバッファ

## 使うツール・ライブラリ

- Superset daemon（Superset に内蔵）

## 前提知識

- Claude Code、Codex CLI、Gemini CLI など CLI 型 AI coding agent の基本的な使い方
- ターミナル操作と複数プロセス管理の基礎知識
- Git による変更管理・diff 確認・merge の基本

## 根拠

> 本质上是多 agent 并行命令行工具，帮你解决多 agent 并行时的隔离、冲突和可视化管理问题

> 可以同时起十几个 Claude Code、Codex CLI、Gemini CLI 等，让它们在同一项目里并行做不同任务

> 再用统一的 dashboard 显示所有 agent 的进度、日志和改动 diff，支持在应用内直接 review 和合并

> 终端 session 是跑在一个后台 daemon 里，你关掉应用、甚至崩溃重启，再打开时所有会话和滚动缓冲都能恢复
