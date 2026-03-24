# promptfoo code scanによるPull Requestセキュリティレビュー

> Pull Request差分内のLLM関連コード（プロンプト、パラメータ変更等）を静的解析し、セキュリティ・コンプライアンス違反を自動検出してコメント追加する

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

人手コードレビューではLLM特有のリスク（プロンプトインジェクション誘発、PII取り扱い不備等）を見落としやすい。promptfoo code scanは専門知識を自動適用し、マージ前に問題を指摘できる

## いつ使うのか

複数人でLLMアプリを開発しコードレビュー負荷が高い時、セキュリティ専門家がチーム内にいない時、コンプライアンス基準を自動チェックしたい時、レビュー品質を標準化したい時

## やり方

1. promptfoo CLIインストール
2. CI/CD（GitHub Actions等）でPull Requestトリガーを設定
3. `promptfoo code scan` コマンドを実行（差分ファイルを引数指定またはGit連携）
4. promptfooが変更箇所を解析し、セキュリティルール違反を検出
5. 検出結果をPRコメントとして自動投稿（GitHub API連携）
6. 開発者がコメントを確認し修正後、再スキャンでクリア確認

### 入力

- Pull Request差分ファイル（Git連携）
- promptfoo code scan設定（ルールセット、無視パス等）
- GitHub APIトークン（PR投稿用）

### 出力

- Pull Requestへのインラインコメント（セキュリティ指摘）
- スキャンレポート（JSON/HTML）
- CI/CDステータス（問題あれば失敗）

## 使うツール・ライブラリ

- promptfoo code scan
- GitHub API（コメント投稿用）
- CI/CD環境

## コード例

```
# CI/CD統合例（概念）
# .github/workflows/code-scan.yml
name: Promptfoo Code Scan
on:
  pull_request:
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0  # 差分取得のため全履歴取得
      - run: npm install -g promptfoo
      - run: promptfoo code scan
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## 前提知識

- Node.js（npm経由でインストール時）またはPython（pip経由インストール時）の実行環境
- LLMプロバイダー（OpenAI、Anthropic等）のAPIキー取得方法
- YAMLファイルの基本文法（promptfoo設定記述時）
- CI/CD（GitHub Actions、GitLab CI等）の基本的な設定方法（CI統合時）
- LLMのプロンプトエンジニアリング基礎知識（評価基準設計時）

## 根拠

> promptfoo is a CLI and library for evaluating and red-teaming LLM apps. Stop the trial-and-error approach - start shipping secure, reliable AI apps.

> Update (March 16, 2026): Promptfoo has joined OpenAI. Promptfoo remains open source and MIT licensed.

> Review pull requests for LLM-related security and compliance issues with code scanning

> npm install -g promptfoo; promptfoo init --example getting-started; cd getting-started; promptfoo eval; promptfoo view
