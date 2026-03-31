# CLI+SKILLSによるトークン効率化

> MCPサーバーの代わりにPlaywright CLIとSKILLSを使ってブラウザ自動化を実行し、コンテキストウィンドウの消費を削減する

- 出典: https://github.com/microsoft/playwright-mcp
- 投稿者: microsoft
- カテゴリ: agent-orchestration

## なぜ使うのか

MCPは大きなツールスキーマと冗長なアクセシビリティツリーをLLMコンテキストに読み込むため、コーディングエージェントが大規模コードベース、テスト、推論を同時に扱う際にコンテキストウィンドウを圧迫する。CLI+SKILLSは簡潔なコマンドベースで動作するため、同じ機能をより少ないトークンで実現できる。

## いつ使うのか

コーディングエージェントが大規模コードベース、テスト、推論を限られたコンテキストウィンドウ内でバランスよく扱う必要がある場合。トークンコストが制約となる高スループット環境。

## やり方

1. Playwright MCPサーバーの代わりにPlaywright CLIをインストール
2. SKILLSとしてブラウザ自動化コマンドを定義（例: `playwright navigate <url>`, `playwright click <selector>`など）
3. LLMエージェントがブラウザ操作が必要な場合、MCPツール呼び出しの代わりにCLIコマンドを実行
4. CLI出力を解析してエージェントの次のアクションを決定

### 入力

- Playwright CLI（インストール済み）
- SKILLSとして定義されたブラウザ自動化コマンド
- コーディングエージェントのコマンド実行機能

### 出力

- トークン消費の削減
- コンテキストウィンドウの効率的な利用
- ブラウザ自動化の実行結果

## 使うツール・ライブラリ

- Playwright CLI
- SKILLS機構（エージェントフレームワーク依存）

## 前提知識

- Model Context Protocol (MCP)の基本概念
- Playwrightブラウザ自動化フレームワークの基礎知識
- LLMエージェントのコンテキストウィンドウとトークン制限の理解
- CLIとSKILLSの概念（コーディングエージェント向け）
- Node.jsとnpxの基本的な使い方

## 根拠

> 「Fast and lightweight. Uses Playwright's accessibility tree, not pixel-based input.」
