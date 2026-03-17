# skill-creatorで対話的にSkillを生成する

> Anthropic公式のskill-creator Skillを使い、Q&A形式で新しいSkillを作成する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動でフォルダ構造やYAMLフロントマターを書くより速く、ベストプラクティスに沿った形式が自動生成される。初心者でも迷わずSkillを作れる。

## いつ使うのか

初めてSkillを作る時、または手動作成より速く確実に作りたい時

## やり方

1. Claudeでskill-creator Skillを有効化 2. 'Use the skill-creator to help me build a skill for [your task]'と依頼 3. 対話形式で質問に答える（タスク内容、使用場面、必要なスクリプト等） 4. Claudeが完全なSkill構造を生成してくれる

### 入力

- 実現したいタスクの説明
- 対話で求められる質問への回答

### 出力

- 完全なSkillフォルダ構造
- SKILL.md（フロントマター付き）
- 必要に応じてスクリプトやリソース

## 使うツール・ライブラリ

- skill-creator（Anthropic公式Skill）

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（SkillsはFree tierでは利用不可）
- YAML基礎知識（フロントマター記述用）
- gitとバージョン管理の基本（Skillsの配布・管理用）
- Python/JavaScriptの基礎（スクリプト含むSkill作成時）
- Claude.ai / Claude Code CLI / Claude APIのいずれかの利用経験

## 根拠

> Skills employ a progressive disclosure architecture for efficiency: 1. Metadata loading (~100 tokens): Claude scans available Skills to identify relevant matches 2. Full instructions (<5k tokens): Load when Claude determines the Skill applies 3. Bundled resources: Files and executable code load only as needed

> SKILL.md with frontmatter: ---
name: my-skill
description: Brief description for skill discovery (keep concise)
---

> Use skill-creator (Recommended): 1. Enable the skill-creator skill in Claude 2. Ask Claude: 'Use the skill-creator to help me build a skill for [your task]' 3. Answer the interactive questions about your workflow 4. Claude generates the complete skill structure for you

> Claude Code CLI: /plugin marketplace add anthropics/skills OR /plugin add /path/to/skill-directory

> Quick Reference: When to Use What - Skills: Reusable procedural knowledge across conversations - Prompts: One-time instructions and immediate context - Projects: Persistent background knowledge within workspaces - Subagents: Independent task execution with specific permissions - MCP: Connecting Claude to external data sources
