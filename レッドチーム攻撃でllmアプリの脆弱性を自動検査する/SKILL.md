# レッドチーム攻撃でLLMアプリの脆弱性を自動検査する

> promptfoo redteam機能を使い、prompt injection、PII漏洩、有害コンテンツ生成等の攻撃パターンを自動生成・実行してセキュリティ脆弱性を検出する

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

LLMアプリは従来のセキュリティテスト手法では検出できない固有の脆弱性（prompt injection等）を持つため、専用の攻撃シミュレーションが必要

## いつ使うのか

LLMアプリを本番リリース前にセキュリティチェックしたい時、定期的な脆弱性スキャンを自動化したい時

## やり方

1. `promptfoo redteam init`でレッドチーム設定を初期化 2. promptfooConfig.yamlにredteam攻撃タイプ（prompt-injection, pii-leak, harmful-content等）を指定 3. `promptfoo redteam run`で攻撃実行 4. ダッシュボードで脆弱性レポート確認 5. 検出された問題をプロンプト改善・ガードレール追加で修正

### 入力

- promptfooConfig.yaml（redteam攻撃タイプ設定）
- テスト対象のLLMエンドポイント

### 出力

- 脆弱性レポート（攻撃成功率・具体的な攻撃例）
- セキュリティダッシュボード

## 使うツール・ライブラリ

- promptfoo redteam機能

## コード例

```
# promptfooConfig.yaml redteam設定例
redteam:
  enabled: true
  plugins:
    - prompt-injection
    - pii-leak
    - harmful-content
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

> 「npm install -g promptfoo / brew install promptfoo / pip install promptfoo」
