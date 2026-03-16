# キーボードショートカットによる高速切り替え

> ⌘1-9でworkspace直接切り替え、⌘Nで新規作成等のショートカットでタスク間を瞬時に移動する

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

マウス操作やメニュー選択は時間がかかり、フロー状態が途切れる。キーボードショートカットにより、複数エージェント間の切り替えを1秒未満で完了でき、思考の中断を最小化できる。

## いつ使うのか

複数タスクを頻繁に行き来する必要がある時

## やり方

1. Supersetで⌘1-9を押すと対応番号のworkspaceに即座に切り替わる
2. ⌘⌥↑/↓で前後のworkspaceに移動
3. ⌘Nで新規workspace作成ダイアログ起動
4. 全ショートカットは⌘/で設定画面から変更可能

### 入力

- 定義済みworkspace群

### 出力

- 即座のコンテキスト切り替え

## 使うツール・ライブラリ

- Superset（Electron shortcut API）

## 前提知識

- git 2.20以上（worktree機能）
- CLIベースのAIエージェント（Claude Code, Cursor Agent等）
- macOS環境（Windows/Linuxは未検証）
- 複数タスクを並列実行する意義の理解
