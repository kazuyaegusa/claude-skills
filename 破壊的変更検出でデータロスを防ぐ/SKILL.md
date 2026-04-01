# 破壊的変更検出でデータロスを防ぐ

> AtlasがマイグレーションSQL生成時に自動的にDROP COLUMNなど破壊的変更を検出し、データ損失リスクを警告・ブロックする

- 出典: https://x.com/naaaamickey/status/2028845338896073107
- 投稿者: なみっきー
- カテゴリ: agent-orchestration

## なぜ使うのか

AIエージェントや自動化パイプラインがスキーマ変更を実行する際、人間が気づかないデータロスが発生する危険性がある。Atlas DS102などのルールで破壊的変更を明示的に承認制にする

## いつ使うのか

本番環境やステージング環境でマイグレーションを実行する時。特にCI/CDパイプラインで自動適用する前に人間のレビューを挟みたい場合

### 具体的な適用場面

- AIエージェントにデータベース操作を任せたいが安全性が心配な場合
- 複数環境（dev/staging/prod）でスキーマドリフトが発生している場合
- マイグレーションの破壊的変更を人間がレビューする体制を作りたい場合
- DBスキーマ変更をGitOpsフローに組み込みたい場合

## やり方

1. atlas schema apply 実行時、Atlasが計画中のALTER文を分析
2. DROP COLUMN、DROP TABLE、データ型変更などを検出
3. データが存在するカラムの削除は DS102 エラーで自動ブロック
4. --auto-approve フラグなしでは適用されない
5. 明示的に承認が必要な場合のみ --auto-approve を追加

### 入力

- 変更前後のスキーマ定義
- 現在のDB内のデータ状態

### 出力

- 破壊的変更の検出結果（DS102など）
- ブロックされたマイグレーション計画

## 使うツール・ライブラリ

- Atlas CLI
- Atlas Destructive Change Detection (DS102)

## コード例

```
-- destructive change detected:
DS102: column "category_description" contains data
Destructive change blocked. Data loss detected.
Migration rejected.
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
