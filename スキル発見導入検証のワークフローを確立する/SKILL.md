# スキル発見→導入→検証のワークフローを確立する

> Awesome Listからスキルを検索し、ローカルにクローンして試用、プロジェクトに適合するか検証してから正式採用する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

未検証のスキルを本番環境に導入するとバグや非互換のリスクがある。試用フェーズで動作確認・カスタマイズを行い、信頼性を担保する

## いつ使うのか

新機能実装前、データ分析タスク開始前、プロジェクトセットアップ時

## やり方

1. Awesome Listで目的に合うカテゴリを探す（例: Data & Analysis）
2. 候補スキルのGitHubでREADME/SKILL.mdを読み、前提条件を確認
3. `git clone` で ~/.claude/skills/ に配置
4. サンプルデータでテスト実行（例: CSVファイルで csv-data-summarizer を試す）
5. 期待通り動作すればプロジェクトのCLAUDE.mdに記載、不要なら削除

### 入力

- Awesome List URL
- プロジェクトの要件定義

### 出力

- 検証済みスキルのリスト
- プロジェクトのCLAUDE.md更新

## 使うツール・ライブラリ

- git
- Claude Code

## コード例

```
# 1. スキルを検索
open https://github.com/BehiSecc/awesome-claude-skills

# 2. クローン
git clone https://github.com/anthropics/skills.git ~/.claude/skills/anthropics

# 3. テスト
cd ~/.claude/skills/anthropics/skills/csv-data-summarizer
claude -p test_data.csv
```

## 前提知識

- Claude Codeの基本的な使い方（スキルのインストール・実行）
- GitHubでのリポジトリ検索・クローン操作
- ~/.claude/skills/ ディレクトリ構造の理解
- （オプション）MCP（Model Context Protocol）の概念
