# 既存ChromeにCDP接続する

> 起動中のChromeをremote debugging有効モードで接続し、AIエージェントからWebSocket経由でブラウザを操作する

- 出典: https://x.com/langchainjp/status/2033188997908832461
- 投稿者: LangChainJP
- カテゴリ: agent-orchestration

## なぜ使うのか

新規ブラウザを起動すると全セッションが失われ再ログインが必要になるが、既存Chromeに接続すればログイン済み状態・開きタブをそのまま利用できる

## いつ使うのか

ログイン済みセッションが必要なWebサービス（Gmail・GitHub・社内ツール等）をAIエージェントに操作させるとき、または既存ブラウザタブを前提とした作業自動化が必要なとき

### 具体的な適用場面

- GmailやGitHub等ログイン必須のWebサービスをAIエージェントに操作させるとき
- 社内イントラネット・2FA必須ツールのブラウザ自動化が必要なとき
- 100個以上開いているタブを前提としたリサーチ・作業自動化タスク

## やり方

1. Chromeをremote debugging有効で起動: `open -a 'Google Chrome' --args --remote-debugging-port=9222`（Mac）または `google-chrome --remote-debugging-port=9222`（Linux）
2. `http://localhost:9222/json` にアクセスしてデバッグエンドポイント一覧を確認
3. chrome-cdp-skillをClaude Codeにインストール
4. AIエージェントのツール呼び出しでスクリーンショット取得・クリック・JS実行などを実行

### 入力

- remote debugging有効で起動済みのChrome（--remote-debugging-port=9222）
- Node.js 22+環境

### 出力

- スクリーンショット（画像）
- ページHTML
- JavaScript実行結果
- クリック・テキスト入力の実行

## 使うツール・ライブラリ

- chrome-cdp-skill (by Petr Baudis)
- Chrome DevTools Protocol (CDP)
- Node.js 22+

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
