# 既存ChromeにCDP接続する

> Chrome DevTools Protocol（CDP）のWebSocketエンドポイントに接続し、すでに起動・ログイン済みのChromeセッションをAIエージェントから操作する

- 出典: https://x.com/langchainjp/status/2033188997908832461
- 投稿者: LangChainJP
- カテゴリ: agent-orchestration

## なぜ使うのか

新規ブラウザプロセスを立ち上げるとログイン状態が失われるが、CDPで既存プロセスに接続すればクッキー・セッションをそのまま使える

## いつ使うのか

AIエージェントにGmail・GitHub・社内ツール等のログイン済みページを操作させたいとき。再ログインが困難なSSOサービスやVPN内リソースへのアクセス時

### 具体的な適用場面

- GmailやGitHub等にログイン済みのChromeからAIエージェントにメール送信・PR作成などを委任したいとき
- 社内VPN内ツール・SSOサービスのページをAIに操作させたいとき（再認証不要）
- 100タブ以上開いた作業環境のまま、特定タブのスクレイピング・操作を自動化したいとき

## やり方

1. Chromeを `--remote-debugging-port=9222` フラグ付きで起動（Mac: `open -a 'Google Chrome' --args --remote-debugging-port=9222`）
2. `chrome-cdp-skill` をNode.js 22+ 環境にインストール
3. エージェントからCDP WebSocket `ws://localhost:9222` に接続
4. スクリーンショット取得・HTML取得・JS実行・クリック・テキスト入力APIを呼び出す

### 入力

- Chrome --remote-debugging-port=9222 で起動済みのインスタンス
- Node.js 22+ 実行環境
- chrome-cdp-skill インストール済み

### 出力

- スクリーンショット（画像）
- ページHTML
- JavaScript実行結果
- クリック・テキスト入力の実行完了

## 使うツール・ライブラリ

- chrome-cdp-skill（Petr Baudis製）
- Chrome DevTools Protocol (CDP)
- Node.js 22+

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
