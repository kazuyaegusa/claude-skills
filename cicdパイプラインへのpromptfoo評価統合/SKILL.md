# CI/CDパイプラインへのpromptfoo評価統合

> promptfoo evalをCI/CDスクリプトに組み込み、プロンプト変更が品質基準を満たさない場合にビルドを失敗させる自動ゲート制御を実現する

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

手動でのプロンプトテストは属人的でリグレッションを見逃しやすい。CI/CDで自動化すれば、Pull Request時点で品質劣化を検出し、本番投入前に修正できる

## いつ使うのか

複数人でプロンプトを編集するプロジェクトで品質を担保したい時、モデル切り替えやプロンプト修正時の影響を自動検証したい時、レッドチームスキャンを定期実行してセキュリティ監視したい時

## やり方

1. promptfoo設定ファイル（promptfoorc.yaml）をリポジトリにコミット
2. CI/CD環境（GitHub Actions、GitLab CI、Jenkins等）にprompfooとNode.jsをインストール
3. APIキーをシークレット環境変数として設定
4. CIスクリプトで `promptfoo eval --output results.json` を実行
5. promptfooが終了コードで成否を返す（アサーション失敗時は非ゼロ）
6. 必要に応じてresults.jsonをアーティファクトとして保存し、PR上でコメント表示
7. promptfoo code scanコマンドを使えば、Pull Request差分に対してセキュリティ問題を自動レビュー可能

### 入力

- promptfoorc.yaml（リポジトリ内）
- CI/CD環境変数（APIキー、設定パス）
- CIスクリプト（.github/workflows/promptfoo.yml 等）

### 出力

- CI/CDビルドのpass/fail判定
- 評価結果JSON（アーティファクト）
- Pull Requestへのコメント（オプション）
- promptfoo code scanの場合はセキュリティレビューコメント

## 使うツール・ライブラリ

- promptfoo CLI
- GitHub Actions / GitLab CI / Jenkins等のCI/CDツール
- promptfoo code scanコマンド（PR用）

## コード例

```
# .github/workflows/promptfoo.yml 例（概念）
name: Promptfoo Evaluation
on:
  pull_request:
    paths:
      - 'prompts/**'
      - 'promptfoorc.yaml'
jobs:
  eval:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm install -g promptfoo
      - run: promptfoo eval --output results.json
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
      - uses: actions/upload-artifact@v3
        with:
          name: eval-results
          path: results.json
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

> Private: LLM evals run 100% locally - your prompts never leave your machine

> Review pull requests for LLM-related security and compliance issues with code scanning

> npm install -g promptfoo; promptfoo init --example getting-started; cd getting-started; promptfoo eval; promptfoo view
