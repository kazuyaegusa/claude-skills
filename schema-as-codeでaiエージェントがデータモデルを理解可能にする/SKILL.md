# Schema as CodeでAIエージェントがデータモデルを理解可能にする

> DBスキーマを宣言的なコードファイルとして管理することで、AIエージェントがリポジトリ内のスキーマ定義を直接読み取り、テーブル構造・関連を理解できるようにする

- 出典: https://x.com/naaaamickey/status/2028845338896073107
- 投稿者: なみっきー
- カテゴリ: agent-orchestration

## なぜ使うのか

AIエージェントがSQLを生成したりデータ操作する際、最新のスキーマ情報が必要。マイグレーションファイルが散在していると理解困難だが、宣言的スキーマファイルなら1ファイルで全体像を把握できる

## いつ使うのか

AIエージェントにデータベース関連タスク（SQL生成、マイグレーション提案、データモデル分析）を任せる時

### 具体的な適用場面

- AIエージェントにデータベース操作を任せたいが安全性が心配な場合
- 複数環境（dev/staging/prod）でスキーマドリフトが発生している場合
- マイグレーションの破壊的変更を人間がレビューする体制を作りたい場合
- DBスキーマ変更をGitOpsフローに組み込みたい場合

## やり方

1. schema/ ディレクトリにテーブル毎のCREATE TABLE文を配置
2. schema/categories.sql、schema/users.sql など分割管理
3. AIエージェントはこれらファイルをRead toolで読み込む
4. テーブル構造・カラム型・制約を理解してSQLやマイグレーションを提案
5. atlas schema apply で実際のDBに反映

### 入力

- 宣言的スキーマファイル群（schema/*.sql）
- AIエージェントのRead tool

### 出力

- AIエージェントが理解したデータモデル
- AIが生成したSQL・マイグレーション提案

## 使うツール・ライブラリ

- Atlas CLI
- Claude Code Read tool
- Git（スキーマファイルのバージョン管理）

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
