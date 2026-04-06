# 使用状況ダッシュボードで分析する

> Claude Codeのセッションログ（.jsonl）を解析し、トークン使用量・コスト・モデル分布などをWebUIで可視化する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

使用量の傾向を把握し、最適化ポイントや予算管理に活かすため

## いつ使うのか

チームでClaude Codeを運用し、コスト管理・最適化が必要な時

## やり方

1. ccflare, claude-devtools等のツールをインストール
2. ~/.claude/sessions/ のログを自動解析
3. WebUIでダッシュボード表示（トークン消費、burn rate、モデル別統計等）

### 入力

- ~/.claude/sessions/ の .jsonl ログファイル

### 出力

- WebUIダッシュボード
- トークン消費統計、コスト予測

## 使うツール・ライブラリ

- ccflare
- better-ccflare
- claude-devtools
- Claudex

## コード例

```
# インストール例
npm install -g ccflare
ccflare
# http://localhost:3000 でダッシュボード起動
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
