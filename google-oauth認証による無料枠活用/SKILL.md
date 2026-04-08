# Google OAuth認証による無料枠活用

> Gemini API Keyの代わりにGoogle アカウントでOAuth認証し、無料枠（60req/min, 1000req/day）を利用する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

APIキー管理コストを削減し、個人・小規模チームでの導入障壁を下げるため

## いつ使うのか

個人開発、Gemini Code Assist License保有組織、API鍵管理を避けたい場合

## やり方

1. `gemini` コマンド実行
2. 初回起動時に「Sign in with Google」を選択
3. ブラウザでGoogle認証完了
4. Code Assist Licenseを持つ組織の場合は `export GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"` を設定してから起動

### 入力

- Google アカウント
- （任意）Google Cloud Project ID

### 出力

- 認証済みGemini CLIセッション

## 使うツール・ライブラリ

- Google OAuth
- Gemini API

## コード例

```
export GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
gemini
```

## 前提知識

- Node.js実行環境（npm/npx利用のため）
- Google アカウント（OAuth認証用）
- （任意）Gemini API Key または Vertex AI認証情報
- （GitHub Action利用時）GitHub リポジトリ管理権限
- （MCP利用時）各MCPサーバーのセットアップ知識

## 根拠

> "Free tier: 60 requests/min and 1,000 requests/day with personal Google account."

> "Powerful Gemini 3 models: Access to improved reasoning and 1M token context window."

> "Built-in tools: Google Search grounding, file operations, shell commands, web fetching."

> "npx @google/gemini-cli" - インストール不要実行

> "Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action"
