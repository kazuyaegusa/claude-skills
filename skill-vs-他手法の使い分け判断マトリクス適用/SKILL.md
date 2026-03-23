# Skill vs 他手法の使い分け判断マトリクス適用

> Skills、Prompts、Projects、Subagents、MCPそれぞれの特性を理解し、タスクに最適な手法を選択する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: agent-orchestration

## なぜ使うのか

各手法には明確な用途の違いがあり、誤用するとトークン浪費や管理コスト増大を招く。適切な使い分けで効率とメンテナンス性が劇的に向上する

## いつ使うのか

新しいワークフローやツールを導入する際、どの形式で実装すべきか迷った時

## やり方

1. 「同じプロンプトを繰り返し入力しているか？」→ Yes ならSkills
2. 「一回限りの指示か？」→ Prompts
3. 「ワークスペース全体で常に参照すべき知識か？」→ Projects
4. 「独立したエージェントとして権限分離が必要か？」→ Subagents
5. 「外部データソース・API統合が主目的か？」→ MCP
6. Skillsは「どのClaudeインスタンスでも使える専門知識」、Subagentsは「特定用途の独立エージェント」、MCPは「外部連携」と整理する

### 入力

- タスクの性質、再利用頻度、外部連携の有無

### 出力

- 最適な実装手法の選択

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（Free tierはSkills非対応）
- Claude Code CLIまたはClaude.ai、Claude APIへのアクセス
- YAMLとMarkdownの基本知識
- gitによるバージョン管理の基礎（チーム配布する場合）
- Skillsが実行するスクリプト言語（Python、JavaScript等）の基礎知識（カスタムSkills作成時）

## 根拠

> Skills employ a progressive disclosure architecture for efficiency: 1. Metadata loading (~100 tokens): Claude scans available Skills to identify relevant matches 2. Full instructions (<5k tokens): Load when Claude determines the Skill applies 3. Bundled resources: Files and executable code load only as needed

> Key insight: If you find yourself typing the same prompt repeatedly across multiple conversations, it's time to create a Skill.

> Use Skills when: Capabilities should be accessible to any Claude instance. They're portable expertise.

> SKILL.md with frontmatter: ---
name: my-skill
description: Brief description for skill discovery (keep concise)
---
# Detailed Instructions

> ⚠️ Important: Skills can execute arbitrary code in Claude's environment. Only install skills from trusted sources.
