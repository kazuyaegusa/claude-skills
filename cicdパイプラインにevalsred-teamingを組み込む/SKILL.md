# CI/CDパイプラインにevals/red teamingを組み込む

> promptfoo CLIをCI/CDスクリプトに統合し、Pull Request時やデプロイ前に自動評価を実行、品質ゲートとして機能させる

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

LLMアプリのプロンプト変更はコードレビューだけでは品質を保証できない。自動評価により、プロンプト変更による性能退行やセキュリティリスクを早期検出できる

## いつ使うのか

プロンプト変更のPull Requestを自動検証したい、デプロイ前にレッドチーム攻撃を必須チェックとして実行したい、継続的なLLM品質モニタリングを構築する場合

## やり方

1. promptfooをCI環境にインストール（npm install promptfoo or Docker image）
2. promptfooconfig.yamlをリポジトリに配置
3. CI/CDスクリプト（GitHub Actions, GitLab CI等）に`promptfoo eval --no-interactive`を追加
4. 評価結果をJSON出力し、assertionsの失敗をCI失敗として扱う
5. promptfoo code-scanでPull Requestの差分をLLMセキュリティの観点で自動レビュー

### 入力

- promptfooconfig.yaml（CI用設定）
- CI/CD環境変数（APIキー）
- Pull Request差分（code-scan用）

### 出力

- CI/CDパイプラインのpass/fail判定
- 評価結果のアーティファクト（JSON/HTML）
- Pull RequestへのコメントまたはAnnotation

## 使うツール・ライブラリ

- promptfoo CLI
- GitHub Actions / GitLab CI / CircleCI等
- promptfoo code-scan（Pull Requestレビュー機能）

## コード例

```
# GitHub Actions例
name: Promptfoo Evals
on: [pull_request]
jobs:
  eval:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm install -g promptfoo
      - run: promptfoo eval --no-interactive
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
      - run: promptfoo code-scan
```

## 前提知識

- LLMの基本概念（プロンプト、トークン、temperature等のパラメータ）
- CLI操作の基礎知識
- YAML設定ファイルの読み書き
- LLMプロバイダー（OpenAI/Anthropic等）のAPIキー取得方法
- CI/CDパイプラインの基本（GitHub Actions等）
- レッドチーム攻撃の基本概念（prompt injection, jailbreak等）

## 根拠

> 「promptfoo is a CLI and library for evaluating and red-teaming LLM apps. Stop the trial-and-error approach - start shipping secure, reliable AI apps.」

> 「Private: LLM evals run 100% locally - your prompts never leave your machine」

> 「Update (March 16, 2026): Promptfoo has joined OpenAI. Promptfoo remains open source and MIT licensed.」

> 「npm install -g promptfoo / brew install promptfoo / pip install promptfoo」

> 「promptfoo eval / promptfoo view / promptfoo redteam」
