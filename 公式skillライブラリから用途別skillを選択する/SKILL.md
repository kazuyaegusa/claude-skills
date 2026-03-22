# 公式Skillライブラリから用途別Skillを選択する

> Anthropic公式の20+Skillsから、ドキュメント操作（docx/pdf/pptx/xlsx）、デザイン（canvas-design/algorithmic-art）、開発（frontend-design/mcp-builder）、コミュニケーション（brand-guidelines/internal-comms）等、タスクに応じたSkillを有効化する。

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

車輪の再発明を避け、既にベストプラクティスが実装されたSkillを即座に利用できる。特にドキュメント操作は複雑なフォーマット保持ロジックが必要で、自作より公式Skillが確実。

## いつ使うのか

ドキュメント生成・編集、デザイン制作、MCP開発、ブランドガイドライン適用など、公式Skillがカバーする領域のタスクを行う時。

## やり方

1. claude.ai → Settings > Capabilities → Skills toggleを有効化
2. Browse available skillsで公式Skillカタログを表示
3. タスクに応じてSkillを選択（例：Word編集→docx、プレゼン作成→pptx、React UI→frontend-design）
4. Claude Codeの場合は`/plugin marketplace add anthropics/skills`でインストール
5. タスク実行時にClaudeが自動でSkillを発動

### 入力

- タスク要件（ドキュメント種別、デザイン要件、開発フレームワーク等）

### 出力

- 有効化された公式Skill
- タスク実行時の自動適用

## 使うツール・ライブラリ

- anthropics/skills（公式リポジトリ）
- Claude.ai Settings
- Claude Code CLI

## コード例

```
# Claude Code CLIでインストール
/plugin marketplace add anthropics/skills

# ローカルフォルダからインストール
/plugin add /path/to/skill-directory
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
