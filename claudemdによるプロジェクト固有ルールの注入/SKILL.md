# CLAUDE.mdによるプロジェクト固有ルールの注入

> プロジェクトルートに `CLAUDE.md` を配置し、コーディング規約、ビルドコマンド、テスト方法、アーキテクチャ情報をClaude Codeに自動読み込ませる

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeはプロジェクトの歴史や慣習を知らない。CLAUDE.mdで明示的に伝えることで、命名規則違反や非推奨API使用を防ぎ、初回から高品質なコードを生成できる

## いつ使うのか

新規メンバーがプロジェクトに参加、レガシーコードベースのモダナイゼーション、複数プロジェクト間でClaude Codeの動作を切り替えたい時

## やり方

1. プロジェクトルートに `CLAUDE.md` を作成
2. 「使用言語・フレームワーク」「ビルド・テストコマンド」「コーディング規約」「禁止パターン」を記述
3. Claude Code起動時に自動読み込み
4. 必要に応じて `.claude/rules/` で特定ファイルパターンに対するルールを追加

### 入力

- CLAUDE.md（マークダウン形式）
- オプションで .claude/rules/*.md

### 出力

- プロジェクト規約に準拠したコード
- 適切なテスト・ビルドコマンドの自動実行

## 使うツール・ライブラリ

- Metabase CLAUDE.md（Clojure REPL-driven開発）
- Giselle CLAUDE.md（TypeScript/Vue3 Composition API規約）

## コード例

```
# 例: CLAUDE.md
## Build
`pnpm build`

## Test
`pnpm test`

## Rules
- Use TypeScript strict mode
- Prefer `type` over `interface`
- No `any` type
- Immutable data structures
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
