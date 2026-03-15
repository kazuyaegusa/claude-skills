# Agent Teams + Git Worktreesで並列開発する

> 複数のClaude Codeエージェントをtmuxで並列起動し、各エージェントにgit worktreeで独立したブランチ作業環境を与えて並列開発する

- 出典: https://x.com/labelmake/status/2032652943250338098
- 投稿者: Kyohei - OSS, 外資IT
- カテゴリ: claude-code-workflow

## なぜ使うのか

独立したタスクを並列実行することで開発速度が向上し、各エージェントが互いのコンテキストを汚染しない

## いつ使うのか

互いに依存しない複数機能を同時開発したい場合、レビューと実装を並列で進めたい場合

## やり方

1. `git worktree add ../feature-branch feature/my-feature` でworktreeを作成
2. tmuxで複数ペインを開き、各ペインで異なるworktreeディレクトリに `cd`
3. 各ペインで `claude` を起動（環境変数でAgent Teamsを有効化）
4. 各エージェントに独立したタスクを割り当て
5. 完了後 `git worktree remove ../feature-branch` でクリーンアップ

### 入力

- 並列実行可能なタスクリスト
- tmux環境

### 出力

- 並列開発されたブランチ群

## 使うツール・ライブラリ

- git worktree
- tmux
- Claude Code Agent Teams（beta）

## コード例

```
git worktree add ../feature-auth feature/auth
git worktree add ../feature-api feature/api
# tmuxで各ディレクトリでclaudeを起動
```

## 前提知識

- Claude Code CLIの基本操作（起動、プロンプト入力、コマンド実行）
- GitおよびGitHubの基本知識
- CLAUDE.md、.claude/ディレクトリ構造の理解
- Claude CodeのPlan Mode、Command、Agent、Skillの概念的な区別

## 根拠

> 「公式・コミュニティのClaude Codeベストプラクティスを1箇所にまとめたリポジトリがGitHub月間トレンド入り」

> "avoid agent dumb zone, do manual /compact at max 50%"

> "use 'use subagents' to throw more compute at a problem"

> "agent teams with tmux and git worktrees for parallel development"
