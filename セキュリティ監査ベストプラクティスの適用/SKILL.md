# セキュリティ監査ベストプラクティスの適用

> Skillsが任意コード実行可能であることを踏まえ、信頼できるソースのみから導入し、コードレビューを徹底する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

悪意あるSkillsはデータ漏洩、プロンプトインジェクション増幅、脆弱性導入のリスクがある。エンタープライズ環境では特に監査が必須

## いつ使うのか

新しいSkillを導入する時、特にエンタープライズ・本番環境への導入前

## やり方

1. 信頼できるソース（公式、obra/superpowers等の著名リポジトリ）からのみインストール
2. SKILL.mdと全スクリプトを導入前にレビュー
3. gitでバージョン管理し、変更履歴を追跡
4. チーム配布前にピアレビュー実施
5. 最小権限原則を適用し、必要なアクセス権のみ付与
6. 定期的に導入済みSkillsを監査
7. 非本番環境で徹底的にテスト後、本番導入

### 入力

- Skillのソースコード、スクリプト、依存関係

### 出力

- セキュリティ監査済み、承認されたSkills

## 使うツール・ライブラリ

- git
- コードレビューツール

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（Free tierはSkills非対応）
- Claude Code CLIまたはClaude.ai、Claude APIへのアクセス
- YAMLとMarkdownの基本知識
- gitによるバージョン管理の基礎（チーム配布する場合）
- Skillsが実行するスクリプト言語（Python、JavaScript等）の基礎知識（カスタムSkills作成時）
