# アクセシビリティツリーベースの操作設計

> スクリーンショットではなく構造化アクセシビリティスナップショットでブラウザ操作

- 出典: https://github.com/microsoft/playwright-mcp
- 投稿者: microsoft
- カテゴリ: dev-tool

## なぜ使うのか

ビジョンモデル不要、決定論的ツール適用が可能、スクリーンショット方式の曖昧性を回避

## いつ使うのか

LLMがブラウザ操作する全ケース（CLI/MCP共通）

## やり方

1. Playwrightのaccessibility tree取得機能を活用
2. 要素セレクタはrole/accessible name/refで指定
3. 座標ベースではなくセマンティックな要素参照で操作

### 入力

- Playwrightブラウザインスタンス

### 出力

- 構造化アクセシビリティスナップショット
- 決定論的要素操作

## 使うツール・ライブラリ

- Playwright

## 前提知識

- MCP（Model Context Protocol）の基本概念
- コーディングエージェントのコンテキストウィンドウ制約
- Playwrightの基本操作知識
- トークン効率とエージェント性能の関係
