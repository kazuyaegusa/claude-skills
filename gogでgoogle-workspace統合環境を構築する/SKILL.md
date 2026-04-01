# gogでGoogle Workspace統合環境を構築する

> Gmail/Calendar/Drive/Sheets等をgog CLIでまとめて操作可能にし、JSON出力でjqやAIエージェントと連携する

- 出典: https://x.com/mlbear2/status/2016359803048886755
- 投稿者: ML_Bear
- カテゴリ: agent-orchestration

## なぜ使うのか

個別APIクライアントを実装するコストを削減し、統一インターフェースで認証・出力形式・エラーハンドリングを標準化できるため

## いつ使うのか

Claude CodeやシェルスクリプトからGoogle Workspaceを操作する必要があり、公式SDKの複雑さや言語依存を避けたいとき

### 具体的な適用場面

- Claude CodeからGmailの検索・送信・ラベル管理を自動化したい
- カレンダーの予定確認・イベント作成をAIエージェントに任せたい
- Google Driveのファイル検索・アップロード・権限管理をスクリプト化したい
- スプレッドシートの読み書きをCLIパイプラインで処理したい
- 複数Googleアカウントを切り替えながら操作したい

## やり方

1. `brew install gogcli` でインストール
2. Google CloudでOAuth 2.0クライアント（デスクトップアプリ）のJSONをダウンロード
3. `gog auth credentials ~/Downloads/client_secret.json` で認証情報を保存
4. `gog auth add you@gmail.com` でアカウント追加（ブラウザ認証、headlessなら `--manual`）
5. `export GOG_ACCOUNT=you@gmail.com` で規定アカウント設定
6. `gog gmail search 'newer_than:7d' --max 10 --json | jq` のようにJSON出力でパイプライン構築

### 入力

- Google Cloud OAuth 2.0クライアント認証情報JSON
- 操作対象のGoogleアカウント
- 必要なスコープ（Gmail, Calendar, Drive等）

### 出力

- JSON形式の操作結果（--jsonフラグ）
- プレーンテキスト（--plain）またはテーブル形式（デフォルト）
- OS keychainに保存された認証トークン

## 使うツール・ライブラリ

- gog CLI (gogcli)
- jq
- Google Cloud OAuth 2.0

## コード例

```
# カレンダー一覧をJSON取得
gog calendar calendars --max 5 --json | jq '.calendars[].summary'

# Gmail検索（過去7日）
gog gmail search 'newer_than:7d' --max 10 --json

# Drive内のPDFを検索
gog drive ls --query "mimeType='application/pdf'" --max 3
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
