# Claude Code CLIでのSkillインストール

> Claude Code CLI環境でマーケットプレイスまたはローカルディレクトリからSkillsをインストールする

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

CLIから直接Skillsを管理することで、開発ワークフローにシームレスに統合でき、バージョン管理やチーム配布が容易になる

## いつ使うのか

Claude Code環境でSkillsを利用したい時、またはチーム用のカスタムSkillsを配布したい時

## やり方

1. マーケットプレイスからインストール: `/plugin marketplace add anthropics/skills`
2. ローカルディレクトリからインストール: `/plugin add /path/to/skill-directory`
3. インストール後、Claudeが自動的にSkillsをスキャンし、関連タスクで利用可能になる

### 入力

- Skillのマーケットプレイスパスまたはローカルディレクトリパス

### 出力

- インストールされ、即座に利用可能なSkills

## 使うツール・ライブラリ

- Claude Code CLI

## コード例

```
/plugin marketplace add anthropics/skills
/plugin add /path/to/skill-directory
```

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（Free tierはSkills非対応）
- Claude Code CLIまたはClaude.ai、Claude APIへのアクセス
- YAMLとMarkdownの基本知識
- gitによるバージョン管理の基礎（チーム配布する場合）
- Skillsが実行するスクリプト言語（Python、JavaScript等）の基礎知識（カスタムSkills作成時）

## 根拠

> Skills employ a progressive disclosure architecture for efficiency: 1. Metadata loading (~100 tokens): Claude scans available Skills to identify relevant matches 2. Full instructions (<5k tokens): Load when Claude determines the Skill applies 3. Bundled resources: Files and executable code load only as needed

> Use Skills when: Capabilities should be accessible to any Claude instance. They're portable expertise.

> ⚠️ Important: Skills can execute arbitrary code in Claude's environment. Only install skills from trusted sources.

> /plugin marketplace add anthropics/skills
/plugin add /path/to/skill-directory

> obra/superpowers - Core skills library for Claude Code with 20+ battle-tested skills including TDD, debugging, and collaboration patterns
