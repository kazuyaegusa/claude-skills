# Slash-Commandsによる定型プロンプトの再利用

> 頻繁に使うプロンプト（コミットメッセージ生成、PR作成、ドキュメント更新等）を `.claude/commands/<name>.md` に保存し、`/name` で即座に呼び出す

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

同じ指示を毎回タイプするのは非効率で、表現のブレが品質低下を招く。Slash-Commandsで標準化されたプロンプトを共有することで、チーム全体の一貫性と生産性が向上

## いつ使うのか

コミット、PR作成、ドキュメント生成、Issue分析、コンテキスト読み込みなど、繰り返し実行する定型タスクがある時

## やり方

1. `.claude/commands/` に `<command-name>.md` を作成
2. ファイル内にプロンプトをマークダウンで記述（パラメータ `{arg}` も使用可能）
3. Claude Codeで `/command-name` を入力して実行
4. 複数コマンドを組み合わせてワークフローを構築

### 入力

- .claude/commands/<name>.md ファイル
- オプションでパラメータ（Issue番号、ブランチ名等）

### 出力

- 標準化されたコミットメッセージ、PR、ドキュメント
- チーム全体で一貫したClaude Code利用

## 使うツール・ライブラリ

- /commit（conventional commit形式でコミット）
- /create-pr（GitHub CLI連携でPR作成）
- /tdd（TDDワークフロー強制）

## コード例

```
# 例: .claude/commands/commit.md
Create a git commit using conventional commit format:
- Analyze staged changes
- Generate concise commit message
- Include emoji prefix
- Run `git commit -m "<message>"`
```

## 前提知識

- Claude Codeの基本的な使い方（CLI起動、プロンプト入力、ツール実行）
- Git/GitHubの基礎知識（ブランチ、コミット、PR）
- ターミナル操作とシェルスクリプトの基本
- Markdown記法の理解
- 使用する言語・フレームワークの基礎知識（TypeScript、Python、Go等）

## 根拠

> 「A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow」

> 「Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities」

> 「Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle」

> 「Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task」

> 「CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards」
