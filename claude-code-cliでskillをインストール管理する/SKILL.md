# Claude Code CLIでSkillをインストール・管理する

> マーケットプレイスまたはローカルディレクトリから、/pluginコマンドでSkillをインストールする

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

CLI環境で即座にSkillを追加・利用開始できる。gitリポジトリ経由で配布されたSkillも簡単に導入可能。

## いつ使うのか

Claude Code CLIを使っている時、チームで共有されたSkillリポジトリを導入する時

## やり方

1. マーケットプレイスから: `/plugin marketplace add anthropics/skills` 2. ローカルから: `/plugin add /path/to/skill-directory` 3. インストール後、Claudeが自動的にメタデータをスキャンして利用可能にする

### 入力

- マーケットプレイス名またはローカルパス

### 出力

- インストールされたSkill（Claudeが自動認識）

## 使うツール・ライブラリ

- Claude Code CLI

## コード例

```
# Install skills from marketplace
/plugin marketplace add anthropics/skills

# Or install from local directory
/plugin add /path/to/skill-directory
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
