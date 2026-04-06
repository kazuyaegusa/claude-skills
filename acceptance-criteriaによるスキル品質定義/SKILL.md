# Acceptance Criteriaによるスキル品質定義

> 各スキルに `references/acceptance-criteria.md` を作成し、正しいimportパターン・認証パターン・async variantを明文化する

- 出典: https://github.com/microsoft/skills
- 投稿者: microsoft
- カテゴリ: agent-orchestration

## なぜ使うのか

LLMが生成したコードが「正しいパターン」に従っているかを自動評価可能にし、スキルの品質を定量的に測定する

## いつ使うのか

スキルを追加・更新した際に、LLM生成コードの品質を担保したい場合。CI/CDで自動的に品質を検証したい場合

## やり方

1. `.github/skills/<skill>/references/acceptance-criteria.md` に正解パターン・NG例を記載 2. `tests/scenarios/<skill>/scenarios.yaml` にテストケースを定義 3. `pnpm harness <skill> --mock` でスコアリング

### 入力

- 正しいコードパターン
- 避けるべきアンチパターン
- テストシナリオ

### 出力

- acceptance-criteria.md
- scenarios.yaml
- スコア（0-100）

## 使うツール・ライブラリ

- GitHub Copilot SDK
- test harness（pnpm harness）

## コード例

```
pnpm harness azure-ai-projects-py --mock --verbose
```

## 前提知識

- AI coding agent（GitHub Copilot、Claude Code、Copilot CLI等）の基本操作
- Markdown形式のドキュメント構造理解
- Symlink（シンボリックリンク）の概念
- YAML形式の設定ファイル
- GitHub Actionsの基本（日次更新ワークフローを活用する場合）
- MCP（Model Context Protocol）の概要（外部ツール統合を使う場合）

## 根拠

> 「Ralph Loop — An iterative code generation and improvement system that: 1. Generate code 2. Evaluate against acceptance criteria 3. Analyze failures 4. Re-generate with feedback 5. Report on quality improvements」（Testing Skills）

> 「Create acceptance criteria in `.github/skills/<skill>/references/acceptance-criteria.md` — Document correct/incorrect import patterns, authentication patterns, async variants」（Contributing）
