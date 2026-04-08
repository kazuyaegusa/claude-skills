# MCP Server統合によるカスタムツール追加

> ~/.gemini/settings.json でMCPサーバーを設定し、Slack/GitHub/DB等の外部サービスをGemini CLIから操作可能にする

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

標準ツール（ファイル操作、シェル、Web fetch）を超えた独自ワークフローを実現するため

## いつ使うのか

Slack通知自動化、GitHub操作、DB クエリ、メディア生成（Imagen/Veo/Lyria）統合時

## やり方

1. `~/.gemini/settings.json` に使用するMCPサーバーのエンドポイント・認証情報を記載
2. Gemini CLI起動時に自動ロード
3. `@サーバー名 コマンド` 形式で呼び出し（例: `@slack Send summary to #dev`）

### 入力

- MCPサーバー設定ファイル（~/.gemini/settings.json）

### 出力

- 外部サービス操作結果

## 使うツール・ライブラリ

- MCP (Model Context Protocol)
- 各種MCPサーバー実装

## コード例

```
# 設定例（~/.gemini/settings.json）
{
  "mcpServers": {
    "slack": { "endpoint": "..." },
    "github": { "endpoint": "..." }
  }
}

# CLI使用例
> @slack Send a summary of today's commits to #dev channel
```

## 前提知識

- Node.js実行環境（npm/npx利用のため）
- Google アカウント（OAuth認証用）
- （任意）Gemini API Key または Vertex AI認証情報
- （GitHub Action利用時）GitHub リポジトリ管理権限
- （MCP利用時）各MCPサーバーのセットアップ知識

## 根拠

> "Powerful Gemini 3 models: Access to improved reasoning and 1M token context window."

> "MCP (Model Context Protocol) support for custom integrations."

> "npx @google/gemini-cli" - インストール不要実行

> "Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action"

> "Use MCP servers to connect new capabilities, including media generation with Imagen, Veo or Lyria"
