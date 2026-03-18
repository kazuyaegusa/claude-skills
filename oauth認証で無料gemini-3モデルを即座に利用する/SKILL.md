# OAuth認証で無料Gemini 3モデルを即座に利用する

> Google OAuthログイン経由で、APIキー不要・日1000リクエスト枠のGemini 3モデル（1Mトークン）にアクセスする

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: context-management

## なぜ使うのか

APIキー管理のオーバーヘッドなしで、個人開発者が高性能LLMをローカル開発に統合できる。Code Assistライセンス保有者はさらに高いレート制限を利用可能。

## いつ使うのか

APIキー管理を避けたい個人開発者、または既存のGoogle Workspaceアカウントで無料LLM利用を開始したいとき

## やり方

1. `gemini`コマンドを実行 2. `Sign in with Google`を選択 3. ブラウザで認証フロー完了 4. 即座に1Mトークンコンテキストで対話開始（有料ライセンス利用時は`export GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"`を事前設定）

### 入力

- 有効なGoogleアカウント
- （オプション）Code AssistライセンスとGCPプロジェクトID

### 出力

- 認証トークン（自動保存）
- 即座に利用可能なGemini 3対話セッション

## 使うツール・ライブラリ

- gemini-cli
- Google OAuth 2.0

## コード例

```
gemini
# ブラウザで認証後、自動的にセッション開始
> Explain the architecture of this codebase
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

> 「Use MCP servers to connect new capabilities, including media generation with Imagen, Veo or Lyria」（MCP統合例）

> 「Ground your queries with built-in Google Search for real-time information」（Search grounding）

> 「Install with Anaconda (for restricted environments)」（制限環境対応）

> 「Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action」（GitHub Actions統合）
