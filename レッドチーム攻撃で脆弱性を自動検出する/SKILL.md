# レッドチーム攻撃で脆弱性を自動検出する

> promptfooのred teamingモードで、prompt injection・jailbreak・PII漏洩・バイアス等の攻撃パターンを自動生成し、LLMアプリの脆弱性レポートを出力する

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

LLMアプリは敵対的入力（adversarial inputs）に対して脆弱で、手動での網羅的検証は不可能。自動化されたレッドチーム攻撃により、リリース前にセキュリティリスクを検出できる

## いつ使うのか

LLMアプリを本番リリースする前にセキュリティ監査を行う、プロンプトインジェクション対策の有効性を検証する、PII漏洩リスクをチェックする場合

## やり方

1. promptfooconfig.yamlにredteam設定を追加（攻撃カテゴリ・対象プロンプト・評価基準）
2. `promptfoo redteam`コマンドで攻撃生成・実行
3. promptfooが敵対的プロンプトを自動生成（数百～数千パターン）
4. 各攻撃に対するLLM応答を評価し、脆弱性を検出
5. Webダッシュボードで脆弱性レポートを確認（カテゴリ別・重要度別）

### 入力

- promptfooconfig.yaml（redteam設定）
- 対象のLLMアプリケーション（API endpoint or prompt）

### 出力

- 脆弱性レポート（JSON/HTML）
- 攻撃成功率・重要度別の統計
- 具体的な攻撃例と応答例

## 使うツール・ライブラリ

- promptfoo CLI（redteamモード）
- promptfooのred teaming engine

## コード例

```
# promptfooconfig.yamlのredteam設定例
redteam:
  enabled: true
  categories:
    - prompt-injection
    - jailbreak
    - pii-leak
  severity: high

# 実行
prompttoo redteam
```

## 前提知識

- LLMの基本概念（プロンプト、トークン、temperature等のパラメータ）
- CLI操作の基礎知識
- YAML設定ファイルの読み書き
- LLMプロバイダー（OpenAI/Anthropic等）のAPIキー取得方法
- CI/CDパイプラインの基本（GitHub Actions等）
- レッドチーム攻撃の基本概念（prompt injection, jailbreak等）
