# スコープ追加時に--force-consentで再認証する

> 後からスコープ（例: Sheets）を追加した際、Googleがrefresh tokenを返さない問題を回避するため --force-consent で再認証する

- 出典: https://x.com/mlbear2/status/2016359803048886755
- 投稿者: ML_Bear
- カテゴリ: dev-tool

## なぜ使うのか

OAuth 2.0の仕様上、初回認証時にすべてのスコープを要求しないと、後から追加したスコープでrefresh tokenが発行されず認証が失敗するため

## いつ使うのか

最初にGmail/Calendar等で認証後、Sheets/Drive等のサービスを後から使おうとしてトークンエラーが出たとき

### 具体的な適用場面

- Claude CodeからGmailの検索・送信・ラベル管理を自動化したい
- カレンダーの予定確認・イベント作成をAIエージェントに任せたい
- Google Driveのファイル検索・アップロード・権限管理をスクリプト化したい
- スプレッドシートの読み書きをCLIパイプラインで処理したい
- 複数Googleアカウントを切り替えながら操作したい

## やり方

`gog auth add you@gmail.com --services sheets --force-consent` を実行し、同意画面を強制表示してrefresh tokenを再取得する

### 入力

- 既存の認証済みアカウント
- 追加するサービス名（sheets, drive等）

### 出力

- 新しいスコープを含むrefresh token
- OS keychainに更新されたトークン

## 使うツール・ライブラリ

- gog CLI

## コード例

```
# Sheetsスコープ追加で再認証
gog auth add you@gmail.com --services sheets --force-consent
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
