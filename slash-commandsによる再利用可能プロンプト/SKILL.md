# Slash-Commandsによる再利用可能プロンプト

> 頻繁に使う複雑なプロンプトを `/commit`, `/tdd` 等の短縮コマンドとして登録し、即座に呼び出す

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

毎回同じ指示を書く手間を省き、チーム全体で統一された開発フローを強制できる

## いつ使うのか

複数人がClaude Codeを使うプロジェクトで、Git操作・テスト・ドキュメント生成の手順を標準化したい時

## やり方

1. `.claude/commands/` 配下にマークダウンファイルを作成（例: `commit.md`）
2. ファイル内にプロンプトテンプレートを記述（引数は `{{arg1}}` 等でパラメータ化可能）
3. Claude Codeで `/commit` と入力すると、ファイル内容が展開されてプロンプトとして実行される
4. 例: `/commit` は「conventional commit形式で差分からコミットメッセージを生成」を自動実行

### 入力

- マークダウン形式のコマンド定義ファイル
- （オプション）コマンド引数

### 出力

- 展開されたプロンプトのClaude Code実行結果

## 使うツール・ライブラリ

- .claude/commands/ 配置
- /create-command（コマンド生成支援）

## コード例

```
# .claude/commands/commit.md
---
description: Generate conventional commit message from staged changes
---

1. Run `git diff --staged`
2. Analyze changes and generate commit message following conventional commit format
3. Execute `git commit -m "<generated-message>"`
```

## 前提知識

- Claude Codeの基本的な使い方（セッション開始、ファイル編集、Bash実行）
- Gitの基礎知識（ブランチ、コミット、PR）
- JSON/YAML形式の理解（設定ファイル記述用）
- （オーケストレータ使用時）Dockerまたはgit worktreeの知識
- （言語特化CLAUDE.md使用時）対象言語のビルドツール知識（pnpm, Gradle, cargo等）

## 根拠

> 「Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.」

> 「Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.」

> 「Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task」

> 「CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards」

> 「ccflare - Claude Code usage dashboard with a web-UI that would put Tableau to shame. Thoroughly comprehensive metrics, frictionless setup, detailed logging, really really nice UI.」
