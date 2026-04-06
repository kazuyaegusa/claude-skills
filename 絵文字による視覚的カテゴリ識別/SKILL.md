# 絵文字による視覚的カテゴリ識別

> 各カテゴリの見出しに絵文字（📄 Document, 🛠 Development, 📊 Data など）を付与し、視覚的にセクションを識別しやすくする

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: other

## なぜ使うのか

長いリストをスクロールする際、テキストだけでは視覚的な手がかりが少なく、目的のセクションを見失いやすい

## いつ使うのか

カテゴリ数が5つを超えてスクロールが必要になった時、またはユーザーが特定セクションを繰り返し探す時

## やり方

1. カテゴリの性質を表す絵文字を選定（Document = 📄, Tools = 🛠 など）
2. Markdown 見出しの前に絵文字を配置
3. Table of Contents にも絵文字を含める

### 入力

- カテゴリ名リスト
- カテゴリの性質

### 出力

- 絵文字付き見出し（例: "📄 Document Skills"）

## 使うツール・ライブラリ

- Unicode 絵文字

## コード例

```
## 📄 Document Skills
## 🛠 Development & Code Tools
## 📊 Data & Analysis
```

## 前提知識

- Claude Code の基本的な使い方（スキルのインストール方法）
- GitHub リポジトリの構造と README.md の役割
- Markdown 記法
- awesome-* リストの概念（例: awesome-python, awesome-go）

## 根拠

> ## 📚 Table of Contents - 投稿内で12のカテゴリに分類されている
