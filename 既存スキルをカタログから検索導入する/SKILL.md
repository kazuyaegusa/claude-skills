# 既存スキルをカタログから検索・導入する

> awesome-claude-skillsリポジトリから目的に合うスキルを見つけ、自プロジェクトにインストールする

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

ゼロから手順を書くよりも、検証済みのスキルを再利用する方が品質・速度ともに優れているため

## いつ使うのか

新しいタスク領域に取り組む前、または既知の問題に対するベストプラクティスを探す時

## やり方

1. GitHubで `BehiSecc/awesome-claude-skills` を開く
2. 目次から該当カテゴリ（例: Development & Code Tools）を選ぶ
3. スキル名横のリンクから詳細・SKILL.mdを確認
4. `git clone` または `/install-skill` コマンドで `~/.claude/skills/` に配置
5. Claude Codeを再起動してスキルを認識させる

### 入力

- タスクの種類（例: PDF操作、セキュリティレビュー）

### 出力

- 該当スキルのリポジトリURL
- SKILL.mdファイル
- 依存ツール・ライブラリのリスト

## 使うツール・ライブラリ

- GitHub
- git
- Claude Code /install-skill コマンド

## 前提知識

- Claude Codeの基本操作（スキルのインストール・実行方法）
- Markdown・YAML frontmatterの基礎知識
- GitHubリポジトリのクローン・PR操作
- Python/Node.js等のパッケージマネージャ利用経験（スキルによる）

## 根拠

> 「A curated list of Claude Skills.」

> 「14カテゴリ（Document Skills, Development & Code Tools, Data & Analysis, Scientific & Research Tools, Writing & Research, Learning & Knowledge, Media & Content, Health & Life Sciences, Collaboration & Project Management, Security & Web Testing, Utility & Automation, Articles & Blog Posts, Collections）」
