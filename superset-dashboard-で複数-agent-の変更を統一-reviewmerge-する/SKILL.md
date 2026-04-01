# Superset dashboard で複数 agent の変更を統一 review・merge する

> Superset の統一 dashboard で全 agent の変更 diff を一覧表示し、アプリ内で直接 review・approve・merge を実行する

- 出典: https://x.com/laogui/status/2035229908134502833
- 投稿者: 老鬼
- カテゴリ: agent-orchestration

## なぜ使うのか

複数 agent が並行で変更すると、各 agent のターミナルを個別に確認するのは非効率。統一 UI で全変更を俯瞰し、コンフリクトを早期発見・解決できる

## いつ使うのか

複数 agent による変更を効率的に確認・統合したい時、または agent 間のファイル競合を早期に発見・解決したい時

### 具体的な適用場面

- Claude Code、Codex CLI、Gemini CLI など複数の異なる AI agent を同じプロジェクトで並行稼働させたい時
- AI agent が長時間実行するタスクを複数走らせ、途中で画面を閉じても進捗を失いたくない時
- 複数 agent による変更を一箇所で diff 確認・approve・merge したい時
- 10個以上の AI agent を同時起動して大規模タスクを並列処理したい時

## やり方

1. Superset dashboard を開く
2. 各 agent セッションのタブで進捗状況を確認
3. 変更が発生した agent の diff ビューを開く
4. dashboard 上で変更内容を review（コード差分を確認）
5. approve ボタンで変更を承認、または reject で却下
6. 複数 agent の変更を順次または一括で merge
7. コンフリクトが検出された場合は dashboard 上で解決

### 入力

- 複数 agent による変更（diff）
- Superset dashboard

### 出力

- review 済み・merge 済みの変更
- コンフリクト解決済みのコードベース

## 使うツール・ライブラリ

- Superset dashboard（Superset に内蔵）

## 前提知識

- Claude Code、Codex CLI、Gemini CLI など CLI 型 AI coding agent の基本的な使い方
- ターミナル操作と複数プロセス管理の基礎知識
- Git による変更管理・diff 確認・merge の基本

## 根拠

> 本质上是多 agent 并行命令行工具，帮你解决多 agent 并行时的隔离、冲突和可视化管理问题

> 可以同时起十几个 Claude Code、Codex CLI、Gemini CLI 等，让它们在同一项目里并行做不同任务

> 再用统一的 dashboard 显示所有 agent 的进度、日志和改动 diff，支持在应用内直接 review 和合并

> 终端 session 是跑在一个后台 daemon 里，你关掉应用、甚至崩溃重启，再打开时所有会话和滚动缓冲都能恢复
