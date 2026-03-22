# SKILL.md 標準形式で独自スキルを作成・共有する

> skill-creator テンプレートを使い、name/description/使用タイミング/具体的手順を記述した SKILL.md を作成し、GitHubで公開してコミュニティに貢献する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

組織固有のベストプラクティスや独自ツールチェーンの使い方をスキル化することで、チーム全体での再利用性と知識継承が可能になるから

## いつ使うのか

チーム独自のワークフロー・ツール・コーディング規約をAIに学習させたいとき、汎用的な知識を発見して他者と共有したいとき

## やり方

1. https://github.com/anthropics/skills/tree/main/skills/skill-creator をベースにする
2. name, description, 使用条件（when to use）を明確に定義
3. 具体的な手順・コード例・前提条件を記述
4. ~/.claude/skills/ に配置してローカルテスト
5. GitHub にリポジトリを作成して公開
6. awesome-claude-skills にPR を送る

### 入力

- 標準化したいワークフロー・ノウハウ
- skill-creator テンプレート

### 出力

- SKILL.md ファイル
- GitHub リポジトリ
- コミュニティへの貢献（PR）

## 使うツール・ライブラリ

- skill-creator template
- GitHub
- markdown

## コード例

```
---
name: my-custom-workflow
description: Deploy to AWS with CDK and run integration tests
---

## When to use
Use when deploying infrastructure changes to AWS staging/production environments.

## Steps
1. Run `cdk synth` to validate CloudFormation templates
2. Execute `cdk deploy --require-approval never` with appropriate AWS profile
3. Wait for deployment completion (check CloudFormation stack status)
4. Run integration tests against deployed endpoints
5. If tests fail, run `cdk rollback` immediately
```

## 前提知識

- Claude Code の基本的な使い方（セットアップ、セッション開始、基本的なプロンプト）
- ~/.claude/skills/ ディレクトリの役割とスキル読み込みの仕組み
- SKILL.md の基本構造（name, description, 使用条件等のフロントマター）
- git の基本操作（clone, pull）
- ターミナル/コマンドラインの基本操作
- （MCP利用時）Node.js/Python環境、API認証の基礎知識

## 根拠

> 「A curated list of Claude Skills」 - awesome-claude-skills リポジトリの冒頭文
