# tmux CLIワーカーでCodex/Gemini/Claudeを並列実行

> `omc team N:codex|gemini|claude "タスク"` で tmux pane内に実際のCLIプロセスを起動し、タスク完了後に自動終了させる

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

MCPサーバー経由ではなく実CLIを直接実行することで、各LLMのネイティブ機能（Codexのアーキテクチャ分析、Geminiの100万トークンコンテキスト）をフルに活用でき、かつ不要時はプロセスが自動終了するためリソース効率が高い

## いつ使うのか

Codexにコードレビューさせながら、Geminiに同時にUI設計を依頼したい場合や、Claude単体では対応できない専門領域のタスク

## やり方

1. tmuxセッション内で作業していることを確認
2. `omc team 2:codex "security review"` のように実行
3. oh-my-claudecodeがtmux paneを分割して `codex` CLIプロセスを起動
4. タスク完了後、paneは自動的に閉じる
5. `omc team status <task-id>` で進捗確認、`omc team shutdown <task-id>` で強制終了可能

### 入力

- tmux がインストールされている環境（macOS: brew install tmux / Ubuntu: apt install tmux / Windows: psmux）
- codex / gemini CLIがインストール済み（オプション、該当プロバイダ使用時のみ）
- tmuxセッション内で作業中

### 出力

- tmux pane内で該当CLIプロセスが起動・実行
- タスク完了後に成果物（.omc/artifacts/ask/*.md）
- プロセス終了後paneは自動的に閉じる

## 使うツール・ライブラリ

- tmux
- codex CLI (npm i -g @openai/codex)
- gemini CLI (npm i -g @google/gemini-cli)
- omc team コマンド

## コード例

```
# Codexで2並列セキュリティレビュー
omc team 2:codex "review auth module for security issues"

# Geminiで2並列UI再設計
omc team 2:gemini "redesign UI components for accessibility"

# 状態確認
omc team status auth-review

# 強制終了
omc team shutdown auth-review
```

## 前提知識

- Claude Code CLI インストール済み
- Claude Max/Pro サブスクリプション または Anthropic API キー
- tmux インストール（macOS: brew install tmux / Ubuntu: apt install tmux / Windows: psmux）
- 基本的なコマンドライン操作知識
- YAML/JSON設定ファイルの読み書き
- （オプション）codex CLI / gemini CLI（異種LLM統合を使う場合）

## 根拠

> 「Team runs as a staged pipeline: team-plan → team-prd → team-exec → team-verify → team-fix (loop)」

> 「v4.4.0 removes the Codex/Gemini MCP servers (x, g providers). Use the CLI-first Team runtime (omc team ...) to spawn real tmux worker panes」
