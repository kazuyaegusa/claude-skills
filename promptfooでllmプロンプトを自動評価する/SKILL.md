# promptfooでLLMプロンプトを自動評価する

> 宣言的YAMLファイルでプロンプト・モデル・テストケース・評価基準を定義し、promptfoo CLIで一括実行・Web UIで結果を可視化する

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

手動での試行錯誤は再現性がなく、変更の影響範囲を把握できない。自動評価により、プロンプト修正時の品質劣化を定量的に検出し、複数モデルのコスト・レイテンシ・品質をデータドリブンで比較できる

## いつ使うのか

プロンプトを変更する前、新しいLLMプロバイダーへの移行を検討する時、本番デプロイ前の品質ゲートとして

## やり方

1. `npm install -g promptfoo` でCLIをインストール
2. `promptfoo init --example getting-started` でサンプル設定を生成
3. 環境変数 `OPENAI_API_KEY` 等でAPIキーを設定
4. YAMLファイルでプロンプト・モデル・テストケースを定義
5. `promptfoo eval` で評価実行（ローカルで完結、キャッシュ機能あり）
6. `promptfoo view` でWeb UIを起動し、結果マトリクスを可視化
7. CI/CDに統合する場合は `promptfoo eval --ci` を実行し、閾値未達時にビルドを失敗させる

### 入力

- YAMLの設定ファイル（プロンプト定義・モデル指定・テストケース・評価基準）
- LLMプロバイダーのAPIキー（環境変数）

### 出力

- 各プロンプト×モデル×テストケースの評価結果マトリクス
- Web UIでの可視化（スコア・レイテンシ・コスト比較）
- JSON/CSVでのエクスポート可能な評価結果

## 使うツール・ライブラリ

- promptfoo（npm/brew/pipで提供）
- Node.js（CLI実行時）

## コード例

```
# promptfoorc.yaml
prompts:
  - "Summarize: {{text}}"
  - "Extract key points from: {{text}}"
providers:
  - openai:gpt-4
  - anthropic:claude-3-5-sonnet-20241022
tests:
  - vars:
      text: "Long article text..."
    assert:
      - type: contains
        value: "key insight"
      - type: cost
        threshold: 0.01
```

## 前提知識

- Node.js/npm/Python環境（promptfooのインストール方法による）
- LLMプロバイダーのAPIキー（OpenAI/Anthropic等）
- YAMLの基本的な構文知識
- LLMアプリの基本的な開発経験（プロンプトエンジニアリング・API呼び出し）

## 根拠

> 「LLM evals run 100% locally - your prompts never leave your machine」

> コードスニペット: `promptfoo init --example getting-started`, `promptfoo eval`, `promptfoo view`
