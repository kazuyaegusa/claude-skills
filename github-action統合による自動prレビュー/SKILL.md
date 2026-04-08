# GitHub Action統合による自動PRレビュー

> Gemini CLI GitHub Actionを使い、PR作成時に自動でコードレビュー・Issue分類を実行する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

人手レビューコストを削減し、一貫性のあるフィードバックを提供するため

## いつ使うのか

チーム開発でのPRレビュー自動化、Issue自動ラベリング、定期的なコード品質チェック時

## やり方

1. リポジトリに `.github/workflows/gemini-cli.yml` を作成
2. `google-github-actions/run-gemini-cli@v1` アクションを設定
3. トリガー（pull_request, issues等）を定義
4. Gemini CLIにプロンプト（例: "Review this PR and suggest improvements"）を渡す
5. 結果をコメントとして自動投稿

### 入力

- GitHub Actionワークフロー定義
- GOOGLE_API_KEY等の認証情報（Secrets）

### 出力

- PR/Issueへの自動コメント

## 使うツール・ライブラリ

- GitHub Actions
- google-github-actions/run-gemini-cli

## コード例

```
# .github/workflows/gemini-cli.yml
name: Gemini CLI PR Review
on:
  pull_request:
    types: [opened, synchronize]
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: google-github-actions/run-gemini-cli@v1
        with:
          prompt: "Review this PR and suggest improvements"
        env:
          GOOGLE_API_KEY: ${{ secrets.GOOGLE_API_KEY }}
```

## 前提知識

- Node.js実行環境（npm/npx利用のため）
- Google アカウント（OAuth認証用）
- （任意）Gemini API Key または Vertex AI認証情報
- （GitHub Action利用時）GitHub リポジトリ管理権限
- （MCP利用時）各MCPサーバーのセットアップ知識

## 根拠

> "Free tier: 60 requests/min and 1,000 requests/day with personal Google account."

> "Powerful Gemini 3 models: Access to improved reasoning and 1M token context window."

> "Built-in tools: Google Search grounding, file operations, shell commands, web fetching."

> "npx @google/gemini-cli" - インストール不要実行

> "Integrate Gemini CLI directly into your GitHub workflows with Gemini CLI GitHub Action"
