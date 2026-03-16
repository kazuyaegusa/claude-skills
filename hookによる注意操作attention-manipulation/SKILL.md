# Hookによる注意操作（Attention Manipulation）

> PreToolUse hookでツール実行前に task_plan.md を読み直し、PostToolUse hookでファイル書き込み後に進捗更新を促し、Stop hookで完了前に全フェーズ完了を検証する。

- 出典: https://github.com/OthmanAdi/planning-with-files
- 投稿者: OthmanAdi
- カテゴリ: claude-code-workflow

## なぜ使うのか

AIエージェントは長時間の会話で元の目標を忘れ、ゴールドリフトやエラーの繰り返しが発生する。計画ファイルを定期的に読み直すことで、意思決定時に常に最新の計画と過去の失敗を参照し、同じ過ちを避けられる。

## いつ使うのか

長期タスクで目標を見失わせたくない場合、同じエラーを繰り返させたくない場合、タスク完了の抜け漏れを防ぎたい場合。

## やり方

1. IDE（例: Cursor）の hooks.json に PreToolUse、PostToolUse、Stop hookを定義
2. PreToolUse: 主要な判断前にスクリプトで task_plan.md を読み込み、エージェントのコンテキストに再注入
3. PostToolUse: ファイル書き込み後にリマインダーを表示し、progress.md 更新を促す
4. Stop: タスク終了時に check-complete スクリプトで task_plan.md の全チェックボックスが完了しているか検証
5. 各hookスクリプトはbash版とPowerShell版を用意し、OS判定で切り替え

### 入力

- hook対応IDE（Cursor、Claude Code、GitHub Copilot、Mastra Code等）
- task_plan.md の存在
- hookスクリプト（init-session.sh/ps1、check-complete.sh/ps1）

### 出力

- エージェントコンテキストへの計画再注入
- 進捗更新の自動リマインダー
- 完了前の検証フィードバック

## 使うツール・ライブラリ

- bash / PowerShell
- IDE hook system (hooks.json)

## 前提知識

- Claude CodeまたはAgent Skills対応IDE（Cursor、Gemini CLI、Kiro、OpenClaw等）の基本操作
- markdownファイルの読み書き
- hookの概念（PreToolUse、PostToolUse、Stop）の理解
- bash または PowerShell の基本知識（hookスクリプトカスタマイズ時）
- gitの基本操作（セッションリカバリー機能利用時）
