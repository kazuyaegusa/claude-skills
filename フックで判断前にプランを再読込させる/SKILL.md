# フックで判断前にプランを再読込させる

> PreToolUse（ツール実行直前）フックでAIにtask_plan.mdを再読込させ、現在のフェーズと目標を思い出させる。

- 出典: https://github.com/OthmanAdi/planning-with-files
- 投稿者: OthmanAdi
- カテゴリ: context-management

## なぜ使うのか

50回以上ツールを呼ぶと、コンテキストの前半（元の目標）が忘れられる。判断前に強制的にプランを読ませることで目標ドリフトを防ぐ（Manusの「Attention Manipulation」原則）。

## いつ使うのか

複数ツール呼び出しを伴うタスク（ファイル編集、コマンド実行、Web検索等）、目標を見失いやすい長期セッション

## やり方

1. .cursor/hooks.json（Cursor）、.github/hooks/planning-with-files.json（GitHub Copilot）、.gemini/settings.json（Gemini CLI）等にフック定義を追加
2. PreToolUseフックにスクリプト（bash: scripts/before-tool.sh / PowerShell: scripts/before-tool.ps1）を指定
3. スクリプトがtask_plan.mdの存在を確認し、AIに「プランを再読込してから判断せよ」と指示を挿入
4. AI側はツール実行前にプランを見直し、現在のフェーズに沿った判断をする

### 入力

- hooks.json（または対応IDE設定ファイル）
- before-tool.sh / before-tool.ps1（フックスクリプト）
- task_plan.md（再読込対象）

### 出力

- AIが判断前にプランを再確認した状態

## 使うツール・ライブラリ

- Cursor hooks.json
- GitHub Copilot hooks
- Gemini CLI settings.json
- Mastra Code hooks
- bash / PowerShell

## コード例

```
# before-tool.sh例
if [ -f ".planning/task_plan.md" ]; then
  echo "⚠️ Re-read task_plan.md before proceeding"
fi
```

## 前提知識

- Claude Code / Cursor / Gemini CLI / Codex等のAIエージェント環境
- Node.js（npx skills addコマンド実行用）
- bash（macOS/Linux）またはPowerShell（Windows）
- Agent Skills仕様の基本理解（SKILL.md, hooks.json等）
- Markdownフォーマットの理解（チェックボックス [ ] / [x] 記法）
