# モデル選択による品質とコスト最適化

> 各サブエージェントのYAMLフロントマターに記載された`model`フィールド（opus, sonnet, haiku）に基づき、タスクの複雑度に応じて最適なClaudeモデルを自動選択する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

深い推論が必要なタスク（アーキテクチャレビュー、セキュリティ監査）にはOpusを、通常のコーディングにはSonnetを、軽量タスク（ドキュメント作成、依存関係チェック）にはHaikuを割り当てることで、品質とコストのバランスを最適化できる

## いつ使うのか

コスト削減が重要なプロジェクト、タスクごとに品質要求が明確に異なる場合、セキュリティやアーキテクチャなど高精度が求められる一部のタスクだけOpusを使いたい場合

## やり方

1. サブエージェント定義ファイルのYAMLフロントマター`model`フィールドを確認または編集
2. `model: opus`（深い推論）、`model: sonnet`（標準コーディング）、`model: haiku`（軽量タスク）、`model: inherit`（メイン会話のモデルを継承）のいずれかを指定
3. Claude Codeがサブエージェントを起動する際、自動的に指定モデルで実行される
4. 必要に応じてプロジェクト固有の要件に合わせてモデルを上書き

### 入力

- タスクの複雑度・重要度の評価
- コスト予算とパフォーマンス要件

### 出力

- タスクごとに最適化されたモデル選択設定
- コストとパフォーマンスのバランスが取れた実行環境

## 使うツール・ライブラリ

- Claude Code CLI（モデル自動選択機能）

## コード例

```
---
name: security-auditor
description: Security vulnerability expert
tools: Read, Grep, Glob
model: opus  # 深い推論が必要なのでOpus
---

---
name: documentation-engineer
description: Technical documentation specialist
tools: Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
model: haiku  # 軽量タスクなのでHaiku
---
```

## 前提知識

- Claude Code CLI がインストールされていること
- Claude Codeの基本操作（エージェント起動、ツール実行）の理解
- YAMLフロントマターの基本構文知識（エージェントカスタマイズ時）
- gitの基本操作（リポジトリクローン、ファイルコピー）
- 対象プロジェクトの技術スタックと開発フローの把握

## 根拠

> 「This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.」

> 「Smart Model Routing: Each subagent includes a model field that automatically routes it to the right Claude model — balancing quality and cost」

> 「Global Subagents: ~/.claude/agents/ - All projects - Lower precedence」「Project Subagents: .claude/agents/ - Current project only - Higher precedence」
