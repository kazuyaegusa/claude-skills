# AI-nativeなセットアップ・デバッグ

> インストールウィザードやダッシュボードの代わりに、Claude Code CLIがセットアップ・監視・デバッグを対話的に実行する

- 出典: https://github.com/qwibitai/nanoclaw
- 投稿者: qwibitai
- カテゴリ: claude-code-workflow

## なぜ使うのか

従来のGUIやCLIウィザードは全ケースを事前実装する必要があるが、AIなら環境固有の問題に動的に対応できる。ユーザーは自然言語で質問し、AIがログ確認・修正を行う

## いつ使うのか

セットアップスクリプトのメンテナンスコストを削減したい時。ユーザー環境が多様でエッジケースが多い時

## やり方

1. `claude`コマンドでClaude Code CLIを起動
2. `/setup`スキルを実行してセットアップ開始
3. Claude Codeが依存関係・認証・コンテナを自動設定
4. 問題発生時は`/debug`を実行してClaude Codeが調査
5. 'なぜスケジューラが動かない？'等の自然言語質問でデバッグ
6. Claude Codeがログ確認・コード修正を提案

### 入力

- Claude Code CLI
- スキル定義（/setup, /debug等）

### 出力

- 環境に応じた動的セットアップ
- 自然言語でのデバッグ支援

## 使うツール・ライブラリ

- Claude Code CLI
- Claude Code Skills

## コード例

```
// ユーザーは以下を実行するだけ
// $ claude
// > /setup
// Claude Codeが依存関係インストール・認証・コンテナセットアップを自動実行
```

## 前提知識

- Claude Codeの基本的な使い方（スキル実行、自然言語でのコード変更依頼）
- Dockerまたはコンテナ技術の基礎知識（なぜファイルシステム分離がセキュリティに有効か）
- Node.js基礎（このプロジェクトはNode.js 20+で実装）
- Claude Agent SDKの概要（Anthropic公式のAgent実行ハーネス）
- フォーク＆ブランチベースのGitワークフロー

## 根拠

> OpenClaw has nearly half a million lines of code, 53 config files, and 70+ dependencies. Its security is at the application level (allowlists, pairing codes) rather than true OS-level isolation.

> NanoClaw provides that same core functionality, but in a codebase small enough to understand: one process and a handful of files. Claude agents run in their own Linux containers with filesystem isolation, not merely behind permission checks.

> Skills over features. Instead of adding features (e.g. support for Telegram) to the codebase, contributors submit claude code skills like /add-telegram that transform your fork.

> No configuration sprawl. Want different behavior? Modify the code. The codebase is small enough that it's safe to make changes.

> AI-native: No installation wizard; Claude Code guides setup. No monitoring dashboard; ask Claude what's happening. No debugging tools; describe the problem and Claude fixes it.
