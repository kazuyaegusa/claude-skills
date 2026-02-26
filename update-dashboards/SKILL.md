---
name: update-dashboards
description: MTGトランスクリプトの新規ファイルを検知し、分析・ナレッジベース・HTMLダッシュボード2種を自動更新するスキル。
user_invocable: true
---

# Update Dashboards — MTG分析・ダッシュボード自動更新スキル

サークルバック経由で蓄積されるMTGトランスクリプトの新規ファイルを検知し、分析レポートとHTMLダッシュボード3種（aiseed_overview.html, sennin_system.html, relationship_graph.html）を更新する。

## 対象プロジェクト

- **プロジェクトディレクトリ**: `/Users/kazuyaegusa/KEWORK/aixeed_mt/`
- **トランスクリプトディレクトリ**: `/Users/kazuyaegusa/KEWORK/shared/mtg_transcripts/`
- **処理済みファイル追跡**: `/Users/kazuyaegusa/KEWORK/aixeed_mt/.processed_transcripts`

## 実行手順

### Phase 1: 新規ファイル検知

1. `.processed_transcripts` ファイルを読み込む（存在しない場合は空リストとして扱う）
2. トランスクリプトディレクトリの全 `.md` ファイルを `Bash` の `ls` で取得する
3. 処理済みリストと比較し、未処理のファイルを特定する
4. 未処理ファイルがない場合は「新規トランスクリプトはありません」と報告して終了する

### Phase 1.5: OpenClawデータ読み込み

1. `scripts/openclaw_digest.md` を `Read` で読み込む（`scripts/extract_openclaw.py` が事前に生成している）
2. 「新規データなし。更新不要。」と記載されている場合はスキップしてPhase 2へ進む
3. 新規データがある場合、以下を抽出する:
   - Discord/Slack の主要メッセージとそのサマリー
   - 新規タスク一覧
   - プロジェクト別メッセージ集計
   - チャンネル別活動量

### Phase 2: 新規トランスクリプトの読み込みと分析

1. 未処理の各ファイルを `Read` ツールで読み込む（並列化可能）
2. 各トランスクリプトを以下のカテゴリに分類する:
   - **開発MTG**: 仙人システム・技術・実装に関する議論 → `analysis_dev.md` に追記
   - **戦略・事業MTG**: 資金調達・事業計画・レベシアに関する議論 → `analysis_strategy.md` に追記
   - **顧客MTG**: FusionAI・顧客・営業に関する議論 → `analysis_customer.md` に追記
3. 各トランスクリプトから以下を抽出する:
   - **要約**: 主要な議題と結論（3-5行）
   - **新規事実**: これまでのナレッジベースにない情報
   - **仙人システム関連**: アーキテクチャ・機能・仕様の変更や新情報
   - **意思決定**: 確定した方針・決定事項
   - **課題・TODO**: 新たに発見された課題や残タスク
4. Phase 1.5 でOpenClawデータを取得している場合、Discord/Slackのデータからも以下を抽出してMTGトランスクリプトと統合する:
   - **新規事実**: Discord/Slackで共有された新情報
   - **意思決定**: チャット上で確定した方針・決定事項
   - **課題/TODO**: チャットで挙がった課題や新タスク

### Phase 3: 分析レポート更新

1. `analysis_dev.md` / `analysis_strategy.md` / `analysis_customer.md` を `Read` で読み込む
2. カテゴリに応じて該当ファイルに新規MTGの分析を追記する
3. 追記フォーマット:
   ```markdown
   ### {ファイル名から抽出したMTGタイトル}（{日付}）
   - **参加者**: {判別可能な場合}
   - **主要議題**: {箇条書き}
   - **決定事項**: {箇条書き}
   - **課題/TODO**: {箇条書き}
   ```

### Phase 4: ナレッジベース更新

1. `knowledge_base.md` を `Read` で読み込む
2. Phase 2 で抽出した「新規事実」をナレッジベースの該当セクションに統合する
3. 既存の情報と矛盾する場合は、新しい情報を優先し、変更を明記する
4. 新規事実がない場合はスキップする

### Phase 5: HTMLダッシュボード更新

#### aiseed_overview.html

1. `aiseed_overview.html` を `Read` で読み込む
2. 以下のタブ/セクションを更新対象とする:
   - **経営概要**: 新規の事業数値・マイルストーン
   - **仙人システム**: 技術仕様の変更・新機能
   - **レベシア**: 投資戦略・LP情報の更新
   - **顧客**: 新規顧客情報・案件進捗
   - **タイムライン**: 新規イベント・マイルストーン
   - **課題**: 新規課題の追加、既存課題のステータス更新
3. **コミュニケーションタブ**が存在する場合、以下をOpenClawデータから更新する:
   - Discord/Slackのチャンネル別活動サマリー
   - 主要な議論・決定事項
   - 新規タスク一覧
   - プロジェクト別メッセージ統計
4. `Edit` ツールで該当箇所を更新する

#### sennin_system.html

1. `sennin_system.html` を `Read` で読み込む
2. 以下のセクションを更新対象とする:
   - **アーキテクチャ**: 構成変更があれば図を更新
   - **技術スタック**: 新ツール・ライブラリの追加
   - **開発タイムライン**: 新マイルストーン・進捗
   - **課題トラッカー**: 新課題の追加、既存課題の解決
   - **開発体制**: 体制変更があれば更新
3. `Edit` ツールで該当箇所を更新する

#### relationship_graph.html（人間関係図）

1. `relationship_graph.html` を `Read` で読み込む
2. 新規MTGで判明した人物関係の変更を反映する:
   - **新規人物の追加**: `nodes` 配列に新ノードを追加（id, name, sub, type, role, desc, size, involvement）
   - **新規関係の追加**: `edges` 配列に新エッジを追加（source, target, type, label）
   - **既存人物の更新**: 役職変更、関与領域の追加
   - **type分類**: core / engineer / advisor / partner / external / client
   - **edge type分類**: management / tech / business / customer / other
3. `Edit` ツールで `nodes` または `edges` の配列に要素を追加/更新する
4. `nodeCount` / `edgeCount` の表示は自動計算されるため変更不要

### Phase 6: 処理済みファイル追跡の更新

1. 処理した全ファイル名を `.processed_transcripts` に追記する
2. ファイルは改行区切りのテキストファイル

### Phase 7: コミット・プッシュ

1. 変更されたファイルをすべて `git add` する
2. コミットメッセージ: `ダッシュボード更新: 新規MTG {N}件を分析・反映`
3. `git push origin main` でプッシュする

## 注意事項

- **推測しない**: トランスクリプトの内容に基づいてのみ更新する
- **既存情報を壊さない**: 追記・更新のみ。既存の正確な情報は削除しない
- **HTMLの構造を維持**: CSSやJavaScriptの構造は変えない。データ部分のみ更新
- **大量の新規ファイル**: 20件以上ある場合は Agent Team を編成して並列処理する
- **トランスクリプトの品質**: サークルバックの文字起こし精度に依存するため、不明瞭な部分は「不明」と記載する
- レポートは日本語で書く
- **OpenClaw DBは直接操作しない**: SQLiteは触らず、`openclaw_digest.md` のみを情報源とする
- **Discord/Slackのプライバシー**: メッセージは要約のみ使用し、個人的な会話は省略する

## Agent Team 編成基準

新規トランスクリプトが **5件以上** の場合、以下のチーム構成で並列処理する:

| エージェント | 型 | 担当 |
|------------|------|------|
| analyzer-dev | Explore | 開発MTGの分析 |
| analyzer-strategy | Explore | 戦略MTGの分析 |
| analyzer-customer | Explore | 顧客MTGの分析 |
| updater | general-purpose | 分析結果を受けてファイル更新・コミット |

5件未満の場合は単独で順次処理する。
