# /codex:adversarialで敵対的レビュー

> Claude Codeターミナルで /codex:adversarial を実行し、通常より厳格な批判的視点でのコードレビューを取得する

- 出典: https://x.com/masahirochaen/status/2038790628021346747
- 投稿者: チャエン | デジライズ CEO《重要AIニュースを毎日最速で発信》
- カテゴリ: claude-code-workflow

## なぜ使うのか

通常レビューでは見逃しやすいバグ・セキュリティ問題・設計上の欠陥を、意図的に攻撃的な目線で洗い出すため

## いつ使うのか

本番リリース前・外部公開APIの実装・セキュリティが重要なコードで見落としリスクをゼロに近づけたいとき

### 具体的な適用場面

- Claude Codeで実装後、同一セッションを維持したままCodeXに別視点のコードレビューを依頼したいとき
- Claude Codeが解決できなかった問題をCodeXに引き継ぐことで別アプローチの解法を得たいとき
- セキュリティ・バグに対して意図的に批判的な視点（adversarial）でレビューしてリリース前の品質を高めたいとき

## やり方

1. Claude Codeのターミナルで `/codex:adversarial` を入力・実行 2. CodeXが厳格モードで潜在バグ・セキュリティ脆弱性・設計の弱点を列挙して返してくる

### 入力

- Claude Codeのアクティブセッション
- ChatGPTアカウント（無料プラン可）

### 出力

- 厳格な批判的レビュー・潜在バグ・セキュリティ指摘リスト

## 使うツール・ライブラリ

- Claude Code CLI
- OpenAI CodeX

## コード例

```
/codex:adversarial
```

## 前提知識

- Claude Code CLIがインストール済みであること
- ChatGPTアカウント（無料プラン含む）が必要

## 根拠

> 「/codex:review：標準コードレビュー」

> 「/codex:adversarial ：厳格な敵対的レビュー」

> 「/codex:rescue：タスクをCodexへ丸ごと委任」

> 「ChatGPT無料プラン含む全ユーザー対象」

> 「ClaudeとCodeXが同じターミナルで使えるだと…」
