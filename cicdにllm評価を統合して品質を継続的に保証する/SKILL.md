# CI/CDにLLM評価を統合して品質を継続的に保証する

> GitHub Actions等のCI/CDパイプラインでprompfoo evalを実行し、プロンプト変更のPull Requestに対して自動テスト・品質チェックを行う

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

LLMアプリの品質はプロンプト変更で容易に劣化する。コードレビューと同様にプロンプト変更も自動テストで保護すべき

## いつ使うのか

チーム開発でプロンプトをバージョン管理している時、本番品質を保ちながら反復開発したい時

## やり方

1. promptfooConfig.yamlをリポジトリにコミット 2. .github/workflows/promptfoo.ymlを作成 3. ワークフロー内で`promptfoo eval`を実行 4. assertionに失敗したらPRをブロック 5. promptfoo code scanningでセキュリティ問題も自動検出

### 入力

- promptfooConfig.yaml
- CI/CD環境（GitHub Actions, GitLab CI等）
- APIキー（CI環境のシークレット）

### 出力

- CI/CDパイプラインの成功/失敗ステータス
- 評価結果サマリー（PR コメント等）

## 使うツール・ライブラリ

- promptfoo CLI
- GitHub Actions / GitLab CI / その他CI/CDツール

## コード例

```
# .github/workflows/promptfoo.yml例
name: Promptfoo Eval
on: [pull_request]
jobs:
  eval:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm install -g promptfoo
      - run: promptfoo eval
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

## 前提知識

- LLM API（OpenAI/Anthropic等）の基本的な利用経験
- コマンドラインツール（npm/pip）の基本操作
- YAMLファイルの基本文法
- （オプション）CI/CDの基本概念（GitHub Actions等）
- （オプション）レッドチーム攻撃・セキュリティテストの基本概念

## 根拠

> 「promptfoo is a CLI and library for evaluating and red-teaming LLM apps. Stop the trial-and-error approach - start shipping secure, reliable AI apps.」

> 「Promptfoo is now part of OpenAI. Promptfoo remains open source and MIT licensed.」

> 「Review pull requests for LLM-related security and compliance issues with code scanning」

> 「npm install -g promptfoo / brew install promptfoo / pip install promptfoo」
