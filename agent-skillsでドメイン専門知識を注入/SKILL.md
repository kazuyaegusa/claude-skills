# Agent Skillsでドメイン専門知識を注入

> Claude Codeに特定分野（DevOps、科学計算、セキュリティ監査等）の専門的な知識と実行能力を付与する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

汎用LLMだけでは不足する専門ドメインの詳細な手順・ベストプラクティス・ツールチェーン知識を補完し、実用的な成果物を生成できるようにするため

## いつ使うのか

汎用的なClaude Codeだけでは専門性が不足する場合（例：CodeQLによる静的解析、学術論文執筆、IaCコード生成）

## やり方

1. リストから目的に合ったスキルリポジトリ（例：Trail of Bits Security Skills、Claude Scientific Skills）を選択
2. `~/.claude/skills/`ディレクトリにスキル定義ファイルをクローン/配置
3. 必要に応じてCLAUDE.mdでスキルの使用方法を指示
4. Claude Code起動時に自動的にスキルがロードされ、関連タスクで利用可能になる

### 入力

- 対象ドメイン（DevOps/科学/セキュリティ等）
- スキルリポジトリのURL

### 出力

- 専門知識を持つClaude Codeインスタンス
- ドメイン固有の成果物（監査レポート、Terraformコード等）

## 使うツール・ライブラリ

- cc-devops-skills
- Trail of Bits Security Skills
- Claude Scientific Skills

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
