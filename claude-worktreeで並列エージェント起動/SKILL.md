# claude --worktreeで並列エージェント起動

> `claude --worktree`フラグを使い、各Claude Codeエージェントを独立したgit worktreeで起動する

- 出典: https://x.com/bcherny/status/2025007393290272904
- 投稿者: Boris Cherny
- カテゴリ: claude-code-workflow

## なぜ使うのか

worktreeは同一リポジトリのオブジェクトDBを共有しつつ、HEAD・インデックス・作業ディレクトリが独立するため、複数エージェントが互いのファイル変更を上書きせず並列作業できる

## いつ使うのか

2つ以上のClaude Codeエージェントを同一リポジトリで同時に動かしたいとき

## やり方

1. `claude --worktree`コマンドを実行してエージェントを起動
2. Claude Codeが自動的に新しいlinked worktreeを作成し、専用ディレクトリにチェックアウト
3. 別ターミナルで同様に`claude --worktree`を実行すると、別のworktreeで独立したエージェントが起動
4. 各エージェントは異なるブランチ・ディレクトリで作業するため干渉しない
5. 完了後は`git worktree remove <path>`でworktreeを削除

### 入力

- git管理されたリポジトリ
- Claude Code CLI（worktreeサポート版）

### 出力

- 各エージェントが独立したブランチ・ディレクトリで作業した成果物
- それぞれのworktreeに独立したコミット履歴

## 使うツール・ライブラリ

- claude CLI（--worktreeフラグ）
- git worktree

## コード例

```
$ claude --worktree
```

## 前提知識

- gitの基本操作（branch, commit, checkout）の理解
- Claude Code CLIのインストールと設定
- git worktreeの仕組み：リポジトリのオブジェクトDB共有・HEAD/インデックス独立の概念

## 根拠

> Introducing: built-in git worktree support for Claude Code

> Now, agents can run in parallel without interfering with one other. Each agent gets its own worktree and can work independently.

> The Claude Code Desktop app has had built-in support for worktrees for a while, and now we're bringing it to CLI too.

> 画像: `$ claude --worktree`（CLIコマンドのデモ）

> git worktree公式ドキュメント: 'Manage multiple working trees attached to the same repository. A git repository can support multiple working trees, allowing you to check out more than one branch at a time.'
