# oh-my-claudecodeプラグインインストールでTeam機能有効化

> Claude Codeに/plugin marketplace経由でoh-my-claudecodeをインストールし、Team・Autopilot・スキル学習などの拡張機能を利用可能にする

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Code標準では単一エージェント実行のみ。oh-my-claudecodeを入れることで、Team（複数Claude協調）・tmuxワーカー（Codex/Gemini並列起動）・自動スキル抽出が使えるようになり、複雑タスクを分割・並列・再利用できる

## いつ使うのか

Claude Codeを初めて使う時、または既存環境にマルチエージェント機能を追加したい時

## やり方

1. `/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode` で marketplace登録
2. `/plugin install oh-my-claudecode` でインストール
3. `/setup` → `/omc-setup` でセットアップ
4. `~/.claude/settings.json` に `"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"` を追加してTeam機能を有効化

### 入力

- Claude Code CLI インストール済み環境
- Claude Max/Pro サブスクリプション または Anthropic APIキー

### 出力

- oh-my-claudecode プラグインが利用可能になり `/team`, `/omc-setup` などのコマンドが使える状態
- ~/.claude/settings.json に Team機能の環境変数が設定される

## 使うツール・ライブラリ

- Claude Code CLI
- oh-my-claudecode plugin

## コード例

```
# インストール
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
/plugin install oh-my-claudecode

# セットアップ
/setup
/omc-setup

# settings.jsonに追加
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
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

> 「OpenClaw integration: Forward Claude Code session events to an OpenClaw gateway to enable automated responses and workflows」
