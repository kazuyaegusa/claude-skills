# xurl をスクリプトやCI/CDに組み込む

> 認証トークンが永続化されているため、xurl をシェルスクリプトや cron、CI/CD パイプラインから呼び出す

- 出典: https://x.com/goroman/status/2035187722114277501
- 投稿者: null-sensei
- カテゴリ: automation-pipeline

## なぜ使うのか

定期実行や自動化パイプラインで X API を利用するため

## いつ使うのか

X投稿の定期収集、自動返信Bot、CI/CDでの投稿通知等

### 具体的な適用場面

- X投稿の自動収集・分析パイプラインで規約違反を避けたい
- 複数のXアカウントやAPIアプリを切り替えて運用する
- CI/CDやcronでX APIを定期実行したい（トークン永続化が必要）
- curlライクなシンプルなCLIでX APIを試したい

## やり方

1. ローカルで `xurl auth oauth2 --app my-app` を実行し、~/.xurl にトークンを保存
2. スクリプト内で `xurl --app my-app GET /2/users/me` のように呼び出す
3. CI/CD では ~/.xurl をシークレットとして環境に配置するか、環境変数 CLIENT_ID/CLIENT_SECRET を設定してトークンを自動取得

### 入力

- ~/.xurl に保存された認証トークン（またはCI/CD環境に配置）

### 出力

- スクリプトやCI/CDから取得したX APIレスポンス

## 使うツール・ライブラリ

- xurl CLI
- bash/cron/GitHub Actions等

## コード例

```
#!/bin/bash
xurl --app my-app GET /2/tweets/search/recent?query=AI
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
