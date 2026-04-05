# カテゴリを機能軸とドメイン軸で分類する

> スキルを「技術的機能」（Document, Development, Data）と「適用領域」（Health, Security, Media）の2軸で分類し、階層化する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: other

## なぜ使うのか

ユーザーの探し方は「何がしたいか」（機能軸）と「どの領域で使うか」（ドメイン軸）の2パターンがあるため、両方に対応することで発見性が向上する

## いつ使うのか

スキル数が30個を超え、単純なリスト表示では見つけにくくなった時

## やり方

1. 上位カテゴリを8-12個定義する（Document Skills, Development & Code Tools, Data & Analysis, Scientific & Research Tools等）
2. 各カテゴリ内で関連性の高いスキルをグルーピング
3. カテゴリ名に絵文字を付けて視認性を高める（📄, 🛠, 📊等）
4. Table of Contentsでカテゴリ間ジャンプを可能にする

### 入力

- 全スキルのリスト
- 各スキルの機能とドメイン情報

### 出力

- カテゴリ階層構造
- Table of Contents
- カテゴリ別セクション

## 使うツール・ライブラリ

- Markdown

## コード例

```
## 📄 Document Skills
## 🛠 Development & Code Tools
## 📊 Data & Analysis
```

## 前提知識

- Claude Code / Claude Skills の基本概念
- GitHubの基本操作（Fork, PR）
- Markdownの記法

## 根拠

> 🛠 Development & Code Tools - web-artifacts-builder, test-driven-development等

> 🔬 Scientific & Research Tools - 125+ scientific skills for bioinformatics
