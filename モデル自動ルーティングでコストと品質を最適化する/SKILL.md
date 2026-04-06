# モデル自動ルーティングでコストと品質を最適化する

> subagentのYAML frontmatterに`model: opus/sonnet/haiku`を指定し、タスクの複雑度に応じて自動的に適切なClaudeモデルを割り当てる

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

深い推論が必要なアーキテクチャレビューやセキュリティ監査にはopusを使い、通常のコーディングにはsonnet、ドキュメント生成や簡単な検索にはhaikuを使うことで、品質を保ちながらAPI利用コストを削減できる

## いつ使うのか

subagentの新規作成時、既存エージェントのコスト最適化時、タスクの複雑度に応じたモデル選択を自動化したい時

## やり方

1. 深い推論が必要なsubagent（security-auditor, architect-reviewer等）に`model: opus`を設定
2. 通常の開発タスク（python-pro, backend-developer等）に`model: sonnet`を設定
3. 軽量タスク（documentation-engineer, seo-specialist等）に`model: haiku`を設定
4. メイン会話のモデルを継承させたい場合は`model: inherit`を使用

### 入力

- タスクの複雑度評価（深い推論 vs 通常コーディング vs 軽量作業）
- コスト予算

### 出力

- タスクに最適化されたモデル割り当て
- API利用コストの削減

## 使うツール・ライブラリ

- Claude Code subagent機能
- Claude API (opus, sonnet, haiku)

## コード例

```
# 深い推論が必要なセキュリティ監査
---
name: security-auditor
model: opus
---

# 通常の開発タスク
---
name: python-pro
model: sonnet
---

# 軽量なドキュメント生成
---
name: documentation-engineer
model: haiku
---
```

## 前提知識

- Claude Codeの基本的な使用経験
- subagentの概念理解（独立したコンテキストを持つ専門AIアシスタント）
- YAML frontmatterの基本構文
- コマンドラインツール（curl, git）の基本操作
- 対象言語・フレームワークの基礎知識（各subagent活用時）
