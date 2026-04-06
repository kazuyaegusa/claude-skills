# Ralph Wiggum手法で自律ループ実行する

> 仕様ファイルを参照しながらClaude Codeを自動で繰り返し実行し、タスク完了まで自律的に動かす

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

人間が毎回プロンプトを入力しなくても、仕様が満たされるまでエージェントが試行錯誤を続けるため

## いつ使うのか

明確な仕様があり、試行錯誤が必要だが人間の監視コストを下げたい時

## やり方

1. PROMPT.md に達成すべき仕様を記述
2. ralph-orchestrator等のスクリプトでClaude Codeを繰り返し起動
3. タスク完了検出（"DONE"マーカー等）または上限回数で終了
4. レート制限・サーキットブレーカーで無限ループ防止

### 入力

- PROMPT.md（仕様定義）
- 終了条件（完了マーカー、最大試行回数）
- レート制限設定

### 出力

- 仕様を満たすコード・成果物
- 実行ログ・試行回数

## 使うツール・ライブラリ

- ralph-orchestrator
- tmux（ライブモニタリング）
- Bash

## コード例

```
#!/bin/bash
while [ $attempts -lt $max ]; do
  claude -p "$(cat PROMPT.md)"
  if grep -q "DONE" output.log; then break; fi
  attempts=$((attempts+1))
done
```

## 前提知識

- Claude Codeの基本的な使い方（CLI起動、プロンプト入力、ツール実行）
- markdown記法
- JSON記法（hooks.json等の設定ファイル）
- Bash/シェルスクリプトの基礎
- Git基本操作
- （Agent Teams利用時）マルチエージェントの概念理解

## 根拠

> "Ralph Orchestrator implements the simple but effective 'Ralph Wiggum' technique for autonomous task completion, continuously running an AI agent against a prompt file until the task is marked as complete or limits are reached."
