# 専門エージェント分業パターン

> タスクの性質に応じて、事前定義された専門エージェント（Oracle: 設計・デバッグ、Librarian: ドキュメント検索、Frontend Engineer: UI実装等）に自動委譲する

- 出典: https://github.com/code-yeongyu/oh-my-openagent
- 投稿者: code-yeongyu
- カテゴリ: agent-orchestration

## なぜ使うのか

1つのモデルで全てをこなすより、各領域の専門家に任せた方が品質が高い。人間の開発チームと同じく、UI設計者・バックエンド開発者・デバッガーという役割分担が効率的

## いつ使うのか

フロントエンド・バックエンド・デバッグ等、異なる専門性が必要なタスク

## やり方

1. メインエージェント（Sisyphus）がタスクを分析
2. タスク内容をカテゴリ分類（visual: UI/UX、business-logic: バックエンド、debugging: デバッグ、documentation: ドキュメント検索）
3. カテゴリに応じた専門エージェントに委譲
4. 専門エージェントが作業を実行し、結果を返す
5. メインエージェントが結果を統合・レビュー

### 入力

- タスク記述
- カテゴリ分類ルール
- 各専門エージェントの設定

### 出力

- 専門エージェントからの高品質な成果物
- メインエージェントによる統合結果

## 使うツール・ライブラリ

- oh-my-opencode plugin（Categories設定）
- 各専門エージェント（Oracle, Librarian, Frontend Engineer等）

## コード例

```
// oh-my-opencode.json設定例
"categories": {
  "visual": {
    "pattern": "(UI|UX|frontend|styling|CSS)",
    "agent": "frontend-engineer"
  },
  "debugging": {
    "pattern": "(debug|fix|error|bug)",
    "agent": "oracle"
  }
}
```

## 前提知識

- OpenCode または Claude Code の基本理解
- LLMエージェント（Claude、GPT、Gemini等）の概念
- LSP（Language Server Protocol）の基本知識
- マルチエージェント・オーケストレーションの概念
