# Gitリポジトリでスキルをバージョン管理・チーム配布する

> カスタムスキルをGitリポジトリで管理し、バージョンタグ付け・ドキュメント化・チーム配布を行う

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

2025年10月時点でClaude.aiは一元的な管理者管理をサポートしていない。Gitベースの配布により、バージョン管理・ロールバック・チーム共有・監査証跡が実現できる

## いつ使うのか

チーム・組織でカスタムスキルを共有したい、バージョン管理・ロールバックが必要、一元管理機能がない環境でのとき

## やり方

1. スキルフォルダ構造をGitリポジトリにコミット
2. セマンティックバージョニングでタグ付け（例: v1.0.0）
3. README、SKILL.md、依存関係を明記
4. チームメンバーはリポジトリをクローン/プル
5. 更新時は新バージョンタグをプッシュ、チームは`git pull`で取得
6. 内部承認フロー・レビュープロセスをPR/マージで実施
7. エンタープライズでは内部Gitサーバー・プライベートリポジトリを利用

### 入力

- スキルフォルダ構造
- Gitリポジトリ

### 出力

- バージョン管理されたスキル、チーム配布可能な形式

## 使うツール・ライブラリ

- Git
- GitHub/GitLab/内部Gitサーバー

## コード例

```
# 例: チームリポジトリから導入
git clone https://github.com/your-org/custom-skills
cd custom-skills
/plugin add ./my-skill

# 更新時
cd custom-skills
git pull
# Claude Code再起動またはスキル再ロード
```

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（Freeプランではスキル利用不可）
- YAML frontmatter、Markdown記法の基礎知識
- Git/GitHubの基本操作（バージョン管理・配布時）
- Python/JavaScriptなどスクリプト言語の基礎（カスタムスキル作成時）
- Claude Code CLI、Claude.ai、またはClaude APIの利用経験
- プロンプトエンジニアリング、MCP、Subagents、Projectsとの違いの理解
