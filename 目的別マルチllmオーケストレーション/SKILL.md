# 目的別マルチLLMオーケストレーション

> 異なるLLMモデル（Opus 4.5、GPT 5.2 Medium、Gemini 3 Pro等）をタスクの性質に応じて自動的に使い分ける

- 出典: https://github.com/code-yeongyu/oh-my-openagent
- 投稿者: code-yeongyu
- カテゴリ: agent-orchestration

## なぜ使うのか

各モデルには得意分野がある（例：GPT 5.2は高度な設計・デバッグ、Gemini 3 ProはフロントエンドUI/UX、Grok Codeは高速コード探索）。適材適所で使い分けることで品質とコスト効率を最大化できる

## いつ使うのか

複数の専門領域にまたがるタスク、または特定領域で最高品質が求められるとき

## やり方

1. メインエージェント（Sisyphus: Opus 4.5 High）がタスクを分析
2. タスク内容に応じて専門エージェントに委譲（Oracle: 設計・デバッグ、Librarian: ドキュメント・ソース検索、Explore: 高速grep、Frontend Engineer: UI実装）
3. 各エージェントが並列実行し、結果をメインエージェントに返却
4. メインエージェントが統合・最終調整

### 入力

- タスク記述（プロンプト）
- 各エージェントのモデル・温度・権限設定
- プロジェクトのコンテキスト

### 出力

- 各専門エージェントからの成果物
- 統合された最終コード・ドキュメント

## 使うツール・ライブラリ

- OpenCode
- oh-my-opencode plugin
- 複数のLLM API（Anthropic、OpenAI、Google）

## コード例

```
// oh-my-opencode.json設定例
{
  "agents": {
    "sisyphus": { "model": "claude-opus-4.5", "temperature": 0.7 },
    "oracle": { "model": "gpt-5.2-medium", "temperature": 0.3 },
    "frontend-engineer": { "model": "gemini-3-pro", "temperature": 0.5 }
  }
}
```

## 前提知識

- OpenCode または Claude Code の基本理解
- LLMエージェント（Claude、GPT、Gemini等）の概念
- LSP（Language Server Protocol）の基本知識
- マルチエージェント・オーケストレーションの概念
