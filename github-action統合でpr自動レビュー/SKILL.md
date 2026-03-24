# GitHub Action統合でPR自動レビュー

> Gemini CLI GitHub Actionを使い、PRが作成されたときに自動でコードレビューコメントを投稿する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: prompt-engineering

## なぜ使うのか

レビュー負荷を削減し、形式的なチェックをAIに任せて、人間は本質的な設計レビューに集中できるため

## いつ使うのか

GitHub上でのPR/Issue管理を自動化したい場合

## やり方

1. リポジトリの`.github/workflows/`にGemini CLI Actionを追加
2. `on: pull_request`トリガーで起動するよう設定
3. 認証（GOOGLE_CLOUD_PROJECT, OAuth認証情報）を環境変数で渡す
4. PRコンテキストを読み込み、レビューコメントを自動投稿
5. Issueトリアージやラベル自動付与も可能

### 入力

- GitHub PR/Issueイベント
- Google Cloud認証情報

### 出力

- 自動投稿されたレビューコメント
- 自動付与されたラベル

## 使うツール・ライブラリ

- google-github-actions/run-gemini-cli
- GitHub Actions

## コード例

```
# .github/workflows/gemini-review.yml
on:
  pull_request:
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: google-github-actions/run-gemini-cli@v1
        with:
          prompt: "Review this PR"
```

## 前提知識

- Node.js実行環境（npm/npx利用のため）
- Googleアカウント（OAuth認証用）
- ターミナル操作の基礎知識
- （GitHub連携時）GitHubリポジトリとActions実行権限
- （MCP統合時）各サービスのAPI認証情報

## 根拠

> 🧠 Powerful Gemini 3 models: Access to improved reasoning and 1M token context window.

> npx @google/gemini-cli

> gemini -p "Explain the architecture of this codebase" --output-format json

> Custom context files (GEMINI.md) to tailor behavior for your projects

> Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action
