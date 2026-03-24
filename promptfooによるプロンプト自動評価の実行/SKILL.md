# promptfooによるプロンプト自動評価の実行

> YAML設定ファイルに評価対象のプロンプト、テストケース、使用モデル、評価基準（アサーション）を記述し、promptfoo evalコマンドで一括実行して結果を可視化する

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

手動テストでは網羅性・再現性に欠け、モデル更新やプロンプト変更時の影響を見落としやすい。宣言的な設定で自動化すれば、継続的にLLM出力品質を監視でき、リグレッションを防げる

## いつ使うのか

プロンプトを新規作成・修正した時、モデルをアップグレードした時、品質要件を定義してベースラインを作りたい時、複数候補から最適プロンプトを選定したい時

## やり方

1. `npm install -g promptfoo` または `brew install promptfoo` でインストール
2. `promptfoo init --example getting-started` でサンプルプロジェクトを生成
3. プロバイダーのAPIキーを環境変数に設定（例: `export OPENAI_API_KEY=sk-abc123`）
4. YAMLファイルにプロンプト、テストケース、モデル（openai:gpt-4, anthropic:claude-3-sonnet等）、アサーション（contains、llm-rubric等）を記述
5. `promptfoo eval` で評価実行
6. `promptfoo view` でWebベースの結果マトリクスを開く
7. 必要に応じてコマンドライン出力やJSON形式でも確認

### 入力

- promptfoorc.yaml（プロンプト定義、テストケース、プロバイダー、アサーション）
- プロバイダーAPIキー（環境変数）
- 評価対象のプロンプトファイルまたはインラインテキスト

### 出力

- 評価結果のWebビュー（モデル×テストケースのマトリクス）
- JSON形式の評価レポート
- コマンドライン上のpass/failサマリ

## 使うツール・ライブラリ

- promptfoo CLI
- Node.js（CLIインストール時）
- 対応LLMプロバイダーAPI（OpenAI、Anthropic、Azure OpenAI、AWS Bedrock、Ollama等）

## コード例

```
# promptfoorc.yaml 例（概念）
prompts:
  - 'あなたは親切なアシスタントです。{{question}}'
providers:
  - openai:gpt-4
  - anthropic:claude-3-sonnet-20240229
tests:
  - vars:
      question: '日本の首都は？'
    assert:
      - type: contains
        value: '東京'
  - vars:
      question: 'Pythonでリストを逆順にする方法は？'
    assert:
      - type: llm-rubric
        value: 'reverse()メソッドまたはスライスを説明している'
```

## 前提知識

- Node.js（npm経由でインストール時）またはPython（pip経由インストール時）の実行環境
- LLMプロバイダー（OpenAI、Anthropic等）のAPIキー取得方法
- YAMLファイルの基本文法（promptfoo設定記述時）
- CI/CD（GitHub Actions、GitLab CI等）の基本的な設定方法（CI統合時）
- LLMのプロンプトエンジニアリング基礎知識（評価基準設計時）

## 根拠

> npm install -g promptfoo; promptfoo init --example getting-started; cd getting-started; promptfoo eval; promptfoo view
