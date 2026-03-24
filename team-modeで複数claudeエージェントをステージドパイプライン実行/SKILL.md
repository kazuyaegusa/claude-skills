# Team Modeで複数Claudeエージェントをステージドパイプライン実行

> 1つのタスクを plan → prd → exec → verify → fix の5段階に分割し、各段階で専門化されたClaudeエージェントを並列または順次実行させる

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

大規模タスクを単一エージェントで実行すると途中で諦める・部分的にしか完了しない問題が起きる。Teamモードは各段階で成果物を検証し、失敗時は自動でfixループに入るため、確実に完了まで到達できる

## いつ使うのか

TypeScript全エラー修正・大規模リファクタリング・複数ファイルにまたがる機能追加など、単一エージェントでは途中で止まるタスク

## やり方

1. `/team N:executor "タスク内容"` の形式でコマンド実行（Nはエージェント数）
2. team-plan: タスクを分解して計画立案
3. team-prd: 要件定義書作成
4. team-exec: 実装実行
5. team-verify: 結果検証
6. team-fix: エラー修正（ループ）
7. 各段階の成果物は `.omc/sessions/*.json` に記録される

### 入力

- Team機能が有効化された Claude Code 環境
- 実行したいタスクの自然言語記述

### 出力

- タスクが完全に完了するまでverify→fixループが継続
- .omc/sessions/*.json にセッション記録
- .omc/state/agent-replay-*.jsonl にリプレイログ

## 使うツール・ライブラリ

- oh-my-claudecode Team Mode
- Claude Code Teams API

## コード例

```
# 3つのexecutorエージェントでTypeScriptエラー全修正
/team 3:executor "fix all TypeScript errors"

# 内部で以下の流れが自動実行される:
# team-plan → team-prd → team-exec → team-verify → team-fix (loop)
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
