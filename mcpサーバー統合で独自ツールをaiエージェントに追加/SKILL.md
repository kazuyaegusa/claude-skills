# MCPサーバー統合で独自ツールをAIエージェントに追加

> `~/.gemini/settings.json` にMCP設定を追加し、@プレフィックスでツールを呼び出す

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

Slack, GitHub, DB, Imagen等の外部サービスをLLMのツールとして登録することで、エージェントの能力を拡張できる

## いつ使うのか

Slackへの通知、GitHubのPR操作、DBクエリ実行等をLLMに委譲したい時

## やり方

1. MCPサーバーをnpmでインストール（例: @modelcontextprotocol/server-slack）
2. `~/.gemini/settings.json` の `mcpServers` セクションに設定追加
3. Gemini CLIを起動して `@slack` 等のプレフィックスでツールを呼び出し
4. LLMが適切なツールを自動選択して実行

### 入力

- MCPサーバーのnpmパッケージまたは実行可能ファイル
- settings.jsonへの設定（command, args, env）

### 出力

- 外部サービスとの統合（Slack投稿、PR作成等）
- LLMからのツール実行結果

## 使うツール・ライブラリ

- Model Context Protocol (MCP)
- @modelcontextprotocol/server-*
- settings.json

## コード例

```
// ~/.gemini/settings.json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {"SLACK_BOT_TOKEN": "xoxb-..."}
    }
  }
}

// Gemini CLI内で
> @slack Send a summary to #dev channel
```

## 前提知識

- Node.js 18以上の基本的な理解
- ターミナル操作の基礎知識
- npmパッケージマネージャーの基本的な使い方
- LLM APIの基本概念（プロンプト、トークン、コンテキストウィンドウ）
- OAuth認証フローの概要理解（ブラウザベース認証）
- JSON形式の基本的なパース方法
- （GitHub Actions利用の場合）GitHub Actionsの基本構文
- （MCP利用の場合）Model Context Protocolの概要

## 根拠

> 「Powerful Gemini 3 models: Access to improved reasoning and 1M token context window」（Gemini 3モデル、1Mトークンコンテキスト）

> 「Run instantly with npx: npx @google/gemini-cli」（npxで即時実行可能）

> 「Non-interactive mode for scripts: gemini -p 'Explain the architecture of this codebase' --output-format json」（スクリプト向け非対話モード、JSON出力）

> 「Configure MCP servers in ~/.gemini/settings.json」（settings.jsonでMCP設定）

> 「Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action」（GitHub Actions統合）
