# promptfooによるレッドチーム（脆弱性スキャン）実施

> promptfoo red teamコマンドで、プロンプトインジェクション、PII漏洩、有害コンテンツ生成など、LLMアプリ特有のセキュリティ脆弱性を自動検出し、ダッシュボードでレポートする

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

LLMアプリは従来のセキュリティテストでは捕捉できない攻撃（プロンプトインジェクション、ジェイルブレイク等）に脆弱。本番投入前に網羅的な脆弱性スキャンを実行することで、インシデントを予防し、コンプライアンス要件を満たせる

## いつ使うのか

LLMアプリを本番リリース前にセキュリティ監査したい時、新しいプロンプトやモデルのリスクを評価したい時、規制対応でセキュリティ証跡が必要な時、定期的な脆弱性再評価をCI/CDに組み込みたい時

## やり方

1. promptfooインストール（前述手順）
2. レッドチーム用のYAML設定ファイルを作成（targets: ターゲットプロンプト、plugins: 脆弱性カテゴリ指定）
3. `promptfoo redteam` コマンド実行（または `promptfoo redteam init` で対話的セットアップ）
4. promptfooが自動生成した攻撃ペイロードをLLMに送信し、応答を分析
5. 脆弱性ダッシュボードで検出された問題（重大度、カテゴリ、サンプル出力）を確認
6. 問題箇所のプロンプトやガードレールを修正し再スキャン

### 入力

- レッドチーム用YAML設定（ターゲットプロンプト、脆弱性プラグイン指定）
- LLMプロバイダーAPIキー
- システムプロンプトやRAGコンテキスト（任意）

### 出力

- 脆弱性ダッシュボード（Webビュー）
- 検出された脆弱性のカテゴリ別レポート（プロンプトインジェクション、PII漏洩、有害出力等）
- 修正推奨アクションと再現サンプル

## 使うツール・ライブラリ

- promptfoo CLI（redteamサブコマンド）
- 対応LLMプロバイダーAPI

## コード例

```
# promptfoorc.yaml レッドチーム設定例（概念）
targets:
  - 'file://system_prompt.txt'
providers:
  - openai:gpt-4
redteam:
  plugins:
    - prompt-injection
    - pii
    - harmful
    - overreliance
# コマンド実行
# promptfoo redteam
# promptfoo view  # 脆弱性ダッシュボードを開く
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

> Test your prompts, agents, and RAGs. Red teaming/pentesting/vulnerability scanning for AI. Compare performance of GPT, Claude, Gemini, Llama, and more. Used by OpenAI and Anthropic.

> npm install -g promptfoo; promptfoo init --example getting-started; cd getting-started; promptfoo eval; promptfoo view
