# 全てのエラーをtask_plan.mdに記録し反復を防ぐ

> テスト失敗、ビルドエラー、API呼び出し失敗等を全てtask_plan.mdの「## Errors」セクションに記録し、試行回数と対応策を追記する。

- 出典: https://github.com/OthmanAdi/planning-with-files
- 投稿者: OthmanAdi
- カテゴリ: automation-pipeline

## なぜ使うのか

AIは過去のエラーを忘れ、同じ失敗を繰り返す。エラーログを永続化することで「この方法は3回試して失敗した→別アプローチへ」と判断できる（Never Repeat Failures原則）。

## いつ使うのか

テスト駆動開発、CI/CD実行、API統合、ビルドプロセス、認証フロー実装

## やり方

1. Bashツール等でコマンド実行→エラー発生
2. task_plan.mdの末尾に「## Errors」セクションがなければ追加
3. 「- [日時] エラー内容: 〜 / 試行回数: 1 / 対応策: 〜」を記載
4. 同じエラーが再発したら試行回数をインクリメント
5. 試行回数が3以上になったら、アプローチを変更（例: ツール変更、設定変更、手動介入）

### 入力

- エラーメッセージ（bash stderr, APIレスポンス等）
- task_plan.md

### 出力

- 更新されたtask_plan.md（エラー履歴・試行回数・対応策）

## 使うツール・ライブラリ

- Edit（task_plan.md更新）
- Bash / Exec等（エラー発生源）

## コード例

```
## Errors
- [2026-03-20 15:00] npm test失敗: TypeError: Cannot read property 'x' / 試行回数: 3 / 対応策: モックデータ追加→再試行
```

## 前提知識

- Claude Code / Cursor / Gemini CLI / Codex等のAIエージェント環境
- Node.js（npx skills addコマンド実行用）
- bash（macOS/Linux）またはPowerShell（Windows）
- Agent Skills仕様の基本理解（SKILL.md, hooks.json等）
- Markdownフォーマットの理解（チェックボックス [ ] / [x] 記法）
