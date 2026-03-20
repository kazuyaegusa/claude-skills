# Stopフックで完了検証を強制する

> セッション終了時（/stop, /exit）にStopフックがtask_plan.mdの全チェックボックスを確認し、未完了があれば警告する。

- 出典: https://github.com/OthmanAdi/planning-with-files
- 投稿者: OthmanAdi
- カテゴリ: automation-pipeline

## なぜ使うのか

AIは「だいたいできた」で停止しがちだが、ユーザーは全フェーズ完了を期待している。完了検証を自動化することで、抜け漏れを防ぐ（Completion Verification原則）。

## いつ使うのか

複数フェーズのタスク、納品前の最終確認、CI/CDパイプライン完走確認

## やり方

1. hooks.jsonのStopフックにcheck-complete.sh（bash）またはcheck-complete.ps1（PowerShell）を指定
2. スクリプトがtask_plan.mdを読み、[ ]（未完了）の数をカウント
3. 未完了がある場合、「⚠️ X tasks incomplete. Review task_plan.md」と警告
4. AIが「まだ完了していないフェーズがあります。続けますか？」とユーザーに確認

### 入力

- task_plan.md（チェックボックス状態）
- hooks.json（Stop設定）

### 出力

- 完了検証結果（警告または承認）

## 使うツール・ライブラリ

- bash / PowerShell
- grep / Select-String（チェックボックス検索）

## コード例

```
# check-complete.sh例
incomplete=$(grep -c '\[ \]' .planning/task_plan.md)
if [ $incomplete -gt 0 ]; then
  echo "⚠️ $incomplete tasks incomplete"
fi
```

## 前提知識

- Claude Code / Cursor / Gemini CLI / Codex等のAIエージェント環境
- Node.js（npx skills addコマンド実行用）
- bash（macOS/Linux）またはPowerShell（Windows）
- Agent Skills仕様の基本理解（SKILL.md, hooks.json等）
- Markdownフォーマットの理解（チェックボックス [ ] / [x] 記法）
