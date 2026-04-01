# Google Search groundingで最新情報を含むコード生成

> Gemini APIのGoogle Search grounding機能を有効にし、プロンプトに最新のWeb情報を反映させる

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

LLMの知識カットオフ後の情報（最新ライブラリAPIや時事問題等）を補完し、より正確な応答を得られる

## いつ使うのか

最新ライブラリのコード例を生成したい、時事問題に関するコードを書きたい、APIドキュメントの最新版を参照したい場合

## やり方

1. Gemini CLI起動時に自動的にGoogle Search groundingが利用可能
2. プロンプトで「最新の〜」「現在の〜」等を含めることで自動的に検索が実行される
3. 応答に引用元URLが含まれる
4. 設定で無効化も可能（settings.json）

### 入力

- Google Search grounding対応のプロンプト
- インターネット接続

### 出力

- 最新情報を含む応答
- 引用元URL

## 使うツール・ライブラリ

- Gemini API
- Google Search grounding

## コード例

```
> Generate a React component using the latest Next.js 15 App Router
# Gemini CLIが自動的にGoogle Searchで最新ドキュメントを参照
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

> 「Powerful Gemini 3 models: Access to improved reasoning and 1M token context window」（Gemini 3モデル、1Mトークンコンテキスト）

> 「Run instantly with npx: npx @google/gemini-cli」（npxで即時実行可能）

> 「Sign in with Google (OAuth login using your Google Account)」（OAuth認証対応）

> 「Non-interactive mode for scripts: gemini -p 'Explain the architecture of this codebase' --output-format json」（スクリプト向け非対話モード、JSON出力）
