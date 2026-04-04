# CLIベースSKILLS統合でトークン効率化

> MCPサーバーではなくPlaywright CLIをSKILLSとして公開し、エージェントが簡潔なコマンド実行でブラウザ操作する

- 出典: https://github.com/microsoft/playwright-mcp
- 投稿者: microsoft
- カテゴリ: agent-orchestration

## なぜ使うのか

MCPは大量のツールスキーマとアクセシビリティツリーをコンテキストに読み込むが、CLIは必要最小限の引数だけで済み、コーディングエージェントが並行処理する他タスク（コード生成・テスト・推論）のためのトークン余地を確保できる

## いつ使うのか

コーディングエージェントが大規模コードベース・テスト・推論をブラウザ自動化と並行実行する場合

## やり方

1. Playwright CLIをインストール（https://github.com/microsoft/playwright-cli）
2. CLIコマンドをSKILLSとしてエージェント設定に登録
3. エージェントは `playwright <command>` 形式で簡潔に呼び出し
4. 出力はstdoutから取得、コンテキスト負荷を最小化

### 入力

- Playwright CLI
- エージェント設定ファイル（SKILLS定義）

### 出力

- トークン消費削減
- 並行処理性能向上

## 使うツール・ライブラリ

- Playwright CLI
- SKILLS機能を持つコーディングエージェント

## 前提知識

- MCP（Model Context Protocol）の基本概念
- コーディングエージェントのコンテキストウィンドウ制約
- Playwrightの基本操作知識
- トークン効率とエージェント性能の関係

## 根拠

> Uses Playwright's accessibility tree, not pixel-based input. No vision models needed, operates purely on structured data
