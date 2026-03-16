# 統合エージェントモニタリング

> 複数稼働中のエージェントのステータスを一元UIで監視し、変更準備完了時に通知を受け取る

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェントを並列実行すると、どれが完了したか・どれがエラーかを個別に確認するのは煩雑。統合モニタリングにより、注意が必要なタスクに即座にフォーカスでき、待ち時間を最小化できる。

## いつ使うのか

複数エージェントを同時稼働させている時

## やり方

1. Supersetで複数workspaceを起動（各々でエージェント実行）
2. Superset UIのworkspaces sidebarで全タスクの状態を一覧表示
3. エージェントが変更をcommitすると、UIに通知が表示される
4. changes panelで差分をレビュー
5. 問題なければマージ、修正が必要なら該当workspaceに切り替え

### 入力

- 稼働中のworkspace群

### 出力

- リアルタイムステータス通知
- 統合diff viewer

## 使うツール・ライブラリ

- Superset UI（React + Electron）

## 前提知識

- git 2.20以上（worktree機能）
- CLIベースのAIエージェント（Claude Code, Cursor Agent等）
- macOS環境（Windows/Linuxは未検証）
- 複数タスクを並列実行する意義の理解

## 根拠

> 「.superset/config.json」「setup/teardown scripts」（preset自動化）

> 「Download Superset for macOS」（ビルド済み配布）
