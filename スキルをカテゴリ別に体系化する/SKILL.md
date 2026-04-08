# スキルをカテゴリ別に体系化する

> スキルをDocument Skills、Development、Data & Analysis、Security等の機能カテゴリに分類し、README上で一覧化する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

ユーザーがタスク領域から逆引きできるようにすることで、発見可能性と利用率が向上するため

## いつ使うのか

新しいスキルをカタログに追加する時、または既存カタログを整理する時

## やり方

1. スキルの主目的を特定（例: PDF操作 → Document Skills）
2. README.mdの該当セクションにリスト項目を追加
3. `[スキル名](リポジトリURL) - 1文の説明` 形式で記述
4. 説明文には「何ができるか」「主要な依存関係」を含める

### 入力

- スキルのリポジトリURL
- SKILL.mdの内容

### 出力

- カテゴリ分類されたREADME.md

## 使うツール・ライブラリ

- Markdown
- GitHub

## コード例

```
- [docx](https://github.com/anthropics/skills/tree/main/skills/docx) - Create, edit, analyze Word docs with tracked changes, comments, formatting.
```

## 前提知識

- Claude Codeの基本操作（スキルのインストール・実行方法）
- Markdown・YAML frontmatterの基礎知識
- GitHubリポジトリのクローン・PR操作
- Python/Node.js等のパッケージマネージャ利用経験（スキルによる）

## 根拠

> 「14カテゴリ（Document Skills, Development & Code Tools, Data & Analysis, Scientific & Research Tools, Writing & Research, Learning & Knowledge, Media & Content, Health & Life Sciences, Collaboration & Project Management, Security & Web Testing, Utility & Automation, Articles & Blog Posts, Collections）」
