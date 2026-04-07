# アクセシビリティツリーベースの自動化を実装する

> スクリーンショットや視覚モデルではなく、構造化されたアクセシビリティスナップショットでブラウザ操作を行う

- 出典: https://github.com/microsoft/playwright-mcp
- 投稿者: microsoft
- カテゴリ: automation-pipeline

## なぜ使うのか

画像ベース入力より高速・軽量で、視覚モデル不要、曖昧さが少なく決定的なツール適用が可能

## いつ使うのか

LLMにブラウザ操作をさせる際、スクリーンショット解析よりも高速・決定的な操作が必要な場合

## やり方

1. browser_snapshotツールでページのアクセシビリティツリーを取得
2. ツリー内の要素をref（参照ID）で特定
3. browser_click, browser_type等のツールにrefを渡して操作
4. 視覚情報ではなく構造情報（role, accessible name等）でページを理解

### 入力

- ブラウザページ
- アクセシビリティツリー取得ツール（browser_snapshot）

### 出力

- 構造化されたページスナップショット（Markdown形式）
- 要素参照ID（ref）
- 決定的なツール呼び出し

## 使うツール・ライブラリ

- Playwright
- @playwright/mcp

## 前提知識

- Model Context Protocol（MCP）の基本概念
- Playwrightの基本的な使い方
- コーディングエージェント（Claude Code/Copilot等）のアーキテクチャ
- トークン消費とコンテキストウィンドウの制約に関する理解
- アクセシビリティツリーの概念
