# skill-creatorで対話的にSkillを生成する

> Anthropic公式のskill-creator Skillを使い、Q&A形式で新しいSkillの構造を自動生成する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動でフロントマター・ディレクトリ構造・ベストプラクティスを把握するより、対話形式で必要な要素を引き出してもらう方が初心者でも高品質なSkillを作れる

## いつ使うのか

初めてSkillを作る場合、または複雑なワークフローをSkill化する際にベストプラクティスに沿った構造を確実に作りたい場合

## やり方

1. Claude.ai/Codeでskill-creator Skillを有効化
2. Claudeに「Use the skill-creator to help me build a skill for [your task]」と指示
3. 対話型の質問に答える（タスク内容、手順、必要なリソース等）
4. Claudeが完全なSkill構造（SKILL.md + scripts + resources）を生成

### 入力

- Skill化したいタスクの説明
- 対話中の質問への回答（使用ツール、手順、例等）

### 出力

- 完全なSkillフォルダ構造（SKILL.md + 必要に応じたscripts/resources/）

## 使うツール・ライブラリ

- skill-creator Skill（Anthropic公式）

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（無料tierはSkills非対応）
- Claude.ai Web、Claude Code CLI、またはClaude APIへのアクセス
- YAMLフロントマターの基本的な理解
- （カスタムSkill作成時）Pythonやシェルスクリプトの基礎知識

## 根拠

> Skills employ a progressive disclosure architecture for efficiency: 1. Metadata loading (~100 tokens): Claude scans available Skills to identify relevant matches 2. Full instructions (<5k tokens): Load when Claude determines the Skill applies 3. Bundled resources: Files and executable code load only as needed

> SKILL.md with frontmatter: ---
name: my-skill
description: Brief description for skill discovery (keep concise)
---

> Claude Code CLI: /plugin marketplace add anthropics/skills OR /plugin add /path/to/skill-directory

> Skills API accessible via /v1/skills endpoint

> Key insight: If you find yourself typing the same prompt repeatedly across multiple conversations, it's time to create a Skill.
