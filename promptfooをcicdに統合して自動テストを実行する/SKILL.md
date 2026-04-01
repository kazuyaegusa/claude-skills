# promptfooをCI/CDに統合して自動テストを実行する

> GitHub Actions等のCI環境でpromptfoo evalを実行し、評価基準を満たさない場合にビルドを失敗させる

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

手動でのプロンプト評価は忘れられやすく、本番にバグが混入しやすい。CI/CDに組み込むことで、全てのコミット・PRで自動的に品質チェックが走り、回帰を防げる

## いつ使うのか

プロンプト変更を含むPRをマージする前、定期的な品質モニタリングとして

## やり方

1. リポジトリに `promptfooconfig.yaml` を配置
2. CI環境の環境変数にLLM APIキーを設定
3. GitHub Actionsワークフローで `npx promptfoo@latest eval --ci` を実行
4. `--threshold` オプションで最低スコアを指定（例: 80%）
5. スコアが閾値未満の場合、ジョブを失敗させてマージをブロック
6. 評価結果をArtifactとして保存し、後から参照可能にする

### 入力

- promptfooの設定ファイル
- CI環境変数（APIキー・閾値）

### 出力

- CIジョブの成功/失敗ステータス
- 評価結果のサマリ（Artifact）

## 使うツール・ライブラリ

- promptfoo
- GitHub Actions / GitLab CI / CircleCI等

## コード例

```
# .github/workflows/promptfoo.yml
name: LLM Eval
on: [pull_request]
jobs:
  eval:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm install -g promptfoo
      - run: promptfoo eval --ci --threshold 0.8
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

## 前提知識

- Node.js/npm/Python環境（promptfooのインストール方法による）
- LLMプロバイダーのAPIキー（OpenAI/Anthropic等）
- YAMLの基本的な構文知識
- LLMアプリの基本的な開発経験（プロンプトエンジニアリング・API呼び出し）

## 根拠

> 「LLM evals run 100% locally - your prompts never leave your machine」

> コードスニペット: `promptfoo init --example getting-started`, `promptfoo eval`, `promptfoo view`
