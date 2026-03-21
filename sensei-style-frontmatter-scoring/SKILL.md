# Sensei-style Frontmatter Scoring

> SkillのYAMLフロントマターに `triggers` (使うべき場面), `anti_triggers` (使ってはいけない場面), `compatibility` (対応Agent)を定義し、スコアリングする

- 出典: https://github.com/microsoft/skills
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

Skillの説明が曖昧だと、Agentが「いつ使うべきか」判断できない。triggerを明示することで、ユーザーの入力(例: 'Cosmos DB接続')に対して自動的に正しいSkillが選ばれる。Senseiパターンでは、この情報の充実度を定量評価する

## いつ使うのか

Skillを公開前に品質チェックしたい時、複数Skillが似た用途で競合する時(triggerで自動選択させる)

## やり方

1. SKILL.mdのYAMLフロントマターに以下を追加:
   - `description`: 150文字以上推奨
   - `triggers`: ["cosmos db", "nosql", "partition key"] 等のキーワードリスト
   - `anti_triggers`: ["sql server", "relational"] 等の除外キーワード
   - `compatibility`: ["copilot", "claude", "gemini"] 等の対応Agent
2. Test harnessでフロントマターを解析し、Low/Medium/Medium-High/Highにスコアリング
3. Low(説明のみ)→Medium(説明150文字以上+triggers)→Medium-High(triggers+anti_triggers)→High(+compatibility)と段階評価

### 入力

- SKILL.mdのYAMLフロントマター

### 出力

- Low/Medium/Medium-High/Highのスコア
- 不足しているフィールドの警告

## 使うツール・ライブラリ

- YAML parser
- Sensei scoring logic

## コード例

```
---
name: azure-cosmos-db-py
description: |
  Cosmos DB patterns for Python — FastAPI service layer, dual auth (AAD + connection string),
  partition key strategies, TDD with pytest-asyncio. Use DefaultAzureCredential for production.
triggers:
  - cosmos db
  - nosql
  - partition key
  - globally distributed database
anti_triggers:
  - sql server
  - relational database
  - mysql
compatibility:
  - copilot
  - claude
  - gemini
---
```

## 前提知識

- AI Coding Agent(GitHub Copilot/Claude/Gemini等)の基本操作
- Git/シンボリックリンクの理解
- YAMLフロントマターの読み書き
- Azure SDK/Foundry SDK(対象ドメイン)の基礎知識
- CI/CD(GitHub Actions等)でのテスト自動化経験(テストハーネス活用時)

## 根拠

> "Sensei-style Scoring — Skills are evaluated on frontmatter compliance: Low(Basic description only) / Medium(Description > 150 chars, has trigger keywords) / Medium-High(Has triggers AND anti-triggers) / High(Triggers + anti-triggers + compatibility field)"

> "128 skills with 1158 test scenarios — all skills have acceptance criteria and test scenarios."
