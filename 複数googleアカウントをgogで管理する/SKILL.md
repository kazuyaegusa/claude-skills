# 複数Googleアカウントをgogで管理する

> gog auth manageで複数アカウントを登録し、GOG_ACCOUNT環境変数またはコマンド引数で切り替える

- 出典: https://x.com/mlbear2/status/2016359803048886755
- 投稿者: ML_Bear
- カテゴリ: dev-tool

## なぜ使うのか

仕事用・個人用など複数アカウントを使い分ける運用で、認証の再入力を避けつつアカウント切り替えを効率化するため

## いつ使うのか

Claude Codeに複数Googleアカウントのデータを扱わせる場合や、個人/組織のアカウントを切り替えてタスクを実行する場合

### 具体的な適用場面

- Claude CodeからGmailの検索・送信・ラベル管理を自動化したい
- カレンダーの予定確認・イベント作成をAIエージェントに任せたい
- Google Driveのファイル検索・アップロード・権限管理をスクリプト化したい
- スプレッドシートの読み書きをCLIパイプラインで処理したい
- 複数Googleアカウントを切り替えながら操作したい

## やり方

1. 各アカウントで `gog auth add account1@gmail.com`, `gog auth add account2@gmail.com` を実行
2. `gog auth manage` で登録済みアカウント一覧確認・規定アカウント設定
3. 規定アカウント設定: `export GOG_ACCOUNT=account1@gmail.com` または各コマンドに `--account account2@gmail.com` を付与
4. OS keychainに各アカウントのトークンが保存され、再認証不要

### 入力

- 複数のGoogleアカウント認証情報
- 各アカウントのOAuthスコープ設定

### 出力

- アカウントごとに分離された操作結果
- OS keychain内の複数トークン

## 使うツール・ライブラリ

- gog CLI
- OS keychain (macOS Keychain / Linux Secret Service / Windows CredMan)

## コード例

```
# アカウント追加
gog auth add work@company.com
gog auth add personal@gmail.com

# 規定アカウント設定
export GOG_ACCOUNT=work@company.com

# 一時的に別アカウント使用
gog gmail labels list --account personal@gmail.com
```

## 前提知識

- Google Cloudプロジェクトの作成とOAuth 2.0クライアント設定
- Homebrew（macOS/Linux）またはGo環境（ソースビルド）
- jq（JSON処理）
- Claude Code / claude CLI（AI連携する場合）

## 根拠

> 「GeminiのGoogle Workspaceコネクタ上手く動かなくてイラつくこと多いから試す価値ありそう」（投稿本文）

> 「gog unifies Gmail, Calendar, Drive, Contacts, Tasks, Sheets, Docs, Slides, and People under one CLI — with JSON output and sane defaults.」（gogcli.sh公式サイト）

> 「gog auth add you@gmail.com --services sheets --force-consent」（公式ドキュメントの再認証手順）

> 「export GOG_ACCOUNT=you@gmail.com」「gog gmail search 'newer_than:7d' --max 10 --json | jq」（公式クイックスタート例）
