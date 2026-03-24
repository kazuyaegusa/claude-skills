# promptfooでの複数モデル並列比較

> 同一プロンプトを複数のLLMプロバイダー（OpenAI、Anthropic、Gemini、Ollama等）に並列送信し、出力品質・コスト・レイテンシを横並びで定量比較する

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

単一モデルに依存すると、コスト高騰やモデル仕様変更でリスクが大きい。複数モデルを比較すればコストパフォーマンスに優れた選択肢を発見でき、ベンダーロックインを回避できる

## いつ使うのか

新規LLMアプリ開発時にモデル選定したい時、既存モデルのコスト削減を検討する時、モデルアップグレード前に性能差を確認したい時、マルチモデル戦略（タスクごとに最適モデル切り替え）を設計したい時

## やり方

1. promptfoorc.yamlの `providers` セクションに複数プロバイダーを列挙（例: openai:gpt-4, anthropic:claude-3-sonnet, openai:gpt-3.5-turbo, ollama:llama2等）
2. 各プロバイダーのAPIキー・エンドポイントを環境変数または設定ファイルに記述
3. `promptfoo eval` 実行で全プロバイダーに同一テストケースを並列送信
4. promptfoo viewでモデル別の出力品質（アサーションpass率）、レスポンスタイム、トークン使用量をマトリクス表示
5. コスト試算機能（設定で有効化）を使えば、各モデルの実行コストも比較可能
6. 最適モデルを選定し、本番設定を更新

### 入力

- promptfoorc.yaml（複数プロバイダー指定）
- 各プロバイダーのAPIキー
- 共通テストケース

### 出力

- モデル×テストケースの評価マトリクス
- 各モデルのpass率・平均レイテンシ・トークン消費量
- コスト比較レポート（オプション）

## 使うツール・ライブラリ

- promptfoo CLI
- 対応プロバイダー（OpenAI、Anthropic、Google AI、Azure OpenAI、AWS Bedrock、Ollama、Replicate、Hugging Face等）

## コード例

```
# promptfoorc.yaml 複数プロバイダー例（概念）
providers:
  - id: openai:gpt-4
    label: GPT-4
  - id: anthropic:claude-3-sonnet-20240229
    label: Claude 3 Sonnet
  - id: openai:gpt-3.5-turbo
    label: GPT-3.5 Turbo
  - id: ollama:llama2
    label: Llama 2 (Ollama)
prompts:
  - '{{prompt}}'
tests:
  - vars:
      prompt: 'Pythonでクイックソートを実装してください'
    assert:
      - type: contains
        value: 'def quicksort'
      - type: llm-rubric
        value: 'コードが正しく動作し、説明が明確である'
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

> npm install -g promptfoo; promptfoo init --example getting-started; cd getting-started; promptfoo eval; promptfoo view
