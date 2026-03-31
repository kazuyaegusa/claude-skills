# プラグインで機能を拡張する

> Claude Code公式リポジトリのpluginsディレクトリを参照し、カスタムコマンドやエージェントを追加する

- 出典: https://github.com/anthropics/claude-code
- 投稿者: anthropics
- カテゴリ: claude-code-workflow

## なぜ使うのか

プロジェクト固有のワークフローや頻繁に行うタスクをプラグイン化することで、さらに効率化できる

## いつ使うのか

標準機能では足りない、プロジェクト固有の自動化やワークフローがある場合

## やり方

1. [plugins/README.md](https://github.com/anthropics/claude-code/tree/main/plugins)で利用可能なプラグインを確認
2. プラグインをインストール（READMEの指示に従う）
3. Claude Codeセッション内でプラグイン提供のコマンドを使用

### 入力

- プラグインのソースコードまたはパッケージ
- プラグイン設定ファイル

### 出力

- 追加されたカスタムコマンド・エージェント

## 使うツール・ライブラリ

- Claude Code plugins（公式リポジトリ）

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
