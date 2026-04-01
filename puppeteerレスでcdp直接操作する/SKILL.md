# PuppeteerレスでCDP直接操作する

> PuppeteerなどのブラウザラッパーライブラリをバイパスしてCDPのWebSocketに直接接続し、既存Chromeプロセスを制御する

- 出典: https://x.com/langchainjp/status/2033188997908832461
- 投稿者: LangChainJP
- カテゴリ: dev-tool

## なぜ使うのか

Puppeteerは新規ブラウザインスタンス起動を前提とした設計で既存セッションへのアタッチが困難。CDPを直接使うことで既存プロセスへの接続・軽量な依存関係・100タブ超の安定動作を実現する

## いつ使うのか

Puppeteer依存を避けたい場合、または既存の起動済みChromeプロセスにアタッチする必要があるとき

### 具体的な適用場面

- GmailやGitHub等にログイン済みのChromeからAIエージェントにメール送信・PR作成などを委任したいとき
- 社内VPN内ツール・SSOサービスのページをAIに操作させたいとき（再認証不要）
- 100タブ以上開いた作業環境のまま、特定タブのスクレイピング・操作を自動化したいとき

## やり方

1. `http://localhost:9222/json` にGETリクエストしてタブ一覧(JSON)を取得
2. 対象タブの `webSocketDebuggerUrl` に WebSocket 接続
3. CDPコマンドをJSONメッセージで送信（例: `Page.captureScreenshot`、`Runtime.evaluate`、`Input.dispatchMouseEvent`）
4. レスポンスの `result` フィールドから結果を取得

### 入力

- Chrome --remote-debugging-port=9222 起動済み
- WebSocketクライアント（Node.js ws ライブラリ等）

### 出力

- CDPコマンドの実行結果（JSON）
- スクリーンショットのbase64データ
- DOM操作・JS評価の結果

## 使うツール・ライブラリ

- Chrome DevTools Protocol (CDP)
- Node.js ws ライブラリ
- chrome-cdp-skill

## コード例

```
// CDPタブ一覧取得 → WebSocket接続 → スクリーンショット
const res = await fetch('http://localhost:9222/json');
const tabs = await res.json();
const ws = new WebSocket(tabs[0].webSocketDebuggerUrl);
ws.send(JSON.stringify({
  id: 1,
  method: 'Page.captureScreenshot',
  params: {}
}));
```

## 前提知識

- Chrome DevTools Protocol (CDP) の基本概念
- Node.js 22+ の実行環境
- Chromeを --remote-debugging-port フラグ付きで起動する方法

## 根拠

> 「すでに開いているタブやログイン済みの状態をそのまま使えるのが特徴」

> 「接続先はChromeのremote debugging（外部デバッグ機能）のWebSocket」

> 「Puppeteer（ブラウザ自動操作ライブラリ）を介さず、既存のChromeに直接つなぐ設計」

> 「Node.js 22+で動作し、スクリーンショット取得、HTML取得、JavaScript実行、クリック、テキスト入力などに対応」

> 「タブを100個以上開いた状態でも安定して扱えるとしている」
