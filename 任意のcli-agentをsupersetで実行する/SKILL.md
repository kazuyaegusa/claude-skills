# 任意のCLI agentをSupersetで実行する

> Claude Code, Codex, Cursor Agent, Gemini CLI, Copilotなど、ターミナルで動くagentなら全てSuperset上で実行できる

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: claude-code-workflow

## なぜ使うのか

agentごとに専用ツールを使うのではなく、統一UIで管理したい。Supersetはagent非依存のターミナルラッパーなので互換性が広い

## いつ使うのか

複数のagentプロバイダを併用したい、または既存のagent CLIをそのまま使いたい時

## やり方

1. Supersetでworkspaceを作成
2. ターミナルで通常通り `claude -p`, `codex`, `cursor-agent` などを実行
3. ⌘T で新しいタブを開き、別のagentを同じworkspaceで走らせることも可能
4. 全てのagent出力はSupersetのターミナルに表示され、履歴も残る

### 入力

- 任意のagent CLI（claude, codex, gemini-cli等）
- 各agentの認証設定

### 出力

- Superset内でのagent実行ログ
- git diffによる変更差分
- 各agentが生成したコード

## 使うツール・ライブラリ

- Superset
- 各種CLI agent（Claude Code, Codex, Cursor Agent等）

## 前提知識

- git 2.20+の基本操作知識
- git worktreeの概念
- ターミナルでのagent CLI実行経験
- macOS環境（Windows/Linux未検証）
- Bun, gh, Caddyのインストール方法

## 根拠

> Supported agents: Claude Code, OpenAI Codex CLI, Cursor Agent, Gemini CLI, GitHub Copilot, OpenCode, Pi
