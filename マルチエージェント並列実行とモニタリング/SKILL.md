# マルチエージェント並列実行とモニタリング

> 複数のCLIエージェント（Claude Code、Codex等）を同時起動し、各エージェントの状態を一元監視する

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: claude-code-workflow

## なぜ使うのか

1つのエージェントの応答待ち中に他のタスクへ着手できれば、開発者の稼働率が上がる。また、一箇所で全エージェントの状態を把握できれば、どのタスクがレビュー待ちかを見逃さない。

## いつ使うのか

複数の独立したタスクがあり、待ち時間を最小化したい場合

## やり方

1. Supersetで複数のworkspaceを作成（⌘N または ⌘⇧N）
2. 各workspaceで異なるCLI agent（claude-code、codex等）を起動
3. Supersetのworkspace sidebarで全エージェントの状態を確認
4. エージェントが変更を完了すると通知が届く
5. ⌘Lでchanges panelを開き、diff viewerでレビュー
6. 問題なければコミット、次のタスクへ切り替え（⌘1-9でworkspace切り替え）

### 入力

- 複数の独立したタスク
- CLIベースのAIエージェント（claude、codex、cursor等）

### 出力

- 並列実行された複数のタスクの完了通知
- レビュー可能な変更差分のリスト

## 使うツール・ライブラリ

- Superset
- Claude Code / Codex / Cursor / Gemini CLI等のCLIエージェント

## 前提知識

- gitの基本操作（branch、merge、worktreeの概念）
- CLIベースのAIエージェント（Claude Code、Codex等）の基本的な使い方
- macOS環境（現時点でmacOSのみサポート）
- Bun v1.0+、Git 2.20+、GitHub CLI、Caddyのインストール
