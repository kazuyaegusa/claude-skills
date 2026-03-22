# Beadsをプロジェクトに導入してエージェントに永続メモリを与える

> BeadsというCLIツールをインストールし、プロジェクトルートで初期化することで、Doltベースのタスク管理DBを作成し、エージェントがJSONでタスクをCRUDできるようにする

- 出典: https://github.com/steveyegge/beads
- 投稿者: steveyegge
- カテゴリ: claude-code-workflow

## なぜ使うのか

エージェントはセッションごとにコンテキストをリセットするため、計画をDBに永続化すれば再起動後も続きから作業でき、依存関係を明示的に管理できる

## いつ使うのか

エージェントが複数セッションにまたがる長期タスクを扱う場合、または複数エージェント・ブランチで並行作業する場合

## やり方

1. `curl -fsSL https://raw.githubusercontent.com/steveyegge/beads/main/scripts/install.sh | bash` でBeads CLIをシステムワイドにインストール
2. プロジェクトディレクトリで `bd init` を実行（`.beads/` ディレクトリとDolt DBが作成される）
3. `echo "Use 'bd' for task tracking" >> AGENTS.md` でエージェントにBD使用を指示
4. エージェントは `bd create "タスク名" -p 0` でタスク作成、`bd ready` でブロッカーのないタスク一覧取得、`bd update <id> --claim` でタスク着手、`bd dep add <child> <parent>` で依存設定を行う

### 入力

- プロジェクトディレクトリ（gitリポジトリ推奨だが不要も可）
- Linux/macOS/Windows/FreeBSD環境

### 出力

- .beads/ ディレクトリ内のDoltデータベース
- JSON形式でタスク一覧・依存グラフを返すCLI
- エージェントが読み書き可能な永続タスクストア

## 使うツール・ライブラリ

- Beads CLI (npm, Homebrew, Go install可能)
- Dolt（バージョン管理可能なSQL DB）

## コード例

```
# システムワイドインストール
curl -fsSL https://raw.githubusercontent.com/steveyegge/beads/main/scripts/install.sh | bash

# プロジェクト初期化
cd your-project
bd init
echo "Use 'bd' for task tracking" >> AGENTS.md

# エージェントが実行するコマンド例
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

> 「Beads provides a persistent, structured memory for coding agents. It replaces messy markdown plans with a dependency-aware graph, allowing agents to handle long-horizon tasks without losing context.」

> 「bd ready: List tasks with no open blockers.」

> 「bd init --stealth: use Beads locally without committing files to the main repo. Perfect for personal use on shared projects.」
