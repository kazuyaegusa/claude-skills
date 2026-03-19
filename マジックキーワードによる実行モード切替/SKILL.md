# マジックキーワードによる実行モード切替

> 自然言語プロンプト内に特定キーワード（autopilot, ralph, ulw, ralplan等）を含めることで、異なるオーケストレーション戦略（自律実行、永続モード、最大並列、計画反復等）を自動選択

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

コマンドライン引数やフラグを覚える学習コストをゼロにし、「やりたいこと」を普通に書くだけでツール側が最適な実行モードを推論・選択する。「Don't learn Claude Code. Just use OMC.」の設計哲学

## いつ使うのか

実行戦略を細かく制御したいが、コマンドフラグは覚えたくない場合。シンプルなタスクではキーワードなしの自然言語だけでも動作する

## やり方

1. プロンプトに以下のいずれかを含める:
   - `autopilot:` エンドツーエンド自律実行
   - `ralph:` 永続モード（verify/fixループで完遂保証）
   - `ulw` 最大並列実行（非Team）
   - `ralplan` 反復計画合意形成
   - `/deep-interview` Socratic質問で要件明確化
   - `/ccg` Codex+Gemini→Claude統合
2. OMCがキーワード検出し、対応するスキル・パイプラインを起動
3. Teamモードは明示的に `/team ...` または `omc team ...` 使用（キーワードトリガーなし）

### 入力

- キーワードを含む自然言語プロンプト

### 出力

- キーワードに応じた実行モードの自動選択と実行

## 使うツール・ライブラリ

- OMC

## コード例

```
# 自律実行
autopilot: build a REST API for managing tasks

# 永続モード（必ず完遂）
ralph: refactor auth module

# 最大並列
ulw fix all linting errors

# 要件明確化
/deep-interview "I want to build a task management app"

# Codex+Gemini統合レビュー
/ccg Review this PR — architecture (Codex) and UI (Gemini)
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

> "Magic keywords: autopilot, ralph, ulw, ralplan, /deep-interview, /ccg"
