# ビルド済みバイナリによる即座導入

> GitHubリリースページから.dmg/.appをダウンロードし、ビルド不要で即座にSupersetを利用開始する

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

ソースからビルドするには依存関係の解決（Bun, Caddy等）と環境構築に時間がかかる。ビルド済みバイナリを提供することで、試用ハードルを下げ、数分で並列エージェント環境を構築できる。

## いつ使うのか

環境構築の手間を省いてすぐに試したい時

## やり方

1. https://github.com/superset-sh/superset/releases/latest にアクセス
2. macOS用の.dmg/.appをダウンロード
3. Applicationsフォルダにドラッグ&ドロップ
4. Supersetを起動し、既存リポジトリを開く
5. workspaceを作成してエージェントを起動

### 入力

- macOS環境

### 出力

- インストール済みSuperset

## 使うツール・ライブラリ

- GitHub Releases

## 前提知識

- git 2.20以上（worktree機能）
- CLIベースのAIエージェント（Claude Code, Cursor Agent等）
- macOS環境（Windows/Linuxは未検証）
- 複数タスクを並列実行する意義の理解
