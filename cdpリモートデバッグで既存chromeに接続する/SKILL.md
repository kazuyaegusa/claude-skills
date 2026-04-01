# CDPリモートデバッグでログイン済みChromeに接続する

> Chromeのプロファイル移動トリックで「non-default data directory」制約を回避し、ログイン済みセッション（Gmail, GitHub等）をそのままAIエージェントから操作する。

- 出典: https://x.com/langchainjp/status/2033188997908832461
- 投稿者: LangChainJP
- カテゴリ: agent-orchestration
- 検証日: 2026-03-16（macOS, Chrome 145, Node.js 24）

## なぜ使うのか

Playwright/Puppeteerは新規ブラウザを起動するため、Gmail・GitHub・社内ツールのログイン状態を使えない。CDPリモートデバッグなら既存プロファイル（Cookie・セッション）をそのまま利用できる。

## macOSの罠と回避策

Chrome 145+のmacOSでは `--remote-debugging-port` に `--user-data-dir` の指定が必須で、かつデフォルトパスと異なることを要求する。プロファイルをコピーしてもKeychainで暗号化されたCookieは復号できない。

**解決策**: プロファイルの実体を別パスに移動し、元の場所にシンボリックリンクを張る。

```
# 実体を移動（1回だけ）
mv ~/Library/Application\ Support/Google/Chrome \
   ~/Library/Application\ Support/Google/ChromeCDP
# 元の場所にシンボリックリンク（通常起動に影響なし）
ln -s ~/Library/Application\ Support/Google/ChromeCDP \
      ~/Library/Application\ Support/Google/Chrome
```

これでCDP起動時に実体パス(`ChromeCDP`)を指定すると:
- Chromeは「non-defaultだ」と判断 → CDPポートを開く
- プロファイルの実体は同じ → Cookie・セッション・拡張機能すべて維持
- 通常起動時はシンボリックリンク経由で同じ実体を読む → 影響なし

## やり方

### 起動スクリプト（推奨）

```bash
cd /Users/apple/Documents/01_Global/sennin_scout && bash scripts/chrome-cdp.sh
```

### 手動

```bash
# Chrome終了
osascript -e 'tell application "Google Chrome" to quit'
sleep 2
# CDP有効で起動
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/Library/Application Support/Google/ChromeCDP"
```

### 接続確認

```bash
curl -s http://localhost:9222/json | python3 -m json.tool
```

### 停止（通常モードに戻す）

```bash
cd /Users/apple/Documents/01_Global/sennin_scout && bash scripts/chrome-cdp.sh stop
```

## コード例: スクリーンショット取得

```javascript
import WebSocket from 'ws';
import { writeFileSync } from 'fs';

const tabs = await fetch('http://localhost:9222/json').then(r => r.json());
const page = tabs.find(t => t.type === 'page');
const ws = new WebSocket(page.webSocketDebuggerUrl);
let id = 0;

ws.on('open', () => {
  ws.send(JSON.stringify({ id: ++id, method: 'Page.enable' }));
  ws.send(JSON.stringify({ id: ++id, method: 'Page.navigate', params: { url: 'https://github.com' } }));
});

ws.on('message', (data) => {
  const msg = JSON.parse(data);
  if (msg.method === 'Page.loadEventFired') {
    setTimeout(() => {
      ws.send(JSON.stringify({ id: ++id, method: 'Page.captureScreenshot', params: {} }));
    }, 1000);
  }
  if (msg.result?.data && msg.id === id) {
    writeFileSync('screenshot.png', Buffer.from(msg.result.data, 'base64'));
    ws.close();
  }
});
```

## MCP連携: chrome-devtools-mcp

npmの `chrome-devtools-mcp` (v0.20.0, Chrome DevTools公式) をMCPサーバーとして登録すると、Claude Codeから直接ブラウザ操作できる。

```json
// ~/.claude/settings.json の mcpServers に追加
{
  "chrome-cdp": {
    "command": "npx",
    "args": ["chrome-devtools-mcp@latest"],
    "env": { "CDP_PORT": "9222" }
  }
}
```

## 検証済み操作

| 操作 | CDP method | 検証結果 |
|------|-----------|---------|
| スクリーンショット | Page.captureScreenshot | OK (42-727KB) |
| ページ遷移 | Page.navigate | OK |
| タブ一覧 | HTTP GET /json | OK |
| JS実行 | Runtime.evaluate | OK |
| ログイン状態 | - | GitHub: OK, Gmail: OK |

## 前提条件

- macOS + Google Chrome
- Node.js 22+ (`ws`パッケージ)
- 初回のみ: プロファイル移動セットアップ（スクリプトで自動）

## 注意

- CDPモードのChromeはLAN内からport 9222にアクセス可能 → 作業中のみ使い、終わったら `scripts/chrome-cdp.sh stop` で通常モードに戻す
- AIエージェントがログイン済みセッションを操作するため、初回はread-only操作（screenshot, get_html）で確認
- プロファイル移動後も通常のChrome起動は影響なし（シンボリックリンク経由）
