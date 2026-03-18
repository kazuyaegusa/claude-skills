# Claude Codeの公式推奨インストール

> npmではなく公式インストールスクリプトまたはパッケージマネージャーを使ってClaude Codeをインストールする

- 出典: https://github.com/anthropics/claude-code
- 投稿者: anthropics
- カテゴリ: claude-code-workflow

## なぜ使うのか

npm経由のインストールは非推奨（deprecated）となっており、公式スクリプトやHomebrew/WinGetを使うことで最新の推奨構成でインストールできる

## いつ使うのか

Claude Codeを新規導入する時、または古いnpmバージョンから移行する時

## やり方

1. MacOS/Linuxの場合: `curl -fsSL https://claude.ai/install.sh | bash` を実行
2. Homebrewの場合: `brew install --cask claude-code` を実行
3. Windowsの場合: `irm https://claude.ai/install.ps1 | iex` を実行（PowerShell）
4. WinGetの場合: `winget install Anthropic.ClaudeCode` を実行
5. インストール後、プロジェクトディレクトリで `claude` コマンドを実行して起動

### 入力

- インターネット接続
- MacOS/Linux/Windowsの実行環境
- （Homebrew/WinGetを使う場合）該当パッケージマネージャーのインストール

### 出力

- システムにインストールされたClaude Code CLI
- `claude` コマンドがターミナルで利用可能になる

## 使うツール・ライブラリ

- curl (MacOS/Linux)
- bash (MacOS/Linux)
- PowerShell (Windows)
- Homebrew (オプション)
- WinGet (オプション)

## コード例

```
# MacOS/Linux推奨
curl -fsSL https://claude.ai/install.sh | bash

# Homebrew
brew install --cask claude-code

# Windows推奨
irm https://claude.ai/install.ps1 | iex

# WinGet
winget install Anthropic.ClaudeCode
```

## 前提知識

- Node.js 18以上（実行環境として必要）
- ターミナル操作の基本知識
- Git の基本概念（Git操作機能を使う場合）
- 自然言語でタスクを指示する際の明確な表現力

## 根拠

> 「Installation via npm is deprecated. Use one of the recommended methods below.」

> 「Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows -- all through natural language commands.」

> 「Use the `/bug` command to report issues directly within Claude Code, or file a GitHub issue」

> 「This repository includes several Claude Code plugins that extend functionality with custom commands and agents. See the plugins directory for detailed documentation on available plugins.」

> MacOS/Linux推奨: `curl -fsSL https://claude.ai/install.sh | bash`
