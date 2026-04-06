# キーボードショートカットで高速workspace切り替えをする

> ⌘1-9で即座に目的のworkspaceに移動し、コンテキストスイッチを最小化する

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

マウス操作やタブ探しでは並列タスク間の移動コストが高い。数字キーで瞬時に切り替えることで「待ち」時間ゼロを実現

## いつ使うのか

複数タスクを頻繁に行き来する、レビュー待ち中に別タスクに即移りたい場合

## やり方

1. Supersetで最大9個のworkspaceを開く
2. ⌘1で1番目、⌘2で2番目...と移動
3. ⌘⌥↑/↓で前後のworkspaceを順次巡回
4. ⌘Nで新規workspace作成
5. Settings > Keyboard Shortcuts（⌘/）でカスタマイズ可能

### 入力

- 開いているworkspace一覧

### 出力

- 目的workspaceへの瞬時遷移

## 使うツール・ライブラリ

- Superset内蔵キーバインド機能

## 前提知識

- Git 2.20+の基本操作（worktree概念の理解）
- CLI AgentのインストールとAPI認証設定
- macOS環境（Windows/Linux未検証）
- Bun v1.0+のインストール（ソースビルド時）
- GitHub CLI（gh）のインストール

## 根拠

> 「All shortcuts are customizable via Settings > Keyboard Shortcuts (⌘/)」（ショートカット説明）
