# LLMアプリの脆弱性をレッドチーミング手法でスキャンする

> promptfooのred teamingモードで、プロンプトインジェクション・PII漏洩・ハルシネーション等の脆弱性を自動検出し、レポートを生成する

- 出典: https://github.com/promptfoo/promptfoo
- 投稿者: promptfoo
- カテゴリ: prompt-engineering

## なぜ使うのか

LLMアプリは従来のWebアプリとは異なる攻撃ベクトル（例: システムプロンプトの無視、禁止された情報の抽出）が存在し、手動テストでは網羅困難。自動化されたレッドチーム手法により、既知の攻撃パターンを継続的にチェックできる

## いつ使うのか

LLMアプリの本番リリース前、プロンプトやシステム設定を変更した後、定期的なセキュリティ監査として

## やり方

1. `promptfoo init --example red-team` でレッドチーム設定を初期化
2. YAMLで検査対象のエンドポイント・システムプロンプト・脆弱性カテゴリを定義
3. `promptfoo redteam` で攻撃パターンを自動生成・実行
4. 脆弱性レポートをWeb UIで確認（ダッシュボード形式）
5. CI/CDで `--fail-on-critical` フラグを指定し、重大な脆弱性検出時にビルドを失敗させる
6. PRレビュー時はcode scanningモードで静的解析を実行

### 入力

- 検査対象のLLMエンドポイント（APIまたはローカルモデル）
- システムプロンプト定義
- 脆弱性カテゴリ指定（injection/PII/harmful content等）

### 出力

- 脆弱性レポート（カテゴリ別の検出数・深刻度）
- 攻撃成功例のログ（入力プロンプト・モデル応答）
- 修正推奨事項

## 使うツール・ライブラリ

- promptfoo（red teaming機能内蔵）

## コード例

```
# redteam-config.yaml
target:
  provider: openai:gpt-4
  systemPrompt: "You are a helpful assistant."
vulnerabilities:
  - prompt-injection
  - pii-leak
  - harmful-content
assertions:
  - type: not-contains
    value: "SYSTEM PROMPT"
  - type: pii-not-present
```

## 前提知識

- Node.js/npm/Python環境（promptfooのインストール方法による）
- LLMプロバイダーのAPIキー（OpenAI/Anthropic等）
- YAMLの基本的な構文知識
- LLMアプリの基本的な開発経験（プロンプトエンジニアリング・API呼び出し）

## 根拠

> コードスニペット: `promptfoo init --example getting-started`, `promptfoo eval`, `promptfoo view`
