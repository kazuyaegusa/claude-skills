# Google検索グラウンディングによるリアルタイム情報統合

> クエリ実行時にGoogle検索結果を自動参照し、最新情報を組み込んだ回答を生成する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

LLMの知識カットオフを超えた最新情報・外部ドキュメントを参照するため

## いつ使うのか

最新ライブラリのAPI仕様確認、トレンド技術の調査、公式ドキュメント参照が必要な場合

## やり方

1. Gemini CLI起動後、通常通りプロンプト入力
2. バックエンドで自動的にGoogle検索APIを実行
3. 検索結果を文脈に統合して回答生成

### 入力

- 自然言語クエリ

### 出力

- Google検索結果を統合した回答

## 使うツール・ライブラリ

- Google Search API
- Gemini API grounding機能

## 前提知識

- Node.js実行環境（npm/npx利用のため）
- Google アカウント（OAuth認証用）
- （任意）Gemini API Key または Vertex AI認証情報
- （GitHub Action利用時）GitHub リポジトリ管理権限
- （MCP利用時）各MCPサーバーのセットアップ知識

## 根拠

> "Powerful Gemini 3 models: Access to improved reasoning and 1M token context window."

> "npx @google/gemini-cli" - インストール不要実行

> "Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action"

> "Custom context files (GEMINI.md) to tailor behavior for your projects"
