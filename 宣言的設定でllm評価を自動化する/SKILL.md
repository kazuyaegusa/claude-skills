# 宣言的設定でLLM評価を自動化する

> YAMLファイルにプロンプト・モデル・テストケース・評価指標を定義し、promptfoo evalコマンドで一括実行する

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

手動での試行錯誤は再現性がなく非効率。設定ファイル化することでバージョン管理・チーム共有・CI/CD統合が可能になる

## いつ使うのか

複数のプロンプトやモデルを体系的に比較評価したい時、eval結果をチームで共有したい時

## やり方

1. `promptfoo init`で設定ファイル生成 2. promptfooConfig.yamlにproviders（モデル）、prompts（プロンプトテンプレート）、tests（入力・期待出力・assertion）を記述 3. `promptfoo eval`で評価実行 4. `promptfoo view`でWeb UIで結果確認

### 入力

- promptfooConfig.yaml（プロバイダー、プロンプト、テストケース定義）
- 環境変数（OPENAI_API_KEY等のAPIキー）

### 出力

- 評価結果のマトリクス（モデル×テストケースの成否・スコア）
- Web UI表示用のHTML/JSON

## 使うツール・ライブラリ

- promptfoo CLI（npm/brew/pip）
- promptfoo Node.jsライブラリ

## コード例

```
# promptfooConfig.yaml例
providers:
  - openai:gpt-4
  - anthropic:claude-3-opus
prompts:
  - "You are a helpful assistant. {{question}}"
tests:
  - vars:
      question: "What is 2+2?"
    assert:
      - type: contains
        value: "4"
```

## 前提知識

- LLM API（OpenAI/Anthropic等）の基本的な利用経験
- コマンドラインツール（npm/pip）の基本操作
- YAMLファイルの基本文法
- （オプション）CI/CDの基本概念（GitHub Actions等）
- （オプション）レッドチーム攻撃・セキュリティテストの基本概念
