# 任意のCLIエージェントをSupersetで実行する

> Claude Code, Cursor Agent, Copilot, Gemini CLI等、あらゆるCLIベースのコーディングエージェントをSupersetのターミナル内で実行する。

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: claude-code-workflow

## なぜ使うのか

エージェントごとに異なるインターフェースを覚える必要がなく、全てを統一されたワークスペース管理・diff表示・通知の仕組みで扱える。ツールのロックインを避けつつ最適なエージェントを選べる。

## いつ使うのか

特定のエージェントに依存したくないとき、タスクごとに最適なエージェントを使い分けたいとき

## やり方

1. Supersetで新規ワークスペースを作成
2. ターミナル内でエージェントのCLIコマンドを実行（例: claude code, cursor agent, copilot cli）
3. エージェントが通常通り動作し、Supersetのdiff viewer・通知・ショートカットが利用可能
4. プリセット（Ctrl+1-9）でよく使うエージェントコマンドを登録しておくと起動が高速化

### 入力

- 任意のCLIコーディングエージェント
- エージェントの起動コマンド

### 出力

- 統一されたワークスペース管理下での任意エージェント実行
- エージェント間の柔軟な切り替え

## 使うツール・ライブラリ

- Superset
- 任意のCLI agent（Claude Code, Cursor, Copilot, Gemini等）

## 前提知識

- git 2.20以上の基礎知識（worktree概念の理解が望ましい）
- macOS環境（現時点でWindows/Linuxは未検証）
- Bun v1.0+, GitHub CLI (gh), Caddy（開発時のみ）
- CLIベースのコーディングエージェント（Claude Code, Cursor Agent等）のいずれか
