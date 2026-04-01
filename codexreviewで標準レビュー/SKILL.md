# /codex:reviewで標準レビュー

> Claude Codeターミナルで /codex:review を実行し、OpenAI CodeXによる標準的なコードレビューを取得する

- 出典: https://x.com/masahirochaen/status/2038790628021346747
- 投稿者: チャエン | デジライズ CEO《重要AIニュースを毎日最速で発信》
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claudeとは異なるモデルのセカンドオピニオンを、ツール切り替えやコンテキスト再入力なしに取得できるため

## いつ使うのか

実装完了後・PR提出前に別モデルの視点でコードを確認したいとき

### 具体的な適用場面

- Claude Codeで実装後、同一セッションを維持したままCodeXに別視点のコードレビューを依頼したいとき
- Claude Codeが解決できなかった問題をCodeXに引き継ぐことで別アプローチの解法を得たいとき
- セキュリティ・バグに対して意図的に批判的な視点（adversarial）でレビューしてリリース前の品質を高めたいとき

## やり方

1. Claude Code CLIを起動し通常通りコーディング作業を行う 2. レビューしたいコードが対象となっている状態で `/codex:review` とターミナルに入力・実行 3. CodeXによるレビュー結果がターミナルに返ってくる

### 入力

- Claude Codeのアクティブセッション
- ChatGPTアカウント（無料プラン可）

### 出力

- OpenAI CodeXによるコードレビュー結果テキスト

## 使うツール・ライブラリ

- Claude Code CLI
- OpenAI CodeX

## コード例

```
/codex:review
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
