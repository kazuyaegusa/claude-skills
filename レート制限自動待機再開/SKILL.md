# レート制限自動待機・再開

> Claude Code APIのレート制限到達時、tmuxセッション検出でリセット時刻まで自動待機し、制限解除後にセッション再開する

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

長時間タスクで手動リトライすると待機時間の計算ミス・タイミング管理の負担が大きい。自動化で無人実行可能にし、深夜バッチ処理などでも中断なく完遂

## いつ使うのか

大量のファイル処理や長時間リファクタリングなど、レート制限に確実に遭遇する作業。短時間タスクでは不要

## やり方

1. `omc wait --start` でデーモン有効化
2. Claude Codeセッションがレート制限に遭遇すると、OMCが検知
3. tmuxセッション情報からリセット時刻を計算
4. スリープ後、自動的に `claude -p --resume` 相当を実行してセッション再開
5. `omc wait --stop` で無効化、`omc wait` でステータス確認

### 入力

- アクティブなtmuxセッション（セッション検出のため）
- Claude Code CLI認証済み環境

### 出力

- レート制限解除後の自動セッション再開
- 待機ステータス情報

## 使うツール・ライブラリ

- tmux
- omc CLI

## コード例

```
# デーモン開始
omc wait --start

# ステータス確認
omc wait

# 停止
omc wait --stop
```

## 前提知識

- Claude Code CLIの基本操作（インストール・認証済み）
- tmuxの基礎知識（ペイン・セッション概念）
- Claude Max/Proサブスクリプション または Anthropic APIキー
- （オプション）Codex CLI・Gemini CLIのインストール（マルチAI機能使用時）
- （オプション）OpenClawゲートウェイ構築知識（外部連携時）
- Node.js/npm環境（OMC npmパッケージインストール用）

## 根拠

> "Multi-agent orchestration for Claude Code. Zero learning curve."

> "v4.4.0 removes the Codex/Gemini MCP servers (x, g providers). Use the CLI-first Team runtime (omc team ...) to spawn real tmux worker panes"

> "Enable Claude Code native teams in ~/.claude/settings.json: {\"env\": {\"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS\": \"1\"}}"

> "omc ask claude \"review this migration plan\" → saves markdown artifact under .omc/artifacts/ask/"

> "omc wait --start → Enable auto-resume daemon (requires tmux for session detection)"
