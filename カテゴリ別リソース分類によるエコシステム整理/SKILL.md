# カテゴリ別リソース分類によるエコシステム整理

> Claude Code の拡張機能を「Agent Skills」「Workflows」「Tooling」「Status Lines」「Hooks」「Slash-Commands」「CLAUDE.md Files」などのカテゴリに分類して整理する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

散在するリソースを体系的に整理することで、開発者が自分のニーズに合った拡張機能を効率的に発見でき、重複や見落としを防げるため

## いつ使うのか

Claude Code エコシステムの全体像を把握したい時、特定のユースケースに適した拡張を探したい時

## やり方

1. 各リソースの主要機能を分析し、カテゴリを定義する
2. カテゴリごとにサブカテゴリ（言語別、ドメイン別など）を設ける
3. 各リソースに簡潔な説明文と作者情報を付与
4. README.md に目次とカテゴリリンクを配置
5. 定期的に新規リソースを追加・更新

### 入力

- GitHub リポジトリ、npm パッケージ、公開されている Claude Code 拡張機能

### 出力

- カテゴリ別に整理された awesome リスト（Markdown 形式）
- 各リソースへのリンクと説明文

## 使うツール・ライブラリ

- GitHub
- Markdown
- awesome.re バッジ

## 前提知識

- Claude Code の基本的な使い方（インストール、セッション開始、プロンプト入力）
- Git の基礎知識（コミット、ブランチ、PR 作成）
- Markdown の基本文法
- シェルスクリプト（Bash）の基礎知識（フック・スラッシュコマンドのカスタマイズに必要）
- JSON の基本構造（フック設定ファイルの編集に必要）

## 根拠

> "A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow."

> "Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities."

> "Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle."

> "Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task"

> "CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards"
