# スキルベースのワークフロー再利用

> TDD/セキュリティレビュー/E2Eテスト/継続学習などのワークフローをSKILL.mdファイルとして定義し、コマンドやエージェントから呼び出し可能にする

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

ワークフローをプロンプトで毎回説明すると一貫性が失われトークンを浪費する。YAMLフロントマター付きマークダウンでワークフローを定義することで再利用性・検索性・保守性を高められる

## いつ使うのか

繰り返し実行する開発プロセス（TDD/レビュー/デプロイ）を標準化したい、チーム全体で同じワークフローを共有したいとき

## やり方

1. skills/<skill-name>/SKILL.md を作成 2. YAMLフロントマターに name/description/tools/patterns を記述 3. マークダウン本文にワークフロー手順を記述（## When to Use, ## How, ## Success Criteria） 4. commands/*.md やagents/*.md から "Use the <skill-name> skill" で参照 5. /plugin install でスキルを自動ロード

### 入力

- SKILL.mdテンプレート
- ワークフロー定義（手順・ツール・成功基準）

### 出力

- ~/.claude/skills/<skill-name>/SKILL.md
- コマンド・エージェントからの参照可能なワークフロー

## 使うツール・ライブラリ

- Claude Code Skill tool
- マークダウン + YAMLフロントマター

## コード例

```
---
name: tdd-workflow
description: Test-driven development with 80%+ coverage
tools: ["Bash", "Edit", "Read"]
patterns: ["red-green-refactor"]
---

# TDD Workflow

## When to Use
- Adding new features
- Fixing bugs (write failing test first)

## How
1. Define interfaces first
2. Write failing tests (RED)
3. Implement minimal code (GREEN)
4. Refactor (IMPROVE)
5. Verify 80%+ coverage with /test-coverage

## Success Criteria
- All tests pass
- Coverage >= 80%
- No console.log in production code
```

## 前提知識

- Claude Code CLI v2.1.0以上のインストール
- Node.js環境（フックスクリプト実行用）
- Git（リポジトリクローン用）
- 対象言語の開発環境（TypeScript/Python/Go等）
- Claude Codeのサブスクリプション（トークン消費制限緩和のため推奨）
- AIエージェント・プロンプトエンジニアリングの基礎知識

## 根拠

> 「Won the Anthropic x Forum Ventures hackathon in Sep 2025 with @DRodriguezFX — built zenith.chat entirely using Claude Code.」

> 「Works across Claude Code, Codex, Cowork, and other AI agent harnesses.」

> 「Continuous Learning v2: The instinct-based learning system automatically learns your patterns」
