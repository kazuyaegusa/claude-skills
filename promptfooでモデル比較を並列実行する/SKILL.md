# promptfooでモデル比較を並列実行する

> 複数のLLMプロバイダー（OpenAI/Anthropic/Bedrock/Ollama等）を同一テストケースで並列評価し、コスト・レイテンシ・品質を一覧比較する

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

異なるAPIを手動で叩いて結果を記録するのは非効率で、公平な比較が難しい。promptfooは並列実行・キャッシュ機能により、同一条件での比較を効率的に実現する

## いつ使うのか

モデル選定時、コスト削減のためのプロバイダー移行検討時、新モデルのベンチマーク時

## やり方

1. YAMLの `providers` セクションに比較対象モデルをリスト化
2. `tests` セクションで共通のテストケースを定義
3. `promptfoo eval` を実行すると、全モデルに対して並列リクエスト
4. Web UIでマトリクス表示（行=テストケース、列=モデル）
5. スコア・コスト・レイテンシを色分けで可視化
6. JSON/CSVエクスポートでスプレッドシート分析も可能

### 入力

- 比較対象モデルのリスト
- 共通テストケース

### 出力

- モデル別の評価スコア・コスト・レイテンシ一覧
- Web UIでのビジュアル比較

## 使うツール・ライブラリ

- promptfoo

## コード例

```
# promptfoorc.yaml
providers:
  - openai:gpt-4o
  - anthropic:claude-3-5-sonnet-20241022
  - bedrock:anthropic.claude-v2
  - ollama:llama3.1
tests:
  - vars:
      query: "Explain quantum computing"
    assert:
      - type: latency
        threshold: 5000  # ms
      - type: cost
        threshold: 0.05
```

## 前提知識

- Node.js/npm/Python環境（promptfooのインストール方法による）
- LLMプロバイダーのAPIキー（OpenAI/Anthropic等）
- YAMLの基本的な構文知識
- LLMアプリの基本的な開発経験（プロンプトエンジニアリング・API呼び出し）

## 根拠

> コードスニペット: `promptfoo init --example getting-started`, `promptfoo eval`, `promptfoo view`

> Web UIスクリーンショット: 評価マトリクス・レッドチームダッシュボード
