# skill-creator で対話的にスキルを生成する

> 公式の skill-creator スキルを有効化し、Claudeとの対話形式で新しいスキルの構造を自動生成する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動でフォルダ構造やフロントマターを書くより、Claudeに質問形式でヒアリングさせた方がベストプラクティスに沿った構造を素早く作れるため

## いつ使うのか

初めてスキルを作る場合、または構造のベストプラクティスを学びたい場合

## やり方

1. Claude で skill-creator スキルを有効化
2. 「Use the skill-creator to help me build a skill for [your task]」と依頼
3. 対話形式の質問に答える
4. Claude が完全なスキル構造（SKILL.md, scripts/, resources/）を生成

### 入力

- タスクの説明
- 対話形式の質問への回答

### 出力

- 完全なスキルフォルダ構造
- SKILL.md（フロントマター付き）
- 必要に応じてスクリプト・リソース

## 使うツール・ライブラリ

- skill-creator（公式スキル）

## 前提知識

- Claude Pro, Max, Team, または Enterprise サブスクリプション（Free tier ではスキル利用不可）
- Claude.ai Web / Claude Code CLI / Claude API のいずれかへのアクセス
- YAMLとMarkdownの基本構文（スキル作成時）
- git の基本操作（チーム配布時）

## 根拠

> Skills employ a **progressive disclosure architecture** for efficiency: 1. **Metadata loading** (~100 tokens): Claude scans available Skills to identify relevant matches 2. **Full instructions** (<5k tokens): Load when Claude determines the Skill applies 3. **Bundled resources**: Files and executable code load only as needed

> **Use Skills when**: Capabilities should be accessible to any Claude instance. They're portable expertise.

> **Key insight**: *If you find yourself typing the same prompt repeatedly across multiple conversations, it's time to create a Skill.*

> ⚠️ **Important**: Skills can execute arbitrary code in Claude's environment. Only install skills from trusted sources.

> The easiest way to create a skill is to use the built-in `skill-creator`: 1. Enable the skill-creator skill in Claude 2. Ask Claude: "Use the skill-creator to help me build a skill for [your task]" 3. Answer the interactive questions about your workflow 4. Claude generates the complete skill structure for you
