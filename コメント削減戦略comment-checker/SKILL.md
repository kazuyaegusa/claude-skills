# コメント削減戦略（Comment Checker）

> AI生成コードから過剰なコメントを自動削減し、人間が書いたコードと区別がつかないレベルに保つ

- 出典: https://github.com/code-yeongyu/oh-my-openagent
- 投稿者: code-yeongyu
- カテゴリ: agent-orchestration

## なぜ使うのか

LLMは過剰なコメントを生成しがちで、「これはAIが書いたな」とすぐ分かる。適切なコメント削減により、コード品質と可読性が向上し、AI生成と人間生成の区別がなくなる

## いつ使うのか

AI生成コードをプロダクションに投入する前、またはコードレビュー基準が厳しいとき

## やり方

1. エージェントがコードを生成
2. Comment Checkerが自動起動し、コメントを分析
3. 自明なコメント（例：`// increment i`）を検出
4. コメントの必要性を判定（複雑なロジック、非自明な仕様のみ残す）
5. 不要コメントを削除、または警告を発行
6. 必要な場合のみ、コメントの代わりにコードの自己文書化（変数名改善、関数分割）を提案

### 入力

- AI生成コード（コメント含む）

### 出力

- 適切なコメント密度に調整されたコード
- 必要に応じた自己文書化コード

## 使うツール・ライブラリ

- oh-my-opencode plugin（Comment Checker hook）

## コード例

```
// Before（AI生成）
function calculate(x: number, y: number): number {
  // Add x and y
  return x + y;
}

// After（Comment Checker適用後）
function calculate(x: number, y: number): number {
  return x + y;
}
```

## 前提知識

- OpenCode または Claude Code の基本理解
- LLMエージェント（Claude、GPT、Gemini等）の概念
- LSP（Language Server Protocol）の基本知識
- マルチエージェント・オーケストレーションの概念

## 根拠

> "When Sisyphus touches comments, he either justifies their existence or nukes them. He keeps your codebase clean."
