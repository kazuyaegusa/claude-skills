# OAuth認証で無料枠（60req/min, 1000req/day）を利用

> 個人GoogleアカウントでSign in with Googleを選択し、APIキー不要で認証する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

APIキー管理が不要で、Gemini 3モデル（1Mトークンコンテキスト）の無料枠を即座に利用できる。個人開発者に最適

## いつ使うのか

個人開発でAPIキーを発行したくない場合、Gemini 3の無料枠を最大限活用したい場合

## やり方

1. `gemini` コマンドを実行
2. 認証方法選択で「Sign in with Google」を選択
3. ブラウザで表示されるOAuth同意画面で許可
4. トークンが `~/.gemini/` に保存され、以降は自動認証

### 入力

- 個人Googleアカウント
- ブラウザアクセス（OAuth認証フロー用）

### 出力

- 認証トークン（~/.gemini/に保存）
- 60req/min, 1000req/dayの無料枠利用可能状態

## 使うツール・ライブラリ

- Gemini CLI
- Google OAuth 2.0

## コード例

```
gemini
# 起動後、ブラウザで認証フローを完了
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

> 「Free tier: 60 requests/min and 1,000 requests/day with personal Google account」（個人Googleアカウントで無料枠利用可能）

> 「Run instantly with npx: npx @google/gemini-cli」（npxで即時実行可能）

> 「Sign in with Google (OAuth login using your Google Account)」（OAuth認証対応）

> 「Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action」（GitHub Actions統合）

> 「Ground your queries with built-in Google Search for real-time information」（Google Search grounding内蔵）
