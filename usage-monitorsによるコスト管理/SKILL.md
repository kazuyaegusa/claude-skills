# Usage Monitorsによるコスト管理

> Claude Codeのトークン消費量・コスト・セッション履歴を可視化し、使用状況を監視・分析する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeを無制限に使うとサブスクリプション上限に達したり、予期しないコストが発生する。リアルタイムで消費状況を把握することで、予算内で効率的に利用できる

## いつ使うのか

複数プロジェクトでClaude Codeを使っており、コストを管理したい場合。チームで使用量を共有・分析したい場合

## やり方

1. Usage Monitorツール（ccflare、CC Usage、Claudex等）をインストール
2. ツールがローカルのClaude Codeログファイル（`~/.claude/logs/`等）を解析
3. Webダッシュボードまたはターミナルで以下を表示：
   - トークン消費量（入力/出力別）
   - 推定コスト
   - セッション履歴
   - burn rate（消費速度）
   - 上限到達予測
4. アラートを設定（例：月間上限の80%到達時に通知）

例：ccflareはTableau並みのWebダッシュボードを提供し、プロジェクト別・モデル別の詳細メトリクスを表示

### 入力

- Claude Codeのログファイル
- サブスクリプションプラン情報

### 出力

- 使用量ダッシュボード（Web/TUI）
- トークン消費グラフ
- コスト予測
- セッション履歴

## 使うツール・ライブラリ

- ccflare（Web UI、詳細メトリクス）
- better-ccflare（ccflareの改良版、複数プロバイダ対応）
- CC Usage（CLI、ローカルログ解析）
- Claudex（会話履歴ブラウザ、全文検索）

## コード例

```
# CC Usage example
ccusage --project myapp --period month
# Output:
# Total tokens: 1,234,567
# Estimated cost: $12.34
# Burn rate: 50K tokens/day
# Days until limit: 18
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
