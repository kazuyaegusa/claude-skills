# Browser Use CLI 2.0をClaude Codeから呼び出す

> Claude Code環境からBrowser Use CLI 2.0を実行してブラウザ操作を行う

- 出典: https://x.com/ix00ai/status/2035292820609925393
- 投稿者: iX
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeとの連携に最適化されているため、従来のツールより速く正確に動作する

## いつ使うのか

Claude Codeでブラウザ自動操作が必要になった時、特に速度と精度を重視する場合

### 具体的な適用場面

- Claude Codeでウェブスクレイピングを自動化したい時
- SNSの通知やメッセージを定期的に抽出・分析したい時
- ブラウザ操作を含む複雑なタスクをAIエージェントに任せたい時
- Playwright等の既存ツールで精度やスピードに不満がある時

## やり方

1. Browser Use CLI 2.0をインストール（具体的なコマンドは投稿に記載なし、公式リポジトリ参照が必要） 2. Claude Codeからclaude -pまたはBash tool経由でBrowser Use CLIコマンドを実行 3. 対象URLと操作内容を指定してブラウザタスクを実行

### 入力

- 操作対象のURL（例: X/Twitter）
- 実行したい操作内容（例: 通知の抽出）

### 出力

- ブラウザ操作の結果データ（例: 抽出された通知リスト）

## 使うツール・ライブラリ

- Browser Use CLI 2.0
- Claude Code

## 前提知識

- Claude Codeの基本的な使い方
- ブラウザ自動化の概念理解（Playwright, Puppeteer等）
- Bash/CLIツールの基本操作

## 根拠

> 「Claude Codeでブラウザ操作するなら、Browser Use CLI 2.0一択かも」

> 「スピード速く、精度も高そう」

> 「動画でやってるのは、・ブラウザで自分のXを開く ・最近の通知を抽出する」
