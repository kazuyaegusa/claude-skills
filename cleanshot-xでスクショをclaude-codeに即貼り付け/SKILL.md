# CleanShot XでスクショをClaude Codeに即貼り付け

> 画面の任意領域をスクリーンショットし、Claude Codeに直接ペースト

- 出典: https://x.com/gorilla0513/status/2034464246608875687
- 投稿者: ゴリラ - 花粉に負けそう
- カテゴリ: claude-code-workflow

## なぜ使うのか

視覚情報を素早くClaude Codeに伝え、指示を具体化できる

## いつ使うのか

デザイン修正、UI実装、エラー画面の共有など視覚情報が必要な時

### 具体的な適用場面

- Claude Codeを頻繁に起動・終了する開発フロー
- 画像やスクリーンショットをGitHub PRに頻繁に貼り付ける必要がある
- 複数プロジェクト・ブランチを切り替えながら作業し、現在位置を把握したい
- PDFや他アプリのUIから文字をコピーしてClaude Codeに渡したい
- Claude Code起動待ち時間を撲滅したい

## やり方

1. CleanShot X（https://cleanshot.com/）をインストール（macOS専用）
2. ショートカットキーで任意領域をスクリーンショット
3. クリップボードにコピーされるので、Claude Codeにペースト

### 入力

- CleanShot X
- スクショ対象の画面

### 出力

- クリップボードに画像がコピーされ、Claude Codeに貼り付け可能

## 使うツール・ライブラリ

- CleanShot X

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
