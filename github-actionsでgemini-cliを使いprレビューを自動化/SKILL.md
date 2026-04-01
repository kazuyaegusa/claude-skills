# GitHub Actionsでgemini-cliを使いPRレビューを自動化

> google-github-actions/run-gemini-cliアクションを使い、PR作成時に自動レビューコメントを投稿する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

手動レビュー前にLLMによる初期チェック（バグ検出、コーディング規約違反等）を行い、レビュー効率を向上させる

## いつ使うのか

PRレビューを自動化したい、Issue triageを自動化したい、@gemini-cliメンション時にLLMを呼び出したい場合

## やり方

1. `.github/workflows/review.yml` を作成
2. `google-github-actions/run-gemini-cli` アクションを使用
3. PR差分を入力として渡し、レビューコメントを生成
4. `GITHUB_TOKEN` でPRへコメント投稿
5. トリガーは `pull_request` イベント

### 入力

- GitHub Actions環境
- GEMINI_API_KEY または GOOGLE_API_KEY
- PR差分データ

### 出力

- PRへの自動レビューコメント
- Issue自動ラベリング

## 使うツール・ライブラリ

- google-github-actions/run-gemini-cli
- GitHub Actions
- GITHUB_TOKEN

## コード例

```
# .github/workflows/review.yml
name: PR Review
on:
  pull_request:
    types: [opened, synchronize]
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: google-github-actions/run-gemini-cli@v1
        with:
          prompt: 'Review this PR for bugs and style issues'
          gemini-api-key: ${{ secrets.GEMINI_API_KEY }}
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

> 「Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action」（GitHub Actions統合）
