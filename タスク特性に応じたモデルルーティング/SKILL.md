# タスク特性に応じたモデルルーティング

> Subagent定義のmodelフィールドでopus/sonnet/haikuを指定し、タスクの複雑度に応じて適切なモデルを自動選択させる

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

深い推論が必要なセキュリティ監査にはopus、日常的なコーディングにはsonnet、ドキュメント生成にはhaikuを使い分けることで、コストと品質を最適化するため

## いつ使うのか

タスクの複雑度が明確で、コスト効率を重視する場合

## やり方

1. Subagent定義のfrontmatterに model: opus / sonnet / haiku を記載
2. security-auditor, architect-reviewer → opus
3. python-pro, backend-developer → sonnet
4. documentation-engineer, seo-specialist → haiku
5. model: inheritで親会話のモデルを継承することも可能

### 入力

- タスクの複雑度（深い推論/通常のコーディング/軽量タスク）

### 出力

- タスクに最適化されたモデルでの実行結果

## 使うツール・ライブラリ

- Claude Code Subagent system

## コード例

```
---
name: security-auditor
model: opus
tools: Read, Grep, Glob
---

You are a security auditor...
```

## 前提知識

- Claude Codeの基本的な使用経験
- Subagentの概念（独立したコンテキストウィンドウ、専門性、ツール権限）の理解
- GitHubからのリポジトリクローンまたはcurlでのファイル取得方法
- ~/.claude/agents/と.claude/agents/の違い（グローバル vs プロジェクト固有）

## 根拠

> opus: Deep reasoning — architecture reviews, security audits, financial logic

> sonnet: Everyday coding — writing, debugging, refactoring

> haiku: Quick tasks — docs, search, dependency checks
