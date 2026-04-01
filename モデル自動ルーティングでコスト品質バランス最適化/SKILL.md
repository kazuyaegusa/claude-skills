# モデル自動ルーティングでコスト・品質バランス最適化

> サブエージェントのfrontmatter `model:` フィールドでopus/sonnet/haikuを指定し、タスク複雑度に応じた最適モデルを自動選択する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

複雑なアーキテクチャレビューや金融ロジックにはopus（高品質・高コスト）、日常的なコーディングにはsonnet（バランス型）、ドキュメント生成やシンプル検索にはhaiku（高速・低コスト）を使い分けることで、コストパフォーマンスを最大化

## いつ使うのか

セキュリティ監査・アーキテクチャレビュー（opus）、通常の機能開発・デバッグ（sonnet）、ドキュメント生成・依存関係チェック（haiku）のように、タスクの重要度・複雑度でモデルを使い分けたい時

## やり方

1. サブエージェント.mdのfrontmatterで `model: opus`（深い推論）、`model: sonnet`（日常的コーディング）、`model: haiku`（高速タスク）のいずれかを指定
2. `model: inherit` でメイン会話と同じモデルを使用
3. サブエージェント呼び出し時、指定されたモデルが自動的に使われる

### 入力

- タスクの複雑度・重要度の評価
- コスト予算

### 出力

- タスクに最適なモデルで実行されるサブエージェント

## 使うツール・ライブラリ

- Claude opus/sonnet/haiku

## コード例

```
---
name: security-auditor
model: opus
---

---
name: python-pro
model: sonnet
---

---
name: documentation-engineer
model: haiku
---
```

## 前提知識

- Claude Codeがインストール・セットアップ済み
- サブエージェントの概念理解（独立したコンテキストウィンドウ、ドメイン特化プロンプト、ツール権限管理）
- 基本的なCLI操作（curl, chmod, git clone等）
- YAMLフロントマター形式の理解（サブエージェント定義ファイルの編集時）
- Claude Codeの /agents コマンドとサブエージェント呼び出し構文の理解
