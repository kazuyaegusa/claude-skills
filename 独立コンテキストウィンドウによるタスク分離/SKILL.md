# 独立コンテキストウィンドウによるタスク分離

> 各サブエージェントは独立したコンテキストウィンドウ内で動作するため、メインの会話履歴と混ざらず、タスク固有の詳細情報が隔離される

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

複数のタスクを並行実行する際、各タスクの詳細（例: セキュリティ監査の結果、API設計の議論、インフラ構築のログ）がメインの会話を汚染せず、それぞれのタスクに集中できる。またメモリ効率が向上し、トークン消費を抑制できる

## いつ使うのか

複数の専門領域にまたがる大規模開発、並行して複数のレビューやテストを実施する場合、メインの会話をクリーンに保ちたい場合

## やり方

1. Claude Codeでサブエージェントを呼び出す際、自動的に独立したコンテキストウィンドウが作成される
2. サブエージェント内での会話や生成物はそのウィンドウ内に留まり、メインの会話には最終結果だけが返される
3. 複数のサブエージェントを同時起動しても、それぞれが独立して動作し干渉しない
4. 必要に応じてサブエージェント間で情報を受け渡す場合は、Meta & Orchestrationカテゴリのエージェント（multi-agent-coordinator, workflow-orchestrator等）を利用

### 入力

- 並行実行するタスク群
- 各タスクに必要な専門知識

### 出力

- 各タスクの独立した実行結果
- クリーンなメイン会話履歴

## 使うツール・ライブラリ

- Claude Code（サブエージェントコンテキスト管理機能）

## コード例

```
# メイン会話で複数サブエージェントを並行起動
> Have the security-auditor review the auth module
> Have the performance-engineer analyze the database queries
> Have the code-reviewer check the PR #123

# 各エージェントは独立したコンテキストで動作し、
# メイン会話には最終レポートだけが返される
```

## 前提知識

- Claude Code CLI がインストールされていること
- Claude Codeの基本操作（エージェント起動、ツール実行）の理解
- YAMLフロントマターの基本構文知識（エージェントカスタマイズ時）
- gitの基本操作（リポジトリクローン、ファイルコピー）
- 対象プロジェクトの技術スタックと開発フローの把握

## 根拠

> 「This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.」

> 「Smart Model Routing: Each subagent includes a model field that automatically routes it to the right Claude model — balancing quality and cost」

> 「Global Subagents: ~/.claude/agents/ - All projects - Lower precedence」「Project Subagents: .claude/agents/ - Current project only - Higher precedence」
