# Skillのセキュリティレビューを実施する

> Skillをインストールする前に、SKILL.mdと全スクリプトをレビューし、悪意あるコードや脆弱性がないか確認する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

Skillは任意のコードをClaude環境で実行できる。信頼できないソースからのSkillは、データ流出やプロンプトインジェクション攻撃のリスクがある

## いつ使うのか

コミュニティSkillをインストールする前、またはエンタープライズ環境でSkillを承認する前

## やり方

1. SKILL.mdの内容を精読し、意図した動作と一致するか確認
2. scripts/内の全スクリプトをコードレビュー
3. 外部API呼び出し、ファイルアクセス、センシティブデータ要求の有無をチェック
4. 信頼できるソース（公式リポジトリ、既知の開発者）からのみインストール
5. 本番環境へのデプロイ前に非本番環境でテスト
6. 定期的に監査・アップデート確認

### 入力

- Skillのソースコード（SKILL.md + scripts + resources）
- ソースの信頼性情報

### 出力

- セキュリティレビューレポート
- 承認/却下の判断

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（無料tierはSkills非対応）
- Claude.ai Web、Claude Code CLI、またはClaude APIへのアクセス
- YAMLフロントマターの基本的な理解
- （カスタムSkill作成時）Pythonやシェルスクリプトの基礎知識
