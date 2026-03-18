# チェックポイント機能で長時間セッションを保存・再開する

> Gemini CLIのチェックポイント機能で、対話履歴とコンテキストをスナップショットとして保存し、後日同じ状態から作業を再開する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: context-management

## なぜ使うのか

複数日にまたがる大規模リファクタリングやデバッグセッションで、コンテキストロストを防ぎ、前回の議論を完全に引き継げる。トークンキャッシュと併用すればコスト削減も可能。

## いつ使うのか

複数日のデバッグ作業、段階的な機能追加で中間状態を保存したい、チームメンバー間でセッションを引き継ぎたい場合

## やり方

1. セッション中に`/checkpoint save <name>`コマンドを実行 2. `~/.gemini/checkpoints/`に状態が保存される 3. 次回起動時に`gemini --resume <name>`で復元 4. （オプション）`--token-cache`フラグでコンテキストをキャッシュしてAPI呼び出しを削減

### 入力

- 保存したいセッションの対話履歴
- チェックポイント名（任意の文字列）

### 出力

- ~/.gemini/checkpoints/<name>.jsonに保存されたセッション状態
- 復元時に完全に再現される対話コンテキスト

## 使うツール・ライブラリ

- gemini-cli
- （オプション）token-cache機能

## コード例

```
# セッション中
> /checkpoint save refactor-auth-2025-03-18

# 翌日
gemini --resume refactor-auth-2025-03-18 --token-cache
> 前回の続きから、次はどのファイルを修正すべき？
```

## 前提知識

- Node.js環境の基本操作（npmまたはnpxの使用経験）
- ターミナル/コマンドラインの基礎知識
- Git操作の基本（GitHub連携を使う場合）
- JSON-RPC 2.0の基礎（MCP Server自作時）
- Google Cloud Projectの概念（Code Assistライセンス利用時）
- CI/CDパイプラインの基礎（GitHub Actions統合時）

## 根拠

> 「Powerful Gemini 3 models: Access to improved reasoning and 1M token context window」（モデル性能）

> 「Custom context files (GEMINI.md) to tailor behavior for your projects」（コンテキストファイル）

> 「Conversation checkpointing to save and resume complex sessions」（チェックポイント機能）

> 「Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action」（GitHub Actions統合）

> 「Configure MCP servers in ~/.gemini/settings.json」（MCP設定方法）
