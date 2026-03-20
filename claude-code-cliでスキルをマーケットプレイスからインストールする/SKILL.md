# Claude Code CLIでスキルをマーケットプレイスからインストールする

> Claude Code CLIの/pluginコマンドを使い、マーケットプレイスまたはローカルディレクトリからスキルをインストールする

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

GitHubリポジトリやローカルで開発したスキルを簡単に利用可能にするため

## いつ使うのか

Claude Code CLIでスキルを利用開始する時

## やり方

1. マーケットプレイスからインストール: `/plugin marketplace add anthropics/skills`
2. ローカルディレクトリからインストール: `/plugin add /path/to/skill-directory`

### 入力

- マーケットプレイスのスキル名（例: anthropics/skills）
- または、ローカルスキルディレクトリのパス

### 出力

- インストール済みスキル（Claude Codeで利用可能）

## 使うツール・ライブラリ

- Claude Code CLI
- /pluginコマンド

## コード例

```
# Install skills from marketplace
/plugin marketplace add anthropics/skills

# Or install from local directory
/plugin add /path/to/skill-directory
```

## 前提知識

- Claude.ai Pro/Max/Team/Enterpriseアカウント（Freeユーザーはスキル利用不可）
- YAML frontmatter、Markdownの基本知識
- （API利用の場合）Anthropic APIキーとAPI仕様の理解
- （Claude Code利用の場合）Claude Code CLIのインストール

## 根拠

> Use Skills when: Capabilities should be accessible to any Claude instance. They're portable expertise.

> ⚠️ Important: Skills can execute arbitrary code in Claude's environment. Only install skills from trusted sources.

> frontend-design - Instructs Claude to avoid 'AI slop' or generic aesthetics and to make bold design decisions. Works very well for React & Tailwind.

> obra/superpowers - Core skills library for Claude Code with 20+ battle-tested skills including TDD, debugging, and collaboration patterns
