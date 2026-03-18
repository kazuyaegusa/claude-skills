# プラグインでClaude Codeを拡張する

> 公式リポジトリのpluginsディレクトリにあるプラグインを導入し、カスタムコマンドやエージェント機能を追加する

- 出典: https://github.com/anthropics/claude-code
- 投稿者: anthropics
- カテゴリ: claude-code-workflow

## なぜ使うのか

標準機能に加えて、プロジェクト固有のワークフローや特殊なタスクに対応するカスタム機能を追加できる

## いつ使うのか

標準機能では対応できない専門的なワークフローや繰り返しタスクを自動化したい時

## やり方

1. https://github.com/anthropics/claude-code/tree/main/plugins にアクセス
2. 必要なプラグインのドキュメントを確認
3. プラグインのインストール手順に従って導入
4. Claude Codeセッション内で拡張コマンド・エージェントを利用

### 入力

- プラグインのドキュメント
- （プラグインによる）設定ファイル・環境変数

### 出力

- 拡張されたClaude Codeコマンド
- カスタムエージェント機能

## 使うツール・ライブラリ

- claude-code plugins
- GitHub リポジトリ

## コード例

```
# 例: pluginsディレクトリを参照
# https://github.com/anthropics/claude-code/tree/main/plugins
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
