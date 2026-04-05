# Todoエンフォーサーによるタスク継続強制

> エージェントがタスクを途中で止めようとした際、TODOリストに未完了項目があれば自動的に継続を強制する仕組み

- 出典: https://github.com/code-yeongyu/oh-my-openagent
- 投稿者: code-yeongyu
- カテゴリ: agent-orchestration

## なぜ使うのか

LLMエージェントは長時間タスクで「疲れて」途中で止まる傾向がある。神話のSisyphusのように、石(タスク)を転がし続けることを強制し完遂させるため

## いつ使うのか

長時間かかる実装タスクや、複数ステップの自動化タスク

## やり方

1. タスク開始時にTODOリストを作成
2. エージェントが各ステップ完了時にTODOを更新
3. エージェントが終了を宣言した際、未完了TODOをチェック
4. 未完了があれば「bouldering mode」で継続を指示
5. 全TODO完了まで繰り返し

### 入力

- 初期タスク定義
- TODOリスト

### 出力

- 完遂されたタスク
- 完了済みTODOリスト

## 使うツール・ライブラリ

- oh-my-opencode の Todo Enforcer hook

## コード例

```
// フック設定で有効化
"hooks": {
  "todo_enforcer": { "enabled": true }
}
```

## 前提知識

- OpenCodeまたはClaude Code等のLLMエージェント環境の基本理解
- 複数LLMサブスクリプション(推奨: Claude Pro, ChatGPT Plus, Gemini Advanced)
- コマンドライン操作の基礎知識
- JSONまたはJSONC設定ファイルの編集スキル
- エージェント型開発の概念(プロンプトエンジニアリング、コンテキスト管理等)
