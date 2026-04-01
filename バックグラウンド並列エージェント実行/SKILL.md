# バックグラウンド並列エージェント実行

> メインエージェントのコンテキストを節約するため、ファイル探索やドキュメント検索等の補助タスクをバックグラウンドで並列実行する高速・低コストなエージェントに委譲する

- 出典: https://github.com/code-yeongyu/oh-my-openagent
- 投稿者: code-yeongyu
- カテゴリ: agent-orchestration

## なぜ使うのか

メインエージェント（高コスト・高性能モデル）がファイル探索に時間を使うとコンテキストが浪費される。並列実行により、メインエージェントは本質的な思考・設計に集中でき、全体の速度とコスト効率が向上する

## いつ使うのか

大規模コードベースの探索、複数ファイルの横断検索、外部ドキュメント参照が必要なとき

## やり方

1. メインエージェント（Sisyphus）がタスクを受け取る
2. 補助タスク（ファイル検索、コードベース探索、ドキュメント取得）を識別
3. 高速・低コストモデル（Explore: Grok Code等）をバックグラウンドで並列起動
4. バックグラウンドエージェントが並列実行し、結果を返す
5. メインエージェントが結果を受け取り、本質的な作業に集中

### 入力

- 補助タスク（検索クエリ、探索範囲等）
- バックグラウンドエージェント設定

### 出力

- 探索結果、ファイル一覧、ドキュメント抜粋等
- メインエージェントへのコンテキスト軽量化

## 使うツール・ライブラリ

- oh-my-opencode plugin（Background Tasks）
- Explore agent（Grok Code）
- Librarian agent（Sonnet 4.5）

## コード例

```
// 設定例（oh-my-opencode.json）
"backgroundTasks": {
  "concurrency": {
    "anthropic": 3,
    "openai": 2,
    "google": 2
  }
}
```

## 前提知識

- OpenCode または Claude Code の基本理解
- LLMエージェント（Claude、GPT、Gemini等）の概念
- LSP（Language Server Protocol）の基本知識
- マルチエージェント・オーケストレーションの概念
