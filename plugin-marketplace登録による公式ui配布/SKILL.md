# Plugin Marketplace登録による公式UI配布

> Claude Codeの `/plugin marketplace add` コマンドでリポジトリを登録し、Browse UIからスキルをインストール可能にする

- 出典: https://github.com/JimLiu/baoyu-skills
- 投稿者: JimLiu
- カテゴリ: claude-code-workflow

## なぜ使うのか

公式のプラグイン管理UIを使えば、ユーザーはコマンドを覚えなくてもGUIでスキルを検索・インストール・更新できる。自動更新機能も利用可能

## いつ使うのか

ユーザーがCLIに不慣れで、GUIでのインストールを好む場合。定期的な更新を自動化したい場合

## やり方

1. リポジトリルートに `plugin-marketplace.json` を作成
2. `plugins` 配列に1つのプラグインとして全スキルを定義(nameやskillsリスト)
3. ユーザーに `/plugin marketplace add JimLiu/baoyu-skills` を実行してもらう
4. Browse UIから「baoyu-skills」を選択し「Install now」をクリック
5. 自動更新を有効化すれば、リポジトリ更新時に自動でスキルが更新される

### 入力

- plugin-marketplace.json(プラグイン定義)
- GitHubリポジトリURL

### 出力

- Claude Code内でのMarketplace登録
- Browse UIからのインストール対応
- 自動更新機能

## 使うツール・ライブラリ

- Claude Code Plugin Marketplace API

## 前提知識

- Claude Codeの基本的な使い方とスキルの概念
- GitHubリポジトリの作成・管理
- JSON形式の理解(plugin-marketplace.json作成のため)
- 環境変数と.envファイルの扱い方
- Bashスクリプトの基本(ClawHub公開スクリプト利用時)

## 根拠

> 「npx skills add jimliu/baoyu-skills」でクイックインストール可能

> 「/plugin marketplace add JimLiu/baoyu-skills」でMarketplace登録

> 「The marketplace now exposes a single plugin so each skill is registered exactly once.」
