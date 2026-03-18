# MCP Serverで外部ツールを拡張しエージェントワークフローを構築する

> ~/.gemini/settings.jsonにMCP（Model Context Protocol）サーバー定義を追加し、Gemini CLIから`@<server名>`で外部API（Slack、GitHub、DB、メディア生成等）を操作する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

LLMの能力を既存のツールチェーンに統合し、「コード分析→Slack通知」「PRレビュー→GitHub comment」「画像生成→S3アップロード」のような複合ワークフローを自然言語で実行できる。

## いつ使うのか

コード変更をトリガーに他システムへ通知したい、AIに外部DBクエリやメディア生成を実行させたい、カスタムビジネスロジックをLLMから呼び出したい場合

## やり方

1. `~/.gemini/settings.json`を編集し、MCPサーバー設定を追加（例: Slack、GitHub、Vertex AI Creative Studio） 2. Gemini CLI起動後、`@github List my open pull requests`のようにサーバーをメンションして操作 3. サーバー側はJSON-RPC 2.0でツール定義を返し、Gemini CLIがLLMにツール実行を仲介 4. 公式MCPサーバー例: https://github.com/GoogleCloudPlatform/vertex-ai-creative-studio/tree/main/experiments/mcp-genmedia

### 入力

- MCPサーバー実装（JSON-RPC 2.0互換）
- ~/.gemini/settings.jsonへのサーバー登録情報
- （オプション）サーバー起動コマンドとポート設定

### 出力

- 外部ツール実行結果（Slack投稿ID、GitHub comment URL等）
- Gemini CLIのセッションログに統合された実行履歴

## 使うツール・ライブラリ

- Model Context Protocol (MCP)
- 任意のMCP対応サーバー（自作可能）
- Vertex AI Creative Studio MCP（Imagen/Veo/Lyria）

## コード例

```
// ~/.gemini/settings.json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-slack"],
      "env": { "SLACK_TOKEN": "xoxb-..." }
    }
  }
}

// Gemini CLI内で実行
> @slack Send today's commit summary to #dev
```

## 前提知識

- Node.js環境の基本操作（npmまたはnpxの使用経験）
- ターミナル/コマンドラインの基礎知識
- Git操作の基本（GitHub連携を使う場合）
- JSON-RPC 2.0の基礎（MCP Server自作時）
- Google Cloud Projectの概念（Code Assistライセンス利用時）
- CI/CDパイプラインの基礎（GitHub Actions統合時）

## 根拠

> 「Powerful Gemini 3 models: Access to improved reasoning and 1M token context window」（モデル性能）

> 「Use MCP servers to connect new capabilities, including media generation with Imagen, Veo or Lyria」（MCP統合例）

> 「Custom context files (GEMINI.md) to tailor behavior for your projects」（コンテキストファイル）

> 「Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action」（GitHub Actions統合）

> 「Configure MCP servers in ~/.gemini/settings.json」（MCP設定方法）
