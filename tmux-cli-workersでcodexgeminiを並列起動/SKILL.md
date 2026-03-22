# tmux CLI workersでCodex/Geminiを並列起動

> tmuxペイン内に実際のcodex/gemini CLIプロセスをオンデマンド起動し、タスク完了時に自動終了させる

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude単体では視野が限定されるが、Codexでアーキテクチャ検証・Geminiで大規模コンテキスト処理を並列実行すればクロスチェックできる。リソースもタスク時のみ消費

## いつ使うのか

セキュリティレビュー（Codex得意）とUI改善（Gemini得意）を同時進行させたい、または大規模コンテキスト（1M token）が必要な時

## やり方

1. tmux, codex CLI, gemini CLI をインストール
2. `omc team 2:codex "review auth module for security issues"` で2つのCodexワーカーを起動
3. `omc team 2:gemini "redesign UI components"` でGeminiワーカーを別途起動
4. `omc team status auth-review` でステータス確認
5. タスク完了時に自動的にワーカープロセス終了
6. `omc team shutdown auth-review` で手動停止も可能

### 入力

- tmux がインストール済み
- codex CLI / gemini CLI がインストール済み
- アクティブなtmuxセッション

### 出力

- 各ワーカーの実行結果がtmuxペインに表示
- タスク完了後、プロセス自動終了でリソース解放

## 使うツール・ライブラリ

- tmux
- @openai/codex CLI
- @google/gemini-cli
- oh-my-claudecode

## コード例

```
omc team 2:codex "review auth module for security issues"
omc team 2:gemini "redesign UI components for accessibility"
omc team status auth-review
omc team shutdown auth-review
```

## 前提知識

- Claude Code CLIの基本操作（インストール・起動）
- Claude Max/ProサブスクリプションまたはAnthropic APIキー
- tmux（CLI workers使用時）
- Node.js/npm（プラグインインストール時）
- Git（スキルのバージョン管理時）

## 根拠

> 「Multi-agent orchestration for Claude Code. Zero learning curve.」

> 「Team runs as a staged pipeline: team-plan → team-prd → team-exec → team-verify → team-fix (loop)」

> 「v4.4.0 removes the Codex/Gemini MCP servers (x, g providers). Use the CLI-first Team runtime (omc team ...) to spawn real tmux worker panes」

> 「32 specialized agents for architecture, research, design, testing, data science」

> 「autopilot: build a REST API for managing tasks - That's it. Everything else is automatic.」
