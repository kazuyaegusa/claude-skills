# 専門特化エージェントチームの編成

> メインエージェント(Sisyphus)の下に、Oracle(デザイン/デバッグ)、Frontend Engineer(UI実装)、Librarian(ドキュメント検索)、Explore(コードベース探索)など役割別サブエージェントを配置

- 出典: https://github.com/code-yeongyu/oh-my-openagent
- 投稿者: code-yeongyu
- カテゴリ: agent-orchestration

## なぜ使うのか

単一エージェントで全てを処理するとコンテキストが肥大化し、各領域の精度が下がる。モデルごとの得意分野を活かし、並列実行で速度と品質を両立するため

## いつ使うのか

複数領域にまたがるタスク、または単一エージェントでコンテキスト超過が予想される場合

## やり方

1. タスク種別を分析(UI、ロジック、調査、リファクタリング等)
2. 各種別に最適なモデルを割り当て(例: Gemini 3 Pro → Frontend、GPT 5.2 → デバッグ)
3. メインエージェントが判断してサブエージェントに委譲
4. サブエージェントの結果をメインエージェントが統合

### 入力

- タスク要件
- 使用可能なLLMモデル一覧
- 各モデルの特性(得意領域、コスト、速度)

### 出力

- エージェント構成定義(JSON/YAML)
- 各エージェントの役割とモデル割り当て

## 使うツール・ライブラリ

- OpenCode
- oh-my-opencode plugin
- 複数LLM API(Claude/GPT/Gemini)

## コード例

```
// opencode.jsonでの設定例
"agents": {
  "sisyphus": { "model": "opus-4.5-high" },
  "oracle": { "model": "gpt-5.2-medium" },
  "frontend": { "model": "gemini-3-pro" },
  "librarian": { "model": "claude-sonnet-4.5" }
}
```

## 前提知識

- OpenCodeまたはClaude Code等のLLMエージェント環境の基本理解
- 複数LLMサブスクリプション(推奨: Claude Pro, ChatGPT Plus, Gemini Advanced)
- コマンドライン操作の基礎知識
- JSONまたはJSONC設定ファイルの編集スキル
- エージェント型開発の概念(プロンプトエンジニアリング、コンテキスト管理等)

## 根拠

> 「Sisyphus (Opus 4.5 High), Oracle (GPT 5.2 Medium), Frontend UI/UX Engineer (Gemini 3 Pro), Librarian (Claude Sonnet 4.5), Explore (Grok Code)」
