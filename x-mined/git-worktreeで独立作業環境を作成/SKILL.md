# git worktreeで独立作業環境を作成

> `git worktree add`でリポジトリに紐づいた複数の作業ディレクトリを作成し、それぞれで異なるブランチを同時チェックアウトする

- 出典: https://x.com/bcherny/status/2025007393290272904
- 投稿者: Boris Cherny
- カテゴリ: claude-code-workflow

## なぜ使うのか

git stashや別クローンと違い、オブジェクトDBを共有するため容量が小さく、ブランチ間の切り替えなしに複数の作業を同時進行できる

## いつ使うのか

現在の作業を中断せずに別ブランチで緊急対応が必要なとき、またはCI並列ビルドや複数エージェント並列実行のとき

## やり方

1. `git worktree add -b <branch-name> <path> <base-branch>` で新worktreeを作成
2. 作成されたパスに移動して作業
3. `git worktree list`で全worktreeを確認
4. 完了後`git worktree remove <path>`で削除
5. 削除し忘れた場合は`git worktree prune`でクリーンアップ

### 入力

- gitリポジトリ
- 新しいブランチ名
- 作業ディレクトリパス

### 出力

- 独立したHEAD・インデックス・作業ディレクトリを持つlinked worktree

## 使うツール・ライブラリ

- git worktree

## コード例

```
$ git worktree add -b emergency-fix ../temp master
$ pushd ../temp
# 作業
$ git commit -a -m 'emergency fix'
$ popd
$ git worktree remove ../temp
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
