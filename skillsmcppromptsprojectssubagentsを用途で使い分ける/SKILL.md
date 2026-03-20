# Skills/MCP/Prompts/Projects/Subagentsを用途で使い分ける

> 5つのアプローチ（Skills/MCP/Prompts/Projects/Subagents）の使い分け基準を理解し、適切な手法を選択する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: agent-orchestration

## なぜ使うのか

それぞれ設計目的が異なるため、誤った手法を使うとトークン浪費・保守性低下・移植性欠如などの問題が起きる

## いつ使うのか

Claudeのカスタマイズ手法を選択する全ての場面

## やり方

1. 再利用可能な手順知識 → Skills
2. 外部データ/API統合 → MCP
3. 一度限りの指示・即座のコンテキスト → Prompts
4. ワークスペース内の永続的背景知識 → Projects
5. 独立したタスク実行（特定権限・独立ワークフロー） → Subagents
6. 「同じプロンプトを複数会話で繰り返し入力している」なら → Skillsに変換

### 入力

- 実現したいタスク・ワークフローの特性
- 再利用性・移植性・独立性の要件

### 出力

- 最適なアプローチの選択

## 使うツール・ライブラリ

- Skills
- MCP
- Prompts
- Projects
- Subagents

## 前提知識

- Claude.ai Pro/Max/Team/Enterpriseアカウント（Freeユーザーはスキル利用不可）
- YAML frontmatter、Markdownの基本知識
- （API利用の場合）Anthropic APIキーとAPI仕様の理解
- （Claude Code利用の場合）Claude Code CLIのインストール

## 根拠

> Skills employ a progressive disclosure architecture for efficiency: 1. Metadata loading (~100 tokens) 2. Full instructions (<5k tokens) 3. Bundled resources

> Use Skills when: Capabilities should be accessible to any Claude instance. They're portable expertise.

> ⚠️ Important: Skills can execute arbitrary code in Claude's environment. Only install skills from trusted sources.

> Q: How much do skills impact token usage? A: Skills are highly efficient thanks to progressive disclosure. Each skill uses only ~100 tokens during metadata scanning to determine relevance.

> obra/superpowers - Core skills library for Claude Code with 20+ battle-tested skills including TDD, debugging, and collaboration patterns
