# Workspace Presetsによる環境構築自動化

> 各worktree作成時に実行されるsetup/teardownスクリプトをプリセット化し、依存関係インストール・環境変数コピー・DB初期化等を自動化する

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

worktreeを手動で作成すると、毎回npm install、.envコピー、DB migration等を繰り返す必要がある。これを自動化すれば、エージェント起動までの時間を30秒以内に短縮できる

## いつ使うのか

同じプロジェクトで頻繁にworktreeを作成する時、または環境構築に3ステップ以上かかる時

## やり方

1. .superset/config.jsonでsetup/teardownコマンドを定義
2. setup.shに「cp ../.env .env && bun install && bun run db:migrate」等のスクリプトを記述
3. Ctrl+1-9でプリセット番号を指定してワークスペースを作成
4. Supersetが自動的にworktree作成→setupスクリプト実行→エージェント起動可能状態まで遷移
5. teardown時はteardown.shで一時ファイル削除・DBクリーンアップ等を実行

### 入力

- .superset/config.json（setup/teardownコマンド定義）
- setup.sh/teardown.shスクリプト
- 環境変数: SUPERSET_WORKSPACE_NAME, SUPERSET_ROOT_PATH

### 出力

- 即座に使える完全な開発環境（依存関係インストール済み）
- teardown時のクリーンアップ完了状態

## 使うツール・ライブラリ

- Bash/Zsh（スクリプト実行）
- Bun/npm/pnpm（依存関係管理）
- 任意のDB migration tool

## コード例

```
# .superset/config.json
{
  "setup": ["./.superset/setup.sh"],
  "teardown": ["./.superset/teardown.sh"]
}

# .superset/setup.sh例
#!/bin/bash
set -e
echo "Setting up workspace: $SUPERSET_WORKSPACE_NAME"
cp "$SUPERSET_ROOT_PATH/.env" .env
bun install --frozen-lockfile
bun run db:migrate
echo "✅ Ready"

# .superset/teardown.sh例
#!/bin/bash
rm -rf node_modules .turbo .next
echo "✅ Cleaned"
```

## 前提知識

- Git 2.20以上（worktree機能）
- macOS環境（Windows/Linux未検証）
- Bun v1.0以上（ランタイム）
- GitHub CLI（gh）
- 使用したいCLIエージェント（Claude Code、Codex等）のインストールと認証設定
- git worktreeの基本概念（ブランチとディレクトリの分離）

## 根拠

> 「Run multiple agents simultaneously without context switching overhead」（並列実行によるコンテキストスイッチング削減）

> 「Run 10+ coding agents simultaneously on your machine」（10個以上の同時実行）

> 「Automate env setup, dependency installation, and more」（Workspace Presetsによる自動化）

> 「Works with any CLI agent that runs in a terminal」（CLI汎用対応）

> 「If it runs in a terminal, it runs on Superset」（ターミナル互換性）
