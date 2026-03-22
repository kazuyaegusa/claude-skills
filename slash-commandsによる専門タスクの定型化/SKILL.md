# Slash Commandsによる専門タスクの定型化

> 複雑なプロンプトや手順を単一のコマンド（例：`/commit`、`/tdd`、`/create-pr`）にカプセル化し、再利用可能にする

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

同じ指示を毎回長文で入力するのは非効率かつ品質がブレる。よく使うワークフロー（PR作成、Issue対応、ドキュメント生成など）をコマンド化することで、一貫性を保ちながら高速に実行できる

## いつ使うのか

頻繁に繰り返すタスク（コミット、PR作成、Issue分析、ドキュメント更新など）があり、手順を標準化したい場合

## やり方

1. `.claude/commands/`ディレクトリに Markdownファイルを作成（例：`commit.md`）
2. ファイル内にプロンプトテンプレートを記述（引数は`${arg1}`形式で埋め込み可能）
3. Claude Codeから`/commit`のように呼び出すと、テンプレートが展開されてプロンプトとして実行される
4. 複雑なワークフローは複数ステップに分割して記述可能

例：`/commit`コマンドは「git statusを確認→diffを取得→conventional commit形式でメッセージ生成→コミット実行」を自動化

### 入力

- Markdownファイル（`.claude/commands/*.md`）
- プロンプトテンプレート
- コマンド引数（オプション）

### 出力

- 定型化されたプロンプトの実行結果
- 自動生成されたコード・ドキュメント・コミットメッセージ等

## 使うツール・ライブラリ

- /commit（conventional commit形式）
- /create-pr（PR作成自動化）
- /tdd（TDD workflow）
- /analyze-issue（GitHub issue分析）
- /create-hook（hook生成支援）

## コード例

```
---
name: commit
description: Create a git commit with conventional commit format
---

1. Run `git status` to see changes
2. Run `git diff` to review modifications
3. Generate a commit message following conventional commits
4. Execute `git commit -m "<message>"`
```

## 前提知識

- Claude Codeの基本的な使い方（CLI操作、プロンプト入力、ファイル編集）
- Gitの基礎知識（branch、commit、PR）
- シェルスクリプト/Python/Node.jsの基礎（Hooks実装時）
- Docker/tmuxの基礎知識（Orchestrators使用時）
- JSON/YAML形式の理解（設定ファイル編集時）

## 根拠

> "Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle."

> "Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task"

> "CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards"

> "Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities."

> "ccflare - Claude Code usage dashboard with a web-UI that would put Tableau to shame. Thoroughly comprehensive metrics, frictionless setup, detailed logging, really really nice UI."
