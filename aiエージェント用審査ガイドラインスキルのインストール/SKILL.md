# AIエージェント用審査ガイドラインスキルのインストール

> App Store審査ガイドラインをAIエージェントが実行可能な形式で提供するスキルをローカル環境に導入する

- 出典: https://x.com/qingq77/status/2035225641398710554
- 投稿者: Geek Lite
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Code等のAIエージェントがXcodeプロジェクトを自動スキャンし、審査ガイドライン違反を検出できるようにするため

## いつ使うのか

App Store提出前の自動チェック環境を初めて構築するとき

### 具体的な適用場面

- iOS/macOSアプリをApp Storeに初めて提出する前
- 過去にリジェクトされたことがあり、再発防止したいとき
- サブスクリプション・IAP・UGC・子供向けなど、審査が厳しいカテゴリのアプリ開発時
- CI/CDパイプラインでApp Store提出前の自動品質チェックを導入したいとき

## やり方

1. ターミナルで `npx skills add truongduy2611/app-store-preflight-skills` を実行
2. スキルが `~/.claude/skills/` 等のディレクトリにインストールされる
3. AIエージェントがこのスキルを参照して審査前チェックを実行可能になる

### 入力

- npm/npxが利用可能な環境
- AIエージェント（Claude Code等）が動作する環境

### 出力

- インストールされたapp-store-preflightスキル
- AIエージェントから参照可能なガイドラインデータベース

## 使うツール・ライブラリ

- npx
- skills CLI
- truongduy2611/app-store-preflight-skills

## コード例

```
npx skills add truongduy2611/app-store-preflight-skills
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
