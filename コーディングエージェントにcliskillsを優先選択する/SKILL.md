# コーディングエージェントにCLI+SKILLsを優先選択する

> Playwright MCPサーバーではなくPlaywright CLIをSKILLsとして公開し、エージェントにはCLIコマンド経由でブラウザ操作をさせる

- 出典: https://github.com/microsoft/playwright-mcp
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

CLI呼び出しは大きなツールスキーマや冗長なアクセシビリティツリーをモデルコンテキストに載せないため、トークン消費が少なく、コードベース・テスト・推論を同時に扱う高スループットエージェントに適している

## いつ使うのか

コーディングエージェント（Claude Code/Copilot等）でブラウザ自動化を行う場合、またはコンテキストウィンドウが限られている場合

## やり方

1. Playwright CLIをインストール
2. エージェント用のSKILLファイルを作成し、CLI操作を定義
3. エージェントがブラウザ操作を行う際、MCPツール呼び出しではなくCLIコマンド実行を選択させる
4. CLIの簡潔な出力をエージェントが解釈して次のアクションを決定

### 入力

- Playwright CLI
- エージェント用SKILLファイル
- 対象ブラウザ（Chrome/Firefox/WebKit）

### 出力

- トークン効率の高いブラウザ自動化
- コードベース・テスト・推論との並行処理

## 使うツール・ライブラリ

- Playwright CLI
- microsoft/playwright-cli

## 前提知識

- Model Context Protocol（MCP）の基本概念
- Playwrightの基本的な使い方
- コーディングエージェント（Claude Code/Copilot等）のアーキテクチャ
- トークン消費とコンテキストウィンドウの制約に関する理解
- アクセシビリティツリーの概念

## 根拠

> 「Fast and lightweight. Uses Playwright's accessibility tree, not pixel-based input.」（Key Features）
