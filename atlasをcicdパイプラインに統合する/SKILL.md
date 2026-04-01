# AtlasをCI/CDパイプラインに統合する

> atlas schema apply コマンドをGitHub Actions、GitLab CI、CircleCIなどに組み込み、スキーマ変更をGitOpsフローで管理する

- 出典: https://x.com/naaaamickey/status/2028845338896073107
- 投稿者: なみっきー
- カテゴリ: automation-pipeline

## なぜ使うのか

手動でのマイグレーション実行はヒューマンエラーや適用漏れが発生しやすい。CI/CDパイプラインに組み込むことで、コードレビュー・自動テスト・承認フローを経た安全なマイグレーションを実現

## いつ使うのか

複数人チームでDB変更を管理する場合、本番環境へのマイグレーションを自動化・安全化したい場合

### 具体的な適用場面

- AIエージェントにデータベース操作を任せたいが安全性が心配な場合
- 複数環境（dev/staging/prod）でスキーマドリフトが発生している場合
- マイグレーションの破壊的変更を人間がレビューする体制を作りたい場合
- DBスキーマ変更をGitOpsフローに組み込みたい場合

## やり方

1. .github/workflows/migrate.yml を作成
2. atlas schema apply --env prod --dry-run でマイグレーション計画を出力
3. 破壊的変更があればCI失敗・人間レビューを要求
4. 承認後に atlas schema apply --env prod --auto-approve で適用
5. Slack/Discord通知で結果を共有

### 入力

- atlas.hcl環境設定
- CI/CDパイプライン設定ファイル
- スキーマファイル（Git管理）

### 出力

- マイグレーション計画のプレビュー
- CI/CDログ
- 適用後のスキーマ状態

## 使うツール・ライブラリ

- Atlas CLI
- GitHub Actions / GitLab CI / CircleCI
- Git

## コード例

```
# .github/workflows/migrate.yml
name: DB Migration
on:
  push:
    branches: [main]
jobs:
  migrate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install Atlas
        run: curl -sSf https://atlasgo.sh | sh
      - name: Dry-run migration
        run: atlas schema apply --env prod --dry-run
      - name: Apply migration
        run: atlas schema apply --env prod --auto-approve
        if: github.event_name == 'push'
```

## 前提知識

- SQLの基本知識（CREATE TABLE、ALTER TABLE）
- マイグレーションツールの概念（Flyway、Liquibase等の経験があると理解しやすい）
- CI/CDパイプラインの基礎知識
- GitOpsの考え方（Infrastructure as Code）

## 根拠

> 「Schema as Code として宣言的に管理すればエージェントもデータモデル理解できる」

> Atlas公式サイト: 'Declarative database schema management — define your desired state, Atlas computes the plan'

> Atlas公式サイト: 'DS102: column "category_description" contains data - Destructive change blocked. Data loss detected.'

> Atlas公式サイト: 'ALTER TABLE "categories" DROP COLUMN "category_description";'

> 「運用フェーズではどうしてもSQL叩く場面が出てくる」（宣言的管理だけでは不十分なケースがある示唆）
