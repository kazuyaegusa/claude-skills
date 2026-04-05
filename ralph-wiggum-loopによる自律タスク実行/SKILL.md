# Ralph Wiggum Loopによる自律タスク実行

> タスク完了まで無人でClaude Codeを繰り返し実行し、仕様充足を自動検証する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

人間の介入なしに複雑なタスクを完遂させ、開発者の認知負荷を削減するため

## いつ使うのか

明確な仕様があり、完了条件を自動判定できるタスクを無人実行したいとき

## やり方

1. タスク仕様をファイル（TASK.md等）に記述
2. Bashスクリプトでループ開始
3. 各イテレーションでClaude Code実行 → 仕様充足チェック
4. 完了検出または制限到達で終了
5. レート制限・サーキットブレーカーで暴走防止
6. ralph-orchestrator, ralph-wiggum-bdd等の実装を参考に構築

### 入力

- タスク仕様（TASK.md）
- 完了判定ロジック（テスト・チェックリスト等）

### 出力

- 仕様を満たすコード・ドキュメント
- 実行ログ

## 使うツール・ライブラリ

- Bashスクリプト
- Claude Code CLI
- tmux（監視用）

## コード例

```
while ! task_complete; do
  claude-code < TASK.md
  run_tests && break
  sleep 30  # Rate limit
done
```

## 前提知識

- Claude Codeの基本操作（CLI使用・セッション管理）
- マークダウンフォーマットの理解
- Bash/Python/TypeScriptのいずれかでスクリプト作成経験
- Git・GitHub CLIの基礎知識
- LLMエージェントの基本概念（プロンプトエンジニアリング・コンテキスト管理）

## 根拠

> "Ralph Wiggum Loop - continuously running an AI agent against a prompt file until the task is marked as complete or limits are reached"
