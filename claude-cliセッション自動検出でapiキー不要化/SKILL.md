# Claude CLIセッション自動検出でAPIキー不要化

> ローカルで動いているClaude CLIの認証セッションをアプリが自動検出し、別途APIキーを設定しなくてもLLM機能を利用できるようにする

- 出典: https://x.com/l_go_mrk/status/2037749522021892427
- 投稿者: AI駆動塾
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude CLIはAnthropicのサブスクリプション認証を使うため、APIキーを別途取得・設定する手間が省ける。ツールのオンボーディング摩擦を大幅に削減し、既存Claude Codeユーザーがゼロ設定で使い始められる

## いつ使うのか

Claude Codeサブスクリプションを持っており、LLM APIキーを別途用意・管理したくないとき

### 具体的な適用場面

- 数百〜数千のTwitterブックマークが溜まり、後から目的の投稿が見つからなくなっている状況
- スクリーンショット付きの技術投稿をブックマークしているが、画像内のコードや図表が検索できない状況
- 技術情報・ツール情報をジャンル別に整理してマインドマップで全体把握したい場合

## やり方

1. Claude Code（claude CLI）を通常通りインストール・ログイン済みの状態にしておく（`claude` コマンドが動く状態）
2. Siftly を起動（`npm run dev`）
3. 設定画面のAIプロバイダー選択で「Claude CLI」オプションを選択する
4. APIキー入力不要でSemantic TaggingおよびCategorization ステージが動作する

### 入力

- ローカルにインストール済みのClaude CLI（有効セッション）
- 有効なClaude Codeサブスクリプション

### 出力

- APIキー設定なしでLLM機能（タグ生成・カテゴリ分類）が動作する状態

## 使うツール・ライブラリ

- claude CLI（Claude Code）

## 前提知識

- Node.js（Next.js 16が動作するバージョン、v18以上推奨）
- Git（リポジトリのクローン用）
- LLM APIキー（Claude / OpenAI等）、またはClaude CLIの有効セッション
- Twitter/Xアカウントのブックマーク機能を使っていること

## 根拠

> It runs a 4-stage AI pipeline on your bookmarks: Entity Extraction → Vision Analysis → Semantic Tagging → Categorization

> Claude CLIセッションを自動検出するから、Claude使ってる人はAPIキー設定すら不要。

> Vision Analysis — reads text, objects, and context from every image/GIF/video thumbnail (30–40 visual tags per image)

> Semantic Tagging — generates 25–35 searchable tags per bookmark for AI-powered search

> Categorization — assigns each bookmark to 1–3 categories with confidence scores
