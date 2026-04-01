# OAuth 2.0 PKCE フローでユーザー認証を完了する

> xurl を使ってブラウザで OAuth 2.0 認証を行い、アクセストークンを取得・保存する

- 出典: https://x.com/goroman/status/2035187722114277501
- 投稿者: null-sensei
- カテゴリ: context-management

## なぜ使うのか

X API でユーザーコンテキストが必要なエンドポイント（投稿、フォロー等）を呼ぶため

## いつ使うのか

OAuth 2.0 User-Context が必要なエンドポイント（投稿、フォロー、ダイレクトメッセージ等）を使うとき

### 具体的な適用場面

- X投稿の自動収集・分析パイプラインで規約違反を避けたい
- 複数のXアカウントやAPIアプリを切り替えて運用する
- CI/CDやcronでX APIを定期実行したい（トークン永続化が必要）
- curlライクなシンプルなCLIでX APIを試したい

## やり方

1. X Developer Portal でアプリの Redirect URI を設定（例: http://127.0.0.1:8080/callback）
2. `xurl auth oauth2 --app my-app` を実行
3. ブラウザが開き、X にログインして認可
4. トークンが自動取得され ~/.xurl に保存される
5. 以降は `xurl --app my-app GET /2/users/me` のようにトークンが自動利用される

### 入力

- 登録済みのアプリ（xurl auth apps add で設定済み）
- X Developer Portal で設定された Redirect URI

### 出力

- アクセストークン（~/.xurl に保存）

## 使うツール・ライブラリ

- xurl CLI

## コード例

```
xurl auth oauth2 --app my-app
# ブラウザで認可後
xurl --app my-app GET /2/users/me
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
