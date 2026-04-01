# ultraworkキーワード起動パターン

> プロンプトに「ultrawork」（または「ulw」）という1ワードを含めるだけで、全ての高度機能（並列エージェント、バックグラウンドタスク、深掘り探索、完遂強制）を自動起動する

- 出典: https://github.com/code-yeongyu/oh-my-openagent
- 投稿者: code-yeongyu
- カテゴリ: agent-orchestration

## なぜ使うのか

複雑な設定や機能理解を不要にし、ユーザーは「何を達成したいか」だけを伝えればよい。エージェント側が自動的に最適戦略を選択・実行する

## いつ使うのか

複雑なタスクで、設定を考える時間を節約したいとき。または、エージェントに最大限の自律性を与えたいとき

## やり方

1. プロンプトに「ultrawork」または「ulw」を含める
2. システムが自動検出し、フル機能モードを起動
3. エージェントがタスクを分析し、必要な専門エージェントを並列起動
4. バックグラウンドタスク実行、TODO継続強制、コメント削減等が自動適用される

### 入力

- ユーザープロンプト + 「ultrawork」または「ulw」キーワード

### 出力

- タスク完了まで自動駆動される実行プロセス
- 最終成果物（コード、ドキュメント等）

## 使うツール・ライブラリ

- oh-my-opencode plugin
- OpenCode

## コード例

```
// ユーザープロンプト例
"Refactor the authentication module to use OAuth2. ultrawork"
// または短縮形
"Add unit tests for all API endpoints. ulw"
```

## 前提知識

- OpenCode または Claude Code の基本理解
- LLMエージェント（Claude、GPT、Gemini等）の概念
- LSP（Language Server Protocol）の基本知識
- マルチエージェント・オーケストレーションの概念
