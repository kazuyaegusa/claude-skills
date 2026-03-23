# YAMLフロントマター + SKILL.md構造でのSkill作成

> 再利用可能なSkillを標準フォーマットで作成し、バージョン管理・共有可能にする

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

統一されたフォーマットにより、Claude.ai、Claude Code、APIの全環境で同じSkillsが動作し、gitでのバージョン管理とチーム配布が容易になる

## いつ使うのか

繰り返し実行するタスクがあり、それを標準化して他の会話やチームメンバーと共有したい時

## やり方

1. ディレクトリ作成: my-skill/
2. SKILL.md作成、YAMLフロントマターで`name`と`description`を定義
3. 詳細な手順、使用例を本文に記載
4. （オプション）scripts/にPython/JS等の実行スクリプト配置
5. （オプション）resources/にテンプレートファイル等配置
6. gitでバージョン管理し、/plugin add でインストール

### 入力

- タスクの手順、必要なスクリプト、テンプレートファイル

### 出力

- 再利用可能なSkillディレクトリ（SKILL.md + オプションでscripts/, resources/）

## 使うツール・ライブラリ

- git
- Claude Code CLI
- Claude.ai
- Claude API

## コード例

```
---
name: my-skill
description: Brief description for skill discovery
---

# Detailed Instructions

Claude will read these instructions when the skill is activated.

## Usage
Explain how to use this skill...

## Examples
Provide clear examples...
```

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（Free tierはSkills非対応）
- Claude Code CLIまたはClaude.ai、Claude APIへのアクセス
- YAMLとMarkdownの基本知識
- gitによるバージョン管理の基礎（チーム配布する場合）
- Skillsが実行するスクリプト言語（Python、JavaScript等）の基礎知識（カスタムSkills作成時）

## 根拠

> /plugin marketplace add anthropics/skills
/plugin add /path/to/skill-directory
