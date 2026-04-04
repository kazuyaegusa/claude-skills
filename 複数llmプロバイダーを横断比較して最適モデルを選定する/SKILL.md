# 複数LLMプロバイダーを横断比較して最適モデルを選定する

> promptfooConfig.yamlに複数のプロバイダー（openai:gpt-4, anthropic:claude-3-opus, bedrock:*, ollama:*等）を列挙し、同一テストケースで一括評価する

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

LLMモデルはタスクによって得意不得意があり、コスト・速度・品質のトレードオフも異なる。実データで比較しないと最適解は分からない

## いつ使うのか

新規プロジェクトでモデル選定する時、既存モデルからの乗り換えを検討する時、コスト削減のため代替モデルを探す時

## やり方

1. promptfooConfig.yamlのprovidersセクションに複数モデルを記述 2. `promptfoo eval`で全モデルに対して同一テスト実行 3. `promptfoo view`でマトリクス表示 4. スコア・レイテンシ・コストを比較して最適モデル選定

### 入力

- promptfooConfig.yaml（複数プロバイダー設定）
- 各プロバイダーのAPIキー

### 出力

- モデル×テストケースの評価マトリクス
- パフォーマンス比較レポート

## 使うツール・ライブラリ

- promptfoo CLI
- 対応プロバイダー: OpenAI, Anthropic, Azure, AWS Bedrock, Google Gemini, Ollama, HuggingFace等

## コード例

```
providers:
  - openai:gpt-4-turbo
  - anthropic:claude-3-opus-20240229
  - azureopenai:chat:gpt-4-deployment
  - bedrock:anthropic.claude-v2
  - ollama:llama2
```

## 前提知識

- LLM API（OpenAI/Anthropic等）の基本的な利用経験
- コマンドラインツール（npm/pip）の基本操作
- YAMLファイルの基本文法
- （オプション）CI/CDの基本概念（GitHub Actions等）
- （オプション）レッドチーム攻撃・セキュリティテストの基本概念
