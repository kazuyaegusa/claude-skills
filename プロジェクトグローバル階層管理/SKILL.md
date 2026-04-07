# プロジェクト/グローバル階層管理

> プロジェクト固有（.claude/agents/）とグローバル（~/.claude/agents/）の2階層でエージェントを管理し、優先順位をプロジェクト優先にする

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

チーム全体で共通エージェントを使いつつ、特定プロジェクトで上書き・カスタマイズが可能になり、柔軟性と一貫性を両立できる

## いつ使うのか

チーム標準とプロジェクト特性のバランスを取りたい時、グローバル設定を部分的に上書きしたい時

## やり方

1. グローバル共通エージェントを `~/.claude/agents/` に配置
2. プロジェクト固有エージェントを `.claude/agents/` に配置
3. 同名エージェントが存在する場合、プロジェクト版が優先される
4. チーム全体で標準セットを共有しつつ、個別プロジェクトで微調整

### 入力

- グローバルエージェント定義
- プロジェクト固有エージェント定義

### 出力

- 階層化されたエージェント管理体系

## 使うツール・ライブラリ

- ファイルシステム（.claude/ と ~/.claude/）

## コード例

```
# Global (all projects)
~/.claude/agents/python-pro.md

# Project-specific (overrides global)
.claude/agents/python-pro.md  # Higher precedence
```

## 前提知識

- Claude Codeの基本操作とサブエージェント概念の理解
- 開発タスクのカテゴリ分類（言語/インフラ/品質等）に関する知識
- Claude APIのモデル違い（opus/sonnet/haiku）の理解
- Markdownとフロントマター（YAML）の基礎知識
- Claude Code組み込みツール（Read, Write, Edit, Bash等）の把握
