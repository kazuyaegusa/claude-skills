# プリセットベースのターミナル分割レイアウト

> よく使うコマンド組み合わせ（dev server + log watch等）をプリセット保存し、Ctrl+1-9で即起動する

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

worktreeごとに毎回ターミナルを分割してコマンド入力すると時間がかかる。プリセット化すれば、複数コマンドを一括起動でき、開発開始が瞬時になる

## いつ使うのか

複数のプロセス（dev server、DB、watch、log監視等）を同時起動したい時

## やり方

1. Settings > Presetsでプリセット作成
2. ターミナル分割レイアウト（split right/down）とコマンドを登録
3. Ctrl+1-9で呼び出し
4. 例：Ctrl+1でbun run dev、Ctrl+2でbun run dev + tail -f logs/app.log

### 入力

- プリセット設定（コマンド＋分割レイアウト）

### 出力

- 分割ターミナルに複数プロセス起動済み状態

## 使うツール・ライブラリ

- Superset terminal presets

## 前提知識

- git worktreeの基本概念（1つのリポジトリから複数の作業ディレクトリを作成できる）
- CLIエージェント（Claude Code、Codex等）の基本的な使い方
- git操作の基礎（branch、merge、diff）
- macOS環境（現時点ではWindows/Linux未対応）
- Bun、Git 2.20+、GitHub CLIのインストール

## 根拠

> 「Orchestrate swarms of Claude Code, Codex, and more in parallel. Works with any CLI agent. Built for local worktree-based development.」

> 「Run 10+ coding agents simultaneously on your machine」「Each task gets its own branch and working directory」

> 「All shortcuts are customizable via Settings > Keyboard Shortcuts (⌘/)」

> 「Works with any CLI-based coding agent」「If it runs in a terminal, it runs on Superset」
