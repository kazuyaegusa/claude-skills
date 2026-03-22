# Progressive Disclosure設計でSkillを構造化する

> Claude Skillsを「メタデータ（~100トークン）→本体指示（<5kトークン）→リソースファイル（必要時のみ）」の3層に分離して、関連性判定を軽量に保ちながら詳細を段階的にロードする設計。

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

全Skillの本体を常時コンテキストに含めるとトークン枯渇するため。メタデータのみスキャンして関連Skillだけフルロードすることで、数十個のSkillを同時利用可能にする。

## いつ使うのか

複数の専門Skillを同時に利用可能にしたいが、コンテキストウィンドウを節約したい時。特に10個以上のSkillをチームで運用する場合。

## やり方

1. `SKILL.md`の冒頭にYAML frontmatterで`name`（識別子）と`description`（簡潔な用途説明）を記載
2. frontmatter以降に詳細な手順・例・ベストプラクティスをMarkdownで記述
3. 実行スクリプトやテンプレートは別ファイル（`scripts/`, `resources/`）に分離し、本体から参照
4. Claudeはタスク受領時に全Skillのfrontmatterをスキャン→関連判定→該当Skillの本体をロード→必要ならリソースファイルを実行

### 入力

- Skillのフォルダ構造（SKILL.md + scripts/ + resources/）
- YAML frontmatter（name, description）
- 本体のMarkdown指示文

### 出力

- 効率的にロード可能なSkillパッケージ
- Claudeによる自動関連性判定と段階的ロード

## 使うツール・ライブラリ

- YAML frontmatter
- Markdown
- Claude Skills API

## コード例

```
---
name: my-skill
description: Brief description for skill discovery
---

# Detailed Instructions
Claude will read these instructions when activated.

## Usage
Explain how to use this skill...

## Examples
Provide clear examples...
```

## 前提知識

- Claude Pro/Max/Team/Enterprise契約（Free tierではSkills利用不可）
- YAML frontmatter、Markdownの基本文法
- gitによるバージョン管理の知識（Skill配布・更新管理に必要）
- Claude.ai/Code/APIのいずれかの使用経験
- （開発系Skillの場合）対象フレームワーク・ライブラリの基礎知識

## 根拠

> 「Skills employ a progressive disclosure architecture for efficiency: 1. Metadata loading (~100 tokens): Claude scans available Skills to identify relevant matches 2. Full instructions (<5k tokens): Load when Claude determines the Skill applies 3. Bundled resources: Files and executable code load only as needed」（Progressive Disclosure設計の具体的トークン数）

> 「Use Skills when: Capabilities should be accessible to any Claude instance. They're portable expertise.」（Skillsの位置づけ）

> 「⚠️ Important: Skills can execute arbitrary code in Claude's environment. Only install skills from trusted sources.」（セキュリティ警告）

> 「obra/superpowers - Core skills library for Claude Code with 20+ battle-tested skills including TDD, debugging, and collaboration patterns」（コミュニティSkillの代表例）

> 「Use skill-creator: 1. Enable the skill-creator skill in Claude 2. Ask Claude: 'Use the skill-creator to help me build a skill for [your task]' 3. Answer the interactive questions about your workflow 4. Claude generates the complete skill structure for you」（skill-creator使用手順）
