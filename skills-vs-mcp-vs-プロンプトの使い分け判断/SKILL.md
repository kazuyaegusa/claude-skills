# Skills vs MCP vs プロンプトの使い分け判断

> タスクの性質に応じて、Skill・MCP・システムプロンプト・サブエージェントのどれを使うべきか判断する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: agent-orchestration

## なぜ使うのか

同じ機能を実現できても、ポータビリティ・トークン効率・保守性・再利用性が大きく異なる。適切な選択をしないと運用コストが増大する

## いつ使うのか

新しい機能を追加する際、または既存のプロンプトやワークフローをリファクタリングする際

## やり方

1. 「再利用可能な手続き的知識」→ Skills
2. 「1回限りの指示・即座のコンテキスト」→ Prompts
3. 「会話をまたいで持続する背景知識」→ Projects
4. 「独立したタスク実行・権限制限」→ Subagents
5. 「外部データソース・API接続」→ MCP
6. 判断基準: 同じプロンプトを複数会話で繰り返すならSkill化。外部データが必要ならMCP。

### 入力

- 実現したい機能の性質（手続き/データ統合/背景知識/独立実行）
- 再利用頻度
- ポータビリティ要件

### 出力

- 最適なアプローチの選択（Skill/MCP/Prompt/Subagent/Project）

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（無料tierはSkills非対応）
- Claude.ai Web、Claude Code CLI、またはClaude APIへのアクセス
- YAMLフロントマターの基本的な理解
- （カスタムSkill作成時）Pythonやシェルスクリプトの基礎知識

## 根拠

> Skills employ a progressive disclosure architecture for efficiency: 1. Metadata loading (~100 tokens): Claude scans available Skills to identify relevant matches 2. Full instructions (<5k tokens): Load when Claude determines the Skill applies 3. Bundled resources: Files and executable code load only as needed

> Claude Code CLI: /plugin marketplace add anthropics/skills OR /plugin add /path/to/skill-directory

> Skills API accessible via /v1/skills endpoint

> Skills vs MCP: Skills = Task-specific expertise and workflows, MCP = External data/API integration. Use Together: Skills can create MCP servers!

> Security: Skills can execute arbitrary code in Claude's environment. Only install skills from trusted sources.
