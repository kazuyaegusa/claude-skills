# Stealthモードでローカル専用タスク管理

> `bd init --stealth` で初期化すると、Beadsの `.beads/` ディレクトリやGitフックをコミットせず、ローカル専用でタスク管理できる

- 出典: https://github.com/steveyegge/beads
- 投稿者: steveyegge
- カテゴリ: agent-orchestration

## なぜ使うのか

共有プロジェクトで個人的にBeadsを使いたいが、チームには強制したくない場合や、.gitignoreに追加してプライベート運用したい場合

## いつ使うのか

チーム全体がBeadsを導入していないプロジェクトで、個人的に使いたい場合

## やり方

1. `bd init --stealth` で初期化
2. `.beads/` を `.gitignore` に追加（自動設定される場合もある）
3. すべてのBDコマンドがローカルで動作し、リモートには影響しない

### 入力

- プロジェクトディレクトリ

### 出力

- ローカル専用.beads/ DB（コミット不要）

## 使うツール・ライブラリ

- Beads CLI

## コード例

```
bd init --stealth
bd create "ローカル実験タスク" -p 3
bd ready
```

## 前提知識

- AIコーディングエージェント（Claude Code, Cursor等）の基本的な使い方
- コマンドラインツールのインストール方法（curl, npm, Homebrew等）
- Gitの基本操作（任意だがあると便利）
- SQLデータベースの概念（Doltが内部で使われる）
- 依存グラフ・DAGの概念（タスク管理に必要）

## 根拠

> 「bd init --stealth: use Beads locally without committing files to the main repo. Perfect for personal use on shared projects.」

> 「bd init --contributor: route planning issues to a separate repo (e.g., ~/.beads-planning). Keeps experimental work out of PRs.」
