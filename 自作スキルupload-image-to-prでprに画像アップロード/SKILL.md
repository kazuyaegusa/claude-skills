# 自作スキル「upload-image-to-pr」でPRに画像アップロード

> GitHub PRのdescriptionに画像を自動でアップロードするClaude Codeスキル

- 出典: https://x.com/gorilla0513/status/2034464246608875687
- 投稿者: ゴリラ - 花粉に負けそう
- カテゴリ: claude-code-workflow

## なぜ使うのか

GitHub APIには画像直接アップロードエンドポイントがないため、ブラウザ自動化で実現

## いつ使うのか

PRにスクリーンショットやデザイン案を頻繁に貼り付ける開発フロー

### 具体的な適用場面

- Claude Codeを頻繁に起動・終了する開発フロー
- 画像やスクリーンショットをGitHub PRに頻繁に貼り付ける必要がある
- 複数プロジェクト・ブランチを切り替えながら作業し、現在位置を把握したい
- PDFや他アプリのUIから文字をコピーしてClaude Codeに渡したい
- Claude Code起動待ち時間を撲滅したい

## やり方

1. https://github.com/tonkotsuboy/github-upload-image-to-pr からスキルを取得
2. Chrome DevTools MCPまたはPlaywrightでPRページを開く（ブラウザにログイン済み前提）
3. コメント欄に画像をアップロード
4. GitHubが発行する永続URL（https://github.com/user-attachments/assets/...）を取得
5. コメントは送信せず、URLのみを取得
6. gh pr edit CLIでPR説明文にURLを埋め込む

### 入力

- 画像ファイル
- PR番号
- ブラウザログイン状態

### 出力

- PRのdescriptionに画像が埋め込まれる

## 使うツール・ライブラリ

- Chrome DevTools MCP
- Playwright MCP
- gh CLI

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
