# リポジトリから直接Happyを実行する

> npmパッケージではなくGitHubリポジトリをクローンして `yarn cli` でHappyを起動する

- 出典: https://x.com/gaijineers/status/2021043018498015248
- 投稿者: gaijineers
- カテゴリ: claude-code-workflow

## なぜ使うのか

開発版を試す、カスタマイズする、またはローカルビルドで最新機能を使いたい場合に必要

## いつ使うのか

npm版ではなく最新のmainブランチを使いたい、またはソースコードを改変して独自機能を追加したいとき

### 具体的な適用場面

- 通勤中にスマホでClaude Codeセッションをレビュー・指示を追加したい
- 自宅PCで開始したCodexセッションを外出先のタブレットから継続したい
- チームで同じClaude Codeセッションを共有・引き継ぎたい
- デスクトップ環境がないときにブラウザだけでAIコーディングを行いたい

## やり方

1. `git clone https://github.com/slopus/happy.git` でリポジトリをクローン
2. リポジトリルートで `yarn install` を実行して依存関係をインストール
3. `yarn cli --help` でヘルプを確認
4. `yarn cli` でClaude Code相当、`yarn cli codex` でCodex相当を起動

### 入力

- git, Node.js, yarn がインストール済みの環境
- https://github.com/slopus/happy へのアクセス

### 出力

- ローカルビルド版のHappy CLI

## 使うツール・ライブラリ

- git
- yarn
- Node.js

## コード例

```
# リポジトリルートで
yarn cli --help
yarn cli            # Claude Code相当
yarn cli codex      # Codex相当
```

## 前提知識

- Claude Code または Codex が既にインストールされている
- Node.js と npm の基本的な使い方
- iOS/Android/Webアプリのインストール方法
- E2E暗号化の基本概念（ペアリング、鍵交換）

## 根拠

> 「Mobile and Web Client for Claude Code & Codex」— 公式READMEより

> 「Use Claude Code or Codex from anywhere with end-to-end encryption.」— 公式説明

> 「npm install -g happy-coder」「happy」「happy codex」— インストール・実行手順

> 「📱 iOS App, 🤖 Android App, 🌐 Web App」— マルチプラットフォーム対応

> 「yarn cli --help」「yarn cli codex」— ソースから実行する方法
