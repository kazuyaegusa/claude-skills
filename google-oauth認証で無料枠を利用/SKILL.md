# Google OAuth認証で無料枠を利用

> API Keyを使わず、個人のGoogleアカウントでOAuthログインし、無料枠（60req/min, 1000req/day）でGemini 3にアクセスする

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: context-management

## なぜ使うのか

API Key管理の手間がなく、Gemini 3モデルの1Mトークンコンテキストを無料で利用できるため

## いつ使うのか

個人開発者、またはGemini Code Assist Licenseを持つ組織ユーザーの場合

## やり方

1. `gemini`コマンドを実行
2. 認証選択画面で「Sign in with Google」を選ぶ
3. ブラウザで認証を完了
4. 組織のCode Assist Licenseを使う場合は`export GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"`を事前に実行

### 入力

- Googleアカウント
- （組織利用時）Google Cloud Project ID

### 出力

- 認証済みGemini CLIセッション
- 60req/min, 1000req/dayの無料枠アクセス

## 使うツール・ライブラリ

- gemini CLI
- Google OAuth

## コード例

```
export GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
gemini
```

## 前提知識

- Node.js実行環境（npm/npx利用のため）
- Googleアカウント（OAuth認証用）
- ターミナル操作の基礎知識
- （GitHub連携時）GitHubリポジトリとActions実行権限
- （MCP統合時）各サービスのAPI認証情報

## 根拠

> 🎯 Free tier: 60 requests/min and 1,000 requests/day with personal Google account.

> npx @google/gemini-cli

> Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action

> Configure MCP servers in ~/.gemini/settings.json to extend Gemini CLI with custom tools

> Ground your queries with built-in Google Search for real-time information
