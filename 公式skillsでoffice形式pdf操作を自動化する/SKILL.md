# 公式SkillsでOffice形式・PDF操作を自動化する

> docx/pdf/pptx/xlsx公式Skillsを使い、Word/PowerPoint/Excel/PDFの作成・編集・分析を実行する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: automation-pipeline

## なぜ使うのか

複雑なOffice形式の操作を手作業で記述する必要がなくなる。トラック変更、コメント、フォーム、数式、グラフなど高度な機能もサポート。

## いつ使うのか

レポート生成、プレゼン資料作成、データ分析結果のExcel出力など、Office形式での成果物が必要な時

## やり方

1. 該当Skillを有効化（例: docx Skill） 2. Claudeに「Word文書を作成して...」等のタスクを依頼 3. Skillが自動ロードされ、適切なライブラリ（python-docx等）を使った操作を実行 4. 成果物（.docx, .pdf, .pptx, .xlsx）を出力

### 入力

- タスク指示（例: 「売上データをExcelグラフ付きで出力」）

### 出力

- Office形式ファイル（.docx/.pdf/.pptx/.xlsx）

## 使うツール・ライブラリ

- docx Skill
- pdf Skill
- pptx Skill
- xlsx Skill

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（SkillsはFree tierでは利用不可）
- YAML基礎知識（フロントマター記述用）
- gitとバージョン管理の基本（Skillsの配布・管理用）
- Python/JavaScriptの基礎（スクリプト含むSkill作成時）
- Claude.ai / Claude Code CLI / Claude APIのいずれかの利用経験
