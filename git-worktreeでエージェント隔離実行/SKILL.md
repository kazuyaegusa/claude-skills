# git worktreeでエージェント隔離実行

> 1つのリポジトリから複数のworktree（独立した作業ディレクトリ）を作成し、それぞれに異なるブランチを割り当てることで、複数のAIエージェントが互いに干渉せずに並列動作する環境を構築する

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: claude-code-workflow

## なぜ使うのか

通常のブランチ切り替えでは、ファイルが上書きされエージェント同士が競合する。worktreeを使えば物理的に別ディレクトリで作業するため、同じリポジトリ内で完全に独立したタスクを並行実行できる。git履歴は共通なのでマージも容易。

## いつ使うのか

複数の独立した開発タスクを同時進行したい時、または複数のAIエージェントに異なる課題を並列で処理させたい時

## やり方

1. `git worktree add <パス> <ブランチ名>` で新しいworktreeを作成
2. 各worktree内でCLIエージェント（`claude -p` や `codex` 等）を起動
3. エージェントがそれぞれのブランチで変更を加える
4. Superset UIで全worktreeの状態を監視
5. 変更が完了したらdiffビューアでレビュー
6. 必要に応じてメインブランチへマージ
7. worktree削除は `git worktree remove <パス>`

### 入力

- ローカルgitリポジトリ
- 複数の独立したタスク（機能追加、バグ修正等）

### 出力

- タスクごとに隔離されたworktree（ディレクトリ＋ブランチ）
- 各エージェントの変更履歴が独立したブランチに記録される

## 使うツール・ライブラリ

- git 2.20+（worktree機能）
- 任意のCLIベースAIエージェント（Claude Code, Codex, Gemini CLI等）

## コード例

```
git worktree add ../worktree-feature-x feature-x
cd ../worktree-feature-x
claude -p "機能Xを実装"
```

## 前提知識

- git 2.20以上がインストールされていること（worktree機能）
- macOS環境（Windows/Linuxは未検証）
- Bun v1.0+ランタイム（ビルド・実行用）
- GitHub CLI（gh）とCaddy（開発サーバー用）のインストール
- CLIベースのAIエージェント（Claude Code, Codex, Gemini CLI等）が動作する環境
- git worktreeの基本概念（複数の作業ディレクトリを同一リポジトリで管理）の理解

## 根拠

> "Orchestrate swarms of Claude Code, Codex, and more in parallel. Works with any CLI agent. Built for local worktree-based development."

> "Isolate each task in its own git worktree so agents don't interfere with each other"

> "git worktree add <パス> <ブランチ名>"（技術的手法として明記）

> ".superset/config.json" で "setup": ["./.superset/setup.sh"] を定義することでワークスペース作成時に自動実行

> "Requirements: macOS, Bun v1.0+, Git 2.20+, gh, caddy"
