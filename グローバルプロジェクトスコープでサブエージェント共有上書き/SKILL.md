# グローバル/プロジェクトスコープでサブエージェント共有・上書き

> グローバル（~/.claude/agents/）とプロジェクト固有（.claude/agents/）の2階層でサブエージェントを管理し、同名エージェントはプロジェクト側が優先される

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

チーム全体で共通のベースエージェントをグローバルに配置しつつ、特定プロジェクトでカスタマイズが必要な場合にプロジェクトローカルで上書きできる。チームの一貫性と柔軟性を両立

## いつ使うのか

チーム標準のエージェントセットを全プロジェクトで共有しつつ、特定プロジェクトのニーズ（レガシーコードベース、特殊な言語バージョン等）に応じてカスタマイズしたい時

## やり方

1. 共通エージェントを `~/.claude/agents/` にインストール（全プロジェクトで利用可能）
2. 特定プロジェクトでカスタマイズが必要な場合、同名エージェントを `.claude/agents/` に配置（プロジェクト内でのみ有効、グローバルを上書き）
3. Claude Codeはプロジェクトローカル → グローバルの順で検索し、最初に見つかったものを使用

### 入力

- グローバルとプロジェクトディレクトリ両方への書き込み権限
- チームのエージェント標準化ポリシー

### 出力

- プロジェクトごとに最適化されたサブエージェントセット
- チーム全体での一貫性維持

## 使うツール・ライブラリ

- Claude Code
- ファイルシステム

## コード例

```
# グローバル（全プロジェクト共通）
~/.claude/agents/python-pro.md

# プロジェクト固有（このプロジェクトのみ上書き）
.claude/agents/python-pro.md
```

## 前提知識

- Claude Codeがインストール・セットアップ済み
- サブエージェントの概念理解（独立したコンテキストウィンドウ、ドメイン特化プロンプト、ツール権限管理）
- 基本的なCLI操作（curl, chmod, git clone等）
- YAMLフロントマター形式の理解（サブエージェント定義ファイルの編集時）
- Claude Codeの /agents コマンドとサブエージェント呼び出し構文の理解

## 根拠

> "This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks."

> "Each subagent includes a `model` field that automatically routes it to the right Claude model — balancing quality and cost"

> "Project Subagents: `.claude/agents/` Current project only, Higher precedence"

> "Global Subagents: `~/.claude/agents/` All projects, Lower precedence"

> "claude plugin marketplace add VoltAgent/awesome-claude-code-subagents"
