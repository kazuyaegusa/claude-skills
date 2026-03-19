# ステージドパイプラインによる協調実行

> Team mode実行時、team-plan（計画）→ team-prd（要件定義）→ team-exec（実装）→ team-verify（検証）→ team-fix（修正ループ）の5段階を自動実行し、各段階で専門エージェントが介入

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

一気通貫実行だと中間成果物の品質が担保されず、後工程で手戻りが発生する。ステージングすることで各段階でverify/fixループを回し、「部分的成功」を許さず完全完遂を保証

## いつ使うのか

複雑な機能追加やリファクタリングで、計画→実装→検証の段階的進行が必要な場合。単純なバグ修正やクイックフィックスには過剰

## やり方

1. `~/.claude/settings.json` で `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` を設定
2. `/team N:executor "task"` または自然言語に `team` キーワードを含めて実行
3. OMCが自動的に以下を順次実行:
   - team-plan: タスク分解、依存関係整理
   - team-prd: 要件定義ドキュメント生成
   - team-exec: 実装（N個のexecutorエージェントが並列）
   - team-verify: テスト・Lint・型チェック
   - team-fix: エラーがあればループ（verify → fix → verify...）
4. 各段階の成果物は `.omc/sessions/*.json` に記録

### 入力

- CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 の環境変数設定
- タスク記述
- 実行エージェント数（例: 3:executor）

### 出力

- 各ステージの成果物（plan文書、PRD、実装コード、テスト結果）
- セッションログ（.omc/sessions/）
- 最終的に全verifyパスしたコード

## 使うツール・ライブラリ

- Claude Code CLI（Team機能有効化）
- OMC plugin

## コード例

```
# settings.json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}

# 実行例
/team 3:executor "fix all TypeScript errors"

# または自然言語
"team: implement user authentication with JWT"
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
