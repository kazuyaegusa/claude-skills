# Claude Codeにgog JSON出力を解釈させる

> gog --json の出力をClaude Codeに渡し、自然言語タスクとして解釈・加工させる

- 出典: https://x.com/mlbear2/status/2016359803048886755
- 投稿者: ML_Bear
- カテゴリ: claude-code-workflow

## なぜ使うのか

jqでの加工が複雑になる場合や、コンテキスト依存の判断（例: メール本文の要約）をAIに任せたい場合、JSON構造をそのまま渡せば良いため

## いつ使うのか

単純なフィルタ・集計ではなく、自然言語理解が必要な判断（優先度付け、カテゴリ分類、要約）をAIに任せたいとき

### 具体的な適用場面

- Claude CodeからGmailの検索・送信・ラベル管理を自動化したい
- カレンダーの予定確認・イベント作成をAIエージェントに任せたい
- Google Driveのファイル検索・アップロード・権限管理をスクリプト化したい
- スプレッドシートの読み書きをCLIパイプラインで処理したい
- 複数Googleアカウントを切り替えながら操作したい

## やり方

1. `gog gmail search '件名' --json > result.json` でJSON保存
2. Claude Codeに「result.jsonを読み込んで、未読メールを重要度順にリスト化して」等のタスク指示
3. または `gog gmail search '件名' --json | claude -p 'このメール一覧から緊急対応が必要なものを抽出して'` のようにパイプライン統合

### 入力

- gog --json 出力のJSONデータ
- Claude Codeへのタスク指示

### 出力

- AIによる分析・加工結果
- 自然言語またはJSON形式の回答

## 使うツール・ライブラリ

- gog CLI
- Claude Code / claude CLI

## コード例

```
# Gmail検索結果をClaude Codeで分析
gog gmail search 'newer_than:7d' --json > emails.json
# Claude Codeに「emails.jsonから緊急対応が必要なメールを抽出」と指示

# パイプライン例（claude CLIがあれば）
gog calendar calendars --json | claude -p 'この中から仕事用カレンダーのIDを特定して'
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
