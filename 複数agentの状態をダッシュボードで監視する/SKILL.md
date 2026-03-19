# 複数agentの状態をダッシュボードで監視する

> Supersetの単一画面で全workspace（agent）のステータス・出力・差分を一覧表示する

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: claude-code-workflow

## なぜ使うのか

10個のターミナルを手動で切り替えると見落としや遅延が発生。1画面で全体を俯瞰すれば、どのagentが待ちかすぐ分かる

## いつ使うのか

複数agentを並列実行し、誰が止まっているか即座に把握したい時

## やり方

1. Supersetを起動
2. 各workspaceでagentのCLI（claude -p, codex, cursorなど）を実行
3. ⌘1-9でworkspace切り替え、またはサイドバーで一覧表示
4. ⌘Lで差分パネル表示、agentの変更を即座にレビュー
5. 通知でagentの完了・エラーを受け取る

### 入力

- 各workspaceのターミナル出力
- git diff情報
- agent CLIのexit code

### 出力

- workspace一覧（status付き）
- diff viewer上のコード差分
- 通知アラート

## 使うツール・ライブラリ

- Superset Desktop App
- Electron（UI基盤）
- 組み込みdiff viewer

## 前提知識

- git 2.20+の基本操作知識
- git worktreeの概念
- ターミナルでのagent CLI実行経験
- macOS環境（Windows/Linux未検証）
- Bun, gh, Caddyのインストール方法
