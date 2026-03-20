# 3ファイルパターンでタスク状態を永続化する

> 全ての複雑タスクをtask_plan.md（フェーズとチェックボックス）、findings.md（調査結果・発見）、progress.md（セッションログ・テスト結果）の3ファイルで管理する。

- 出典: https://github.com/OthmanAdi/planning-with-files
- 投稿者: OthmanAdi
- カテゴリ: claude-code-workflow

## なぜ使うのか

AIのコンテキストは揮発するが、ファイルは永続する。プランをディスクに書き出すことで、セッションをまたいで目標を維持し、エラー履歴を蓄積し、繰り返し失敗を回避できる。

## いつ使うのか

3ステップ以上のタスク、複数セッションにまたがる作業、コンテキストリセット（/clear）後の再開時

## やり方

1. タスク受領時、npx skills add OthmanAdi/planning-with-files でスキルをインストール
2. /planning-with-files:plan（または/plan）を実行
3. AIが自動で.planning/ディレクトリにtask_plan.md, findings.md, progress.mdを生成
4. task_plan.mdにフェーズごとのチェックボックス（[ ]）を記載、完了時に[x]で更新
5. findings.mdに調査結果・設計メモ・発見を追記（コンテキストに詰め込まない）
6. progress.mdにセッションログ・エラー・テスト結果を時系列で記録
7. フック（PreToolUse / PostToolUse / Stop）がプラン再読込・更新リマインダー・完了検証を自動実行

### 入力

- タスク記述（ユーザーが/planコマンド後に入力）
- プロジェクトディレクトリ（.planning/が作成される）

### 出力

- task_plan.md（フェーズ・チェックボックス・エラーログ）
- findings.md（調査結果・設計ドキュメント）
- progress.md（セッション履歴・テスト結果）

## 使うツール・ライブラリ

- npx skills（Agent Skills仕様のインストーラー）
- Claude Code / Cursor / Gemini CLI / Codex / GitHub Copilot等（16+プラットフォーム対応）
- hooks.json（Cursor / GitHub Copilot / Gemini CLI / Mastra Code等で自動読込）

## 前提知識

- Claude Code / Cursor / Gemini CLI / Codex等のAIエージェント環境
- Node.js（npx skills addコマンド実行用）
- bash（macOS/Linux）またはPowerShell（Windows）
- Agent Skills仕様の基本理解（SKILL.md, hooks.json等）
- Markdownフォーマットの理解（チェックボックス [ ] / [x] 記法）

## 根拠

> Re-read plan before major decisions (via PreToolUse hook) / Remind you to update status after file writes (via PostToolUse hook) / Verify completion before stopping (via Stop hook)
