# CleanShot XのOCRでトークン削減

> 画像内テキストをOCRで抽出してテキストとしてClaude Codeに渡す

- 出典: https://x.com/gorilla0513/status/2034464246608875687
- 投稿者: ゴリラ - 花粉に負けそう
- カテゴリ: claude-code-workflow

## なぜ使うのか

画像として送るよりトークン使用量が少なく、コストと処理速度が改善される

## いつ使うのか

PDF、他アプリのUI、コピペできないテキストをClaude Codeに渡したい時

### 具体的な適用場面

- Claude Codeを頻繁に起動・終了する開発フロー
- 画像やスクリーンショットをGitHub PRに頻繁に貼り付ける必要がある
- 複数プロジェクト・ブランチを切り替えながら作業し、現在位置を把握したい
- PDFや他アプリのUIから文字をコピーしてClaude Codeに渡したい
- Claude Code起動待ち時間を撲滅したい

## やり方

1. CleanShot XのOCR機能で画像内文字を認識
2. テキストをコピー
3. Claude Codeにテキストとして貼り付け

### 入力

- CleanShot X
- 文字を含む画像・PDF・UI

### 出力

- テキスト形式でクリップボードにコピー

## 使うツール・ライブラリ

- CleanShot X OCR

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
