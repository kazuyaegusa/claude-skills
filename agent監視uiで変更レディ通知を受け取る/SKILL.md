# Agent監視UIで変更レディ通知を受け取る

> Superset UIで全Agentのステータスを一元表示し、変更完了時に通知を受け取る

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

複数Agentを起動すると、どれが完了したか・レビュー待ちかの把握が困難。統合UIで「待ち」から「レビュー」への遷移をスムーズにする

## いつ使うのか

10+のAgentを同時実行し、完了順にレビュー・マージしていきたい場合

## やり方

1. Supersetで複数workspaceを作成し、各々でAgentを起動
2. 左サイドバー（⌘B）で全workspace一覧を表示
3. 各workspaceのステータス（実行中/変更あり/エラー）がリアルタイム更新
4. 変更完了したworkspaceをクリックして切り替え
5. 内蔵diffビューア（⌘L）で変更を確認・編集
6. 必要に応じてgit commit/pushまたは外部エディタ連携（⌘O）

### 入力

- 起動中の複数Agent
- 各workspaceのgit status

### 出力

- 変更検出通知
- diff表示
- 外部エディタへのワンクリック連携

## 使うツール・ライブラリ

- Superset内蔵UIコンポーネント（React + Electron）
- git status/diff

## 前提知識

- Git 2.20+の基本操作（worktree概念の理解）
- CLI AgentのインストールとAPI認証設定
- macOS環境（Windows/Linux未検証）
- Bun v1.0+のインストール（ソースビルド時）
- GitHub CLI（gh）のインストール

## 根拠

> 「Scripts have access to environment variables: SUPERSET_WORKSPACE_NAME, SUPERSET_ROOT_PATH」（config.json仕様）
