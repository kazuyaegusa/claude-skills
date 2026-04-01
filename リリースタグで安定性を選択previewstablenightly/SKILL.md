# リリースタグで安定性を選択（preview/stable/nightly）

> npm installで `@preview`, `@latest`, `@nightly` タグを指定して、リリースの安定性を制御する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

最新機能を試したい場合はnightly/preview、本番利用ではstableを選び、回帰リスクを管理できる

## いつ使うのか

新機能をいち早く試したい場合（nightly/preview）、本番環境で使う場合（stable）

## やり方

1. 最新安定版: `npm install -g @google/gemini-cli@latest`
2. プレビュー版（火曜23:59 UTC公開）: `npm install -g @google/gemini-cli@preview`
3. ナイトリー版（毎日00:00 UTC公開）: `npm install -g @google/gemini-cli@nightly`
4. バージョン確認: `gemini --version`

### 入力

- npm
- 希望するリリースタグ

### 出力

- 指定したバージョンのGemini CLI
- 安定性レベルに応じた機能セット

## 使うツール・ライブラリ

- npm
- @google/gemini-cli

## コード例

```
# 安定版
npm install -g @google/gemini-cli@latest

# プレビュー（毎週火曜23:59 UTC）
npm install -g @google/gemini-cli@preview

# ナイトリー（毎日00:00 UTC）
npm install -g @google/gemini-cli@nightly
```

## 前提知識

- Node.js 18以上の基本的な理解
- ターミナル操作の基礎知識
- npmパッケージマネージャーの基本的な使い方
- LLM APIの基本概念（プロンプト、トークン、コンテキストウィンドウ）
- OAuth認証フローの概要理解（ブラウザベース認証）
- JSON形式の基本的なパース方法
- （GitHub Actions利用の場合）GitHub Actionsの基本構文
- （MCP利用の場合）Model Context Protocolの概要

## 根拠

> 「Install with Anaconda: conda create -y -n gemini_env -c conda-forge nodejs」（Anaconda環境でのインストール手順）
