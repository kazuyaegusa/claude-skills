# 段階的開示アーキテクチャでSkillsを設計する

> Claude Skillsを、メタデータスキャン（~100トークン）→フル命令ロード（<5kトークン）→リソースロード（必要時のみ）の3段階で構成する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

複数のSkillsを同時に利用可能な状態に保ちながら、コンテキストウィンドウを圧迫しない。Claudeが関連性を判断してから詳細を読み込むため、無関係なSkillはトークンコストがほぼゼロになる。

## いつ使うのか

再利用可能なタスク手順を作る時、特に複数のリソースファイルやスクリプトを含む複雑なワークフローの場合

## やり方

1. SKILL.mdにYAMLフロントマター（name, description）を記述 2. descriptionは簡潔にしてスキル発見用に最適化 3. 詳細な命令はフロントマター後に記述 4. scripts/やresources/フォルダに実行可能コードやテンプレートを配置 5. 命令内で必要なリソースを参照する形にして、Claudeが判断してロードできるようにする

### 入力

- 再利用したいタスクの手順
- 必要なスクリプト・テンプレートファイル
- スキル発見用の簡潔な説明文

### 出力

- my-skill/SKILL.md（フロントマター+詳細命令）
- my-skill/scripts/（実行可能スクリプト）
- my-skill/resources/（テンプレート等）

## 使うツール・ライブラリ

- Claude.ai / Claude Code / Claude API
- YAML（フロントマター）
- Python/JavaScript（スクリプト用）

## コード例

```
---
name: my-skill
description: Brief description for skill discovery (keep concise)
---

# Detailed Instructions

Claude will read these instructions when the skill is activated.

## Usage
Explain how to use this skill...

## Examples
Provide clear examples...
```

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（SkillsはFree tierでは利用不可）
- YAML基礎知識（フロントマター記述用）
- gitとバージョン管理の基本（Skillsの配布・管理用）
- Python/JavaScriptの基礎（スクリプト含むSkill作成時）
- Claude.ai / Claude Code CLI / Claude APIのいずれかの利用経験

## 根拠

> Skills employ a progressive disclosure architecture for efficiency: 1. Metadata loading (~100 tokens): Claude scans available Skills to identify relevant matches 2. Full instructions (<5k tokens): Load when Claude determines the Skill applies 3. Bundled resources: Files and executable code load only as needed

> Use skill-creator (Recommended): 1. Enable the skill-creator skill in Claude 2. Ask Claude: 'Use the skill-creator to help me build a skill for [your task]' 3. Answer the interactive questions about your workflow 4. Claude generates the complete skill structure for you

> Claude Code CLI: /plugin marketplace add anthropics/skills OR /plugin add /path/to/skill-directory

> Quick Reference: When to Use What - Skills: Reusable procedural knowledge across conversations - Prompts: One-time instructions and immediate context - Projects: Persistent background knowledge within workspaces - Subagents: Independent task execution with specific permissions - MCP: Connecting Claude to external data sources

> frontend-design - Instructs Claude to avoid 'AI slop' or generic aesthetics and to make bold design decisions. Works very well for React & Tailwind.
