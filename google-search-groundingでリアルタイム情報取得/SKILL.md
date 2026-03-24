# Google Search groundingでリアルタイム情報取得

> Gemini CLIの標準機能でGoogle Searchをgrounding sourceとして使い、最新情報を含む回答を得る

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: prompt-engineering

## なぜ使うのか

LLMの知識カットオフを超えた情報（最新ライブラリバージョン、ニュースなど）を参照できるため

## いつ使うのか

最新のAPIドキュメント、ニュース、技術動向を参照したい場合

## やり方

1. Gemini CLI起動時、特に設定不要で自動的にGoogle Search groundingが有効
2. プロンプトで「最新の〜」や「現在の〜」のように問うと、検索結果を元に回答
3. 必要に応じて`--disable-grounding`フラグで無効化も可能

### 入力

- 自然言語プロンプト（最新情報を問う内容）

### 出力

- Google Search結果を統合した回答

## 使うツール・ライブラリ

- Gemini API（Google Search grounding機能）

## コード例

```
gemini
> What are the latest breaking changes in React 19?
```

## 前提知識

- Node.js実行環境（npm/npx利用のため）
- Googleアカウント（OAuth認証用）
- ターミナル操作の基礎知識
- （GitHub連携時）GitHubリポジトリとActions実行権限
- （MCP統合時）各サービスのAPI認証情報

## 根拠

> 🎯 Free tier: 60 requests/min and 1,000 requests/day with personal Google account.

> 🧠 Powerful Gemini 3 models: Access to improved reasoning and 1M token context window.

> npx @google/gemini-cli

> gemini -p "Explain the architecture of this codebase" --output-format json

> Custom context files (GEMINI.md) to tailor behavior for your projects
