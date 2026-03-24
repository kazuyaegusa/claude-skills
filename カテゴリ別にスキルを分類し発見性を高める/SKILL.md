# カテゴリ別にスキルを分類し発見性を高める

> スキルを機能別カテゴリ（Document Skills, Development & Code Tools, Data & Analysis等）に分類し、ユーザーが目的に応じてスキルを発見しやすくする

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: dev-tool

## なぜ使うのか

300以上のスキルを単純に列挙すると、ユーザーは目的のスキルを見つけられない。カテゴリ分類により、ユーザーは「PDF処理がしたい」「セキュリティレビューをしたい」といった目的から逆引きでスキルを探せる

## いつ使うのか

多数のスキルを管理・公開する時、または既存のAwesome Listが肥大化してナビゲーションが困難になった時

## やり方

1. スキルの主な用途・ドメインを分析（例: ドキュメント処理、開発ツール、データ分析、セキュリティ等）
2. README.mdの目次（Table of Contents）にカテゴリを列挙
3. 各カテゴリごとにセクション（## 見出し）を作成
4. カテゴリ内でスキルを箇条書き（`- [スキル名](URL) - 説明`）で列挙
5. 絵文字を使ってカテゴリを視覚的に区別（例: 📄 Document Skills, 🛠 Development & Code Tools）

### 入力

- スキルのリスト
- 各スキルの主な用途・ドメイン

### 出力

- カテゴリ分類されたREADME.md
- 目次（Table of Contents）
- カテゴリごとのセクション

## 使うツール・ライブラリ

- Markdown

## コード例

```
## 📚 Table of Contents  
- [📄 Document Skills](#-document-skills)  
- [🛠 Development & Code Tools](#-development--code-tools)  
- [📊 Data & Analysis](#-data--analysis)  

## 📄 Document Skills  
- [docx](...) - Create, edit, analyze Word docs  
- [pdf](...) - Extract text, tables, metadata
```

## 前提知識

- Claude Code（またはClaude Skills対応のAI agent）の基本的な使い方
- GitHubの基本操作（リポジトリ作成、Fork、Pull Request）
- Markdown記法の理解
- SKILL.mdファイルの構造（name, description等）に関する知識

## 根拠

> ## 📄 Document Skills - [docx](https://github.com/anthropics/skills/tree/main/skills/docx) - Create, edit, analyze Word docs with tracked changes, comments, formatting.

> ## 🛠 Development & Code Tools - [test-driven-development](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) - Use when implementing any feature or bugfix, before writing implementation code
