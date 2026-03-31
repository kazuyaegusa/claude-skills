---
name: install-skill
description: カタログからスキルを ~/.claude/skills/ にインストールする
---

指定されたスキルをインストールしてください。

**スラッグ**: $ARGUMENTS
**データベース**: 以下のパスを順に探し、最初に見つかったものを使用してください:
1. `~/KEWORK/claude_research/data/skills.db`
2. `~/Documents/01_Global/claude_research/data/skills.db`
3. `~/KEWORK/core/claude_research/data/skills.db`

**カタログ**: データベースと同じ親ディレクトリの `../catalog/raw/`

## 手順

1. DB からスキル情報を取得:
```sql
SELECT name, slug, category, source_url, quality_score FROM skills WHERE slug = '$ARGUMENTS';
```

2. `catalog/raw/{category}/{slug}/content/` から SKILL.md を探す

3. SKILL.md が存在する場合:
   - `~/.claude/skills/{slug}/` ディレクトリを作成
   - SKILL.md をコピー
   - README.md があればコピー
   - DB の is_installed を 1 に更新

4. SKILL.md が存在しない場合:
   - インストール不可の旨を表示
   - 代替として source_url を案内
