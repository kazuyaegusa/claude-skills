# 3ファイルパターンによる永続化

> 全ての複雑タスクで task_plan.md（フェーズと進捗）、findings.md（調査結果）、progress.md（セッションログとテスト結果）の3ファイルを作成し、重要な情報をコンテキストではなくファイルに保存する。

- 出典: https://github.com/OthmanAdi/planning-with-files
- 投稿者: OthmanAdi
- カテゴリ: claude-code-workflow

## なぜ使うのか

AIエージェントのコンテキストウィンドウは有限かつ揮発性があり、リセットや長時間使用で記憶が失われる。ファイルシステムは永続的で容量制限がないため、「ディスク=長期記憶」として機能させることで、タスクの連続性を保証できる。

## いつ使うのか

3ステップ以上のタスク、調査タスク、プロジェクト作成、多数のツール呼び出しを伴うタスクの場合。単純な質問や1ファイル編集、クイック検索には不要。

## やり方

1. 複雑タスク開始時に task_plan.md（チェックボックス付きフェーズ管理）、findings.md（発見・調査メモ）、progress.md（実行ログ）を作成
2. 各ファイルをプロジェクトディレクトリに配置
3. hookを使って、ツール実行前に task_plan.md を読み直し、ツール実行後にステータス更新を促す
4. 2回のview/browser操作ごとに findings.md へ発見を保存（2-Action Rule）
5. エラー発生時は必ず progress.md にログし、試行回数とアプローチ変更を記録
6. タスク完了前にStop hookで全フェーズのチェックボックス完了を検証

### 入力

- 複雑なタスク記述
- プロジェクトディレクトリへの書き込み権限
- hook対応IDE（Claude Code、Cursor、Gemini CLI等）

### 出力

- task_plan.md（フェーズごとのチェックボックス付き計画）
- findings.md（調査結果の蓄積）
- progress.md（実行履歴とエラーログ）

## 使うツール・ライブラリ

- Claude Code Plugin
- Agent Skills仕様対応エージェント（Cursor、Gemini CLI、Kiro、OpenClaw等16プラットフォーム）

## 前提知識

- Claude CodeまたはAgent Skills対応IDE（Cursor、Gemini CLI、Kiro、OpenClaw等）の基本操作
- markdownファイルの読み書き
- hookの概念（PreToolUse、PostToolUse、Stop）の理解
- bash または PowerShell の基本知識（hookスクリプトカスタマイズ時）
- gitの基本操作（セッションリカバリー機能利用時）
