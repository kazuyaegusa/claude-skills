# 特定ドメイン（セキュリティ、開発等）のスキルをTipとして強調する

> README冒頭にTipセクションを設け、特に重要なスキル（例: セキュリティ対策）を強調表示し、ユーザーの注意を引く

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: agent-orchestration

## なぜ使うのか

AI agentでWebアプリを生成する際、セキュリティ対策を怠ると脆弱性が混入しやすい。重要なスキルを冒頭で強調することで、ユーザーがリスクを認識し、適切なスキルを使用する確率が高まる

## いつ使うのか

特定のスキルが多くのユーザーに関係し、かつ見落とされると重大な問題（セキュリティ脆弱性、データ損失等）が発生する可能性がある時

## やり方

1. README.mdの冒頭（目次の前後）に`>[!Tip]`ブロックを挿入
2. ブロック内で特に重要なスキル（例: VibeSec-Skill）へのリンクと、なぜそれが重要かを説明
3. 例: 「If you use Claude to build web applications, do yourself a favor and use [VibeSec-Skill](...) to avoid getting hacked.」

### 入力

- 強調すべきスキルのリスト
- 各スキルの重要性に関する説明

### 出力

- README.md内のTipブロック

## 使うツール・ライブラリ

- Markdown（GitHubのアラートブロック記法）

## コード例

```
>[!Tip]
>If you use Claude to build web applications, do yourself a favor and use [VibeSec-Skill](https://github.com/BehiSecc/VibeSec-Skill) to avoid getting hacked.
```

## 前提知識

- Claude Code（またはClaude Skills対応のAI agent）の基本的な使い方
- GitHubの基本操作（リポジトリ作成、Fork、Pull Request）
- Markdown記法の理解
- SKILL.mdファイルの構造（name, description等）に関する知識

## 根拠

> >[!Tip] If you use Claude to build web applications, do yourself a favor and use [VibeSec-Skill](https://github.com/BehiSecc/VibeSec-Skill) to avoid getting hacked.

> ## 🛠 Development & Code Tools - [test-driven-development](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) - Use when implementing any feature or bugfix, before writing implementation code

> ## 🤝 Contribution - If you have suggestions, improvements, or new resources to add: 1. Fork this repo 2. Make your changes 3. Submit a Pull Request

> リポジトリURL: https://github.com/BehiSecc/awesome-claude-skills
