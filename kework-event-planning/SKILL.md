---
name: kework-event-planning
description: KEWORK/AiXEEDのオフ会・ミーティング・イベントの企画・会場リサーチ・日程調整・参加者案内を行うスキル。
user_invocable: true
triggers:
  - オフ会
  - 会場
  - 日程調整
  - ミーティング
  - リサーチ
  - イベント
  - 会場候補
  - 日程候補
  - オフ会の日程
  - 会場をリサーチ
  - MTG日程
  - フォローアップミーティング
  - 参加者案内
  - 開催場所
  - コワーキング
  - 懇親会
  - 貸し会議室
---

# KEWORK Event Planning — イベント企画・会場リサーチ・日程調整スキル

KEWORK/AiXEEDのオフ会、ミーティング、イベントの企画から案内文作成までを一貫して行う。

## 引数

```
/kework-event-planning <タスク内容>
```

例:
- `/kework-event-planning 福岡オフ会の日程・会場候補をリサーチする`
- `/kework-event-planning 大阪オフ会（3月30日）の会場・詳細を確定し参加者へ案内する`
- `/kework-event-planning マレーシアオフ会の実現可能性・コスト・日程を調査する`
- `/kework-event-planning 次回MTG日程を調整する（谷内・高橋・後藤）`
- `/kework-event-planning 来週金曜にテスト太郎さんとフォローアップミーティングを設定する`

## 実行手順

### Phase 0: タスク種別の判定

タスク内容から以下のいずれかに分類する:

| 種別 | 判定キーワード | 進むPhase |
|------|---------------|-----------|
| **会場リサーチ** | 会場候補、リサーチ、コワーキング、貸し会議室 | Phase 1 |
| **日程調整** | 日程調整、MTG日程、ミーティング設定 | Phase 2 |
| **イベント案内** | 案内、参加者へ、詳細を確定 | Phase 3 |
| **海外イベント調査** | マレーシア、海外、実現可能性、コスト | Phase 4 |
| **総合企画** | 上記の複数を含む | Phase 1 → 2 → 3 を順に実行 |

タスク内容が不明確な場合は `AskUserQuestion` でユーザーに確認する:
- question: "イベントの種類・場所・日程について教えてください"
- options に「オフ会（国内）」「オフ会（海外）」「オンラインMTG」「その他」を含める

---

### Phase 1: 会場リサーチ

#### Step 1.1: 地域・条件の特定

タスク内容から以下を抽出する:
- **開催地域**: 都市名（福岡、大阪、東京、etc.）
- **日程**: 指定日 or 候補期間
- **参加人数**: 不明なら10-20名をデフォルトとする
- **予算感**: 不明なら1人3,000-5,000円をデフォルトとする

#### Step 1.2: Web検索で会場候補を収集

`WebSearch` ツールで以下のクエリを順に検索する:

```
# コワーキングスペース（イベント利用可）
"{都市名} コワーキングスペース イベントスペース 貸切 {人数}人"

# 貸し会議室
"{都市名} 貸し会議室 {人数}人 {日付があれば日付}"

# レンタルスペース（懇親会向き）
"{都市名} レンタルスペース パーティー {人数}人 飲食可"
```

検索プラットフォーム別の追加クエリ:

```
# スペースマーケット
"site:spacemarket.com {都市名} イベント {人数}人"

# インスタベース
"site:instabase.jp {都市名} イベント 貸切"
```

#### Step 1.3: Google Maps / Places APIでの補完（APIキーがある場合）

環境変数 `GOOGLE_MAPS_API_KEY` が設定されている場合のみ実行する:

```bash
# 周辺の会場検索
curl -s "https://maps.googleapis.com/maps/api/place/textsearch/json?query=${都市名}+コワーキングスペース+イベント&language=ja&key=${GOOGLE_MAPS_API_KEY}" | python3 -c "
import json, sys
data = json.load(sys.stdin)
for r in data.get('results', [])[:10]:
    print(f\"- {r['name']} | 評価: {r.get('rating', 'N/A')} | {r.get('formatted_address', '')}\")"
```

APIキーがない場合はWebSearch結果のみで進める。

#### Step 1.4: 候補リスト・比較表の作成

以下のフォーマットで比較表を作成する:

```markdown
## 会場候補比較表 — {都市名}オフ会

| # | 会場名 | 場所・アクセス | 収容人数 | 料金（税込） | 設備 | 飲食 | 備考 |
|---|--------|--------------|---------|------------|------|------|------|
| 1 | {名前} | {最寄駅}徒歩{分}分 | {人数}名 | {料金}/h or {料金}/日 | WiFi, プロジェクター, etc. | 可/不可/持ち込み可 | {特記事項} |
| 2 | ... | ... | ... | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... | ... | ... | ... |

### おすすめ
- **コスパ重視**: {会場名} — {理由}
- **アクセス重視**: {会場名} — {理由}
- **懇親会向き**: {会場名} — {理由}
```

---

### Phase 2: 日程調整

#### Step 2.1: 参加者・候補日の特定

タスク内容から以下を抽出する:
- **参加者リスト**: 名前を列挙
- **候補日**: 指定日 or 期間
- **時間帯**: 不明なら平日19:00-21:00 or 土日13:00-17:00をデフォルト

#### Step 2.2: カレンダー確認（macOS Calendar.app）

ローカルのCalendar.appで既存予定を確認する:

```bash
# 指定日の予定を確認（osascript）
osascript -e '
tell application "Calendar"
    set targetDate to date "2026年3月30日"
    set endDate to targetDate + (1 * days)
    set allEvents to {}
    repeat with cal in calendars
        set evts to (every event of cal whose start date >= targetDate and start date < endDate)
        repeat with evt in evts
            set end of allEvents to (summary of evt) & " | " & (start date of evt as string) & " - " & (end date of evt as string)
        end repeat
    end repeat
    return allEvents
end tell'
```

```bash
# 特定の週の予定一覧（月曜〜日曜）
osascript -e '
tell application "Calendar"
    set startDate to date "2026年3月30日"
    set endDate to startDate + (7 * days)
    set allEvents to {}
    repeat with cal in calendars
        set evts to (every event of cal whose start date >= startDate and start date < endDate)
        repeat with evt in evts
            set end of allEvents to (summary of evt) & " | " & (start date of evt as string)
        end repeat
    end repeat
    return allEvents
end tell'
```

#### Step 2.3: iCal形式でイベント出力

日程が確定したらiCalファイルを生成する:

```bash
cat > /tmp/kework_event.ics << 'ICAL_EOF'
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//KEWORK//Event Planning//JA
BEGIN:VEVENT
DTSTART:20260330T100000
DTEND:20260330T170000
SUMMARY:KEWORK 大阪オフ会
LOCATION:{会場名}, {住所}
DESCRIPTION:KEWORK/AiXEEDオフ会\n参加者: {参加者リスト}\n詳細: {URL}
ORGANIZER:mailto:info@kework.jp
END:VEVENT
END:VCALENDAR
ICAL_EOF
echo "iCalファイル生成: /tmp/kework_event.ics"
```

#### Step 2.4: Calendar.appにイベント追加（ユーザー確認後）

**ユーザーの許可を取ってから実行する。**

```bash
osascript -e '
tell application "Calendar"
    tell calendar "KEWORK"
        set newEvent to make new event with properties {summary:"KEWORK 大阪オフ会", start date:date "2026年3月30日 10:00", end date:date "2026年3月30日 17:00", location:"{会場名}"}
    end tell
end tell'
```

---

### Phase 3: イベント案内文の作成

#### Step 3.1: 案内文テンプレート

以下のテンプレートをベースに、タスク内容に合わせてカスタマイズする:

```markdown
# {イベント名} のご案内

{挨拶文 — KEWORKメンバー各位 / AiXEEDコミュニティの皆さま}

## 開催概要

| 項目 | 詳細 |
|------|------|
| 日時 | {YYYY年MM月DD日（曜日）HH:MM - HH:MM} |
| 場所 | {会場名} |
| 住所 | {住所} |
| アクセス | {最寄駅}から徒歩{分}分 |
| 参加費 | {金額}（{内訳: 会場費 + 飲食費 etc.}） |
| 定員 | {人数}名 |
| 持ち物 | ノートPC（任意）、名刺（あれば） |

## タイムテーブル（案）

| 時間 | 内容 |
|------|------|
| {開始} | 開場・受付 |
| {+15分} | オープニング・自己紹介 |
| {+45分} | メインセッション / LT |
| {+30分} | 休憩 |
| {+60分} | ワークショップ / ディスカッション |
| {+30分} | クロージング・集合写真 |
| {終了後} | 懇親会（任意・別会計） |

## 参加申込

{申込方法の説明 — Discordスレッド / Google Form / Linear etc.}

**申込締切: {日付}**

## 会場マップ

Google Maps: {URL}

## お問い合わせ

{担当者名} / {連絡先}
```

#### Step 3.2: 媒体別フォーマット変換

案内文を以下の形式でも出力する:

- **Discord投稿用**: 2000文字以内に要約、Embed形式を意識
- **メール用**: 件名 + 本文のプレーンテキスト

---

### Phase 4: 海外イベント調査（コスト・実現可能性）

#### Step 4.1: 基本情報リサーチ

`WebSearch` で以下を調査する:

```
# フライト相場
"{出発地} {目的地} 航空券 相場 {月}"

# 宿泊相場
"{目的地} ホテル 相場 1泊 {参加人数}人"

# 会場
"{目的地} coworking space event {人数}人"

# ビザ・入国要件
"{目的地} 日本人 ビザ 入国要件 {年}"
```

#### Step 4.2: コスト見積テンプレート

```markdown
## {目的地}オフ会 コスト見積

### 1人あたりの概算

| 項目 | 最安 | 標準 | 備考 |
|------|------|------|------|
| 航空券（往復） | {金額} | {金額} | {出発地}発、{日数}泊{日数+1}日 |
| 宿泊（{泊数}泊） | {金額} | {金額} | ドミトリー / ビジネスホテル |
| 会場費（割勘） | {金額} | {金額} | {人数}人で割った場合 |
| 食費（{日数}日分） | {金額} | {金額} | 現地相場ベース |
| 交通費（現地） | {金額} | {金額} | 空港↔市内 + 移動 |
| **合計** | **{金額}** | **{金額}** | |

### 全体予算（{人数}名参加の場合）

| 項目 | 金額 |
|------|------|
| 会場費 | {金額} |
| 共用備品・通信費 | {金額} |
| 予備費（10%） | {金額} |
| **団体支出合計** | **{金額}** |

### 実現可能性の評価

- **ビザ**: {不要 / 要申請 / 詳細}
- **直行便**: {あり / なし（乗継{都市}）}
- **治安**: {概要}
- **通信環境**: {概要}
- **推奨時期**: {ベストシーズン}
- **総合判定**: {おすすめ度 ★★★★☆ + コメント}
```

---

### Phase 5: 成果物の保存

すべての成果物を以下のディレクトリに保存する:

```bash
mkdir -p ~/KEWORK/events/{イベント名_YYYYMMDD}
```

保存するファイル:
- `research.md` — 会場リサーチ結果・比較表
- `announcement.md` — 参加者案内文
- `cost_estimate.md` — コスト見積（海外の場合）
- `event.ics` — カレンダーファイル（日程確定時）

最後にユーザーに以下を報告する:
- 成果物の保存先パス
- 次のアクション（会場予約、案内送信、etc.）の提案

## 注意事項

- **事実ベース**: WebSearchで確認した情報のみを記載する。料金・空き状況は変動するため「{日付}時点の情報」と明記する
- **日本語出力**: すべての出力は日本語で行う
- **カレンダー操作は許可制**: Calendar.appへの書き込みは必ずユーザーの許可を取ってから実行する
- **APIキー不要で動作**: Google Maps APIキーがなくてもWebSearch fallbackで動作する
- **金額は税込表示**: 特に断りがなければ税込で記載する
