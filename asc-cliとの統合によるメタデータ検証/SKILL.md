# asc CLIとの統合によるメタデータ検証

> App Store Connect CLI（asc）でメタデータをpullし、AIエージェントが審査ガイドラインに照らしてスクリーンショット・説明文・プライバシーポリシー等を検証する

- 出典: https://x.com/qingq77/status/2035225641398710554
- 投稿者: Geek Lite
- カテゴリ: agent-orchestration

## なぜ使うのか

メタデータ不備（誤解を招く説明、必須情報の欠落等）はコードと無関係にリジェクトされる頻出原因であるため

## いつ使うのか

App Store Connectのメタデータ入力完了後、提出前の最終チェック時

### 具体的な適用場面

- iOS/macOSアプリをApp Storeに初めて提出する前
- 過去にリジェクトされたことがあり、再発防止したいとき
- サブスクリプション・IAP・UGC・子供向けなど、審査が厳しいカテゴリのアプリ開発時
- CI/CDパイプラインでApp Store提出前の自動品質チェックを導入したいとき

## やり方

1. `brew install asc` でApp Store Connect CLIをインストール
2. `asc metadata pull` でアプリのメタデータをJSON形式でローカルにダウンロード
3. AIエージェントがpull結果のJSONを読み込み、ガイドライン違反（例: プライバシーポリシーURL欠落、スクリーンショット不足）をチェック
4. 検出された問題を修正後、`asc metadata push` で反映

### 入力

- App Store Connect APIキー
- アプリのバンドルID
- メタデータ（説明文、スクリーンショット、プライバシーポリシー等）

### 出力

- ローカルにpullされたメタデータJSON
- ガイドライン違反検出レポート

## 使うツール・ライブラリ

- asc CLI
- app-store-preflight-skills
- ASC CLI Skills (rudrankriyam/app-store-connect-cli-skills)

## コード例

```
brew install asc
asc metadata pull
# AIエージェントがpull結果をスキャン
```

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
