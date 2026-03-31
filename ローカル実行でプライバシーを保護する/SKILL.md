# ローカル実行でプライバシーを保護する

> promptfooはすべての評価処理をローカル環境で実行し、プロンプトや評価データを外部サーバーに送信しない

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

LLMアプリ開発では機密情報を含むプロンプトを扱うことが多い。ローカル実行により、プロンプトや評価結果の外部流出リスクをゼロにできる

## いつ使うのか

機密性の高いプロンプトやデータを扱う、社内規定で評価データの外部送信が禁止されている、オフライン環境で評価を実行したい場合

## やり方

1. promptfooをローカル環境にインストール（npm/brew/pip）
2. promptfooconfig.yamlとテストデータをローカルに配置
3. promptfoo eval実行時、promptfooはLLM APIに直接リクエストを送信（promptfoo自体のサーバーを経由しない）
4. 評価結果はローカルの.promptfoo/ディレクトリに保存
5. promptfoo viewもローカルサーバーとして起動（外部アクセス不可）

### 入力

- ローカル環境のprompttooインストール
- promptfooconfig.yaml
- LLM APIキー（ローカル環境変数）

### 出力

- ローカルの.promptfoo/ディレクトリに保存される評価結果
- ローカルホスト上のWebダッシュボード

## 使うツール・ライブラリ

- promptfoo CLI（ローカルインストール）

## コード例

```
# すべてローカルで完結
npm install -g promptfoo
export OPENAI_API_KEY=sk-...
prompttoo eval  # データはローカルに保存
prompttoo view  # http://localhost:15500 で起動
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
