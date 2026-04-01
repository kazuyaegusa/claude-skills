# Atlas Schema as Codeでスキーマを宣言的に管理する

> SQLテーブル定義を宣言的なコードとして記述し、Atlasが現在のDB状態との差分を自動計算してマイグレーションを生成する

- 出典: https://x.com/naaaamickey/status/2028845338896073107
- 投稿者: なみっきー
- カテゴリ: agent-orchestration

## なぜ使うのか

手動でALTER TABLE文を書く方式では変更漏れやスキーマドリフトが発生しやすく、AIエージェントがスキーマを理解できない。宣言的管理により「あるべき状態」を定義すれば、Atlasが安全な移行手順を自動生成する

## いつ使うのか

DBスキーマ変更を頻繁に行うプロジェクトで、マイグレーション管理を自動化・安全化したい時。特にAIエージェントがスキーマを参照する必要がある場合

### 具体的な適用場面

- AIエージェントにデータベース操作を任せたいが安全性が心配な場合
- 複数環境（dev/staging/prod）でスキーマドリフトが発生している場合
- マイグレーションの破壊的変更を人間がレビューする体制を作りたい場合
- DBスキーマ変更をGitOpsフローに組み込みたい場合

## やり方

1. Atlasをインストール（brew install ariga/tap/atlas または公式サイトから）
2. schema/categories.sql に CREATE TABLE 文で望ましいスキーマを定義
3. atlas.hcl に env "local" { url = "mysql://..." } などで接続先を定義
4. atlas schema apply --env local を実行
5. Atlasが現在のDBとの差分を計算し、ALTER文を提案
6. 破壊的変更があれば DS102 エラーでブロック
7. 問題なければ承認して適用

### 入力

- 宣言的に記述されたスキーマファイル（schema/*.sql）
- atlas.hcl環境設定ファイル
- 既存データベースの接続情報

### 出力

- 自動生成されたマイグレーションSQL
- 破壊的変更の検出レポート（DS102など）
- 適用後のスキーマ状態

## 使うツール・ライブラリ

- Atlas CLI
- atlasgo.io

## コード例

```
-- schema/categories.sql
CREATE TABLE 'categories' (
  'id' int NOT NULL AUTO_INCREMENT,
  'category_name' varchar(255) NOT NULL,
  'updated_at' timestamp NULL ON UPDATE CURRENT_TIMESTAMP,
  'created_at' timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY ('id')
);

-- 実行コマンド
atlas schema apply --env local

-- 出力例
-- modify "categories" table:
-> ALTER TABLE "categories" DROP COLUMN "category_description";
-- destructive change detected: DS102
-- column "category_description" contains data
Destructive change blocked.
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
