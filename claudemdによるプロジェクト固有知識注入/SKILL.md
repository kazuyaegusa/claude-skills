# CLAUDE.mdによるプロジェクト固有知識注入

> リポジトリルートまたは `.claude/` に `CLAUDE.md` を配置し、ビルドコマンド、コーディング規約、アーキテクチャ等を記述する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeがセッション開始時に読み込むことで、プロジェクト特有の文脈を毎回説明する手間を省き、初見でも適切な判断ができるようにする

## いつ使うのか

新規メンバーやエージェントが頻繁にジョインするプロジェクト、または特殊な開発フローを採用している場合

## やり方

1. プロジェクトルートに `CLAUDE.md` を作成
2. 以下を記述: ビルド/テストコマンド、ディレクトリ構造、使用技術スタック、コーディング規約、テスト方針、デプロイ手順
3. Claude Codeは新規セッション時に自動読み込み（明示的に指示不要）
4. 言語特化例: Metabaseの `CLAUDE.md` は「REPL駆動開発」「インクリメンタル変更」を強調

### 入力

- プロジェクトの技術仕様・開発ルール

### 出力

- Claude Codeがプロジェクト文脈を理解した状態での応答

## 使うツール・ライブラリ

- CLAUDE.md 配置（リポジトリルートまたは .claude/）

## コード例

```
# CLAUDE.md 例

## Build Commands
- `pnpm install` - Install dependencies
- `pnpm test` - Run Vitest tests

## Coding Standards
- Use Biome for formatting (no Prettier)
- Prefer Composition API for Vue 3
- All async functions must have timeout handling
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
