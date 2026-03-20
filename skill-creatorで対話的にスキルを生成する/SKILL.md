# skill-creatorで対話的にスキルを生成する

> 公式のskill-creatorスキルを使い、Q&A形式でスキルを自動生成させる

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動でSKILL.mdのフォーマットを覚える必要がなく、対話を通じてベストプラクティスに沿ったスキル構造が得られるため

## いつ使うのか

初めてスキルを作る時、またはフォーマットを覚えていない時

## やり方

1. Claude.aiまたはClaude Codeでskill-creatorスキルを有効化
2. Claudeに「Use the skill-creator to help me build a skill for [your task]」と指示
3. 対話形式の質問（ワークフロー内容、使用場面、必要なリソース等）に回答
4. Claudeが完全なスキル構造を自動生成

### 入力

- 作りたいスキルの目的・タスク内容
- skill-creatorの対話質問への回答

### 出力

- SKILL.md
- 必要に応じてscripts/やresources/ディレクトリ

## 使うツール・ライブラリ

- skill-creator（公式スキル）

## 前提知識

- Claude.ai Pro/Max/Team/Enterpriseアカウント（Freeユーザーはスキル利用不可）
- YAML frontmatter、Markdownの基本知識
- （API利用の場合）Anthropic APIキーとAPI仕様の理解
- （Claude Code利用の場合）Claude Code CLIのインストール

## 根拠

> Skills employ a progressive disclosure architecture for efficiency: 1. Metadata loading (~100 tokens) 2. Full instructions (<5k tokens) 3. Bundled resources

> Use Skills when: Capabilities should be accessible to any Claude instance. They're portable expertise.

> Key insight: If you find yourself typing the same prompt repeatedly across multiple conversations, it's time to create a Skill.

> ⚠️ Important: Skills can execute arbitrary code in Claude's environment. Only install skills from trusted sources.

> Q: How much do skills impact token usage? A: Skills are highly efficient thanks to progressive disclosure. Each skill uses only ~100 tokens during metadata scanning to determine relevance.
