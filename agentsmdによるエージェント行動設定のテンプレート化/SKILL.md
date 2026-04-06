# AGENTS.mdによるエージェント行動設定のテンプレート化

> ルートに `AGENTS.md` を配置し、エージェントのペルソナ・ワークフロー・使用スキルを宣言的に定義する

- 出典: https://github.com/microsoft/skills
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

プロジェクトごとにエージェントの振る舞いをカスタマイズし、チーム全体で一貫した開発体験を提供する

## いつ使うのか

複数のエージェントペルソナを使い分けたい場合。プロジェクト固有のワークフローをエージェントに教えたい場合

## やり方

1. リポジトリルートに `AGENTS.md` を作成 2. エージェントペルソナ（backend/frontend/infrastructure/planner等）を定義 3. 各ペルソナで使用するスキル・プロンプトを明記 4. エージェント起動時に自動ロード

### 入力

- エージェントペルソナ定義
- 使用スキルリスト
- ワークフロー指示

### 出力

- AGENTS.md
- エージェント起動時の自動ロード

## 使うツール・ライブラリ

- GitHub Copilot
- Claude Code
- Copilot CLI

## コード例

```
# AGENTS.md
## Backend
- Skills: azure-cosmos-db-py, fastapi-router-py
- Workflow: TDD, Pydantic models
```

## 前提知識

- AI coding agent（GitHub Copilot、Claude Code、Copilot CLI等）の基本操作
- Markdown形式のドキュメント構造理解
- Symlink（シンボリックリンク）の概念
- YAML形式の設定ファイル
- GitHub Actionsの基本（日次更新ワークフローを活用する場合）
- MCP（Model Context Protocol）の概要（外部ツール統合を使う場合）
