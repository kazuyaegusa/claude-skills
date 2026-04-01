# Claude起動時にプロンプト同時実行

> claude 起動コマンドの後にプロンプト文字列を続けて書くことで、起動直後に自動実行

- 出典: https://x.com/gorilla0513/status/2034464246608875687
- 投稿者: ゴリラ - 花粉に負けそう
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Code起動待ち時間を撲滅し、即座にタスクを開始できる

## いつ使うのか

定型的なタスク（PRレビュー、レポート生成等）をClaude Codeに即座に依頼したい時

### 具体的な適用場面

- Claude Codeを頻繁に起動・終了する開発フロー
- 画像やスクリーンショットをGitHub PRに頻繁に貼り付ける必要がある
- 複数プロジェクト・ブランチを切り替えながら作業し、現在位置を把握したい
- PDFや他アプリのUIから文字をコピーしてClaude Codeに渡したい
- Claude Code起動待ち時間を撲滅したい

## やり方

1. ターミナルで `claude "依頼したいプロンプト"` と入力
2. Claude Codeが起動し、指定したプロンプトが自動実行される
例：`claude "https://github.com/tonkotsuboy/fugafuga/pull/97 の レビューを確認し、必要に応じて返信しておいて。 レビュー結果についてSlackで私宛にtimes-kano-とんこつで投稿して"`

### 入力

- claude CLI
- 実行したいプロンプト文字列

### 出力

- Claude Code起動後にプロンプトが自動実行される

## 使うツール・ライブラリ

- claude CLI

## コード例

```
$ claude "https://github.com/tonkotsuboy/fugafuga/pull/97 の レビューを確認し、必要に応じて返信しておいて。 レビュー結果についてSlackで私宛にtimes-kano-とんこつで投稿して"
```

## 前提知識

- Claude Codeの基本操作
- ターミナルの基本コマンド
- macOS環境（CleanShot X, Raycastを使う場合）
- GitHub CLIの基本操作（PRアップロードスキル利用時）
- MCPまたはPlaywrightの基礎知識（画像アップロードスキル作成時）

## 根拠

> 「Claude Code起動待ちの短い時間を撲滅」

> 「画像を貼り付けて読み取らせるよりもトークン使用量が少ない」

> 「GitHub APIには画像を直接アップロードするエンドポイントが存在しない」

> 「ブラウザ自動化（Playwright MCP / Chrome DevTools MCP）でPRページを開く→コメント欄に画像アップロード→発行されたURLを取得し、テキストエリアをクリアしてコメントは送信しない」

> 「私は ⌥⌘T で起動させている ターミナルのT」
