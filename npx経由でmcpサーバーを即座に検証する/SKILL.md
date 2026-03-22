# npx経由でMCPサーバーを即座に検証する

> 開発中のMCPサーバーをクローン不要・設定不要でInspector UIに接続し、tools/resources/promptsを対話的にテストする

- 出典: https://github.com/modelcontextprotocol/inspector
- 投稿者: modelcontextprotocol
- カテゴリ: prompt-engineering

## なぜ使うのか

専用のテストクライアントを実装せずに、サーバー実装の正確性を視覚的に確認できるため、開発速度が大幅に向上する

## いつ使うのか

MCPサーバーの初期開発時、機能追加後の動作確認時、クライアント統合前の事前検証時

## やり方

1. サーバーのビルド成果物（例: build/index.js）を用意
2. `npx @modelcontextprotocol/inspector node build/index.js` を実行
3. 自動的に開くブラウザ（localhost:6274）でUI操作
4. 環境変数や引数が必要な場合は `-e key=value` または末尾に引数を追加

### 入力

- ビルド済みMCPサーバーのエントリーポイント（例: node build/index.js）
- サーバーが必要とする環境変数・コマンドライン引数（任意）

### 出力

- ブラウザUI（デフォルトポート6274）でのインタラクティブなサーバーテスト環境
- tools/resources/promptsの一覧と実行結果の可視化

## 使うツール・ライブラリ

- npx
- @modelcontextprotocol/inspector

## コード例

```
# 基本起動
npx @modelcontextprotocol/inspector node build/index.js

# 環境変数と引数を渡す
npx @modelcontextprotocol/inspector -e API_KEY=xxx -e DEBUG=true node build/index.js arg1 arg2

# ポートカスタマイズ
CLIENT_PORT=8080 SERVER_PORT=9000 npx @modelcontextprotocol/inspector node build/index.js
```

## 前提知識

- Node.js ^22.7.5以上
- MCPサーバーの基本概念（tools/resources/prompts）の理解
- MCPのトランスポート種別（stdio/SSE/Streamable HTTP）の違い
- JSON形式の設定ファイル記述能力（mcp.json）

## 根拠

> 「npx @modelcontextprotocol/inspector node build/index.js」— インストール不要でMCPサーバーを起動
