# Raycastスニペットで`claude`コマンド即時入力

> 短い入力（例：c;）でClaude Code起動コマンドを自動展開

- 出典: https://x.com/gorilla0513/status/2034464246608875687
- 投稿者: ゴリラ - 花粉に負けそう
- カテゴリ: claude-code-workflow

## なぜ使うのか

claude -p "..." のような長いコマンドを毎回打たずに済む

## いつ使うのか

Claude Codeを頻繁に起動し、コマンド入力が面倒な時

### 具体的な適用場面

- Claude Codeを頻繁に起動・終了する開発フロー
- 画像やスクリーンショットをGitHub PRに頻繁に貼り付ける必要がある
- 複数プロジェクト・ブランチを切り替えながら作業し、現在位置を把握したい
- PDFや他アプリのUIから文字をコピーしてClaude Codeに渡したい
- Claude Code起動待ち時間を撲滅したい

## やり方

1. Raycastのスニペット機能（https://www.raycast.com/core-features/snippets）を開く
2. 短縮キー（例：c;）に対して展開テキスト（例：claude）を登録
3. ターミナルで c; と打つだけでclaudeコマンドが入力される

### 入力

- Raycast
- スニペット設定

### 出力

- 短い入力で長いコマンドが自動入力される

## 使うツール・ライブラリ

- Raycast Snippets

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
