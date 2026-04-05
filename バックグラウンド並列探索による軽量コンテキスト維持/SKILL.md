# バックグラウンド並列探索による軽量コンテキスト維持

> メインエージェントのコンテキストを軽量に保つため、ファイル探索やコードベース調査を安価で高速なモデルにバックグラウンドで並列実行させる

- 出典: https://github.com/code-yeongyu/oh-my-openagent
- 投稿者: code-yeongyu
- カテゴリ: agent-orchestration

## なぜ使うのか

メインエージェント自身が探索すると時間とコンテキストを消費する。並列タスクで地図を作成し、メインエージェントは結果のみ受け取ることで効率化

## いつ使うのか

大規模コードベースでのファイル探索、複数箇所の同時調査が必要な場合

## やり方

1. メインエージェントがタスクを分析
2. 探索系タスクを特定(ファイル検索、コードベーススキャン等)
3. 安価な高速モデル(Grok Code等)にバックグラウンドタスクとして投入
4. メインエージェントは並列実行中に他の作業を継続
5. 探索結果を統合して次のステップへ

### 入力

- 探索クエリ
- 対象コードベース

### 出力

- ファイルパス一覧
- 関連コード箇所
- 構造マップ

## 使うツール・ライブラリ

- oh-my-opencode の Background Tasks
- Explore agent (Grok Code)
- Contextual Grep

## コード例

```
// バックグラウンドタスク設定
"background_tasks": {
  "concurrency": {
    "openai": { "max_concurrent": 3 },
    "anthropic": { "max_concurrent": 2 }
  }
}
```

## 前提知識

- OpenCodeまたはClaude Code等のLLMエージェント環境の基本理解
- 複数LLMサブスクリプション(推奨: Claude Pro, ChatGPT Plus, Gemini Advanced)
- コマンドライン操作の基礎知識
- JSONまたはJSONC設定ファイルの編集スキル
- エージェント型開発の概念(プロンプトエンジニアリング、コンテキスト管理等)
