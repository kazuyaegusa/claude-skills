# tmux CLIワーカーによるマルチAI並列実行

> tmux上で複数のAI CLI（claude/codex/gemini）を独立ペインとしてオンデマンド起動し、同一タスクを並列処理または異なる観点（セキュリティ/UI/実装）で分業させる

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

MCPサーバー経由だとプロセス管理が複雑化・デバッグ困難・リソース常駐するが、tmux CLIなら各AIがネイティブプロセスとして動作し、タスク完了時に自動終了してリソースを解放できる。視認性も向上（ペイン分割で各AI出力を同時表示）

## いつ使うのか

複数AIモデルの視点を並列取得したい場合（Codexでアーキテクチャ分析 + Geminiで大規模コンテキスト処理など）、またはCodex/Gemini CLIを使う必要があるタスク（OMCのClaude統合だけでは不足する場合）

## やり方

1. tmuxセッション内で `omc team N:provider "task"` を実行（例: `omc team 2:codex "security review"`）
2. OMCがN個のtmuxペインを自動生成し、各ペインで指定providerのCLI（codex/gemini/claude）を起動
3. タスク文字列を各CLIに渡して並列実行
4. `omc team status <task-id>` でリアルタイム進捗確認
5. 完了後 `omc team shutdown <task-id>` で全ペイン終了（または自動終了）
6. 結果は `.omc/artifacts/ask/` にMarkdownで保存

### 入力

- アクティブなtmuxセッション
- codex/gemini CLIのインストール（該当プロバイダー使用時）
- タスク記述文字列
- ワーカー数とプロバイダー指定（例: 2:codex）

### 出力

- 各AIの実行結果Markdown（.omc/artifacts/ask/以下）
- tmuxペインでのリアルタイム出力
- タスクステータス情報

## 使うツール・ライブラリ

- tmux
- omc CLI（oh-my-claude-sisyphus npm package）
- codex CLI（オプション）
- gemini CLI（オプション）

## コード例

```
# 2つのCodexワーカーでセキュリティレビュー
omc team 2:codex "review auth module for security issues"

# Geminiワーカーでアクセシビリティ確認
omc team 2:gemini "redesign UI components for accessibility"

# ステータス確認
omc team status auth-review

# 終了
omc team shutdown auth-review
```

## 前提知識

- Claude Code CLIの基本操作（インストール・認証済み）
- tmuxの基礎知識（ペイン・セッション概念）
- Claude Max/Proサブスクリプション または Anthropic APIキー
- （オプション）Codex CLI・Gemini CLIのインストール（マルチAI機能使用時）
- （オプション）OpenClawゲートウェイ構築知識（外部連携時）
- Node.js/npm環境（OMC npmパッケージインストール用）

## 根拠

> "Team runs as a staged pipeline: team-plan → team-prd → team-exec → team-verify → team-fix (loop)"

> "v4.4.0 removes the Codex/Gemini MCP servers (x, g providers). Use the CLI-first Team runtime (omc team ...) to spawn real tmux worker panes"

> "Enable Claude Code native teams in ~/.claude/settings.json: {\"env\": {\"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS\": \"1\"}}"

> "omc wait --start → Enable auto-resume daemon (requires tmux for session detection)"
