# 4種類のインストール方法提供

> プラグイン/手動コピー/対話型インストーラー/curlスタンドアロンの4通りでエージェントを導入可能にする

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

ユーザーの技術レベル・プロジェクト要件・ネットワーク環境に応じて最適な導入方法を選べるようにし、導入障壁を最小化する

## いつ使うのか

チーム全体に標準エージェントセットを配布したい時、個別プロジェクトで必要なエージェントのみ選択したい時

## やり方

1. **プラグイン（推奨）**: `claude plugin install voltagent-lang` でカテゴリ一括導入
2. **手動**: リポジトリをcloneし、`~/.claude/agents/` or `.claude/agents/` に必要なファイルをコピー
3. **対話型インストーラー**: `./install-agents.sh` でカテゴリ/エージェント選択→自動インストール
4. **curlスタンドアロン**: `curl -sO https://raw.../install-agents.sh && chmod +x && ./install-agents.sh` でclone不要導入

### 入力

- 導入方法の選択
- 必要なカテゴリ/エージェント

### 出力

- ~/.claude/agents/ または .claude/agents/ にインストールされたエージェント定義

## 使うツール・ライブラリ

- claude CLI
- Bash
- curl

## コード例

```
# Option 1: Plugin
claude plugin install voltagent-lang

# Option 2: Manual
cp categories/02-language-specialists/python-pro.md ~/.claude/agents/

# Option 3: Interactive
./install-agents.sh

# Option 4: Standalone
curl -sO https://raw.../install-agents.sh && chmod +x && ./install-agents.sh
```

## 前提知識

- Claude Codeの基本操作とサブエージェント概念の理解
- 開発タスクのカテゴリ分類（言語/インフラ/品質等）に関する知識
- Claude APIのモデル違い（opus/sonnet/haiku）の理解
- Markdownとフロントマター（YAML）の基礎知識
- Claude Code組み込みツール（Read, Write, Edit, Bash等）の把握

## 根拠

> 「4 installation options: Plugin (Recommended), Manual Installation, Interactive Installer, Standalone Installer」
