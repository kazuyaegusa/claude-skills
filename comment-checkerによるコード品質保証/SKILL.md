# Comment Checkerによるコード品質保証

> LLMが過剰なコメントを追加しようとすると警告し、人間が書いたコードと区別がつかないレベルに保つ

- 出典: https://github.com/code-yeongyu/oh-my-openagent
- 投稿者: code-yeongyu
- カテゴリ: agent-orchestration

## なぜ使うのか

LLMは「説明的すぎるコメント」を大量に追加しがち。これはコードの可読性を下げ、保守性を悪化させる。人間が書いたコードレベルに保つべき

## いつ使うのか

プロダクションコード、コードレビューでコメント過多を避けたい場合

## やり方

1. Comment Checker hookが有効
2. エージェントがコメントを追加しようとすると検出
3. 必要性を正当化させるか、削除させる

### 入力

- LLM生成コード

### 出力

- 過剰コメントのないクリーンなコード

## 使うツール・ライブラリ

- oh-my-opencode Comment Checker hook

## 前提知識

- OpenCodeの基本的な使い方
- LLM API（Claude, GPT, Gemini等）のアクセス権
- npm/Node.js環境
- マルチエージェントオーケストレーションの概念理解
- LSP/ASTの基本的な理解（リファクタリング機能を使う場合）
