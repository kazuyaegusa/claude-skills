# アクセシビリティツリーベースの自動化

> スクリーンショットやビジョンモデルの代わりに、Playwrightのアクセシビリティツリーを使ってブラウザ操作を行う

- 出典: https://github.com/microsoft/playwright-mcp
- 投稿者: microsoft
- カテゴリ: agent-orchestration

## なぜ使うのか

スクリーンショットベースのアプローチは曖昧性が高く、ビジョンモデルが必要で、決定論的なツール適用が難しい。アクセシビリティツリーは構造化データとして明確で、LLMが直接理解でき、高速かつ軽量。

## いつ使うのか

ブラウザ自動化が必要なあらゆる場面で、特にトークン効率と決定論的動作が重要な場合。ビジョンモデルを避けたい場合。

## やり方

1. Playwright MCPの`browser_snapshot`ツールを使用してページのアクセシビリティツリーを取得
2. LLMがアクセシビリティツリーから要素のrole、name、ref（参照ID）を特定
3. `browser_click`や`browser_type`などのツールで、refパラメータを使って正確に要素を指定
4. スクリーンショットなしで操作を完了

### 入力

- Playwright MCPサーバー
- ブラウザページ

### 出力

- 構造化されたアクセシビリティスナップショット（マークダウン形式）
- 明確な要素参照（ref）
- 決定論的なブラウザ操作

## 使うツール・ライブラリ

- Playwright
- @playwright/mcp

## 前提知識

- Model Context Protocol (MCP)の基本概念
- Playwrightブラウザ自動化フレームワークの基礎知識
- LLMエージェントのコンテキストウィンドウとトークン制限の理解
- CLIとSKILLSの概念（コーディングエージェント向け）
- Node.jsとnpxの基本的な使い方

## 根拠

> 「Fast and lightweight. Uses Playwright's accessibility tree, not pixel-based input.」
