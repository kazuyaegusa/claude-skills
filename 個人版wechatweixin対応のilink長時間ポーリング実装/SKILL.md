# 個人版WeChat（Weixin）対応のilink長時間ポーリング実装

> 公式API未公開の個人版WeChatに対し、ilink非公式APIを使った長時間ポーリング方式でメッセージ受信を実現する

- 出典: https://github.com/chenhg5/cc-connect
- 投稿者: chenhg5
- カテゴリ: agent-orchestration

## なぜ使うのか

企業版WeChat（WeCom）と異なり、個人版WeChatには公式Bot APIが存在しないため、非公式プロトコルを使う必要がある

## いつ使うのか

個人版WeChatでAIエージェントを使いたいが公式APIがない場合

## やり方

1. `weixin setup` コマンドでQRコードログインを実行
2. ilink APIエンドポイントへ長時間ポーリング接続（HTTP long polling）
3. 新規メッセージ受信時にレスポンスが返る
4. メッセージをエージェントに転送し、応答をilink APIで送信
5. 画像・ファイルはCDN経由でアップロード
6. ※beta版のみの機能（`cc-connect@beta`）

### 入力

- WeChatアカウント（QRログイン）
- ilink非公式APIエンドポイント

### 出力

- 個人版WeChatでのBot動作

## 使うツール・ライブラリ

- ilink非公式API
- HTTP long polling実装

## コード例

```
// 疑似コード（beta版）
resp := httpClient.Get(ilinkEndpoint + "?long_poll=true")
if resp.StatusCode == 200 {
  var msg WeixinMessage
  json.Unmarshal(resp.Body, &msg)
  handleMessage(msg)
}
```

## 前提知識

- 各チャットプラットフォームのBot API基礎知識（認証、メッセージ送受信）
- WebSocketまたはLong Pollingの概念
- AIエージェント（Claude Code、Gemini CLI等）の基本的な使い方
- Go言語の基礎（ソースビルドする場合）
- TOML設定ファイルの記法

## 根拠

> "10 Chat Platforms — Feishu, DingTalk, Slack, Telegram, Discord, WeChat Work, LINE, QQ, QQ Bot (Official), plus Weixin (personal ilink)"

> "WebSocket / Long Polling — no public IP needed"

> "Personal WeChat (Weixin ilink) — beta / pre-release only"
