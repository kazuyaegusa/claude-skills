# Claude CodeをAPIキーなしで起動する

> Anthropic APIキーを使わず、ローカルまたはサブスクリプション認証でClaude Codeを起動する

- 出典: https://x.com/ubermenscchh/status/2035390128819167502
- 投稿者: Hasan
- カテゴリ: claude-code-workflow

## なぜ使うのか

per-token課金を回避し、レート制限なし・完全ローカルで動作させるため。コードが外部に送出されないのでプライバシーも担保できる

## いつ使うのか

Claude Codeの月額課金以外にAPIトークン費用が発生しているとき、またはコードをAnthropicサーバーに送りたくないとき

### 具体的な適用場面

- APIコストを気にせず大量のコーディングタスクをClaude Codeに任せたい開発者
- コードや機密情報を外部サーバーに送りたくないプライバシー重視の開発環境

## やり方

投稿に添付された画像に具体的手順が記載されていたと推定されるが、本分析では画像を取得できなかったため手順を確認できない。一般的な手法として: (1) Ollamaをインストールしてローカルでモデルを起動 `ollama serve`、(2) `ANTHROPIC_BASE_URL=http://localhost:11434/v1` と `ANTHROPIC_API_KEY=ollama`（ダミー値）を環境変数に設定、(3) `claude` コマンドを起動 — という方法が知られているが、本投稿がこの手法を指しているかは未確認

### 入力

- claude CLI（インストール済み）
- ローカルLLMサーバー（例: Ollama）またはclaude.aiサブスクリプション

### 出力

- APIキー不要・課金ゼロ・ローカル完結で動作するClaude Code環境

## 使うツール・ライブラリ

- claude CLI
- Ollama（ローカルLLM使用時）

## 前提知識

- claude CLIのインストール（npm install -g @anthropic-ai/claude-code）
- ローカルLLMを使う場合はOllamaまたは互換サーバーのセットアップ

## 根拠

> You can now run Claude Code for FREE.

> No API costs. No rate limits. 100% local on your machine.

> Here's how to run Claude Code locally (100% free & fully private):
