# Agent SkillsでClaude Codeに専門知識を付与する

> Agent Skillsカテゴリのリソース（例: Claude Scientific Skills、Trail of Bits Security Skills、claude-code-hooks-sdk）をインストールし、Claude Codeに科学研究、セキュリティ監査、DevOps等の専門タスクを実行させる

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeは汎用的だが、ドメイン固有の知識（例: CodeQLによる静的解析、Kubernetes設定生成、学術論文執筆）を持たない。Agent Skillsは、専門家が作成したプロンプト・スクリプト・設定ファイルをパッケージ化し、Claude Codeに専門能力を追加する

## いつ使うのか

Claude Codeで専門的なタスク（セキュリティ監査、科学データ解析、IaCコード生成）を繰り返し実行する必要がある時

## やり方

1. awesome-claude-codeの「Agent Skills 🤖」セクションから目的に合うスキルを選択（例: Trail of Bits Security Skills）
2. スキルのGitHubリポジトリをクローン: `git clone https://github.com/trailofbits/skills`
3. スキルのREADMEに従いインストール（多くは `~/.claude/skills/` 等にコピー）
4. Claude Codeを起動し、スキルが有効化されていることを確認
5. スキルが提供するコマンド（例: `/security-audit`）を実行

### 入力

- 対象ドメイン（セキュリティ、DevOps、科学研究等）
- Claude Code環境（`~/.claude/` ディレクトリへのアクセス）

### 出力

- Claude Codeで利用可能な専門スキル
- スキル固有のスラッシュコマンド or サブエージェント

## 使うツール・ライブラリ

- Claude Scientific Skills
- Trail of Bits Security Skills
- cc-devops-skills
- Superpowers

## 前提知識

- Claude Codeの基本的な使い方（インストール、起動、プロンプト入力）
- Claude Codeの設定ファイル構造（.claude/ディレクトリ、hooks.json、commands/、skills/）
- GitHubの基本操作（リポジトリのクローン、READMEの読解）
- JSON、Markdown、Bashの基礎知識

## 根拠

> # Awesome Claude Code - A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow.

> ## Agent Skills 🤖 - Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

> ## Hooks 🪝 - Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.

> ## Slash-Commands 🔪 - Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task.

> ## Tooling 🧰 - Tooling denotes applications that are built on top of Claude Code and consist of more components than slash-commands and CLAUDE.md files.
