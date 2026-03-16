# セッションリカバリー機能

> コンテキストが埋まり /clear を実行した際、~/.claude/projects/ から前回セッションデータを自動検出し、計画ファイル更新後の会話を抽出してキャッチアップレポートを生成する。

- 出典: https://github.com/OthmanAdi/planning-with-files
- 投稿者: OthmanAdi
- カテゴリ: claude-code-workflow

## なぜ使うのか

AIエージェントの会話がトークン上限に達してリセットされると、それまでの作業履歴が失われる。この機能により、前回セッションで何が話されたかを自動復元し、ユーザーが手動で要約しなくても継続可能にする。

## いつ使うのか

長期プロジェクトで複数セッションにわたる作業を行う場合、コンテキストリセット後も作業を継続したい場合。

## やり方

1. /clear 実行後、スキルが ~/.claude/projects/ 内の前回セッションデータをチェック
2. 計画ファイル（task_plan.md等）の最終更新タイムスタンプを取得
3. その時刻以降の会話ログを抽出（失われた可能性のあるコンテキスト）
4. キャッチアップレポートとして表示し、ユーザーが同期可能にする
5. 自動コンパクトを無効化（autoCompact: false）することで、コンテキスト最大活用後にクリアするのが推奨

### 入力

- ~/.claude/projects/ 内の前回セッションデータ
- 計画ファイルの最終更新タイムスタンプ

### 出力

- キャッチアップレポート（前回セッションの失われたコンテキスト要約）

## 使うツール・ライブラリ

- Claude Code sessionデータ構造

## 前提知識

- Claude CodeまたはAgent Skills対応IDE（Cursor、Gemini CLI、Kiro、OpenClaw等）の基本操作
- markdownファイルの読み書き
- hookの概念（PreToolUse、PostToolUse、Stop）の理解
- bash または PowerShell の基本知識（hookスクリプトカスタマイズ時）
- gitの基本操作（セッションリカバリー機能利用時）

## 根拠

> When your context fills up and you run /clear, this skill automatically recovers your previous session. How it works: 1. Checks for previous session data in ~/.claude/projects/ 2. Finds when planning files were last updated 3. Extracts conversation that happened after (potentially lost context) 4. Shows a catchup report so you can sync
