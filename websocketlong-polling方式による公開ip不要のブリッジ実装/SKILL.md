# WebSocket/Long Polling方式による公開IP不要のブリッジ実装

> チャットプラットフォームのWebSocketまたはLong Polling APIを使い、ローカルマシンからプラットフォームへ能動的に接続することで、公開IPやポート開放なしでメッセージを受信する

- 出典: https://github.com/chenhg5/cc-connect
- 投稿者: chenhg5
- カテゴリ: agent-orchestration

## なぜ使うのか

Webhook方式は公開URLが必須でセキュリティリスクが高いが、WebSocket/Long Pollingならローカルから接続するだけで済み、ファイアウォール内でも安全に動作する

## いつ使うのか

公開サーバーを立てたくない、ローカルマシンのAIエージェントを外部から操作したい場合

## やり方

1. Feishu/DingTalk/Telegram等のWebSocket/Long Polling APIエンドポイントへ接続
2. サーバー側からのイベント（メッセージ受信等）をリアルタイムで取得
3. 受信したメッセージをローカルのAIエージェントプロセスへ転送
4. エージェントの出力をチャットAPIで返信
5. 接続が切れたら自動再接続

### 入力

- チャットプラットフォームのBot認証情報（APIキー、トークン）
- WebSocket/Long Polling対応のチャットプラットフォームAPI

### 出力

- チャットアプリからのメッセージ受信
- AIエージェントへのコマンド転送と結果返信

## 使うツール・ライブラリ

- Go標準のWebSocketライブラリ
- Telegram Bot API (Long Polling)
- Feishu WebSocket API
- DingTalk Stream API
- Discord Gateway API

## コード例

```
// Go WebSocket接続例（疑似コード）
conn, _, err := websocket.DefaultDialer.Dial(apiEndpoint, headers)
for {
  var msg PlatformMessage
  err := conn.ReadJSON(&msg)
  if err != nil { reconnect(); continue }
  response := forwardToAgent(msg)
  sendToPlatform(response)
}
```

## 前提知識

- 各チャットプラットフォームのBot API基礎知識（認証、メッセージ送受信）
- WebSocketまたはLong Pollingの概念
- AIエージェント（Claude Code、Gemini CLI等）の基本的な使い方
- Go言語の基礎（ソースビルドする場合）
- TOML設定ファイルの記法

## 根拠

> "WebSocket / Long Polling — no public IP needed"
