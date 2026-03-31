# 宣言的なevals設定でプロンプトを自動評価する

> YAML設定ファイルにプロンプト・モデル・テストケース・評価基準を記述し、promptfoo CLIで一括評価を実行する

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

手動評価は再現性が低く、プロンプト変更の影響を定量的に追跡できない。宣言的設定により評価をコード化し、バージョン管理・自動化・チーム共有が可能になる

## いつ使うのか

プロンプト改善のPDCAを回す、複数のプロンプトバリエーションを体系的に比較する、プロンプトの性能退行（regression）を防ぎたい場合

## やり方

1. `promptfoo init --example getting-started`でテンプレート生成
2. promptfooconfig.yaml にプロンプト（prompts配列）、モデル（providers配列）、テストケース（tests配列）を記述
3. `promptfoo eval`で評価実行（結果はJSON/CSVで出力）
4. `promptfoo view`でWebベースのUI起動、プロンプト×モデルのマトリクス表示
5. 評価基準（assertionsフィールド）でpass/failを自動判定

### 入力

- promptfooconfig.yaml（プロンプト定義、モデル設定、テストケース、評価基準）
- LLMプロバイダーのAPIキー（環境変数）

### 出力

- 評価結果（JSON/CSV）
- Webダッシュボード（promptfoo view）
- pass/fail判定レポート

## 使うツール・ライブラリ

- promptfoo CLI（npm/brew/pip）
- promptfooconfig.yaml（設定ファイル）

## コード例

```
# インストール・実行例
npm install -g promptfoo
promptfoo init --example getting-started
export OPENAI_API_KEY=sk-...
cd getting-started
prompttoo eval
prompttoo view
```

## 前提知識

- LLMの基本概念（プロンプト、トークン、temperature等のパラメータ）
- CLI操作の基礎知識
- YAML設定ファイルの読み書き
- LLMプロバイダー（OpenAI/Anthropic等）のAPIキー取得方法
- CI/CDパイプラインの基本（GitHub Actions等）
- レッドチーム攻撃の基本概念（prompt injection, jailbreak等）
