# Slash Commandsでタスク固有プロンプトをテンプレート化

> 頻繁に使う複雑なプロンプト（PR作成、GitHub Issue修正、TDD実装等）を再利用可能なコマンドとして定義

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

毎回同じ指示を書く手間を削減し、プロンプト品質を標準化してClaude Codeの出力品質を安定させるため

## いつ使うのか

PR作成、Issue修正、コミットメッセージ生成、ドキュメント更新など定型的だが複雑な指示を繰り返す場合

## やり方

1. `.claude/commands/`ディレクトリに`<コマンド名>.md`ファイルを作成
2. Markdownでプロンプトテンプレートを記述（引数プレースホルダー含む）
3. Claude Code内で`/<コマンド名>`として呼び出し
4. 必要に応じて引数を渡してテンプレート展開

### 入力

- コマンド名
- プロンプトテンプレート（Markdown）
- （オプション）パラメータ

### 出力

- 再利用可能なSlash Command
- 標準化された成果物（PR、コミット、ドキュメント等）

## 使うツール・ライブラリ

- /create-pr
- /fix-github-issue
- /tdd-implement
- /commit

## 前提知識

- Claude Codeの基本的な使い方（CLIでの起動、プロンプト入力、ファイル操作）
- Git、GitHub、PR、Issueなどの基本概念
- JSONファイルの編集（hooks.json等の設定）
- ターミナル操作、シェルスクリプトの基礎
- （リソースによって）Docker、Node.js、Python、Rust等の環境構築知識

## 根拠

> > A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow.

> Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

> Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.

> Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task

> CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards
