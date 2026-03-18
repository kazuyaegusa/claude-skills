# Google Search groundingでリアルタイム情報を統合する

> Gemini CLIの組み込みGoogle Search grounding機能を使い、LLMの応答に最新のWeb情報を根拠として含める

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: prompt-engineering

## なぜ使うのか

ライブラリの最新API仕様、セキュリティ脆弱性情報、ベストプラクティスの変化など、学習データに含まれない情報を参照しながらコード生成できる。

## いつ使うのか

最新のフレームワークバージョンに対応したコード生成、既知の脆弱性を避けた実装、現在のベストプラクティスに従ったリファクタリングをしたい場合

## やり方

1. Gemini CLI起動時に自動的に有効（Google Search groundingはGemini API標準機能） 2. プロンプトで「最新の〜」「現在の〜」と指定すると、LLMが検索結果を参照して回答 3. 応答には引用元URLが含まれる 4. （詳細）https://ai.google.dev/gemini-api/docs/grounding を参照

### 入力

- リアルタイム情報が必要なプロンプト（例: 「Next.js 15の最新の認証方法」）

### 出力

- Web検索結果を統合したLLM応答
- 引用元URL

## 使うツール・ライブラリ

- gemini-cli
- Google Search grounding (Gemini API標準機能)

## コード例

```
> Show me the latest authentication pattern for Next.js 15
# → Geminiが検索結果を参照し、2025年3月時点の最新情報を含めて回答
# 応答末尾に引用元URLが表示される
```

## 前提知識

- Node.js環境の基本操作（npmまたはnpxの使用経験）
- ターミナル/コマンドラインの基礎知識
- Git操作の基本（GitHub連携を使う場合）
- JSON-RPC 2.0の基礎（MCP Server自作時）
- Google Cloud Projectの概念（Code Assistライセンス利用時）
- CI/CDパイプラインの基礎（GitHub Actions統合時）

## 根拠

> 「Free tier: 60 requests/min and 1,000 requests/day with personal Google account」（OAuth認証での無料枠）

> 「Powerful Gemini 3 models: Access to improved reasoning and 1M token context window」（モデル性能）

> 「Custom context files (GEMINI.md) to tailor behavior for your projects」（コンテキストファイル）

> 「Ground your queries with built-in Google Search for real-time information」（Search grounding）

> 「Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action」（GitHub Actions統合）
