# モデル自動ルーティング設定

> エージェント定義の `model` フィールドで opus/sonnet/haiku を指定し、タスク特性に応じて自動的に最適モデルに振り分ける

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

深い推論が必要なタスク（セキュリティ監査、アーキテクチャレビュー）は opus、日常的なコーディングは sonnet、軽量タスク（ドキュメント生成、検索）は haiku と分けることで、品質を維持しながらコストを最小化できる

## いつ使うのか

コスト最適化と品質保証を両立させたい時、タスクの複雑度が明確に異なる複数エージェントを運用する時

## やり方

1. エージェント定義のフロントマターに `model: opus` / `sonnet` / `haiku` を追加
2. 深い推論が必要（例: security-auditor, architect-reviewer）→ opus
3. 日常コーディング（例: python-pro, backend-developer）→ sonnet
4. 軽量タスク（例: documentation-engineer, seo-specialist）→ haiku
5. 必要に応じて `model: inherit` で親会話のモデルを継承

### 入力

- タスクの推論深度要件
- コスト制約

### 出力

- model フィールド付きエージェント定義
- 自動的に最適モデルにルーティングされる実行環境

## 使うツール・ライブラリ

- Claude Code モデル選択API

## コード例

```
model: opus  # deep reasoning
model: sonnet  # everyday coding
model: haiku  # quick tasks
model: inherit  # use main conversation's model
```

## 前提知識

- Claude Codeの基本操作とサブエージェント概念の理解
- 開発タスクのカテゴリ分類（言語/インフラ/品質等）に関する知識
- Claude APIのモデル違い（opus/sonnet/haiku）の理解
- Markdownとフロントマター（YAML）の基礎知識
- Claude Code組み込みツール（Read, Write, Edit, Bash等）の把握

## 根拠

> 「Smart Model Routing: opus (Deep reasoning), sonnet (Everyday coding), haiku (Quick tasks)」
