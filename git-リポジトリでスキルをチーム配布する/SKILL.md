# git リポジトリでスキルをチーム配布する

> スキルフォルダをgitリポジトリに格納し、チームメンバーが `/plugin add` や git clone で共有・バージョン管理する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

2025年10月時点では claude.ai に中央管理機能がなく、Enterprise でも git ベースの配布が推奨されているため。バージョンタグでロールバックや更新管理も可能

## いつ使うのか

チーム内で統一したワークフロー（TDD、デバッグ手順、コーディング規約）を共有したい場合

## やり方

1. スキルフォルダを git リポジトリに push（例: github.com/team/our-skills）
2. チームメンバーは `git clone` または `/plugin add /path/to/skill` でインストール
3. 更新時は `git pull` して最新版を取得
4. 本番適用前に非本番環境でテスト

### 入力

- スキルフォルダ（SKILL.md + scripts/）
- git リポジトリ（GitHub, GitLab 等）

### 出力

- チーム全員が同じスキルセットを利用可能
- バージョン管理されたスキル履歴

## 使うツール・ライブラリ

- git
- Claude Code CLI (`/plugin add`)

## コード例

```
# Install from git
/plugin add /path/to/cloned/repo/skill-folder

# Or from marketplace
/plugin marketplace add anthropics/skills
```

## 前提知識

- Claude Pro, Max, Team, または Enterprise サブスクリプション（Free tier ではスキル利用不可）
- Claude.ai Web / Claude Code CLI / Claude API のいずれかへのアクセス
- YAMLとMarkdownの基本構文（スキル作成時）
- git の基本操作（チーム配布時）
