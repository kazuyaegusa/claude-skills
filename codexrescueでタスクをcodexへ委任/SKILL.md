# /codex:rescueでタスクをCodeXへ委任

> Claude Codeターミナルで /codex:rescue を実行し、現在処理中のタスクをそのままOpenAI CodeXに引き継いで処理させる

- 出典: https://x.com/masahirochaen/status/2038790628021346747
- 投稿者: チャエン | デジライズ CEO《重要AIニュースを毎日最速で発信》
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claudeが解決できなかった問題に対し、コンテキストを再入力せずに別モデルの問題解決アプローチを試せるため

## いつ使うのか

Claudeが同じアプローチを繰り返して進まないとき、または特定の問題でCodeXの得意分野を活かしたいとき

### 具体的な適用場面

- Claude Codeで実装後、同一セッションを維持したままCodeXに別視点のコードレビューを依頼したいとき
- Claude Codeが解決できなかった問題をCodeXに引き継ぐことで別アプローチの解法を得たいとき
- セキュリティ・バグに対して意図的に批判的な視点（adversarial）でレビューしてリリース前の品質を高めたいとき

## やり方

1. Claude Codeがタスクに詰まった、または別モデルを試したい状態で `/codex:rescue` を入力・実行 2. 現在のタスクコンテキストがCodeXに渡され、CodeXが続きを処理する 3. 結果がターミナルに返ってくる

### 入力

- Claude Codeのアクティブセッション（タスクコンテキスト付き）
- ChatGPTアカウント（無料プラン可）

### 出力

- CodeXによるタスク処理結果

## 使うツール・ライブラリ

- Claude Code CLI
- OpenAI CodeX

## コード例

```
/codex:rescue
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
