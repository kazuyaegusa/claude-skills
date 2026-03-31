# Claude Codeをインストールして起動する

> ターミナルからClaude Codeをインストールし、プロジェクトディレクトリで起動する

- 出典: https://github.com/anthropics/claude-code
- 投稿者: anthropics
- カテゴリ: claude-code-workflow

## なぜ使うのか

インストール方法が複数あり、npm経由は非推奨となっているため、公式推奨の方法を使うことで最新・安定版を導入できる

## いつ使うのか

Claude Codeを初めて導入する時、または新しいマシンで環境構築する時

## やり方

1. OSに応じたインストールコマンドを実行する（MacOS/Linuxは `curl -fsSL https://claude.ai/install.sh | bash`、Windowsは `irm https://claude.ai/install.ps1 | iex`、またはHomebrew/WinGetを使用）
2. プロジェクトのルートディレクトリに移動
3. ターミナルで `claude` コマンドを実行

### 入力

- インターネット接続
- Node.js 18以上（npm経由の場合）
- Anthropic APIキーまたはClaude Codeサブスクリプション

### 出力

- ターミナルで動作するClaude Codeセッション
- 自然言語でのコードベース操作環境

## 使うツール・ライブラリ

- curl/irm（インストールスクリプト実行）
- Homebrew（MacOS/Linux）
- WinGet（Windows）
- npm（非推奨だが利用可能）

## コード例

```
# MacOS/Linux推奨インストール
curl -fsSL https://claude.ai/install.sh | bash

# Windows推奨インストール
irm https://claude.ai/install.ps1 | iex

# Homebrew経由（MacOS/Linux）
brew install --cask claude-code

# WinGet経由（Windows）
winget install Anthropic.ClaudeCode

# プロジェクトで起動
cd /path/to/your/project
claude
```

## 前提知識

- ターミナル操作の基本知識
- Gitの基本的な概念（コミット、PR）
- Node.js環境（npm経由インストール時）
- Anthropic APIキーまたはClaude Codeサブスクリプション
- コーディング経験（対象コードベースの言語に対する基本理解）

## 根拠

> "Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows -- all through natural language commands."

> "curl -fsSL https://claude.ai/install.sh | bash"

> "This repository includes several Claude Code plugins that extend functionality with custom commands and agents."

> "Use the `/bug` command to report issues directly within Claude Code"

> "Learn more in the [official documentation](https://code.claude.com/docs/en/overview)."
