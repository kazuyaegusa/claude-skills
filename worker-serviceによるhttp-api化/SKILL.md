# Worker ServiceによるHTTP API化

> Bunで常駐HTTPサーバー（port 37777）を起動し、フックスクリプトからHTTP経由でメモリ操作する

- 出典: https://github.com/thedotmack/claude-mem
- 投稿者: thedotmack
- カテゴリ: claude-code-workflow

## なぜ使うのか

フックスクリプトはClaude Codeから毎回起動されるため、毎回DB接続やAI呼び出しを初期化すると遅い。Workerを常駐させることで初期化コストを償却し、レスポンス速度を向上できる

## いつ使うのか

Claude Codeインストール時（自動セットアップ）。再起動時やWorkerクラッシュ時は手動再起動が必要

## やり方

1. `npx claude-mem install`時にBunをインストール（未存在なら） 2. Worker起動スクリプト（`bun run worker`）をバックグラウンド実行 3. フックスクリプトは`fetch('http://localhost:37777/...')`でWorker APIを呼び出す 4. Workerは10種のエンドポイントを提供（/session/start, /observation/create, /search等）

### 入力

- フックスクリプトからのHTTPリクエスト

### 出力

- JSON形式のレスポンス（要約/Observation/検索結果等）
- Web Viewer UI（http://localhost:37777）

## 使うツール・ライブラリ

- Bun
- SQLite
- Chroma
- Claude Agent SDK

## コード例

```
// Worker起動（概念）
Bun.serve({
  port: 37777,
  fetch: async (req) => {
    if (req.url.endsWith('/search')) return handleSearch(req);
    if (req.url.endsWith('/observation/create')) return handleObservation(req);
    // ...
  }
});
```

## 前提知識

- Claude Codeの基本的な使い方（ツール使用、セッション概念）
- Node.js 18+のインストール
- SQLiteの基本知識（オプション：データ構造理解のため）
- MCP（Model Context Protocol）の概念（オプション：検索ツール理解のため）

## 根拠

> 「Claude-Mem seamlessly preserves context across sessions by automatically capturing tool usage observations, generating semantic summaries, and making them available to future sessions.」

> 「Worker Service - HTTP API on port 37777 with web viewer UI and 10 search endpoints, managed by Bun」
