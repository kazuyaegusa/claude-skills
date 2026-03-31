---
name: list-skills
description: インストール済みスキルと高品質スキルの一覧を表示する
---

以下の SQLite データベースからスキル一覧を表示してください。

**データベース**: 以下のパスを順に探し、最初に見つかったものを使用してください:
1. `~/KEWORK/claude_research/data/skills.db`
2. `~/Documents/01_Global/claude_research/data/skills.db`
3. `~/KEWORK/core/claude_research/data/skills.db`

見つからない場合は「skills.db が見つかりません。claude_research リポをクローンしてください」と表示してください。

## 1. インストール済みスキル

```sql
SELECT name, slug, category, quality_score, install_location
FROM skills WHERE is_installed = 1
ORDER BY quality_score DESC;
```

## 2. カテゴリ別 Top 5（品質スコア順）

各カテゴリ（claude-code, prompts, mcp-servers, tools）について:

```sql
SELECT name, slug, category, quality_score, stars, evaluation_summary
FROM skills WHERE category = '{category}'
ORDER BY COALESCE(quality_score, 0) DESC, stars DESC
LIMIT 5;
```

## 3. カタログ統計

```sql
SELECT category, COUNT(*) as cnt,
       ROUND(AVG(quality_score), 2) as avg_score
FROM skills GROUP BY category ORDER BY cnt DESC;
```
