# CLAUDE.mdによるプロジェクト文脈の注入

> プロジェクト固有のルール・構造・慣習をClaude Codeに自動的に理解させる

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

毎回同じ文脈説明を繰り返す無駄を排除し、一貫性のある出力を得るため

## いつ使うのか

プロジェクト固有の文脈をClaude Codeに常に認識させたいとき

## やり方

1. プロジェクトルートまたは`.claude/`に`CLAUDE.md`を配置
2. ビルドコマンド・ディレクトリ構造・コーディング規約・用語集を記述
3. Claude Codeが自動的に読み込んで文脈として利用
4. Metabase（Clojure REPL駆動開発）、Giselle（pnpm+Vitest）等の実装例を参考に作成

### 入力

- ビルド・テストコマンド
- ディレクトリ構造
- コーディング規約
- プロジェクト固有用語

### 出力

- 文脈を踏まえたClaude Codeの出力

## 使うツール・ライブラリ

- Markdownフォーマット

## コード例

```
# CLAUDE.md例
## Build
`pnpm build`

## Structure
- `src/`: Source code
- `tests/`: Vitest tests

## Conventions
- Use Vue 3 Composition API
- Prefer `type` over `interface`
```

## 前提知識

- Claude Codeの基本操作（CLI使用・セッション管理）
- マークダウンフォーマットの理解
- Bash/Python/TypeScriptのいずれかでスクリプト作成経験
- Git・GitHub CLIの基礎知識
- LLMエージェントの基本概念（プロンプトエンジニアリング・コンテキスト管理）

## 根拠

> "Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities."

> "Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle."

> "Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task"

> "CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards"

> "Agent Teams - Launch Claude Code session that is connected to a swarm of Claude Code Agents"
