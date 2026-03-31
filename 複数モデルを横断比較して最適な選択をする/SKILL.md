# 複数モデルを横断比較して最適な選択をする

> promptfooconfig.yamlのproviders配列に複数のLLMプロバイダーを列挙し、同一テストケースで性能・コスト・レイテンシを比較する

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

モデルごとに得手不得手があり、タスクに応じた最適なモデルは異なる。横断比較により、コスト・品質・速度のトレードオフを定量的に判断できる

## いつ使うのか

新規プロジェクトでどのLLMを採用すべきか判断する、既存モデルから別モデルへの移行を検討する、マルチモデル戦略（タスクごとに最適モデルを使い分け）を設計する場合

## やり方

1. promptfooconfig.yamlのprovidersに複数モデルを記述（openai:gpt-4, anthropic:claude-3-opus, etc.）
2. 各プロバイダーのAPIキーを環境変数に設定
3. `promptfoo eval`で全モデルに対して同一テストケースを実行
4. promptfoo viewのマトリクス表示で、モデル×テストケースの結果を並べて比較
5. 評価指標（精度・コスト・レイテンシ）をカスタム定義可能

### 入力

- promptfooconfig.yaml（複数providers）
- 各プロバイダーのAPIキー

### 出力

- モデル×テストケースのマトリクス
- 性能・コスト・レイテンシの比較表
- 推奨モデルのランキング

## 使うツール・ライブラリ

- promptfoo CLI
- promptfooがサポートするプロバイダー（OpenAI, Anthropic, Azure, Bedrock, Ollama等）

## コード例

```
# promptfooconfig.yamlの例
providers:
  - openai:gpt-4
  - anthropic:claude-3-opus
  - openai:gpt-3.5-turbo
  - ollama:llama3

tests:
  - description: "複雑な推論タスク"
    vars:
      input: "..."
    assert:
      - type: contains
        value: "期待される回答の一部"
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

> 「Update (March 16, 2026): Promptfoo has joined OpenAI. Promptfoo remains open source and MIT licensed.」

> 「npm install -g promptfoo / brew install promptfoo / pip install promptfoo」

> 「promptfoo eval / promptfoo view / promptfoo redteam」
