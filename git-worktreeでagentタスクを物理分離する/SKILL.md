# git worktreeでagentタスクを物理分離する

> 1つのgitリポジトリから複数のworking directoryを作り、それぞれ独立したブランチで作業させる

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: claude-code-workflow

## なぜ使うのか

同一ディレクトリで複数agentを走らせると、ファイル競合・git状態の衝突が起きる。worktreeなら同じリポジトリの異なるブランチが並存できる

## いつ使うのか

複数のfeature開発を並行したい、かつagentに任せたい時

## やり方

1. `git worktree add <path> <branch>` で新しいworktreeを作成
2. Supersetは各workspaceにworktreeを自動割り当て
3. 各agentは独立したディレクトリで `claude -p` などを実行
4. `.superset/setup.sh` で環境変数コピー・依存インストールを自動化
5. 終わったら `git worktree remove` で削除

### 入力

- 親リポジトリのパス
- 各タスク用のブランチ名
- setup/teardownスクリプト

### 出力

- 独立した作業ディレクトリ（worktree）
- 各ブランチのコミット履歴
- 衝突のない並行開発状態

## 使うツール・ライブラリ

- git worktree
- Superset（workspace管理UI）
- .superset/config.json（setup/teardown定義）

## コード例

```
{
  "setup": ["./.superset/setup.sh"],
  "teardown": ["./.superset/teardown.sh"]
}

# .superset/setup.sh
cp ../.env .env
bun install
```

## 前提知識

- git 2.20+の基本操作知識
- git worktreeの概念
- ターミナルでのagent CLI実行経験
- macOS環境（Windows/Linux未検証）
- Bun, gh, Caddyのインストール方法

## 根拠

> Isolate each task in its own git worktree so agents don't interfere with each other

> Worktree Isolation: Each task gets its own branch and working directory

> Supported agents: Claude Code, OpenAI Codex CLI, Cursor Agent, Gemini CLI, GitHub Copilot, OpenCode, Pi
