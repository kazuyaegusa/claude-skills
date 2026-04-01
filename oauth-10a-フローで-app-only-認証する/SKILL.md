# OAuth 1.0a フローで App-only 認証する

> xurl を使って OAuth 1.0a でアプリ認証を行い、ユーザーコンテキスト不要なエンドポイントにアクセスする

- 出典: https://x.com/goroman/status/2035187722114277501
- 投稿者: null-sensei
- カテゴリ: context-management

## なぜ使うのか

読み取り専用の操作（ツイート検索、ユーザー情報取得等）に OAuth 2.0 のユーザー認証が不要な場合に簡易に使えるため

## いつ使うのか

ユーザーコンテキスト不要なエンドポイント（ツイート検索、公開ユーザー情報取得等）を使うとき

### 具体的な適用場面

- X投稿の自動収集・分析パイプラインで規約違反を避けたい
- 複数のXアカウントやAPIアプリを切り替えて運用する
- CI/CDやcronでX APIを定期実行したい（トークン永続化が必要）
- curlライクなシンプルなCLIでX APIを試したい

## やり方

1. X Developer Portal でアプリの API Key と API Secret Key を取得
2. `xurl auth oauth1 --app my-app` を実行
3. PIN ベースの認証フローを完了
4. トークンが ~/.xurl に保存され、以降は自動利用される

### 入力

- 登録済みのアプリ（API Key と API Secret Key）

### 出力

- OAuth 1.0a トークン（~/.xurl に保存）

## 使うツール・ライブラリ

- xurl CLI

## コード例

```
xurl auth oauth1 --app my-app
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
