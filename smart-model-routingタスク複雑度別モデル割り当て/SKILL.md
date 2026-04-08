# Smart Model Routing（タスク複雑度別モデル割り当て）

> agentのタスク特性に応じてopus（深い推論）/sonnet（通常コーディング）/haiku（軽量タスク）を使い分ける

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

全てopusで実行するとコストが爆発し、全てhaikuでは品質が低下する。セキュリティ監査はopus、日常的なコーディングはsonnet、ドキュメント生成はhaikuと割り当てることで、品質とコスト効率を両立できる

## いつ使うのか

コスト最適化しつつ品質を担保したいとき

## やり方

1. agentの役割を分析（深い推論が必要か／定型作業か）
2. opus: セキュリティ監査、アーキテクチャレビュー、金融ロジック等
3. sonnet: 通常の実装・デバッグ・リファクタリング
4. haiku: ドキュメント生成、依存関係チェック、検索タスク
5. frontmatterの`model`フィールドに指定
6. `model: inherit`で親会話のモデルを継承も可能

### 入力

- agentが実行するタスクの種類
- 必要な推論の深さ

### 出力

- 最適なモデルが割り当てられたagent定義

## 使うツール・ライブラリ

- Claude API（opus/sonnet/haiku）

## コード例

```
# セキュリティ監査は深い推論が必要
---
name: security-auditor
model: opus
---

# 通常のバックエンド開発
---
name: backend-developer
model: sonnet
---

# ドキュメント生成は軽量でOK
---
name: documentation-engineer
model: haiku
---
```

## 前提知識

- Claude Codeの基本操作（subagent作成・呼び出し）
- YAML frontmatterの理解
- Claude APIのモデル種別（opus/sonnet/haiku）の特性
- ~/.claude/agents/ と .claude/agents/ の違い（global/project-specific）
- 最小権限の原則（Principle of Least Privilege）

## 根拠

> Standard template with YAML frontmatter: name, description, tools, model

> Smart Model Routing: opus (deep reasoning), sonnet (everyday coding), haiku (quick tasks)
