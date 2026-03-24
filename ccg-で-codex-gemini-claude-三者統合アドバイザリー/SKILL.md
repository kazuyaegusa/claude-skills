# /ccg で Codex + Gemini + Claude 三者統合アドバイザリー

> 1つのタスクに対し、`/ask codex` と `/ask gemini` を並列実行し、両者の回答をClaudeが統合して最終レコメンデーションを返す

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

Codexはアーキテクチャ・セキュリティ分析に強く、Geminiは大規模コンテキストとUI設計に強い。両方の視点を取り入れることで、バックエンド・フロントエンド双方に配慮した設計判断ができる

## いつ使うのか

PR全体レビュー（アーキテクチャ + UI両面）、フルスタック機能設計、技術選定で複数LLMの意見を聞きたい場合

## やり方

1. `/ccg <タスク内容>` を実行
2. oh-my-claudecodeが内部で `/ask codex "<タスク>"` と `/ask gemini "<タスク>"` を並列起動
3. 各CLIが `.omc/artifacts/ask/*.md` に成果物を出力
4. Claudeが両者の回答を読み込み、矛盾点・補完点を分析
5. 統合された最終レコメンデーションを返す

### 入力

- codex CLI インストール済み
- gemini CLI インストール済み
- レビュー対象のコード・設計ドキュメント

### 出力

- .omc/artifacts/ask/codex-*.md（Codex回答）
- .omc/artifacts/ask/gemini-*.md（Gemini回答）
- Claudeによる統合レコメンデーション

## 使うツール・ライブラリ

- codex CLI
- gemini CLI
- oh-my-claudecode /ccg skill

## コード例

```
/ccg Review this PR — architecture (Codex) and UI components (Gemini)

# 内部で以下が並列実行:
# /ask codex "Review this PR — architecture"
# /ask gemini "Review this PR — UI components"
# Claude: 両者の回答を統合して返答
```

## 前提知識

- Claude Code CLI インストール済み
- Claude Max/Pro サブスクリプション または Anthropic API キー
- tmux インストール（macOS: brew install tmux / Ubuntu: apt install tmux / Windows: psmux）
- 基本的なコマンドライン操作知識
- YAML/JSON設定ファイルの読み書き
- （オプション）codex CLI / gemini CLI（異種LLM統合を使う場合）

## 根拠

> 「Multi-agent orchestration for Claude Code. Zero learning curve.」

> 「v4.4.0 removes the Codex/Gemini MCP servers (x, g providers). Use the CLI-first Team runtime (omc team ...) to spawn real tmux worker panes」

> 「OpenClaw integration: Forward Claude Code session events to an OpenClaw gateway to enable automated responses and workflows」

> 「/ccg Review this PR — architecture (Codex) and UI components (Gemini)」
