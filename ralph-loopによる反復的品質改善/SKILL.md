# Ralph Loopによる反復的品質改善

> Generate → Evaluate → Analyze → Re-generate のサイクルを閾値到達まで繰り返し、LLM生成コードの品質を段階的に向上させる

- 出典: https://github.com/microsoft/skills
- 投稿者: microsoft
- カテゴリ: agent-orchestration

## なぜ使うのか

1回の生成では不十分な場合でも、フィードバックループでacceptance criteriaを満たすコードに収束させる

## いつ使うのか

スキルの品質が低い場合や、新規スキル追加時に段階的に改善したい場合。CI/CDでの自動品質向上

## やり方

1. スキル/シナリオに基づいてコード生成 2. acceptance criteriaで評価（0-100点） 3. 失敗箇所をLLM向けフィードバックに変換 4. フィードバック付きで再生成 5. 閾値（例: 85点）到達まで繰り返し

### 入力

- 初期生成コード
- acceptance criteria
- max_iterations
- threshold

### 出力

- 改善されたコード
- iteration履歴
- 最終スコア

## 使うツール・ライブラリ

- GitHub Copilot SDK
- test harness

## コード例

```
pnpm harness azure-ai-projects-py --ralph --mock --max-iterations 5 --threshold 85
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
