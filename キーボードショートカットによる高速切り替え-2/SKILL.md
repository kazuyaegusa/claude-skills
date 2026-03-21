# キーボードショートカットによる高速切り替え

> ⌘1-9で各workspaceへ瞬時に切り替え、⌘Lでdiff panel表示、⌘Oで外部エディタ起動などをショートカットで実行

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

マウス操作やメニュー探索は時間の無駄。ショートカットで操作を筋肉記憶化すれば、エージェント間の切り替えコストが実質ゼロになる。

## いつ使うのか

複数workspaceを頻繁に切り替える場合、UIの応答速度を最大化したい場合

## やり方

1. Supersetを起動
2. Settings > Keyboard Shortcuts（⌘/）でショートカット一覧を確認
3. 頻繁に使う操作（workspace切り替え、terminal分割、diff表示等）のショートカットを覚える
4. 実作業でショートカットを使い、マウスに触らずに操作を完結させる

### 入力

- Supersetのキーボードショートカット設定

### 出力

- マウス不要の高速ワークフロー

## 使うツール・ライブラリ

- Superset

## 前提知識

- gitの基本操作（branch、merge、worktreeの概念）
- CLIベースのAIエージェント（Claude Code、Codex等）の基本的な使い方
- macOS環境（現時点でmacOSのみサポート）
- Bun v1.0+、Git 2.20+、GitHub CLI、Caddyのインストール
