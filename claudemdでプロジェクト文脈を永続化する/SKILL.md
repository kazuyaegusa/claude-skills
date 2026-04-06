# CLAUDE.mdでプロジェクト文脈を永続化する

> プロジェクトルートに CLAUDE.md を配置し、コーディング規約・ビルドコマンド・アーキテクチャ情報を記述する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

毎セッションで同じ説明をする手間を省き、Claudeが常にプロジェクト固有のルールを把握できるため

## いつ使うのか

チーム開発でコーディング規約を統一したい時、特定フレームワーク・言語のルールを明示したい時

## やり方

1. プロジェクトルートに CLAUDE.md を作成
2. ビルドコマンド、テストコマンド、コーディング規約、禁止事項などを記述
3. Claude Codeが自動で読み込み、全応答に反映

### 入力

- プロジェクトのビルド・テスト手順
- コーディング規約（命名、型、エラーハンドリング等）
- 禁止事項・セキュリティガイドライン

### 出力

- CLAUDE.md ファイル
- Claudeの全応答に反映される文脈

## 使うツール・ライブラリ

- markdown

## コード例

```
# ビルド
`pnpm build`

# テスト
`pnpm test`

# コーディング規約
- TypeScript strict mode
- `any` 禁止
- 非同期は async/await
```

## 前提知識

- Claude Codeの基本的な使い方（CLI起動、プロンプト入力、ツール実行）
- markdown記法
- JSON記法（hooks.json等の設定ファイル）
- Bash/シェルスクリプトの基礎
- Git基本操作
- （Agent Teams利用時）マルチエージェントの概念理解

## 根拠

> "Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities."

> "Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle."

> "Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task"

> "CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards"

> "A well-designed desktop app that provides detailed observability into your Claude Code sessions by analyzing the session logs. Provides turn-based context data across numerous categories, compaction visualization, subagent execution trees, and custom notification triggers."
