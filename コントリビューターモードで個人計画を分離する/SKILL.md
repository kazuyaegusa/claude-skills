# コントリビューターモードで個人計画を分離する

> `bd init --contributor` でBeadsを初期化すると、計画用タスクを別リポジトリ（例: `~/.beads-planning`）に保存し、PR時に実験的なタスクが混入しないようにする

- 出典: https://github.com/steveyegge/beads
- 投稿者: steveyegge
- カテゴリ: agent-orchestration

## なぜ使うのか

フォークしたOSSプロジェクトで個人的な計画メモや試行錯誤をコミットせず、本番タスクだけをPRに含めたい

## いつ使うのか

OSSプロジェクトのフォークで作業し、個人メモをPRから除外したい場合

## やり方

1. フォークしたプロジェクトで `bd init --contributor` を実行
2. Beadsは個人計画を `~/.beads-planning` などの別ディレクトリで管理
3. 本番タスクのみプロジェクト内の `.beads/` に保存
4. PRを作成してもコントリビューター用タスクは含まれない

### 入力

- フォークしたリポジトリ

### 出力

- 個人計画用の分離DB（~/.beads-planning等）
- クリーンなPR（計画タスク混入なし）

## 使うツール・ライブラリ

- Beads CLI

## コード例

```
cd forked-project
bd init --contributor
bd create "実験: 新UIパターン" -p 2  # ~/.beads-planningに保存
# PRには含まれない
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
