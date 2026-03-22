# ワンクリックエディタ/ターミナル遷移による高速レビュー

> diff viewerで変更確認後、⌘Oでエディタまたはターミナルを開いて即座に編集できる

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェントの出力を別エディタで開き直すと時間がかかる。Superset内でdiff確認し、必要な時だけ外部エディタに遷移すれば、レビュー→修正のサイクルが劇的に速くなる

## いつ使うのか

エージェント生成コードを最終調整したい時。または、コミット前にコードレビューしたい時

## やり方

1. エージェント完了通知を受け取る
2. ⌘Lで変更パネルを開く
3. Built-in diff viewerで差分確認
4. 詳細編集が必要なら⌘Oでエディタ（VSCode等）を開く
5. または⌘Tでターミナルを開いてgit操作
6. ⌘⇧Cでパスをコピーして別ツールへ

### 入力

- エージェントが作成した変更（git diff）
- 外部エディタ設定（VSCode、Cursor等）

### 出力

- レビュー済み変更
- エディタまたはターミナルでの直接編集

## 使うツール・ライブラリ

- Superset built-in diff viewer
- 外部エディタ（VSCode、Cursor等）

## 前提知識

- git worktreeの基本概念（1つのリポジトリから複数の作業ディレクトリを作成できる）
- CLIエージェント（Claude Code、Codex等）の基本的な使い方
- git操作の基礎（branch、merge、diff）
- macOS環境（現時点ではWindows/Linux未対応）
- Bun、Git 2.20+、GitHub CLIのインストール

## 根拠

> 「Review and edit changes quickly with the built-in diff viewer and editor」
