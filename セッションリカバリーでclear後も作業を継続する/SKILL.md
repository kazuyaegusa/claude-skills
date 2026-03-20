# セッションリカバリーで/clear後も作業を継続する

> /clearでコンテキストをリセットした後、前回の.planning/ファイルと~/.claude/projects/セッションデータから会話履歴を復元する。

- 出典: https://github.com/OthmanAdi/planning-with-files
- 投稿者: OthmanAdi
- カテゴリ: claude-code-workflow

## なぜ使うのか

コンテキストが200kトークンで埋まった時、/clearすると会話履歴が消える。しかしプランファイルは残っているため、「最終更新以降の会話」を抽出して引き継げば、作業を継続できる。

## いつ使うのか

長期タスク（数時間～数日）、コンテキスト上限到達時、複数セッションにまたがる開発

## やり方

1. /clearを実行（コンテキストリセット）
2. 新しいセッション開始時、スキルが~/.claude/projects/から前回のセッションデータを検索
3. .planning/task_plan.md等の最終更新時刻を取得
4. その時刻以降の会話を抽出（potentially lost context）
5. 「前回はここまで進んでいました」とキャッチアップレポートを表示
6. ユーザーが確認後、続きを実行

### 入力

- ~/.claude/projects/（セッション履歴）
- .planning/task_plan.md等（最終更新時刻）

### 出力

- キャッチアップレポート（前回の進捗・未完了タスク）

## 使うツール・ライブラリ

- Claude Code session storage
- Read（ファイル読込）
- Bash（ファイルタイムスタンプ取得）

## コード例

```
# キャッチアップ例
前回セッション（2026-03-20 14:00）:
- task_plan.md最終更新: 14:30
- 完了フェーズ: 1/3
- 未完了: Phase 2, 3
続きから開始します。
```

## 前提知識

- Claude Code / Cursor / Gemini CLI / Codex等のAIエージェント環境
- Node.js（npx skills addコマンド実行用）
- bash（macOS/Linux）またはPowerShell（Windows）
- Agent Skills仕様の基本理解（SKILL.md, hooks.json等）
- Markdownフォーマットの理解（チェックボックス [ ] / [x] 記法）
