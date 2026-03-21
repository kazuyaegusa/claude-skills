# Claude Code CLIでSkillをインストール・管理する

> コマンドラインから/plugin marketplaceや/plugin addでSkillをインストール・有効化する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

CLI環境ではブラウザUIが使えないため、コマンドでSkillを追加・管理する必要がある。またGit管理されたSkillをローカルから直接追加できる

## いつ使うのか

Claude Codeを使っている場合、またはGitリポジトリで管理されたカスタムSkillをチームで共有する場合

## やり方

1. マーケットプレイスからインストール: `/plugin marketplace add anthropics/skills`
2. ローカルディレクトリから追加: `/plugin add /path/to/skill-directory`
3. インストール後、Claudeはタスクに応じて自動的にSkillを検出・ロード

### 入力

- Skillのマーケットプレイス名またはローカルパス

### 出力

- Claude Code環境にインストールされたSkill

## 使うツール・ライブラリ

- Claude Code CLI

## コード例

```
/plugin marketplace add anthropics/skills
/plugin add /path/to/skill-directory
```

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（無料tierはSkills非対応）
- Claude.ai Web、Claude Code CLI、またはClaude APIへのアクセス
- YAMLフロントマターの基本的な理解
- （カスタムSkill作成時）Pythonやシェルスクリプトの基礎知識

## 根拠

> Skills employ a progressive disclosure architecture for efficiency: 1. Metadata loading (~100 tokens): Claude scans available Skills to identify relevant matches 2. Full instructions (<5k tokens): Load when Claude determines the Skill applies 3. Bundled resources: Files and executable code load only as needed

> Claude Code CLI: /plugin marketplace add anthropics/skills OR /plugin add /path/to/skill-directory

> Security: Skills can execute arbitrary code in Claude's environment. Only install skills from trusted sources.

> Known issue (Oct 18, 2025): Linux path bug - Agent SDK uses hardcoded macOS paths instead of environment home directory

> Enterprise: As of October 2025, Claude.ai does not support centralized admin management for custom skills. Use version control and internal repositories for team skill distribution.
