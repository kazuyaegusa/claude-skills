# ユニバーサルCLIエージェント対応アーキテクチャ

> 特定のエージェントに依存せず、任意のCLIベースエージェント（Claude Code、Codex、Cursor、Gemini CLI等）をプラグイン不要で実行できる

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: claude-code-workflow

## なぜ使うのか

エージェント市場は急速に進化しており、特定ツールに依存すると将来的に乗り換えコストが発生する。標準入出力を扱うCLIインターフェースに統一すれば、どのエージェントでも互換性を保てる

## いつ使うのか

新しいエージェントを試したい時、または複数のエージェントを同時に使い分けたい時

## やり方

1. Supersetは内部的にpty（pseudo-terminal）を使ってエージェントプロセスを起動
2. ユーザーは任意のCLIコマンド（claude、codex、cursor-agent等）をターミナルから実行
3. エージェントの標準出力・標準エラー出力はSupersetが自動的にキャプチャして表示
4. Ctrl+C等の制御信号も正常に伝達される
5. エージェント終了時のexit codeも取得可能

### 入力

- 実行可能なCLIエージェントコマンド（PATH上に存在）
- エージェント用の認証トークン・APIキー（環境変数経由）

### 出力

- エージェントの標準出力・エラー出力のリアルタイム表示
- エージェント完了時のexit code

## 使うツール・ライブラリ

- 任意のCLI coding agent（Claude Code、Codex、Cursor等）
- pty（pseudo-terminal）

## コード例

```
# Supersetターミナルで任意のエージェントを起動
$ claude -p "Implement feature X"
$ codex --task "Fix bug Y"
$ cursor-agent --file src/app.ts

# 複数ワークスペースで異なるエージェントを並列実行
Workspace 1: claude
Workspace 2: codex
Workspace 3: cursor-agent
```

## 前提知識

- Git 2.20以上（worktree機能）
- macOS環境（Windows/Linux未検証）
- Bun v1.0以上（ランタイム）
- GitHub CLI（gh）
- 使用したいCLIエージェント（Claude Code、Codex等）のインストールと認証設定
- git worktreeの基本概念（ブランチとディレクトリの分離）
