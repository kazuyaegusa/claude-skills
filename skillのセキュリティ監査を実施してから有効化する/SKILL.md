# Skillのセキュリティ監査を実施してから有効化する

> コミュニティSkillや自作Skillを有効化する前に、SKILL.md・scripts/の全コードをレビューし、データ窃取・プロンプトインジェクション・権限昇格リスクがないか確認する。

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

SkillはClaude環境で任意コード実行可能なため、悪意あるSkillは認証情報窃取やシステム侵害を引き起こしうる。特にEnterprise環境では一度の侵害が組織全体に波及。

## いつ使うのか

コミュニティSkillを初めて導入する時、自作Skillをチーム配布する前、Enterprise環境でSkillを運用する時。

## やり方

1. Skillインストール前にGitHubリポジトリの作者・スター数・コミット履歴を確認
2. SKILL.mdで外部API呼び出し・ファイルアクセス・環境変数参照の有無をチェック
3. scripts/内の全スクリプトをコードレビュー（特にネットワーク通信・eval使用・シェル実行）
4. テスト環境で動作検証（本番データを使わない）
5. Enterpriseの場合は内部リポジトリでバージョン管理し、承認プロセスを経てから配布
6. 定期監査（四半期ごと等）で不要Skillの削除と更新チェック

### 入力

- Skillのソースコード（SKILL.md + scripts/）
- 作者の信頼性情報（GitHub履歴、コミュニティ評価）

### 出力

- セキュリティ監査レポート
- 承認済みSkillリスト

## 使うツール・ライブラリ

- コードレビューツール
- gitバージョン管理
- 内部リポジトリ

## 前提知識

- Claude Pro/Max/Team/Enterprise契約（Free tierではSkills利用不可）
- YAML frontmatter、Markdownの基本文法
- gitによるバージョン管理の知識（Skill配布・更新管理に必要）
- Claude.ai/Code/APIのいずれかの使用経験
- （開発系Skillの場合）対象フレームワーク・ライブラリの基礎知識
