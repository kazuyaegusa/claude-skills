# 複数モデルの目的別オーケストレーション

> タスクの性質に応じて最適なLLMモデルを自動選択・実行し、コスト・速度・品質を最適化

- 出典: https://github.com/code-yeongyu/oh-my-openagent
- 投稿者: code-yeongyu
- カテゴリ: agent-orchestration

## なぜ使うのか

全タスクを最高性能モデルで実行するとコスト高、全て安価モデルでは品質低下。タスク別に最適モデルを使い分ければ両立可能

## いつ使うのか

複数LLMサブスクリプションを持ち、コストと品質を最適化したい場合

## やり方

1. タスクをカテゴリ分類(visual, business-logic, exploration等)
2. 各カテゴリに最適モデルを事前定義
3. タスク実行時に自動的に該当モデルを選択
4. 高度な判断はOpus/GPT-5、探索はGrok、UIはGeminiなど使い分け
5. 結果を統合

### 入力

- タスク定義
- 利用可能モデル一覧

### 出力

- 最適化されたタスク実行結果

## 使うツール・ライブラリ

- oh-my-opencode の Categories feature
- 複数LLM API

## コード例

```
// カテゴリ別モデル設定
"categories": {
  "visual": { "model": "gemini-3-pro" },
  "business-logic": { "model": "opus-4.5" },
  "exploration": { "model": "grok-code" }
}
```

## 前提知識

- OpenCodeまたはClaude Code等のLLMエージェント環境の基本理解
- 複数LLMサブスクリプション(推奨: Claude Pro, ChatGPT Plus, Gemini Advanced)
- コマンドライン操作の基礎知識
- JSONまたはJSONC設定ファイルの編集スキル
- エージェント型開発の概念(プロンプトエンジニアリング、コンテキスト管理等)
