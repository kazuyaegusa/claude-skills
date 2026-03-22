# CLAUDE.mdによるプロジェクト文脈の注入

> プロジェクトルートまたは`.claude/`ディレクトリに`CLAUDE.md`ファイルを配置し、コーディング規約・アーキテクチャ・ビルドコマンド等の文脈情報をClaude Codeに自動的に伝える

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

プロジェクトごとに異なる言語、フレームワーク、命名規則、テスト方針を毎回説明するのは非効率。CLAUDE.mdに記述しておけば、Claude Codeがセッション開始時に自動で読み込み、文脈に沿った提案をしてくれる

## いつ使うのか

複数人でClaude Codeを使う場合、プロジェクト固有の規約が多い場合、新メンバーのオンボーディングを効率化したい場合

## やり方

1. プロジェクトルートに`CLAUDE.md`を作成
2. 以下の情報を記述：
   - ビルド/テスト/デプロイコマンド
   - コーディング規約（命名規則、フォーマッタ、linter）
   - アーキテクチャ概要（モジュール構成、依存関係）
   - 重要な制約（例：「必ずテストを先に書く」）
3. Claude Codeはセッション開始時に自動で読み込む
4. 必要に応じて`/context-prime`コマンドで明示的に再読み込み

### 入力

- CLAUDE.mdファイル
- プロジェクトの規約・アーキテクチャ・コマンド情報

### 出力

- 文脈に沿ったコード生成
- 規約違反の自動検出と修正提案
- 適切なビルド/テストコマンドの実行

## 使うツール・ライブラリ

- Metabase CLAUDE.md（Clojure/ClojureScript、REPL駆動開発）
- Giselle CLAUDE.md（pnpm、Vitest、厳格なフォーマット）
- LangGraphJS CLAUDE.md（TypeScript、monorepo、yarn workspaces）

## コード例

```
# Project: MyApp

## Build Commands
- `npm run dev` - Start dev server
- `npm test` - Run tests
- `npm run lint` - Lint code

## Coding Standards
- Use TypeScript strict mode
- Follow Airbnb style guide
- **Always write tests before implementation (TDD)**

## Architecture
- `/src/components` - React components
- `/src/lib` - Shared utilities
- `/src/api` - API client
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
