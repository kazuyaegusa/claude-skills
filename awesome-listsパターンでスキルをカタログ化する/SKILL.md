# Awesome Listsパターンでスキルをカタログ化する

> GitHub上でClaude Skillsを分野別（Document、Development、Security等）に分類し、各スキルのリポジトリリンクと1行説明を列挙したREADMEを作成する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: other

## なぜ使うのか

スキルが分散していると発見性が低く、ユーザーは必要な機能を見逃す。カテゴリ分類とTable of Contentsにより、目的に応じて素早く関連スキルを探せる

## いつ使うのか

オープンソースのツールやプラグインが複数のリポジトリに分散している時、コミュニティ駆動で拡張可能なカタログを作りたい時

## やり方

1. スキルを機能ドメインでグループ化（📄Document, 🛠Development, 🔬Scientific等）
2. 各カテゴリ内でスキルをアルファベット順にリスト化
3. 各エントリは`[スキル名](リポジトリURL) - 1行説明`の形式で記述
4. READMEの冒頭にTable of Contentsを配置し、アンカーリンクで各セクションにジャンプ可能にする
5. 新規スキルはPRで追加できるようContribution項を設ける

### 入力

- 各スキルのGitHubリポジトリURL
- スキルの簡潔な説明文
- 適切なカテゴリ分類

### 出力

- カテゴリ別に整理されたMarkdown形式のAwesome List
- コミュニティがPRで追加できるメンテナンス可能なカタログ

## 使うツール・ライブラリ

- GitHub
- Markdown

## コード例

```
## 🛠 Development & Code Tools
- [test-driven-development](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) - Use when implementing any feature or bugfix, before writing implementation code
- [aws-skills](https://github.com/zxkane/aws-skills) - AWS development with CDK best practices, cost optimization MCP servers, and serverless/event-driven architecture patterns
```

## 前提知識

- Claude Codeの基本的な使い方（プロンプト実行、ツール呼び出し）
- GitHubリポジトリのクローン・PRの基本操作
- SKILL.mdの配置場所（`~/.claude/skills/`）の理解
- （MCPスキル使用時）Model Context Protocolの概念とサーバーインストール方法
