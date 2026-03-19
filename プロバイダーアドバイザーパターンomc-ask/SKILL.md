# プロバイダーアドバイザーパターン（omc ask）

> 単一タスクを複数AIプロバイダー（claude/codex/gemini）に同時問い合わせし、各回答をMarkdownアーティファクトとして保存、後で比較・統合する

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

各AIモデルには得意分野がある（Codex=コードレビュー・セキュリティ、Gemini=大規模コンテキスト・UI、Claude=汎用推論）。単一モデルだけだと見落としや偏りが生じるため、クロスバリデーションで品質向上

## いつ使うのか

アーキテクチャ決定やPRレビューなど、複数視点での検証が重要な意思決定時。単純な情報取得には過剰

## やり方

1. `omc ask <provider> --prompt "question"` を実行（provider: claude, codex, gemini）
2. 指定providerのCLIが起動され、promptが渡される
3. 回答は `.omc/artifacts/ask/<provider>-<timestamp>.md` に自動保存
4. 複数providerに同じ質問をしたい場合、順次実行またはシェルスクリプトでループ
5. （オプション）`/ccg` スキルで「codex + gemini → Claude統合」を自動化

### 入力

- 質問・タスク記述
- 使用したいprovider名（claude/codex/gemini）
- （オプション）--agent-prompt で特定エージェント役割指定

### 出力

- 各providerの回答Markdown（.omc/artifacts/ask/）
- 環境変数 OMC_ASK_ADVISOR_SCRIPT, OMC_ASK_ORIGINAL_TASK

## 使うツール・ライブラリ

- omc CLI
- 対応するprovider CLI（codex/gemini）

## コード例

```
# Claudeにマイグレーション計画レビュー依頼
omc ask claude "review this migration plan"

# Codexにアーキテクチャリスク分析依頼
omc ask codex --prompt "identify architecture risks"

# Geminiに UI改善提案依頼
omc ask gemini --prompt "propose UI polish ideas"

# 特定エージェントロール指定
omc ask claude --agent-prompt executor --prompt "draft implementation steps"
```

## 前提知識

- Claude Code CLIの基本操作（インストール・認証済み）
- tmuxの基礎知識（ペイン・セッション概念）
- Claude Max/Proサブスクリプション または Anthropic APIキー
- （オプション）Codex CLI・Gemini CLIのインストール（マルチAI機能使用時）
- （オプション）OpenClawゲートウェイ構築知識（外部連携時）
- Node.js/npm環境（OMC npmパッケージインストール用）

## 根拠

> "v4.4.0 removes the Codex/Gemini MCP servers (x, g providers). Use the CLI-first Team runtime (omc team ...) to spawn real tmux worker panes"

> "Workers spawn on-demand and die when their task completes — no idle resource usage"

> "omc ask claude \"review this migration plan\" → saves markdown artifact under .omc/artifacts/ask/"

> "hooks: session-start, stop, keyword-detector, ask-user-question, pre-tool-use, post-tool-use (6 active in bridge.ts)"
