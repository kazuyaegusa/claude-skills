# スマートモデルルーティング

> タスクの複雑さに応じてopus/sonnet/haikuを自動選択し、品質とコストを最適化する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

全タスクにOpusを使うとコストが高く、全てHaikuでは品質が低下する。タスク特性に応じたモデル選択により、品質を保ちながらコストを最小化できる

## いつ使うのか

エージェントのコスト対効果を最適化したい時、または特定タスクで高精度が必要な時

## やり方

1. `model: opus`：深い推論が必要（アーキテクチャレビュー、セキュリティ監査、金融ロジック等）
2. `model: sonnet`：日常的なコーディング（実装、デバッグ、リファクタリング等）
3. `model: haiku`：クイックタスク（ドキュメント生成、検索、依存関係チェック等）
4. `model: inherit`：メイン会話と同じモデルを使用

### 入力

- タスクの複雑度評価

### 出力

- 適切なモデルが選択されたエージェント実行

## 使うツール・ライブラリ

- Claude opus/sonnet/haiku

## コード例

```
# 高精度が必要なエージェント
---
name: security-auditor
model: opus
---

# 日常的なコーディング
---
name: python-pro
model: sonnet
---

# クイックタスク
---
name: documentation-engineer
model: haiku
---
```

## 前提知識

- Claude Code CLIがインストールされている
- claude plugin機能の基本的な理解
- サブエージェントの概念（独立したコンテキストウィンドウ、ドメイン特化型プロンプト）
- Markdown/YAMLの基本文法
