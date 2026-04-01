# PuppeteerなしでCDP WebSocketに直接接続する

> Puppeteerなどのブラウザ自動化ライブラリを介さず、Chrome DevTools Protocol (CDP)のWebSocketエンドポイントに直接接続してブラウザを操作する

- 出典: https://x.com/langchainjp/status/2033188997908832461
- 投稿者: LangChainJP
- カテゴリ: agent-orchestration

## なぜ使うのか

Puppeteerはブラウザのライフサイクル管理（起動・終了）を前提とした設計のため既存セッションへの接続が困難。CDPに直接接続することで軽量かつ既存Chromeを柔軟に制御できる

## いつ使うのか

Puppeteerを使いたくない（または使えない）環境で既存のChromeタブをプログラムから制御したいとき、特に100以上のタブが開いた状態でも安定した操作が必要なとき

### 具体的な適用場面

- GmailやSlackなどOAuth認証が必要なWebアプリをAIエージェントに操作させたいが、毎回ログインフローを実装したくない場合
- 社内ツール（VPN内・SSO経由）など自動ログインが困難なページをAIエージェントで自動操作したい場合
- すでに100以上のタブを開いた作業セッションの中から特定のタブをAIに処理させたい場合

## やり方

1. `http://localhost:9222/json` でタブ一覧（JSON配列）を取得する
2. 各タブの `webSocketDebuggerUrl` フィールドを取得する
3. Node.jsの `ws` ライブラリ等でWebSocket接続を確立する
4. CDPコマンドをJSONで送信する（例: `{"id":1,"method":"Page.captureScreenshot","params":{}}`）
5. レスポンスをJSONで受信して結果を処理する

### 入力

- remote debugging有効化済みのChrome
- Node.js 22+（またはWebSocket接続できる任意のランタイム）

### 出力

- CDPコマンドへのレスポンス（JSON）
- スクリーンショット（base64エンコード画像）
- ページのDOM/HTML

## 使うツール・ライブラリ

- Chrome DevTools Protocol (CDP)
- ws（Node.js WebSocketライブラリ）
- Node.js 22+

## コード例

```
// Node.jsでCDPに直接接続する例
const WebSocket = require('ws');
const res = await fetch('http://localhost:9222/json');
const tabs = await res.json();
const ws = new WebSocket(tabs[0].webSocketDebuggerUrl);
ws.on('open', () => {
  ws.send(JSON.stringify({id:1, method:'Page.captureScreenshot', params:{}}));
});
ws.on('message', (data) => console.log(JSON.parse(data)));
```

## 前提知識

- Chrome DevTools Protocol (CDP) の基本概念（タブ管理・メッセージング）
- Node.js 22以上の実行環境
- Chromeを --remote-debugging-port フラグ付きで起動できる権限
- WebSocketの基礎知識

## 根拠

> 「すでに開いているタブやログイン済みの状態をそのまま使えるのが特徴」

> 「接続先はChromeのremote debugging（外部デバッグ機能）のWebSocket」

> 「Puppeteer（ブラウザ自動操作ライブラリ）を介さず、既存のChromeに直接つなぐ設計」

> 「Node.js 22+で動作し、スクリーンショット取得、HTML取得、JavaScript実行、クリック、テキスト入力などに対応」

> 「タブを100個以上開いた状態でも安定して扱えるとしている」
