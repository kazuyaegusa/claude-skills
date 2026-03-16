# エラーの永続化とアプローチ変更

> 失敗したアクションとその理由を progress.md に記録し、同じ方法を5回繰り返さず、試行回数とアプローチ変更を追跡する。

- 出典: https://github.com/OthmanAdi/planning-with-files
- 投稿者: OthmanAdi
- カテゴリ: agent-orchestration

## なぜ使うのか

AIエージェントはコンテキストが長くなると過去の失敗を忘れ、同じエラーを繰り返す。失敗履歴を明示的にログし、それを次の判断前に読み直すことで、異なるアプローチへの切り替えを促せる。

## いつ使うのか

試行錯誤が必要なタスク、不安定なAPIやツールとのやりとり、デバッグ作業。

## やり方

1. ツール実行が失敗した際、progress.md にエラー詳細、試行回数、失敗理由を記録
2. PreToolUse hookで progress.md も読み直し、過去の失敗を参照
3. 同じ方法で3回失敗したら、アプローチ変更を計画に記載
4. 新しい方法を試行し、結果を再度ログ

### 入力

- ツール実行のエラー結果
- 過去の試行履歴

### 出力

- progress.md（エラーログと試行回数）
- アプローチ変更の計画更新

## 前提知識

- Claude CodeまたはAgent Skills対応IDE（Cursor、Gemini CLI、Kiro、OpenClaw等）の基本操作
- markdownファイルの読み書き
- hookの概念（PreToolUse、PostToolUse、Stop）の理解
- bash または PowerShell の基本知識（hookスクリプトカスタマイズ時）
- gitの基本操作（セッションリカバリー機能利用時）
