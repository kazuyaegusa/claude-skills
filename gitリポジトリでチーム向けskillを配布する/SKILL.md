# Gitリポジトリでチーム向けSkillを配布する

> カスタムSkillをGitリポジトリで管理し、バージョン管理とコードレビューを経てチームに配布する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: other

## なぜ使うのか

2025年10月時点でClaude.aiは集中管理型のSkill配布機能を持たない。Gitによるバージョン管理とピアレビューにより、セキュリティとメンテナンス性を確保する

## いつ使うのか

チームや組織内でカスタムSkillを共有する場合、またはエンタープライズ環境でSkillのセキュリティとバージョン管理を厳密に行いたい場合

## やり方

1. カスタムSkillをGitリポジトリにコミット
2. Gitタグでバージョン管理（例: v1.0.0）
3. プルリクエストでコードレビュー実施
4. チームメンバーは `/plugin add <repo-url>` でインストール
5. 定期的に監査・更新を実施

### 入力

- カスタムSkillのフォルダ構造
- Gitリポジトリ
- バージョン管理ポリシー
- コードレビュープロセス

### 出力

- バージョン管理されたSkillリポジトリ
- チーム全体で共有可能なSkill

## 使うツール・ライブラリ

- Git
- GitHub/GitLab/Bitbucket等

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（無料tierはSkills非対応）
- Claude.ai Web、Claude Code CLI、またはClaude APIへのアクセス
- YAMLフロントマターの基本的な理解
- （カスタムSkill作成時）Pythonやシェルスクリプトの基礎知識

## 根拠

> Claude Code CLI: /plugin marketplace add anthropics/skills OR /plugin add /path/to/skill-directory
