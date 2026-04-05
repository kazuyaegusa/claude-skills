# Slash Commandsによるワークフロー標準化

> 頻出タスクを再利用可能なコマンドとしてパッケージ化し、チーム全体で統一された手順を実行する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

毎回同じプロンプトを書く非効率を排除し、ベストプラクティスを組織知化するため

## いつ使うのか

チーム全体で手順を統一したいタスク（コミット・PR作成・ドキュメント生成等）があるとき

## やり方

1. `.claude/commands/{command-name}.md`にプロンプトテンプレートを定義
2. パラメータ化が必要な場合は変数を埋め込み
3. `/command-name`で起動
4. `/commit`（Conventional Commits形式）、`/tdd`（Red-Green-Refactorガイド）等の実装例を参考に作成

### 入力

- コマンド定義（.mdファイル）
- 実行時パラメータ（任意）

### 出力

- 標準化されたタスク実行結果

## 使うツール・ライブラリ

- Markdownフォーマット
- Claude Code CLI

## コード例

```
<!-- /commit.md -->
Create a git commit using Conventional Commits format:
1. Analyze staged changes
2. Generate commit message with type (feat/fix/docs)
3. Add emoji prefix
4. Run `git commit -m "<message>"`
```

## 前提知識

- Claude Codeの基本操作（CLI使用・セッション管理）
- マークダウンフォーマットの理解
- Bash/Python/TypeScriptのいずれかでスクリプト作成経験
- Git・GitHub CLIの基礎知識
- LLMエージェントの基本概念（プロンプトエンジニアリング・コンテキスト管理）

## 根拠

> "Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task"
