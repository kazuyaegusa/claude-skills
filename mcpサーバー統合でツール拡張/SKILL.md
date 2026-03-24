# MCPサーバー統合でツール拡張

> `~/.gemini/settings.json`でMCPサーバーを設定し、Slack、DB、メディア生成などの外部ツールをGemini CLIから呼び出す

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: dev-tool

## なぜ使うのか

標準のファイル操作・シェル実行だけでなく、APIやサービスへの統合を自然言語で実行できるため

## いつ使うのか

GitHub、Slack、DBなど複数サービスをAIで統合操作したい場合

## やり方

1. `~/.gemini/settings.json`を編集してMCPサーバーエンドポイントを追加
2. 各MCPサーバーの認証情報を設定
3. Gemini CLI内で`@github List my open pull requests`や`@slack Send summary`のように呼び出す
4. カスタムMCPサーバーを作成して独自ツールを追加可能

### 入力

- MCPサーバーの設定ファイル（settings.json）
- 各サービスの認証情報

### 出力

- 外部サービスへのAI経由での操作実行

## 使うツール・ライブラリ

- Model Context Protocol（MCP）
- 各種MCPサーバー実装

## コード例

```
> @github List my open pull requests
> @slack Send a summary of today's commits to #dev channel
```

## 前提知識

- Node.js実行環境（npm/npx利用のため）
- Googleアカウント（OAuth認証用）
- ターミナル操作の基礎知識
- （GitHub連携時）GitHubリポジトリとActions実行権限
- （MCP統合時）各サービスのAPI認証情報

## 根拠

> 🧠 Powerful Gemini 3 models: Access to improved reasoning and 1M token context window.

> npx @google/gemini-cli

> gemini -p "Explain the architecture of this codebase" --output-format json

> Custom context files (GEMINI.md) to tailor behavior for your projects

> Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action
