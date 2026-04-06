# スキル説明の1行標準化

> 各スキルの説明を「何をするか」を端的に示す1行（~80文字）に統一し、ユーザーが一覧から瞬時に判断できるようにする

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

詳細な説明はリポジトリ内の SKILL.md に任せ、カタログでは「このスキルは自分のタスクに関係あるか」の判断材料だけを提供すべき

## いつ使うのか

新規スキルをカタログに追加する時、または既存スキルの説明が長すぎて可読性が低下している時

## やり方

1. スキルの core capability を特定
2. 動詞で始まる簡潔な文を作成（Create, Extract, Analyze など）
3. 主要な入出力やサポート形式を列挙（例: DOCX, PPTX, XLSX）
4. 80文字以内に収める

### 入力

- スキルの SKILL.md または README
- スキルの主要機能・対応形式

### 出力

- 1行説明文（例: "Extract text, tables, metadata, merge & annotate PDFs"）

## コード例

```
[pdf](https://github.com/anthropics/skills/tree/main/skills/pdf) - Extract text, tables, metadata, merge & annotate PDFs.
```

## 前提知識

- Claude Code の基本的な使い方（スキルのインストール方法）
- GitHub リポジトリの構造と README.md の役割
- Markdown 記法
- awesome-* リストの概念（例: awesome-python, awesome-go）

## 根拠

> [docx](https://github.com/anthropics/skills/tree/main/skills/docx) - Create, edit, analyze Word docs - 1行説明の実例
