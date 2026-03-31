---
name: search-skills
description: AIスキルカタログからキーワードで検索する
---

以下の SQLite データベースからスキルを検索してください。

**データベース**: 以下のパスを順に探し、最初に見つかったものを使用してください:
1. `~/KEWORK/claude_research/data/skills.db`
2. `~/Documents/01_Global/claude_research/data/skills.db`
3. `~/KEWORK/core/claude_research/data/skills.db`

見つからない場合は「skills.db が見つかりません。claude_research リポをクローンしてください」と表示してください。

**検索キーワード**: $ARGUMENTS

以下の SQL を実行して結果を表示してください:

```sql
SELECT name, category, quality_score, stars, evaluation_summary, source_url
FROM skills
WHERE (name LIKE '%keyword%' OR description LIKE '%keyword%')
ORDER BY COALESCE(quality_score, 0) DESC, stars DESC
LIMIT 20;
```

（keyword は $ARGUMENTS の内容で置換）

結果は以下の形式で表示:
1. スキル名、カテゴリ、スコア、★数
2. 評価サマリー
3. GitHub URL
