# Git不要モードでBeadsを使う

> 環境変数 `BEADS_DIR` を設定し `bd init --quiet --stealth` で初期化することで、Gitリポジトリがなくても任意のディレクトリでBeadsを動作させる

- 出典: https://github.com/steveyegge/beads
- 投稿者: steveyegge
- カテゴリ: agent-orchestration

## なぜ使うのか

非Git VCS（Sapling, Jujutsu等）やモノレポの一部、CI/CD環境など、Gitフックやリポジトリ前提の操作が不要・不可能な場合でもBeadsを使いたい

## いつ使うのか

Gitを使わないプロジェクト、モノレポの特定サブディレクトリ、CI/CDパイプライン、一時的な評価環境でBeadsを使いたい場合

## やり方

1. `export BEADS_DIR=/path/to/your/project/.beads` でDB配置先を明示
2. `bd init --quiet --stealth` で初期化（`--stealth` はgit操作を完全無効化）
3. `bd create`, `bd ready`, `bd update`, `bd close` などすべてのコアコマンドがGit呼び出しなしで動作

### 入力

- 任意のディレクトリパス（Gitリポジトリ不要）

### 出力

- 指定ディレクトリ内の.beads/ DB
- Git操作なしで動作するタスク管理

## 使うツール・ライブラリ

- Beads CLI
- Dolt

## コード例

```
export BEADS_DIR=/path/to/your/project/.beads
bd init --quiet --stealth
bd create "Fix auth bug" -p 1 -t bug
bd ready --json
bd update bd-a1b2 --claim
bd close bd-a1b2 "Fixed"
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
