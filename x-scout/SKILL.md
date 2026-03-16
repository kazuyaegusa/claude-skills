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
5. **再現キットを実際に試して動作確認する**
6. 検証結果をユーザーに報告する

ユーザーは「このX投稿が良さそう」とURLを投げるだけ。スキル抽出から動作検証まで一気通貫で実行する。

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

### 4. 再現キットの自動検証

パイプライン完了後、生成された再現キットを **必ず** 実際に試す。これはオプションではなく標準フローの一部。

#### 手順

1. `~/.claude/x-reproductions/` から該当投稿IDの再現キットディレクトリを特定する
2. `README.md` を読み、セットアップ手順を確認する
3. リポジトリのclone（`/tmp/` 配下に）、依存インストールなど前提条件を整える
4. READMEの「検証手順」または「Quick Start」に従い、最小限のコマンドで動作確認する
5. 出力結果（JSON構造、終了コード、エラーの有無）を記録する

#### 判定基準

| 結果 | 判定 |
|------|------|
| 期待通りのJSON/出力が返った | OK — そのまま報告 |
| 依存不足で失敗（Camofox等） | 部分OK — 基本機能はOK、拡張機能は要追加セットアップと報告 |
| クローン/実行自体が失敗 | NG — エラー内容を報告し、代替手段を提案 |

#### 注意

- 再現キットが複数ある場合は、最も基本的なもの（starter-kit）を優先して試す
- `/tmp/` にクローンし、本番環境を汚さない
- タイムアウトは30秒に設定（ネットワーク依存のため余裕を持つ）

### 5. 報告フォーマット

パイプライン結果 **と検証結果** を以下の形式で報告する:

```
## X Scout 結果

**投稿**: {URL}
**著者**: {著者名}

### 抽出されたスキル
- [{カテゴリ}] {スキル名}: {説明}

### 再現キット検証結果

**{キット名}**: {OK / 部分OK / NG}

- 実行コマンド: `{実際に実行したコマンド}`
- 出力サンプル: {JSONの主要フィールドや出力の要約}
- 終了コード: {0/1/2}
- 所感: {sennin_scoutへの組み込み可否、品質の評価}

### 次のアクション候補
- [ ] sennin_scoutに組み込む → {具体的な組み込み方法}
- [ ] スキルをClaude Codeで使う → 次回から自動トリガー
- [ ] 詳細調査が必要 → kework-web-research スキルで深掘り
```

### 7. seed_urls.txt への記録

処理したURLを `data/seed_urls.txt` に追記して履歴を残す（重複チェック付き）:

```bash
cd /Users/kazuyaegusa/KEWORK/sennin_scout
grep -qF '{URL}' data/seed_urls.txt || echo '{URL}' >> data/seed_urls.txt
```

### 8. 検証レポートの作成（オプション）

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
