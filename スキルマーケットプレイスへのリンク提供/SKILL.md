# スキルマーケットプレイスへのリンク提供

> Collectionsセクションに、スキル検索・インストールを支援する外部サービス（agentskill.sh等）へのリンクを含める

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

GitHubリポジトリだけでは検索性に限界がある。専用マーケットプレイスを併用することで、より洗練された発見体験を提供できる

## いつ使うのか

スキル総数が100を超え、GitHub READMEだけでは管理が困難になった時点

## やり方

1. スキル検索・閲覧に特化した外部サービスを調査
2. Collectionsセクションに「Browse and install」エントリとして追加
3. 対応AI開発ツール（Claude Code、Cursor、Windsurf等）を列挙

### 入力

- スキルマーケットプレイスのURL
- 掲載スキル数と対応ツール情報

### 出力

- マーケットプレイスへのリンクエントリ

## コード例

```
- [agentskill.sh](https://agentskill.sh) - Browse and install 69,000+ AI agent skills for Claude Code, Cursor, Copilot, Windsurf, Zed, and 20+ AI tools.
```

## 前提知識

- Claude Codeの基本的な使い方とスキルシステムの理解
- SKILL.mdフォーマットの概念
- GitHubの基本操作（リポジトリ閲覧、PR作成）
- Markdown記法

## 根拠

> 「If you use Claude to build web applications, do yourself a favor and use VibeSec-Skill to avoid getting hacked」- セキュリティスキルの明示的推奨

> 「agentskill.sh - Browse and install 69,000+ AI agent skills」- 大規模スキルマーケットプレイスの存在
