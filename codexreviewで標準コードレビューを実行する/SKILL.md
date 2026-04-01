# /codex:reviewで標準コードレビューを実行する

> Claude Codeのターミナル内でOpenAI Codexによる標準的なコードレビューを実行する

- 出典: https://x.com/masahirochaen/status/2038790628021346747
- 投稿者: チャエン | デジライズ CEO《重要AIニュースを毎日最速で発信》
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claudeセッションを中断せずに別AIの視点でレビューを取得できる。ツール切り替えコストなしに複数AIの判断を組み合わせてレビュー品質を上げられる。

## いつ使うのか

Claudeのレビューに加えて別AIの視点を追加したいとき、またはCodexのレビュースタイルを試したいとき

### 具体的な適用場面

- PRマージ前にClaudeレビューに加え別AIの視点を追加してレビュー網羅性を高めたいとき
- Claudeがタスクでループ・停止した際に別AIへコンテキストごと引き継いで解決を試みるとき
- セキュリティ重要コード（認証・API設計）に対して敵対的視点での問題洗い出しが必要なとき

## やり方

1. Claude Codeを起動する (`claude`)
2. レビューしたいコードをコンテキストに含める（ファイルを開く等）
3. チャット入力欄に `/codex:review` と入力してEnter
4. Codexがそのコンテキストをもとにコードレビューコメントを返す

### 入力

- 稼働中のClaude Codeセッション
- レビュー対象コードのコンテキスト

### 出力

- Codexによる標準コードレビューコメント（バグ・改善点の指摘）

## 使うツール・ライブラリ

- Claude Code CLI
- OpenAI Codex

## コード例

```
/codex:review
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
