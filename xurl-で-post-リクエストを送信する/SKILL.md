# xurl で POST リクエストを送信する

> JSON ボディを含む POST リクエストを X API に送信する

- 出典: https://x.com/goroman/status/2035187722114277501
- 投稿者: null-sensei
- カテゴリ: dev-tool

## なぜ使うのか

ツイート投稿、ユーザーフォロー等の書き込み操作を行うため

## いつ使うのか

ツイート投稿、フォロー、リツイート等の書き込み操作を自動化するとき

### 具体的な適用場面

- X投稿の自動収集・分析パイプラインで規約違反を避けたい
- 複数のXアカウントやAPIアプリを切り替えて運用する
- CI/CDやcronでX APIを定期実行したい（トークン永続化が必要）
- curlライクなシンプルなCLIでX APIを試したい

## やり方

1. OAuth 2.0 認証済みのアプリを用意
2. `xurl POST /2/tweets -d '{"text":"Hello, world!"}'` のように実行
3. `-H` でヘッダーを追加可能: `xurl POST /2/tweets -H 'Content-Type: application/json' -d '{...}'`

### 入力

- OAuth 2.0 認証済みアプリ
- JSON リクエストボディ

### 出力

- X API のレスポンス（JSON）

## 使うツール・ライブラリ

- xurl CLI

## コード例

```
xurl POST /2/tweets -d '{"text":"Hello, world!"}'
```

## 前提知識

- X Developer Portal でアプリを作成し、Client ID / Client Secret を取得していること
- OAuth 2.0 を使う場合、Developer Portal で Redirect URI を設定していること
- xurl CLI がインストールされていること（Homebrew/npm/Go/shell script）

## 根拠

> 投稿本文: 「X の操作は公式のCLIのこれ使ってる（ブラウザで自動化すると規約違反っぽいんで」

> GitHub: xdevplatform/xurl - A curl-like CLI Tool for the X API

> README抜粋: Multi-app support — register multiple X API apps with separate credentials and tokens

> README抜粋: Persistent token storage in YAML (~/.xurl), auto-migrates from legacy JSON

> README抜粋: xurl auth apps add my-app --client-id YOUR_CLIENT_ID --client-secret YOUR_CLIENT_SECRET
