# プロジェクト横断的な審査ガイドライン違反スキャン

> Xcodeプロジェクト内のソースコード・Info.plist・entitlements・設定ファイルを横断的に検査し、100以上の審査ガイドライン項目に照らして違反を検出する

- 出典: https://x.com/qingq77/status/2035225641398710554
- 投稿者: Geek Lite
- カテゴリ: other

## なぜ使うのか

単一ファイルの問題だけでなく、複数ファイルにまたがる設定の不整合や、コード内の不適切なAPI利用もリジェクト原因になるため

## いつ使うのか

Xcodeプロジェクトのコーディング完了後、App Store提出前の全数チェック時

### 具体的な適用場面

- iOS/macOSアプリをApp Storeに初めて提出する前
- 過去にリジェクトされたことがあり、再発防止したいとき
- サブスクリプション・IAP・UGC・子供向けなど、審査が厳しいカテゴリのアプリ開発時
- CI/CDパイプラインでApp Store提出前の自動品質チェックを導入したいとき

## やり方

1. AIエージェントにXcodeプロジェクトのルートディレクトリを指定
2. スキルが以下を自動検査:
   - Info.plistの必須キー（NSPrivacyAccessedAPITypes, NSUserTrackingUsageDescription等）
   - コード内の禁止API呼び出し（プライベートAPI、非推奨SDK等）
   - entitlementsの不適切な宣言
   - サードパーティSDKのガイドライン違反
3. 違反項目ごとに該当ファイル・行番号・修正方法を提示

### 入力

- Xcodeプロジェクト（.xcodeproj/.xcworkspace）
- ソースコード（Swift/Objective-C）
- Info.plist, entitlements, Build Settings

### 出力

- ガイドライン違反の詳細リスト（ファイル名・行番号・違反内容）
- 修正推奨事項

## 使うツール・ライブラリ

- app-store-preflight-skills
- Claude Code等のAIエージェント

## 前提知識

- iOS/macOSアプリ開発の基礎知識
- Xcodeプロジェクトの構造理解
- App Store審査プロセスの概要把握
- Claude Code等のAIエージェントツールの基本操作
- npm/npxコマンドの利用経験

## 根拠

> 终于有人把 App Store 被拒的坑整理成规则库了

> 这是个给 Claude Code AI Agent 用的 skill，专门在提交前扫描 iOS/macOS 项目的元数据、代码、配置，抓常见导致被拒的问题

> npx skills add truongduy2611/app-store-preflight-skills

> This skill integrates with the `asc` CLI (`brew install asc`) and the ASC CLI Skills

> The `references/guidelines/` directory contains a **complete index of all 100+ Apple Review Guidelines** and **10 app-type specific checklists**
