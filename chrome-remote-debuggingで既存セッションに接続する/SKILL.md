# Chrome remote debuggingで既存セッションに接続する

> Chromeのremote debugging機能が公開するWebSocket(CDP)に接続し、すでに起動済みのChromeブラウザをAIエージェントからそのまま操作する

- 出典: https://x.com/langchainjp/status/2033188997908832461
- 投稿者: LangChainJP
- カテゴリ: agent-orchestration

## なぜ使うのか

既存セッションに接続することで、Gmail・GitHub・社内ツールなど認証済みのページをログインフローを経ずに操作できる。新規ブラウザ起動は不要

## いつ使うのか

AIエージェントが認証済みWebアプリ（Gmail, GitHub, 社内ツール等）を操作する必要があり、ログインフローの自動化が困難または不要な場合

### 具体的な適用場面

- GmailやSlackなどOAuth認証が必要なWebアプリをAIエージェントに操作させたいが、毎回ログインフローを実装したくない場合
- 社内ツール（VPN内・SSO経由）など自動ログインが困難なページをAIエージェントで自動操作したい場合
- すでに100以上のタブを開いた作業セッションの中から特定のタブをAIに処理させたい場合

## やり方

1. Chromeを `--remote-debugging-port=9222` フラグ付きで起動する（既存Chromeが起動済みの場合は再起動が必要）。Macの場合: `open -a 'Google Chrome' --args --remote-debugging-port=9222`
2. `http://localhost:9222/json` にGETリクエストを送ってタブ一覧を取得する
3. 対象タブの `webSocketDebuggerUrl` フィールドを取得する（例: `ws://localhost:9222/devtools/page/XXXXX`）
4. そのWebSocket URLに接続してCDPメッセージ（JSON形式）を送受信する
5. chrome-cdp-skillをClaude Code skillとして追加し、スクリーンショット・HTML取得・JS実行・クリック・テキスト入力などのコマンドを実行する

### 入力

- remote debugging有効化済みのChrome（--remote-debugging-port=9222で起動）
- Node.js 22以上
- chrome-cdp-skill

### 出力

- ページスクリーンショット（画像）
- ページHTML
- JavaScript実行結果
- クリック・テキスト入力の実行確認

## 使うツール・ライブラリ

- chrome-cdp-skill（Petr Baudis作）
- Chrome DevTools Protocol (CDP)
- Node.js 22+

## コード例

```
# Chromeをremote debugging有効で起動（Mac）
open -a 'Google Chrome' --args --remote-debugging-port=9222

# タブ一覧取得
curl http://localhost:9222/json
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
