# モデル自動ルーティング設定

> 各サブエージェントのfrontmatterに `model: opus/sonnet/haiku` を記述し、タスクの複雑度に応じてClaudeモデルを自動選択させる

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

深い推論が必要なアーキテクチャレビューやセキュリティ監査はOpusに、日常的なコーディングはSonnetに、ドキュメント生成やシンプルな検索はHaikuに振り分けることで、品質とコストを最適化するため

## いつ使うのか

新規サブエージェントを作成する時、または既存エージェントのコスト効率を最適化したい時

## やり方

1. エージェント定義ファイルのYAML frontmatterに `model:` フィールドを追加
2. 深い推論が必要(アーキテクチャレビュー、セキュリティ監査、金融ロジック)なら `model: opus`
3. 日常的なコーディング(書く、デバッグ、リファクタ)なら `model: sonnet`
4. クイックタスク(ドキュメント、検索、依存関係チェック)なら `model: haiku`
5. メイン会話のモデルを継承したい場合は `model: inherit`
6. Claude Codeがエージェント起動時にこのフィールドを読み取り、自動的に適切なモデルへルーティング

### 入力

- エージェントの責務と必要な推論深度
- コスト制約(Opus > Sonnet > Haiku)

### 出力

- frontmatter内の `model:` フィールド
- 実行時の自動モデル選択

## 使うツール・ライブラリ

- Claude Code model routing

## コード例

```
---
name: security-auditor
description: Security vulnerability expert
tools: Read, Grep, Glob
model: opus
---

You are a security auditor...
```

## 前提知識

- Claude Code CLIの基本操作(/agents コマンド、サブエージェント概念)
- Markdownの読み書き(frontmatterとYAML構文)
- Bashコマンド(curl, chmod)の基礎知識
- プロジェクトとグローバルの設定ファイル配置の違い(~/.config vs .config的な概念)
- 開発ライフサイクル(開発→テスト→デプロイ→運用)の理解

## 根拠

> 「This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.」

> 「Tool Assignment Philosophy: Each subagent's tools field specifies Claude Code built-in tools, optimized for their role」

> 「Smart Model Routing: Each subagent includes a model field that automatically routes it to the right Claude model — balancing quality and cost」

> 「Project Subagents: .claude/agents/ Current project only Higher precedence, Global Subagents: ~/.claude/agents/ All projects Lower precedence」

> 「4 installation options: As Claude Code Plugin, Manual Installation, Interactive Installer, Standalone Installer, Agent Installer」
