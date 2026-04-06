# 分野別カテゴリ分類によるスキル整理

> Claude Skills を機能分野ごと（Document Skills, Development & Code Tools, Data & Analysis など）に分類し、Markdown の Table of Contents で構造化する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: other

## なぜ使うのか

数百のスキルが無秩序に並んでいると目的のスキルを見つけられないため、ユーザーのタスク領域に応じた分類が必要

## いつ使うのか

スキルカタログが20件を超えて検索性が低下した時、または複数の機能領域にまたがるスキルが混在している時

## やり方

1. スキルの主要機能を特定
2. 機能領域ごとにセクションを作成（📄 Document Skills, 🛠 Development & Code Tools など）
3. 各セクション内でスキル名、リポジトリリンク、簡潔な説明（1行）をリスト化
4. README 冒頭に Table of Contents を配置し、各セクションへのアンカーリンクを設定

### 入力

- スキルリポジトリのリスト（URL、名前、説明）
- 各スキルの主要機能・対象領域

### 出力

- 分野別に整理された README.md
- 目次セクション（Table of Contents）
- 各カテゴリごとのスキルリスト

## 使うツール・ライブラリ

- Markdown
- GitHub リポジトリ

## コード例

```
## 📄 Document Skills
- [docx](https://github.com/anthropics/skills/tree/main/skills/docx) - Create, edit, analyze Word docs
- [pdf](https://github.com/anthropics/skills/tree/main/skills/pdf) - Extract text, tables, metadata
```

## 前提知識

- Claude Code の基本的な使い方（スキルのインストール方法）
- GitHub リポジトリの構造と README.md の役割
- Markdown 記法
- awesome-* リストの概念（例: awesome-python, awesome-go）

## 根拠

> ## 📚 Table of Contents - 投稿内で12のカテゴリに分類されている

> [docx](https://github.com/anthropics/skills/tree/main/skills/docx) - Create, edit, analyze Word docs - 1行説明の実例
