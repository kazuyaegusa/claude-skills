# TODO継続強制メカニズム

> エージェントがTODOリストを完了せずに停止した場合、システムが自動的に「bouldering mode」（boulder = 巨石を転がし続ける）に強制復帰させ、タスク完遂まで駆動し続ける

- 出典: https://github.com/code-yeongyu/oh-my-openagent
- 投稿者: code-yeongyu
- カテゴリ: agent-orchestration

## なぜ使うのか

LLMエージェントは複雑なタスクで途中停止しがちで、ユーザーが何度も「続けて」と促す必要がある。自動継続により、人間の介入なしにタスク完遂率が劇的に向上する

## いつ使うのか

多段階タスク、または過去にエージェントが途中で止まった経験があるとき

## やり方

1. エージェントがTODOリストを作成
2. 各TODOの完了状態を追跡
3. エージェントが応答を終了しようとした際、未完了TODOがあればチェック
4. 未完了の場合、「TODO未完了検出。継続します」というメッセージとともに自動的に次のTODOを実行
5. 全TODO完了まで繰り返す

### 入力

- TODOリスト（エージェントが自動生成）
- 各TODOの完了状態

### 出力

- 全TODO完了までの継続実行
- 完了した全タスクの成果物

## 使うツール・ライブラリ

- oh-my-opencode plugin（Todo Continuation Enforcer）

## コード例

```
// 内部動作（ユーザーからは見えない）
if (remainingTodos.length > 0 && agent.isAboutToStop()) {
  agent.inject("You still have incomplete TODOs. Continue bouldering.");
  agent.resume();
}
```

## 前提知識

- OpenCode または Claude Code の基本理解
- LLMエージェント（Claude、GPT、Gemini等）の概念
- LSP（Language Server Protocol）の基本知識
- マルチエージェント・オーケストレーションの概念
