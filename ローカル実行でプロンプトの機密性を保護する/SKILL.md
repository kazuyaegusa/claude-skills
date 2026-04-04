# ローカル実行でプロンプトの機密性を保護する

> promptfooは100%ローカルで動作し、プロンプトやテストデータを外部サービスに送信しない

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

プロンプトにはビジネスロジックや機密情報が含まれる場合があり、外部サービスに送信するとデータ漏洩リスクがある

## いつ使うのか

プロンプトに機密情報が含まれる場合、データガバナンス要件が厳しい企業環境で利用する場合

## やり方

1. promptfooをローカル環境にインストール（npm/brew/pip） 2. promptfoo eval実行時、LLM APIへのリクエストのみ発生（promptfoo自体のサーバーには通信しない） 3. 評価結果もローカルに保存 4. promptfoo viewでローカルWebサーバーを起動して結果表示

### 入力

- promptfooConfig.yaml（ローカルファイル）
- APIキー（環境変数）

### 出力

- ローカルファイルシステムに保存された評価結果

## 使うツール・ライブラリ

- promptfoo CLI（ローカル実行）

## コード例

```
# promptfooは外部サービスにデータ送信しない
# promptfoo eval → LLM APIのみにリクエスト
# promptfoo view → localhost:15500でWeb UI起動
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
