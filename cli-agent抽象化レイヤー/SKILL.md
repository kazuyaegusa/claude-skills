# CLI agent抽象化レイヤー

> 任意のCLIベースエージェント（Claude Code, Codex, Cursor等）を統一インターフェースで実行できるようにする

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: claude-code-workflow

## なぜ使うのか

エージェントごとに異なる起動方法・設定を吸収し、切り替えコストを最小化するため

## いつ使うのか

複数のエージェントを使い分けたい場合、エージェントの乗り換えを検討する場合

## やり方

1. エージェントをターミナルで実行できることを確認
2. Supersetのworkspace作成時にエージェント種別を選択
3. 内部的にそのエージェントのCLIコマンドを起動
4. 標準入出力をSupersetのUIに統合
5. エージェント終了時に結果を取得

### 入力

- CLIで実行可能なエージェント（claude, codex, cursor等）
- エージェントの実行コマンドパス

### 出力

- 統一されたエージェント実行環境
- エージェント間のシームレスな切り替え

## 使うツール・ライブラリ

- node-pty / xterm.js (ターミナルエミュレーション)
- 各エージェントのCLI

## 前提知識

- git worktreeの基本概念（メインリポジトリと独立した作業ツリー）
- CLIベースのAIコーディングエージェントの使用経験
- macOS環境（現時点でWindows/Linuxは未検証）
- Bun v1.0+、git 2.20+、gh CLI、Caddyのインストール

## 根拠

> 「Works with any CLI agent that runs in a terminal」
