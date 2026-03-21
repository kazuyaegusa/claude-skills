# プロジェクト/グローバルの優先順位設計

> プロジェクト固有のサブエージェント（`.claude/agents/`）とグローバルエージェント（`~/.claude/agents/`）の2層構造を採用し、同名の場合はプロジェクト優先とする

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

チーム全体で共通エージェントを使いつつ、特定プロジェクトではカスタマイズ版を優先できるようにし、柔軟性と一貫性を両立するため

## いつ使うのか

複数プロジェクトで異なるコーディング規約やテストパターンを適用したい時、グローバルエージェントをプロジェクトごとに上書きしたい時

## やり方

1. 全プロジェクトで共通に使うエージェントは `~/.claude/agents/` に配置
2. プロジェクト固有のルールや設定が必要な場合、同名エージェントを `.claude/agents/` に配置
3. Claude Codeは起動時にプロジェクトディレクトリを優先チェックし、なければグローバルを参照
4. バージョン管理: プロジェクト固有エージェントは `.claude/agents/` をgit管理し、チーム全体で共有

### 入力

- エージェントのスコープ（全プロジェクト共通 or プロジェクト固有）
- 同名エージェントの優先順位要件

### 出力

- 柔軟なエージェント管理（グローバル + プロジェクトオーバーライド）
- チーム全体での一貫性とプロジェクト固有カスタマイズの両立

## 使うツール・ライブラリ

- Claude Code agent discovery mechanism
- Git（プロジェクトエージェントの共有用）

## コード例

```
# グローバルエージェント（全プロジェクトで利用）
~/.claude/agents/code-reviewer.md

# プロジェクト固有エージェント（このプロジェクトのみ）
.claude/agents/code-reviewer.md  # 同名だがプロジェクト固有ルールを含む

# 優先順位: プロジェクト > グローバル
```

## 前提知識

- Claude Codeの基本的な使い方（サブエージェント機能の理解）
- YAMLフロントマターとMarkdownの読み書き
- コマンドラインツール（claude CLI、curl、bash）の操作経験
- 開発ドメイン知識（各サブエージェントを効果的に使うため、対象領域の基礎理解が必要）

## 根拠

> 「This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.」

> 「model field that automatically routes it to the right Claude model — balancing quality and cost: opus (Deep reasoning), sonnet (Everyday coding), haiku (Quick tasks)」

> 「Project Subagents: .claude/agents/ (Current project only, Higher precedence) / Global Subagents: ~/.claude/agents/ (All projects, Lower precedence)」
