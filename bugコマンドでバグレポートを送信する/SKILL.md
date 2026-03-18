# /bugコマンドでバグレポートを送信する

> Claude Codeセッション内で `/bug` コマンドを実行し、問題を直接AnthropicのGitHub Issuesに報告する

- 出典: https://github.com/anthropics/claude-code
- 投稿者: anthropics
- カテゴリ: claude-code-workflow

## なぜ使うのか

ターミナルを離れずにフィードバックを送信でき、セッションコンテキストを含めた詳細なバグレポートを作成できる

## いつ使うのか

Claude Code使用中にバグや予期しない動作に遭遇した時

## やり方

1. Claude Codeセッション中に `/bug` と入力
2. プロンプトに従ってバグの詳細を記述
3. 送信後、GitHub Issueとして記録される

### 入力

- バグの詳細説明
- （自動収集）セッションコンテキスト・使用データ

### 出力

- GitHub Issue登録
- Anthropicチームへのフィードバック送信

## 使うツール・ライブラリ

- claude CLI
- /bug コマンド

## コード例

```
# Claude Codeセッション内で
/bug
```

## 前提知識

- Node.js 18以上（実行環境として必要）
- ターミナル操作の基本知識
- Git の基本概念（Git操作機能を使う場合）
- 自然言語でタスクを指示する際の明確な表現力

## 根拠

> 「Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows -- all through natural language commands.」

> 「Use the `/bug` command to report issues directly within Claude Code, or file a GitHub issue」

> 「This repository includes several Claude Code plugins that extend functionality with custom commands and agents. See the plugins directory for detailed documentation on available plugins.」

> MacOS/Linux推奨: `curl -fsSL https://claude.ai/install.sh | bash`

> Windows推奨: `irm https://claude.ai/install.ps1 | iex`
