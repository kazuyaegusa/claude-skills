# ステータスラインで作業環境を常時表示

> Claude Code画面下部にカレントディレクトリ、ブランチ名、diff、モデル名等を表示

- 出典: https://x.com/gorilla0513/status/2034464246608875687
- 投稿者: ゴリラ - 花粉に負けそう
- カテゴリ: claude-code-workflow

## なぜ使うのか

複数プロジェクト・ブランチを切り替える際に現在位置を迷わず把握できる

## いつ使うのか

複数リポジトリ・ブランチで並行作業し、現在地を見失いがちな時

### 具体的な適用場面

- Claude Codeを頻繁に起動・終了する開発フロー
- 画像やスクリーンショットをGitHub PRに頻繁に貼り付ける必要がある
- 複数プロジェクト・ブランチを切り替えながら作業し、現在位置を把握したい
- PDFや他アプリのUIから文字をコピーしてClaude Codeに渡したい
- Claude Code起動待ち時間を撲滅したい

## やり方

1. Claude Codeで `/statusline 表示したい内容` を実行
2. Claude Codeが設定を自動生成し、~/.claude/settings.json に追加
3. 例：`📂 ~/git/repo 🐙 repo-name │ 🌿 main +2 ~3 🧠 53% │ 💪 claude-sonnet-4-6`

### 入力

- Claude Code
- 表示したい情報（ディレクトリ、ブランチ、モデル等）

### 出力

- 画面下部に常時ステータス表示

## 使うツール・ライブラリ

- Claude Code
- statusline.sh

## コード例

```
/statusline 表示したい内容
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
