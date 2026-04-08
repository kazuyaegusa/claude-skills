# スキル定義をSKILL.md形式で記述する

> Claude Codeが読み込める標準フォーマット（SKILL.md）で、タスクの手順・ツール・制約を構造化記述する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

マークダウン形式の知識パッケージにすることで、AIエージェントが自律的に読み込み・実行できるようになるため

## いつ使うのか

チーム内で繰り返し行う作業をスキルとして標準化したい時

## やり方

1. `~/.claude/skills/{skill-name}/SKILL.md` を作成
2. フロントマターで `name`, `description`, `triggers` を定義
3. 本文でステップバイステップの手順、使用ツール、エラーハンドリングを記述
4. コードスニペット・設定例があれば含める
5. 依存関係（pip install, npm install等）を明記

### 入力

- タスクの要件
- 必要なツール・API
- 期待される出力形式

### 出力

- SKILL.mdファイル
- 依存パッケージリスト

## 使うツール・ライブラリ

- Markdown
- YAML frontmatter
- Claude Code Skill仕様

## コード例

```
---
name: pdf-logo-remover
description: PDFの全ページからロゴ/ウォーターマークを自動検出・一括除去するスキル
---

## 使い方
1. `/remove-pdf-logo <PDFパス>` を実行
2. スクリプトがロゴ領域を検出
3. 除去後のPDFが出力される
```

## 前提知識

- Claude Codeの基本操作（スキルのインストール・実行方法）
- Markdown・YAML frontmatterの基礎知識
- GitHubリポジトリのクローン・PR操作
- Python/Node.js等のパッケージマネージャ利用経験（スキルによる）

## 根拠

> 「A curated list of Claude Skills.」
