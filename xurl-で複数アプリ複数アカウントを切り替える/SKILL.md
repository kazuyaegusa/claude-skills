# xurl で複数アプリ・複数アカウントを切り替える

> 登録済みの複数アプリや複数アカウントを --app または対話的ピッカーで選択する

- 出典: https://x.com/goroman/status/2035187722114277501
- 投稿者: null-sensei
- カテゴリ: dev-tool

## なぜ使うのか

開発・本番環境や複数のXアカウントを使い分ける運用で、毎回認証し直さずに済むため

## いつ使うのか

複数のX APIアプリやアカウントを並行運用するとき

### 具体的な適用場面

- X投稿の自動収集・分析パイプラインで規約違反を避けたい
- 複数のXアカウントやAPIアプリを切り替えて運用する
- CI/CDやcronでX APIを定期実行したい（トークン永続化が必要）
- curlライクなシンプルなCLIでX APIを試したい

## やり方

1. 複数アプリを登録: `xurl auth apps add prod-app ...` `xurl auth apps add dev-app ...`
2. デフォルトアプリを設定: `xurl auth apps select` で対話的に選択
3. リクエスト時に --app でオーバーライド: `xurl --app dev-app GET /2/users/me`
4. 1つのアプリに複数のOAuth 2.0アカウントがある場合、`xurl auth oauth2 users select --app my-app` で切り替え

### 入力

- 複数の登録済みアプリ設定

### 出力

- 選択されたアプリ・アカウントでのAPIレスポンス

## 使うツール・ライブラリ

- xurl CLI

## コード例

```
xurl auth apps select
xurl --app dev-app GET /2/users/me
xurl auth oauth2 users select --app my-app
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
