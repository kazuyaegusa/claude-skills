# npxで即座にGemini CLIを起動

> インストール不要で、npxコマンドを使ってGemini CLIをその場で実行する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: prompt-engineering

## なぜ使うのか

グローバルインストールせずに試用でき、依存関係の競合を避けられる

## いつ使うのか

初回試用時、または複数バージョンを切り替えたい場合

## やり方

1. ターミナルで`npx @google/gemini-cli`を実行
2. 認証プロンプトが表示されたら「Sign in with Google」を選択
3. ブラウザで認証フローを完了
4. ターミナルに戻り、プロンプトで質問や指示を入力

### 入力

- Node.js実行環境
- インターネット接続（npxパッケージ取得用）

### 出力

- Gemini CLIの対話セッション起動

## 使うツール・ライブラリ

- npx
- @google/gemini-cli

## コード例

```
npx @google/gemini-cli
```

## 前提知識

- Node.js実行環境（npm/npx利用のため）
- Googleアカウント（OAuth認証用）
- ターミナル操作の基礎知識
- （GitHub連携時）GitHubリポジトリとActions実行権限
- （MCP統合時）各サービスのAPI認証情報

## 根拠

> 🎯 Free tier: 60 requests/min and 1,000 requests/day with personal Google account.

> Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action

> Configure MCP servers in ~/.gemini/settings.json to extend Gemini CLI with custom tools

> Ground your queries with built-in Google Search for real-time information
