# /codex:rescueでタスクをCodexに丸ごと委任する

> 進行中のタスクをまるごとOpenAI Codexに渡し、解決を委任する

- 出典: https://x.com/masahirochaen/status/2038790628021346747
- 投稿者: チャエン | デジライズ CEO《重要AIニュースを毎日最速で発信》
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claudeがタスクでスタックしたときやループに入ったとき、コンテキストを失わずに別AIへ引き継げる。AI間の協調でタスク完了率を上げる逃げ道になる。

## いつ使うのか

Claudeが同じアプローチを繰り返して解決できない状態が続いたとき、またはCodexのアプローチを別途試したいとき

### 具体的な適用場面

- PRマージ前にClaudeレビューに加え別AIの視点を追加してレビュー網羅性を高めたいとき
- Claudeがタスクでループ・停止した際に別AIへコンテキストごと引き継いで解決を試みるとき
- セキュリティ重要コード（認証・API設計）に対して敵対的視点での問題洗い出しが必要なとき

## やり方

1. Claude Codeセッションでタスクが行き詰まる
2. `/codex:rescue` と入力してEnter
3. 現在のタスクコンテキストがCodexに渡される
4. Codexがそのタスクの解決を試みる

### 入力

- 稼働中のClaude Codeセッション
- 解決できていないタスクのコンテキスト全体

### 出力

- Codexによるタスク解決の試み・実装コードまたは解決策の提示

## 使うツール・ライブラリ

- Claude Code CLI
- OpenAI Codex

## コード例

```
/codex:rescue
```

## 前提知識

- Claude Code CLIのインストールと起動（`claude` コマンドが使える状態）
- ChatGPTアカウント（無料プランでも可）
- Codex連携の有効化（具体的な設定・認証手順は投稿に記載なし）

## 根拠

> /codex:review：標準コードレビュー

> /codex:adversarial ：厳格な敵対的レビュー

> /codex:rescue：タスクをCodexへ丸ごと委任

> ChatGPT無料プラン含む全ユーザー対象

> ClaudeとCodeXが同じターミナルで使えるだと…
