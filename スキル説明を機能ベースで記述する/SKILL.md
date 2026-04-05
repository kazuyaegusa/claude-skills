# スキル説明を機能ベースで記述する

> 各スキルの説明文を「何ができるか」を中心に、動詞+対象+付加情報の形式で簡潔に記述する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

ユーザーが自分のユースケースとマッチするかを素早く判断でき、クリック前にスキルの有用性を評価できる

## いつ使うのか

新しいスキルをAwesomeリストに追加する時、または既存エントリーの説明が不明瞭な時

## やり方

1. 動詞で始める（Create, Extract, Manage, Generate等）
2. 対象を明示する（Word docs, PDFs, Slack messages等）
3. 主要機能を2-4個列挙する（tracked changes, comments, formatting等）
4. 50文字以内に収める

### 入力

- スキルのREADMEまたはSKILL.md
- スキルの主要機能リスト

### 出力

- 1行の機能説明文

## コード例

```
[docx](https://github.com/anthropics/skills/tree/main/skills/docx) - Create, edit, analyze Word docs with tracked changes, comments, formatting.
```

## 前提知識

- Claude Code / Claude Skills の基本概念
- GitHubの基本操作（Fork, PR）
- Markdownの記法

## 根拠

> 🤝 Contribution - Fork this repo, Make your changes, Submit a Pull Request
