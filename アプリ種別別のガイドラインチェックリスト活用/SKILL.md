# アプリ種別別のガイドラインチェックリスト活用

> 全アプリ共通・サブスク/IAP・UGC・子供向け・ヘルスケア・ゲーム・macOS・AI・金融等、10種類の特化チェックリストから該当するものを選んで検証する

- 出典: https://x.com/qingq77/status/2035225641398710554
- 投稿者: Geek Lite
- カテゴリ: other

## なぜ使うのか

App Storeの審査基準はアプリ種別により異なり、該当カテゴリ特有の違反パターンを見落とすとリジェクトされるため

## いつ使うのか

サブスクリプション・IAP・UGC・子供向け・ヘルスケア・AI機能等、特別な審査基準が適用されるアプリを開発しているとき

### 具体的な適用場面

- iOS/macOSアプリをApp Storeに初めて提出する前
- 過去にリジェクトされたことがあり、再発防止したいとき
- サブスクリプション・IAP・UGC・子供向けなど、審査が厳しいカテゴリのアプリ開発時
- CI/CDパイプラインでApp Store提出前の自動品質チェックを導入したいとき

## やり方

1. `references/guidelines/by-app-type/` ディレクトリ内のチェックリストを確認
2. 自分のアプリに該当するもの（例: subscription_iap.md, social_ugc.md）を特定
3. AIエージェントに「このチェックリストに従ってプロジェクトをスキャンせよ」と指示
4. 各チェック項目に対する検証結果を取得

### 入力

- アプリのカテゴリ・機能特性の把握
- Xcodeプロジェクト
- Info.plist, entitlements等の設定ファイル

### 出力

- カテゴリ特化ガイドライン違反の検出結果
- 修正が必要な箇所のリスト

## 使うツール・ライブラリ

- app-store-preflight-skills
- references/guidelines/by-app-type/*.md

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
