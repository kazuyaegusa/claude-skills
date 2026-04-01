# Claude CLIセッション自動検出でAPIキー不要化

> ローカルで動作するアプリがClaude CLIの認証済みセッションを自動検出し、APIキーの手動設定なしにClaude APIを利用できるようにする。

- 出典: https://x.com/l_go_mrk/status/2037749522021892427
- 投稿者: AI駆動塾
- カテゴリ: dev-tool

## なぜ使うのか

Claude CLIサブスク認証を持つユーザーが別途APIキーを取得・管理する手間を省けるため、セットアップコストが大幅に下がる。特にClaudeサブスク利用者が多いユーザー層への導入障壁を下げる効果がある。

## いつ使うのか

Claude CLIサブスク認証済みのマシンでローカルAIアプリを動かす際に、APIキー管理を省略したいとき

### 具体的な適用場面

- Xのブックマークが数百件以上あり「あの投稿どこだっけ」が頻発している
- スクリーンショット付き投稿をブックマークしているがOCRなしで内容検索できずにいる
- API課金を避けながらClaude CLIサブスク認証でローカルAIアプリを動かしたい

## やり方

1. Claude Codeをインストールしてログイン済みの状態にする（`claude login`）
2. Siftlyの `.env` でAIプロバイダーをClaudeに設定するか、未設定のまま起動
3. SiftlyがローカルのClaude CLIセッショントークンを自動読み取り、API呼び出しに使用する
4. 追加のAPIキー設定なしでパイプラインが動作する

### 入力

- Claude CLIの認証済みセッション（`claude login`完了済み）

### 出力

- APIキー設定なしでのClaude API利用

## 使うツール・ライブラリ

- Claude CLI（claude-code）

## 前提知識

- Node.js / npm の基本操作
- Xにログイン済みのブラウザ環境
- Claude CLIセッション or Claude/OpenAI APIキー（いずれか）
- git clone・npm install・npm run dev が実行できる環境

## 根拠

> 「4段階AIパイプライン: Import → Entity Extraction → Vision Analysis → Semantic Tagging → Categorization」（README）

> 「Entity Extraction — mines hashtags, URLs, mentions, and 100+ known tools from raw tweet data (free, zero API calls)」（README）

> 「Vision Analysis — reads text, objects, and context from every image/GIF/video thumbnail (30–40 visual tags per image)」（README）

> 「Semantic Tagging — generates 25–35 searchable tags per bookmark for AI-powered search」（README）

> 「Categorization — assigns each bookmark to 1–3 categories with confidence scores」（README）
