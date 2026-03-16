---
name: x-scout
description: X投稿URLを受け取り、技術情報の抽出・スキル化・再現キット生成・検証レポート作成を自動実行するスキル
triggers:
  - "x.com"
  - "twitter.com"
  - "/status/"
  - "この投稿"
  - "このツイート"
  - "このポスト"
  - "スキル抽出"
  - "技術調査"
  - "使えそう"
  - "良さそう"
  - "試してみたい"
  - "取り込みたい"
  - "分析して"
---

# X Scout - X投稿からの技術発見・スキル化スキル

## 概要

X投稿のURLを受け取り、sennin_scoutのx_skill_minerパイプラインを実行して:
1. 投稿内容をスクレイピング
2. リンク先を深掘り
3. 技術的な知見をスキルとして抽出
4. ローカル再現キットを生成
5. 検証レポートを作成

ユーザーは「このX投稿が良さそう」とURLを投げるだけ。

## 実行手順

### 1. URLの検出

ユーザーのメッセージからX/Twitter URLを抽出する。パターン:
```
https://x.com/{user}/status/{id}
https://twitter.com/{user}/status/{id}
```

複数URLが含まれる場合はすべて処理する。

### 2. パイプライン実行

```bash
cd /Users/kazuyaegusa/KEWORK/sennin_scout && python3 -m x_skill_miner '{URL}'
```

複数URLの場合:
```bash
cd /Users/kazuyaegusa/KEWORK/sennin_scout && python3 -m x_skill_miner '{URL1}' '{URL2}'
```

cookiesファイルが `.env` の `X_COOKIES_FILE` に指定されている場合:
```bash
cd /Users/kazuyaegusa/KEWORK/sennin_scout && python3 -m x_skill_miner --cookies "$X_COOKIES_FILE" '{URL}'
```

**タイムアウト**: パイプラインはLLM呼び出しを含むため、1URLあたり最大5分かかる。`timeout` を 600000 (10分) に設定する。

### 3. 結果の確認と報告

パイプライン完了後、以下を確認してユーザーに報告する:

#### 抽出されたスキル
```bash
ls ~/.claude/skills/x-mined/
cat ~/.claude/skills/x-mined/index.json | python3 -m json.tool | tail -30
```

#### 再現キット
```bash
ls ~/.claude/x-reproductions/
cat ~/.claude/x-reproductions/index.json | python3 -m json.tool | tail -30
```

### 4. 報告フォーマット

パイプライン結果を以下の形式で報告する:

```
## X Scout 結果

**投稿**: {URL}
**著者**: {著者名}

### 抽出されたスキル
- [{カテゴリ}] {スキル名}: {説明}
- [{カテゴリ}] {スキル名}: {説明}

### 再現キット
- {タイトル}: {パス}

### 次のアクション候補
- [ ] 再現キットを試す → `cd {再現キットパス} && cat README.md`
- [ ] スキルをClaude Codeで使う → 次回から自動トリガー
- [ ] 詳細調査が必要 → kework-web-research スキルで深掘り
```

### 5. seed_urls.txt への記録

処理したURLを `data/seed_urls.txt` に追記して履歴を残す（重複チェック付き）:

```bash
cd /Users/kazuyaegusa/KEWORK/sennin_scout
grep -qF '{URL}' data/seed_urls.txt || echo '{URL}' >> data/seed_urls.txt
```

### 6. 検証レポートの作成（オプション）

ユーザーが「レポートにして」「まとめて」と言った場合、またはパイプライン結果が特に有用な場合:

1. `data/reports/` に `{YYYY-MM-DD}_{topic}_report.md` を作成
2. WorkOSレポート (`data/reports/2026-03-16_workos_report.md`) を参考フォーマットとして使用
3. 以下を含める:
   - サービス/ツールの概要
   - 主要機能
   - 料金体系（あれば）
   - 当社での活用シナリオ
   - 競合比較
   - リスク・注意点
   - 推奨アクション

## エラー時の対応

| エラー | 対処 |
|--------|------|
| `ModuleNotFoundError` | `cd /Users/kazuyaegusa/KEWORK/sennin_scout && pip install -r requirements.txt` |
| `Credit balance is too low` | `ANTHROPIC_API_KEY` が環境に漏れていないか確認。`claude -p` はサブスク認証を使う |
| スクレイピング失敗 | Syndication APIフォールバックで動作するはず。完全に失敗した場合はURL形式を確認 |
| タイムアウト | LLM呼び出しが遅い場合がある。再実行で解決することが多い |

## 注意事項

- `claude -p` 実行時は `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_BASE_URL` を環境から除外する（パイプライン内部で自動処理済み）
- スキル出力先: `~/.claude/skills/x-mined/`
- 再現キット出力先: `~/.claude/x-reproductions/`
