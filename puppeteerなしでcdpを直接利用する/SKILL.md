# PuppeteerなしでCDPを直接利用する

> Puppeteer等の高レベルラッパーを経由せず、CDP WebSocketに直接接続してブラウザを制御する

- 出典: https://x.com/langchainjp/status/2033188997908832461
- 投稿者: LangChainJP
- カテゴリ: agent-orchestration

## なぜ使うのか

PuppeteerはCDPをラップしているが新規インスタンス起動前提の設計のため、稼働中Chromeへのアタッチには直接CDPを使う方がシンプルで確実

## いつ使うのか

既存ブラウザセッションにアタッチしたいとき、またはPuppeteerが想定していない低レベルCDPコマンドを直接叩く必要があるとき

### 具体的な適用場面

- GmailやGitHub等ログイン必須のWebサービスをAIエージェントに操作させるとき
- 社内イントラネット・2FA必須ツールのブラウザ自動化が必要なとき
- 100個以上開いているタブを前提としたリサーチ・作業自動化タスク

## やり方

1. `http://localhost:9222/json/version` でブラウザのCDPエンドポイントURLを取得
2. WebSocketクライアントで `ws://localhost:9222/devtools/browser/<id>` に接続
3. CDP JSON-RPCプロトコルでコマンド送信: `{"id":1,"method":"Page.captureScreenshot","params":{}}` など
4. 利用可能なメソッド例: `Runtime.evaluate`（JS実行）、`Input.dispatchMouseEvent`（クリック）、`DOM.getDocument`（HTML取得）

### 入力

- ChromeのCDP WebSocket URL（ws://localhost:9222/...）

### 出力

- CDPコマンドのJSON-RPCレスポンス（スクリーンショットデータ・DOMデータ・実行結果等）

## 使うツール・ライブラリ

- Chrome DevTools Protocol (CDP)
- WebSocketクライアント（ws等）

## 前提知識

- Chromeをremote debugging有効で起動する方法の理解
- Node.js 22+環境
- Claude Code / AIエージェント環境
- Chrome DevTools Protocolの基本概念（JSON-RPC over WebSocket）

## 根拠

> 「すでに開いているタブやログイン済みの状態をそのまま使えるのが特徴」

> 「接続先はChromeのremote debugging（外部デバッグ機能）のWebSocket」

> 「Puppeteer（ブラウザ自動操作ライブラリ）を介さず、既存のChromeに直接つなぐ設計」

> 「Node.js 22+で動作し、スクリーンショット取得、HTML取得、JavaScript実行、クリック、テキスト入力などに対応」

> 「タブを100個以上開いた状態でも安定して扱えるとしている」
