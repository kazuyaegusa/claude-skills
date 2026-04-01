# xurl で X API アプリを登録・永続化する

> X API の Client ID と Client Secret を xurl に登録し、~/.xurl に保存する

- 出典: https://x.com/goroman/status/2035187722114277501
- 投稿者: null-sensei
- カテゴリ: dev-tool

## なぜ使うのか

環境変数を毎回セットする手間を省き、複数アプリを名前で切り替えられるようにするため

## いつ使うのか

初回セットアップ時、または新しいX APIアプリを追加するとき

### 具体的な適用場面

- X投稿の自動収集・分析パイプラインで規約違反を避けたい
- 複数のXアカウントやAPIアプリを切り替えて運用する
- CI/CDやcronでX APIを定期実行したい（トークン永続化が必要）
- curlライクなシンプルなCLIでX APIを試したい

## やり方

1. X Developer Portal でアプリを作成し Client ID と Client Secret を取得
2. `xurl auth apps add my-app --client-id YOUR_CLIENT_ID --client-secret YOUR_CLIENT_SECRET` を実行
3. 複数アプリがある場合は `xurl auth apps add prod-app ...` `xurl auth apps add dev-app ...` のように登録
4. ~/.xurl（YAML形式）に認証情報が保存される

### 入力

- X API の Client ID
- X API の Client Secret

### 出力

- ~/.xurl に登録されたアプリ設定（YAML）

## 使うツール・ライブラリ

- xurl CLI

## コード例

```
xurl auth apps add my-app --client-id YOUR_CLIENT_ID --client-secret YOUR_CLIENT_SECRET
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
