# Skills vs Prompts/Projects/Subagents/MCPを使い分ける

> タスクの性質に応じて、Skills、システムプロンプト、Projects、Subagents、MCPを適切に選択する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: agent-orchestration

## なぜ使うのか

各ツールには明確な役割分担がある。誤った選択はトークン浪費や機能不足を招く。Skillsは「繰り返し使う手順知識」に最適。

## いつ使うのか

新しいワークフローを設計する時、既存のシステムプロンプトをSkills化すべきか判断する時

## やり方

1. 繰り返し使う手順 → Skills 2. 1回限りの指示・即座のコンテキスト → Prompts 3. ワークスペース内の永続的な背景知識 → Projects 4. 独立したタスク実行・制限されたツールアクセス → Subagents 5. 外部データソース・API接続 → MCP 6. Subagents + Skills の組み合わせで、独立性と専門知識を両立可能

### 入力

- タスクの性質（再利用性、外部接続の有無、独立性等）

### 出力

- 最適なツール選択
- 効率的なトークン利用
- 保守しやすいワークフロー

## 使うツール・ライブラリ

- Skills
- System Prompts
- Projects
- Subagents
- MCP

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（SkillsはFree tierでは利用不可）
- YAML基礎知識（フロントマター記述用）
- gitとバージョン管理の基本（Skillsの配布・管理用）
- Python/JavaScriptの基礎（スクリプト含むSkill作成時）
- Claude.ai / Claude Code CLI / Claude APIのいずれかの利用経験

## 根拠

> Skills employ a progressive disclosure architecture for efficiency: 1. Metadata loading (~100 tokens): Claude scans available Skills to identify relevant matches 2. Full instructions (<5k tokens): Load when Claude determines the Skill applies 3. Bundled resources: Files and executable code load only as needed

> Claude Code CLI: /plugin marketplace add anthropics/skills OR /plugin add /path/to/skill-directory

> Quick Reference: When to Use What - Skills: Reusable procedural knowledge across conversations - Prompts: One-time instructions and immediate context - Projects: Persistent background knowledge within workspaces - Subagents: Independent task execution with specific permissions - MCP: Connecting Claude to external data sources

> obra/superpowers - Core skills library for Claude Code with 20+ battle-tested skills including TDD, debugging, and collaboration patterns. Installation: /plugin marketplace add obra/superpowers-marketplace

> Security: Skills can execute arbitrary code in Claude's environment. Only install skills from trusted sources. Review SKILL.md and all scripts before enabling a skill.
