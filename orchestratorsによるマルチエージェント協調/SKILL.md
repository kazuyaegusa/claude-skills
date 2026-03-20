# Orchestratorsによるマルチエージェント協調

> 複数のClaude Codeインスタンスまたは異なるAIエージェントを並列・逐次実行し、大規模タスクを分割・統合する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

単一エージェントでは、コンテキスト制限・長時間実行・複雑タスクで限界がある。複数エージェントを協調させることで、並列化・専門化・耐障害性を実現できる

## いつ使うのか

大規模プロジェクト・複数機能の並行開発・長時間タスク（数時間〜数日）を扱う場合

## やり方

1. タスクの性質に応じたOrchestratorを選定（例：並列実行→「Claude Squad」、タスク分割→「Claude Task Runner」、自律実行→「Auto-Claude」）
2. Orchestratorをインストール（多くはCLIツール）
3. タスクを分割定義（例：「フロントエンド実装」「バックエンド実装」「テスト作成」を別エージェントに割り当て）
4. Orchestratorを起動し、各エージェントの進捗を監視
5. 各エージェントの出力を統合・レビュー

### 入力

- タスク分割定義（各エージェントが担当する範囲）
- 各エージェントの設定（CLAUDE.md、スキル等）
- 統合ルール（マージ戦略、競合解決方法）

### 出力

- 並列実行による時間短縮
- 専門化による品質向上
- 各エージェントのgit branch（人間がレビュー・マージ）

## 使うツール・ライブラリ

- Claude Squad（複数Claude Code/Codex/Aiderを並列管理）
- Auto-Claude（自律SDLC、カンバンUI）
- TSK（Docker sandbox内で並列エージェント実行）
- sudocode（軽量オーケストレーター、仕様フレームワーク統合）

## コード例

```
# 概念例（Claude Squad的な使い方）
claude-squad start \
  --task "frontend: Implement login UI" \
  --task "backend: Implement /auth API" \
  --task "test: Write E2E tests"
# 各タスクが独立したClaude Codeインスタンスで並列実行される
```

## 前提知識

- Claude Codeの基本的な使い方（CLI起動、プロンプト入力、ファイル操作承認等）
- gitの基礎知識（branch, commit, PR等）
- 開発ワークフローの基礎（TDD, CI/CD, コードレビュー等の概念）
- JSON/Markdown形式の読み書き（Hooks設定、CLAUDE.md記述に必要）

## 根拠

> 「Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.」

> 「Claude Squad - manages multiple Claude Code, Codex (and other local agents including Aider) in separate workspaces, allowing you to work on multiple tasks simultaneously.」
